using Lab_rab_5.Domain;
using SerializerLib;
using System.Timers;

class Programm
{
    static void Main(string[] args)
    {
        Serializer serializer = new();
        List<Hospital> list_of_hospital = new() { new Hospital(), new Hospital(666, "SecondCircle", "Hell"), new Hospital(666, "ThirdCircle", "Hell"), new Hospital(666, "ForthCircle", "Hell"), new Hospital(666, "FifthCircle", "Hell") };
        
        Console.WriteLine("SerializeXML");
        serializer.SerializeXML(list_of_hospital, "D:/AA_curs2/sem1/C#/Lab_rab_5/Hospital1.xml");
        var list1 = serializer.DeSerializeXML("D:/AA_curs2/sem1/C#/Lab_rab_5/Hospital1.xml").ToList();
        bool check = true;
        for (int i = 0; i < list1.Count; i++)
            check = check && list1[i].Equals(list_of_hospital[i]);
        if (check)
            Console.WriteLine("Коллекции равны");
        else
            Console.WriteLine("Коллекции НЕ равны");

        Console.WriteLine("SerializeByLINQ");
        serializer.SerializeByLINQ(list_of_hospital, "D:/AA_curs2/sem1/C#/Lab_rab_5/Hospital2.xml");
        var list2 = serializer.DeSerializeByLINQ("D:/AA_curs2/sem1/C#/Lab_rab_5/Hospital2.xml").ToList();
        check = true;
        for (int i = 0; i < list2.Count; i++)
            check = check && list2[i].Equals(list_of_hospital[i]);
        if (check)
            Console.WriteLine("Коллекции равны");
        else
            Console.WriteLine("Коллекции НЕ равны");
        
        Console.WriteLine("SerializeJSON");
        serializer.SerializeJSON(list_of_hospital, "D:/AA_curs2/sem1/C#/Lab_rab_5/Hospital3.JSON");
        var list3 = serializer.DeSerializeJSON("D:/AA_curs2/sem1/C#/Lab_rab_5/Hospital3.JSON").ToList();
        check = true;
        for (int i = 0; i < list3.Count; i++)
            check = check && list3[i].Equals(list_of_hospital[i]);
        if (check)
            Console.WriteLine("Коллекции равны");
        else
            Console.WriteLine("Коллекции НЕ равны");
    }
}

