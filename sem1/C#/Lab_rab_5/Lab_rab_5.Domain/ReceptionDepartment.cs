using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab_rab_5.Domain
{
    public class ReceptionDepartment : IEquatable<ReceptionDepartment>
    {
        public int AmountOfPatient { get; set; }
        public string ReceptionName { get; set; }

        public ReceptionDepartment(int amountOfPatient, string receptionName)
        {
            AmountOfPatient = amountOfPatient;
            ReceptionName = receptionName;
        }

        public ReceptionDepartment() : this(666, "FirstCircle")
        {

        }

        public bool Equals(ReceptionDepartment? other)
        {
            return this.ReceptionName == other.ReceptionName && this.AmountOfPatient == other.AmountOfPatient;
        }
    }
}
