using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab_rab_5.Domain
{
    public interface ISerializer
    {
        IEnumerable<Hospital> DeSerializeByLINQ(string fileName);
        IEnumerable<Hospital> DeSerializeXML(string fileName);
        IEnumerable<Hospital> DeSerializeJSON(string fileName);
        void SerializeByLINQ(IEnumerable<Hospital> xxx, string fileName);
        void SerializeXML(IEnumerable<Hospital> xxx, string fileName);
        void SerializeJSON(IEnumerable<Hospital> xxx, string fileName);
    }
}
