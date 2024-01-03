using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab_rab_1.Entities
{
    internal class Journal
    {
        List<string> all_events;
        public Journal()
        {
            all_events = new();
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
