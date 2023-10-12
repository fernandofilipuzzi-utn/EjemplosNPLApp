using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WindowsFormsApp13.Models
{
    class Calificacion
    {
        public int Puntuacion { get; set; }
        public string Contenido { get; set; }

        public override string ToString()
        {
            return $"{Contenido};{Puntuacion} ";
        }
    }
}
