using System.IO;
using Lab_rab_4.Entities;
class Programm
{
    static void Main(string[] args)
    {
        string directway = "D://Bekarev_Lab4//";
        DirectoryInfo directory = new DirectoryInfo(directway);
        if(directory.Exists)
            directory.Delete(true);
        directory.Create();
        Random random = new Random();
        (new FileInfo(directway + Path.GetRandomFileName().Insert(12, ".txt"))).Create().Close();
        for (int i = 0; i < 9; i++)
        {
            int rnd = random.Next(4);
            if (rnd == 0)
                (new FileInfo(directway + Path.GetRandomFileName().Insert(12, ".txt"))).Create().Close();
            else if(rnd == 1)
                (new FileInfo(directway + Path.GetRandomFileName().Insert(12, ".rtf"))).Create().Close();
            else if(rnd == 2)
                (new FileInfo(directway + Path.GetRandomFileName().Insert(12, ".dat"))).Create().Close();
            else
                (new FileInfo(directway + Path.GetRandomFileName().Insert(12, ".inf"))).Create().Close();
        }
        foreach(var file in directory.GetFiles())
            Console.WriteLine($"File {file.Name} with extension {file.Extension}");
        List<Passanger> list = new List<Passanger>();
        list.Add(new Passanger("4", 2, false));
        list.Add(new Passanger("3", 3, true));
        list.Add(new Passanger("1", 5, false));
        list.Add(new Passanger("2", 4, true));
        list.Add(new Passanger("5", 1, true));

        FileService<Passanger> file_serv = new();
        FileInfo file_old = directory.GetFiles("*.txt")[0];
        try
        {
            file_serv.SaveData(list, file_old.FullName);
            string new_path = (directway + "RenameFile.txt");
            FileInfo new_file = new(directway);
            file_old.CopyTo(new_path);
            file_old.Delete(); 
            List<Passanger> new_list = file_serv.ReadFile(new_path).ToList();
            MyCustomComparer<Passanger> my_comparer = new();
            List<Passanger> sorted_list = (new_list.OrderBy(x => x, my_comparer).Select(x => x)).ToList();
            Console.WriteLine("Old list:");
            foreach (var item in list)
            {
                Console.WriteLine(item.ToString());
            }
            Console.WriteLine("Sorted by Name list:");
            foreach (var item in sorted_list)
            {
                Console.WriteLine(item.ToString());
            }
            List<Passanger> list_sorted_by_age = (list.OrderBy(x => x.age).Select(x => x)).ToList();
            Console.WriteLine("Sorted by Age list:");
            foreach (var item in list_sorted_by_age)
            {
                Console.WriteLine(item.ToString());
            }
        }
        catch (IOException ex)
        {
            Console.WriteLine($"Exception have been catch {ex.Message}");
        }
    }
}