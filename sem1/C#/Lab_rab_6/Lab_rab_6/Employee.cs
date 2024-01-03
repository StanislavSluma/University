using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab_rab_6
{
    internal class Employee
    {
        public string Name { get; set; }
        public int Age { get; set; }
        public bool Merried { get; set; }

        public Employee(string name, int age, bool merried)
        {
            Name = name;
            Age = age;
            Merried = merried;
        }

        public Employee() : this("First", 18, true) { }
    }
}
