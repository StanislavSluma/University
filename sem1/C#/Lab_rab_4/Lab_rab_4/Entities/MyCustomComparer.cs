using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab_rab_4.Entities
{
    internal class MyCustomComparer<T> : IComparer<T> where T : Passanger
    {
        public int Compare(T? x, T? y)
        {
            if (x == null || y == null) throw new ArgumentNullException();
            return string.Compare(x.name, y.name, StringComparison.Ordinal); 
        }
    }
}
