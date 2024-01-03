using ClassLibrary;

class Programm
{
    public static async Task Main(string[] args)
    { 
        Console.Write("Запуск");

        StreamService<Passanger> stream_serv = new();
        stream_serv.OutConsole += (int Id, string method) =>
        {
            Console.WriteLine($"\nПоток {Id} {method}");
        };

        Progress<int> progress = new Progress<int>(x => Console.Write($"\rВыполнение: {x}%"));
        MemoryStream mem_stream = new();
        List<Passanger> collection = new List<Passanger>() {};

        for (int i = 0; i < 1000; i++)
        {
            collection.Add(new Passanger(i, $"Name {i * i}", Convert.ToBoolean(i % 4)));
        }

        string filename = "D:/AA_curs2/sem1/C#/Lab_rab_8/Passanger.JSON";
        if (File.Exists(filename))
            File.Delete(filename);

        var task1 = stream_serv.WriteToStreamAsync(mem_stream, collection, progress);
        Thread.Sleep(300);
        var task2 = stream_serv.CopyFromStreamAsync(mem_stream,filename, progress);
        await task2;
        int statistics = await stream_serv.GetStatisticsAsync(filename, x => x.Baggage);
        Console.WriteLine($"\nКол-во пасажиров с багажом: {statistics}");
    }
}