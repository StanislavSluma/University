using System;
using System.Runtime.ExceptionServices;
using System.Runtime.InteropServices;
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

        building.AddLifer(new Lifer("First"));
        building.AddLifer(new Lifer("Second"));
        building.AddLifer(new Lifer("Third"));

        building.LiferBuyTarif("First", "Serv #1");
        building.LiferBuyTarif("First", "Serv #3");
        building.LiferBuyTarif("Second", "Serv #1");
        building.LiferBuyTarif("Second", "Serv #2");
        building.LiferBuyTarif("Third", "Serv #1");
        building.LiferBuyTarif("Third", "Serv #2");
        building.LiferBuyTarif("Third", "Serv #3");
        building.LiferBuyTarif("Third", "Serv #4");

        Console.WriteLine("");
        
        Console.WriteLine($"Amount Serv #1: {building.AmountServiece("Serv #1")}");
        Console.WriteLine($"Amount Serv #2: {building.AmountServiece("Serv #2")}");
        Console.WriteLine($"Amount Serv #3: {building.AmountServiece("Serv #3")}");
        Console.WriteLine($"Amount Serv #4: {building.AmountServiece("Serv #4")}");

        Console.WriteLine("");
        journal.AllEvents();
        Console.WriteLine("");

        Console.WriteLine("Tarif list ordered by price:");
        List<Tarif> tarif_list = building.GetTarifSortedList();
        foreach(Tarif tarif in tarif_list)
            Console.WriteLine($"Tarif {tarif.Serv} Price {tarif.Price}");
        Console.WriteLine($"\nAll price in building: {building.PriceOfAllTarifs()}");

        Console.WriteLine($"\nAll price First: {building.UsedTarifsOfLifer("First")}");
        Console.WriteLine($"All price Second: {building.UsedTarifsOfLifer("Second")}");
        Console.WriteLine($"All price Third: {building.UsedTarifsOfLifer("Third")}");
        Console.WriteLine($"\nRichest Lifer: {building.GetRichestLifer()}");

        Console.WriteLine($"\nAmount Lifer Who Payed More Then Setted(299): {building.AmountMoreThenSetted(299)}");
        var list = building.ListOfServicePrice("First");
        foreach (var item in list)
        {
            Console.Write($"{item} ");
        }
        building.GroupBy();
    }
}
