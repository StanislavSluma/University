using Lab_rab_1.Collections;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab_rab_1.Entities
{
    internal class Journal
    {
        MyCustomCollection<string> all_events;
        public Journal()
        {
            all_events = new MyCustomCollection<string>();
        }
        public void AllEvents()
        {
            for(int i = 0; i < all_events.Count; i++)
            {
                Console.WriteLine(all_events[i]);
            }
        }
        public void AddEvent(string str)
        {
            all_events.Add(str);
        }
    }
}
