using Lab_rab_4.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab_rab_4.Entities
{
    internal class FileService<T> : IFileService<T> where T : Passanger
    {
        public IEnumerable<T> ReadFile(string fileName)
        {
            using (BinaryReader reader = new BinaryReader(File.Open(fileName, FileMode.OpenOrCreate)))
            {
                while (reader.PeekChar() > -1)
                {
                    string name = reader.ReadString();
                    int age = reader.ReadInt32();
                    bool merried = reader.ReadBoolean();
                    yield return new Passanger(name, age, merried) as T;
                }
                yield break;
            }
        }
        public void SaveData(IEnumerable<T> data, string fileName)
        {
            FileInfo file = new FileInfo(fileName);
            if (file.Exists)
                file.Delete();
            using (BinaryWriter writer = new BinaryWriter(File.Open(fileName, FileMode.OpenOrCreate)))
            {
                foreach (var item in data)
                {
                    writer.Write(item.name);
                    writer.Write(item.age);
                    writer.Write(item.merried);
                }
            }
        }
    }
}
