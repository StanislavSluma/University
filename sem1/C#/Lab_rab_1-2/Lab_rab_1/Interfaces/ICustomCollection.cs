using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab_rab_1.Interfaces
{
    internal interface ICustomCollection<T>
    {
        int Count { get; } // amount items in collection
        T this[int index] { get; set; } // Indexator
        void Reset(); // cursor in begin
        void Next(); // cursor in next position
        void Prev(); // cursor in prev position
        T Current(); // current item under cursor
        void Add(T item); // add item
        void Remove(T item); // remove item
        T RemoveCurrent(); // remove current item
    }
}