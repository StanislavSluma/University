using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace Lab_rab_1.Entities
{
    internal class HMS // Housing Maintence Servieces
    {
        Dictionary<string,Tarif> tarif_dict;
        Dictionary<string,Lifer> lifer_dict;
        public delegate void Delegate(string str);
        public event Delegate? Event;

        public HMS()
        {
            tarif_dict = new();
            lifer_dict = new();
        }
        public void AddTarif(Tarif tarif)
        {
            tarif_dict.Add(tarif.Serv, tarif);
            Event?.Invoke($"HMS - AddTarif: {tarif.Price} => {tarif.Serv}");
        }
        public void AddLifer(Lifer lifer)
        {
            lifer_dict.Add(lifer.Fullname, lifer);
            Event?.Invoke($"HMS - AddLifer: {lifer.Fullname}");
        }
        public void LiferBuyTarif(string name, string Service)
        {
            if (lifer_dict.ContainsKey(name))
            {
                if (tarif_dict.ContainsKey(Service))
                {
                    lifer_dict[name].BuyTarif(tarif_dict[Service]);
                    Event?.Invoke($"Lifer {name} buy Tarif {Service}");
                }
                else
                {
                    Console.WriteLine($"Tarif {Service} not search");
                    Event?.Invoke($"Tarif {Service} not search");
                }
            }
            else
            {
                Console.WriteLine($"Lifer {name} not record in HMS");
                Event?.Invoke($"Tarif {Service} not record in HMS");
            }
        }
        public int AmountServiece(string serv)
        {
            int result = 0;
            foreach(var lifer in lifer_dict)
            {
                for (int i = 0; i < lifer.Value.Tarif_list.Count; i++)
                {
                    if (lifer.Value.Tarif_list[i].Serv == serv)
                    {
                        result++;
                    }
                }
            }
            return result;
        }
        public int PriceOfAllTarifs()
        {
            int result = (from lifer in lifer_dict
                           select lifer.Value.Tarif_list.Aggregate((x, y) => 
                           Addition<Tarif>.Add<Tarif>(x, y)).Price).Aggregate((x,y)=>x+y);
            return result;
        }
        public List<Tarif> GetTarifSortedList()
        {
            var res = tarif_dict.OrderBy(x => x.Value.Price).Select(x => x.Value);
            return res.ToList();
        }
        public int UsedTarifsOfLifer(string fullname)
        {
            int result = (from tarif in lifer_dict[fullname].Tarif_list
                          select tarif).Aggregate((x, y) => Addition<Tarif>.Add<Tarif>(x, y)).Price;
            return result;
        }
        public string GetRichestLifer()
        {
            string result = (from lifer in lifer_dict
                             orderby lifer.Value.Tarif_list.Aggregate((x, y) =>
                             Addition<Tarif>.Add<Tarif>(x, y)).Price
                             select lifer.Value).First().Fullname;
            return result;
        }
        public int AmountMoreThenSetted(int setted)
        {
            int amount = (from lifer in lifer_dict
                          select lifer.Value.Tarif_list.Aggregate((x, y) =>
                          Addition<Tarif>.Add<Tarif>(x, y)).Price).Count(x => x > setted);
            return amount;
        }

        public List<(int, int)> GroupBy()
        {
            List<(int, int)> list = new() { (1, 1), (1, 2), (1, 3), (2, 1), (3, 1), (3, 2), (2, 2), (2, 3) };
            var res = (list.GroupBy(x => x.Item1).First(group => group.Key == 1)).ToList();
            Console.WriteLine();
            foreach (var el in res)
            {
                Console.WriteLine(el);
            }
            return res;
        }
        public List<int> ListOfServicePrice(string fullname)
        {
            var result = lifer_dict[fullname].Tarif_list.Select(x => x.Price).ToList();
            return result;
        }
    }
}
