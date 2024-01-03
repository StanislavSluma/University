using Lab_rab_1.Collections;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab_rab_1.Entities
{
    internal class HMS // Housing Maintence Servieces
    {
        MyCustomCollection<Tarif> tarif_list;
        MyCustomCollection<Lifer> lifer_list;
        public delegate void Delegate(string str);
        public event Delegate? Event;

        public HMS()
        {
            tarif_list = new MyCustomCollection<Tarif>();
            lifer_list = new MyCustomCollection<Lifer>();
        }
        public void AddTarif(Tarif tarif)
        {
            tarif_list.Add(tarif);
            Event?.Invoke($"HMS - AddTarif: {tarif.Price} => {tarif.Serv}");
        }
        public void AddLifer(Lifer lifer)
        {
            lifer_list.Add(lifer);
            Event?.Invoke($"HMS - AddLifer: {lifer.Fullname}");
        }
        public int UsedTarifsOfLifer(string fullname)
        {
            Tarif result = new Tarif(0, "");
            for (int i = 0; i < lifer_list.Count; i++)
            {
                if (lifer_list[i].Fullname == fullname)
                {
                    for(int j = 0; j < lifer_list[i].Tarif_list.Count; j++)
                    {
                        result = Addition<Tarif>.Add<Tarif>(result, lifer_list[i].Tarif_list[j]);
                    }
                    break;
                }
            }
            return result.Price;
        }

        public int AmountServiece(string serv)
        {
            int result = 0;
            for(int i = 0; i < lifer_list.Count; i++)
            {
                for(int j = 0; j < lifer_list[i].Tarif_list.Count; j++)
                {
                    if (lifer_list[i].Tarif_list[j].Serv == serv)
                    {
                        result++;
                    }
                }
            }
            return result;
        }

        public int PriceOfAllTarifs()
        {
            int result = 0;
            for (int i = 0; i < lifer_list.Count; i++)
            {
                for (int j = 0; j < lifer_list[i].Tarif_list.Count; j++)
                {
                    result += lifer_list[i].Tarif_list[j].Price;
                }
            }
            return result;
        }
    }
}
