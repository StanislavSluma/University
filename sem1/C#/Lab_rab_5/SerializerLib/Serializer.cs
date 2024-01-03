using Lab_rab_5.Domain;
using System.Xml.Linq;
using System.Xml.Serialization;
using System.Text.Json;
using System;

namespace SerializerLib
{
    public class Serializer : ISerializer
    {
        public IEnumerable<Hospital> DeSerializeByLINQ(string fileName)
        {
            XDocument xdoc = XDocument.Load(fileName);
            var res = xdoc.Element("ListOfHospital")
                .Elements("Hospital")
                .Select(x => new Hospital
                (
                    int.Parse(x.Element("Department").Element("AmountOfPatient").Value),
                    x.Element("Department").Element("ReceptionName").Value,
                    x.Element("HospitalName").Value
                ));
            return res;
        }
        public IEnumerable<Hospital> DeSerializeXML(string fileName)
        {
            XmlSerializer formatter = new XmlSerializer(typeof(List<Hospital>));
            using (FileStream fs = new FileStream(fileName, FileMode.OpenOrCreate))
            {
                return formatter.Deserialize(fs) as List<Hospital>;
            }
        }
        public IEnumerable<Hospital> DeSerializeJSON(string fileName)
        {
            using (FileStream fs = new FileStream(fileName, FileMode.OpenOrCreate))
            {
                var res = JsonSerializer.Deserialize<IEnumerable<Hospital>>(fs);
                return res;
            }
        }
        public void SerializeByLINQ(IEnumerable<Hospital> xxx, string fileName)
        {
            XDocument xdoc = new XDocument();
            XElement list_of_hospital = new XElement("ListOfHospital");
            foreach(var elem in xxx)
            {
                XElement hospital = new XElement("Hospital");
                hospital.Add(new XElement("HospitalName", elem.HospitalName));
                XElement depart = new XElement("Department");
                depart.Add(new XElement("AmountOfPatient", elem.Department.AmountOfPatient));
                depart.Add(new XElement("ReceptionName", elem.Department.ReceptionName));
                hospital.Add(new XElement(depart));
                list_of_hospital.Add(hospital);
            }
            xdoc.Add(list_of_hospital);
            xdoc.Save(fileName);
        }
        public void SerializeXML(IEnumerable<Hospital> xxx, string fileName)
        {
            XmlSerializer formatter = new XmlSerializer(typeof(List<Hospital>));
            using (FileStream fs = new FileStream(fileName, FileMode.OpenOrCreate))
            {
                formatter.Serialize(fs, xxx.ToList());
            }
        }
        public void SerializeJSON(IEnumerable<Hospital> xxx, string fileName)
        {
            using (FileStream fs = new FileStream(fileName, FileMode.OpenOrCreate))
            {
                JsonSerializer.Serialize(fs, xxx, new JsonSerializerOptions { WriteIndented = true});
            }
        }
    }
}