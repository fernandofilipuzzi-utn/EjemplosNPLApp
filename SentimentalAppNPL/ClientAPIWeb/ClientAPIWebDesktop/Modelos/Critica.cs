using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace ClientAPIWebDesktop.Modelos
{
    class Critica
    {
        [JsonProperty("id")]
        public int Id { get; set; }

        [JsonProperty("mensaje")]
        public string Mensaje { get; set; }

        [JsonProperty("calificacion")]
        public int Calificacion { get; set; }

        public override string ToString()
        { 
            return $"{Id},{Mensaje},{Calificacion}";
        }
    }
}
