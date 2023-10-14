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

        [JsonProperty("comentario")]
        public string Comentario { get; set; }

        [JsonProperty("valoracion")]
        public int Valoracion { get; set; }

        public override string ToString()
        { 
            return $"{Id},{Comentario},{Valoracion}";
        }
    }
}
