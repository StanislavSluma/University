using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace Lab_rab_1.Entities
{
    internal class Lifer
    {
        List<Tarif> tarif_list;
        string? fullname;

        public Lifer(string? fullname)
        {
            this.tarif_list = new();
            this.fullname = fullname;
        }
        public void BuyTarif(Tarif tarif)
        {
            tarif_list.Add(tarif);
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
        public List<Tarif>? Tarif_list
        {
            get
            {
                return tarif_list;
            }
        }
    }
}
