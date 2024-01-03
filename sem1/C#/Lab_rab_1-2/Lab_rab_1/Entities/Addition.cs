using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;

namespace Lab_rab_1.Entities
{
    internal class Addition<T>
    {
        public Addition() { }
        public static T Add<T>(T left, T right) where T : IAdditionOperators<T, T, T>
        {
            return left + right;
        }
    }
}
