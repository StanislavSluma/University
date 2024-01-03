using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;
using Lab_rab_1.Collections;

namespace Lab_rab_1.Entities
{
    internal class Lifer
    {
        public delegate void Delegate(string str);
        public event Delegate Event;

        MyCustomCollection<Tarif> tarif_list;
        string? fullname;

        public Lifer(string? fullname)
        {
            this.tarif_list = new MyCustomCollection<Tarif>();
            this.fullname = fullname;
        }

        public void BuyTarif(Tarif tarif)
        {
            tarif_list.Add(tarif);
            if(Event != null)
                Event($"Lifer - BuyTarif: {tarif.Price} => {tarif.Serv}");
        }

        public void DeleteTarif(Tarif tarif)
        {
            tarif_list.Remove(tarif);
        }

        public string? Fullname
        {
            get
            {
                return fullname;
            }
            set
            {
                if (value == null)
                    fullname = "";
                else
                    fullname = value;
            }
        }
        public MyCustomCollection<Tarif>? Tarif_list
        {
            get
            {
                return tarif_list;
            }
        }
    }
}
