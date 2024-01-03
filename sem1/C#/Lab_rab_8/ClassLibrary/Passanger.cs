using System;
using System.Collections.Generic;
using System.ComponentModel.Design.Serialization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassLibrary
{
    public class Passanger
    {
        public int Id { get; set; }
        public string? Name { get; set; }
        public bool Baggage { get; set; }
        public Passanger(int id, string? name, bool baggage)
        {
            Id = id;
            Name = name;
            Baggage = baggage;
        }
    }
}
