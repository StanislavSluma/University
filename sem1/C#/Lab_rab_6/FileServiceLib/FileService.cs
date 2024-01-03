using Lab_rab_6;
using System.Text.Json;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace FileServiceLib
{

    public class FileService<T> : IFileService<T> where T: class
    {
        public IEnumerable<T> ReadFile(string fileName)
        {
            using (FileStream fs = new FileStream(fileName, FileMode.OpenOrCreate))
            {
                 return JsonSerializer.Deserialize<IEnumerable<T>>(fs);
            }
        }

        public void SaveData(IEnumerable<T> data, string fileName)
        {
            using (FileStream fs = new FileStream(fileName, FileMode.OpenOrCreate))
            {
                JsonSerializer.Serialize(fs, data, new JsonSerializerOptions { WriteIndented = true });
            }
        }
    }
}