namespace Lab_rab_5.Domain
{
    public class Hospital : IEquatable<Hospital>
    {
        public ReceptionDepartment Department { get; set; }
        public string HospitalName { get; set; }

        public Hospital(int amountOfPatient, string reseptionName, string hospitalName)
        {
            Department = new ReceptionDepartment(amountOfPatient, reseptionName);
            HospitalName = hospitalName;
        }

        public Hospital(string hospitalName)
        {
            Department = new();
            HospitalName = hospitalName;
        }

        public Hospital() : this("Hell")
        {

        }

        public bool Equals(Hospital other)
        {
            return this.HospitalName == other.HospitalName && this.Department.Equals(other.Department);
        }
    }
}