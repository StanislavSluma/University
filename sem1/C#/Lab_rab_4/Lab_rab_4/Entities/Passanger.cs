using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab_rab_4.Entities
{
    internal class Passanger
    {
        public string? name;
        public int age;
        public bool merried;

        public Passanger(string name, int age, bool merried)
        {
            this.name = name;
            this.age = age;
            this.merried = merried;
        }

        public override string ToString()
        {
            string result = new string($"Name: {this.name}, Age: {this.age}, Merried: {this.merried}");
            return result;
        }
    }
}
