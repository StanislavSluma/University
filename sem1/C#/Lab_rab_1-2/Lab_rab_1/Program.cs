using System;
using System.Runtime.InteropServices;
using Lab_rab_1.Collections;
using Lab_rab_1.Entities;

class Programm
{
    public static void Main(string[] args)
    {
        Journal journal = new Journal();
        HMS building = new HMS();
        building.Event += journal.AddEvent;

        building.AddTarif(new Tarif(100, "Serv #1"));
        building.AddTarif(new Tarif(200, "Serv #2"));
        building.AddTarif(new Tarif(50, "Serv #3"));
        building.AddTarif(new Tarif(250, "Serv #4"));

        MyCustomCollection<Lifer> lifers = new MyCustomCollection<Lifer>() { new Lifer("First"), new Lifer("Second"), new Lifer("Third") };
        lifers[0].Event += (string str) => Console.WriteLine($"{str}");
        lifers[1].Event += (string str) => Console.WriteLine($"{str}");
        lifers[2].Event += (string str) => Console.WriteLine($"{str}");

        lifers[0].BuyTarif(new Tarif(100, "Serv #1"));
        lifers[0].BuyTarif(new Tarif(50, "Serv #3"));
        lifers[1].BuyTarif(new Tarif(100, "Serv #1"));
        lifers[1].BuyTarif(new Tarif(200, "Serv #2"));
        lifers[2].BuyTarif(new Tarif(100, "Serv #1"));
        lifers[2].BuyTarif(new Tarif(200, "Serv #2"));
        lifers[2].BuyTarif(new Tarif(50, "Serv #3"));
        lifers[2].BuyTarif(new Tarif(250, "Serv #4"));

        Console.WriteLine("");
        building.AddLifer(lifers[0]);
        building.AddLifer(lifers[1]);
        building.AddLifer(lifers[2]);
        Console.WriteLine($"Amount Serv #1: {building.AmountServiece("Serv #1")}");
        Console.WriteLine($"Amount Serv #2: {building.AmountServiece("Serv #2")}");
        Console.WriteLine($"Amount Serv #3: {building.AmountServiece("Serv #3")}");
        Console.WriteLine($"Amount Serv #4: {building.AmountServiece("Serv #4")}");
        Console.WriteLine($"All price First: {building.UsedTarifsOfLifer("First")}");
        Console.WriteLine($"All price Second: {building.UsedTarifsOfLifer("Second")}");
        Console.WriteLine($"All price Third: {building.UsedTarifsOfLifer("Third")}");
        Console.WriteLine($"All price in building: {building.PriceOfAllTarifs()}");
        Console.WriteLine("");
        journal.AllEvents();

        Console.WriteLine("Foreach");
        foreach(var lifer in lifers)
        {
            Console.WriteLine($"{lifer.Fullname}");
        }
        Console.WriteLine("try - catch");
        try
        {
            var a = lifers[7];
        }
        catch(IndexOutOfRangeException)
        {
            Console.WriteLine("IndexOfRange");
        }
        try
        {
            lifers.Remove(new Lifer("asdasd"));
        }
        catch(Exception e)
        {
            if(e.Message == "Item Not Found")
            {
                Console.WriteLine(e.Message);
            }
        }
    }
}
