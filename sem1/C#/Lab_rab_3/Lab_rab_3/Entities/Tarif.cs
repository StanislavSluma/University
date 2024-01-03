using System;
using System.Collections.Generic;
using System.Data.Common;
using System.Linq;
using System.Reflection.Metadata.Ecma335;
using System.Text;
using System.Threading.Tasks;
using System.Numerics;

namespace Lab_rab_1.Entities
{
    internal class Tarif : IAdditionOperators <Tarif, Tarif, Tarif>
    {
        int price;
        string? serv;
        public Tarif(int price, string serv)
        {
            this.Price = price;
            this.Serv = serv;
        }
        public int Price
        {
            get
            {
                return price;
            }
            set
            {
                if (value < 0)
                    price = 0;
                else
                    price = value;
            }
        }
        public string? Serv
        {
            get
            {
                return serv;
            }
            set
            {
                if (value == null)
                    serv = "Serv #1";
                else
                    serv = value;
            }
        }
        public static Tarif operator +(Tarif left, Tarif right)
        {
            return new Tarif(left.Price + right.Price, "");
        }
    }
}
