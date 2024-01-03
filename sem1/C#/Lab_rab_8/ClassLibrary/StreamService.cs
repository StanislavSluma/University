using System.Text;
using System.Text.Json;

namespace ClassLibrary
{
    public class StreamService<T>
    {
        Semaphore sem = new Semaphore(1, 1);
        public delegate void Delegate(int Id, string method);
        public event Delegate? OutConsole;
        private object locker = new();
        public async Task WriteToStreamAsync(Stream stream, IEnumerable<T> data, IProgress<int> progress)
        {
            sem.WaitOne();
            int i = 1;
            int percent = 0;
            OutConsole?.Invoke(Thread.CurrentThread.ManagedThreadId, "начал запись");
            stream.Write(Encoding.ASCII.GetBytes("[\n"));
            foreach (var item in data)
            {
                await JsonSerializer.SerializeAsync(stream, item, new JsonSerializerOptions { WriteIndented = true });
                if (i != 1000)
                    stream.Write(Encoding.ASCII.GetBytes(",\n"));
                if (i / 10 >= percent)
                {
                    Thread.Sleep(30);
                    progress.Report(percent);
                    percent++;
                }
                i++;
            }
            stream.Write(Encoding.ASCII.GetBytes("\n]"));
            await Task.Delay(100);
            OutConsole?.Invoke(Thread.CurrentThread.ManagedThreadId, "закончил запись");
            sem.Release();
        }
        public async Task CopyFromStreamAsync(Stream stream, string filename, IProgress<int> progress)
        {
            sem.WaitOne();
            using FileStream fs = new FileStream(filename, FileMode.OpenOrCreate);
            stream.Position = 0;

            /*OutConsole?.Invoke(Thread.CurrentThread.ManagedThreadId, "начал копирование");
            stream.CopyToAsync(fs);
            progress.Report(100);
            OutConsole?.Invoke(Thread.CurrentThread.ManagedThreadId, "закончил копирование");*/

            OutConsole?.Invoke(Thread.CurrentThread.ManagedThreadId, "начал копирование");
            int i = 1;
            int percent = 0;
            fs.Write(Encoding.ASCII.GetBytes("[\n"));
            await foreach (var item in JsonSerializer.DeserializeAsyncEnumerable<T>(stream))
            {
                await JsonSerializer.SerializeAsync(fs, item, new JsonSerializerOptions() { WriteIndented = true });
                if (i != 1000)
                    fs.Write(Encoding.ASCII.GetBytes(",\n"));
                if (i / 10 >= percent)
                {
                    Thread.Sleep(30);
                    progress.Report(percent);
                    percent++;
                }
                i++;
            }
            fs.Write(Encoding.ASCII.GetBytes("\n]"));
            await Task.Delay(100);
            OutConsole?.Invoke(Thread.CurrentThread.ManagedThreadId, "закончил копирование");
            sem.Release();
        }
        public async Task<int> GetStatisticsAsync(string fileName, Func<T, bool> filter)
        {
            int res = 0;
            using FileStream fs = new FileStream(fileName, FileMode.OpenOrCreate);
            var collect = await JsonSerializer.DeserializeAsync<IEnumerable<T>>(fs);
            res = collect.Count(x => filter(x));
            return res;
        }

    }
}