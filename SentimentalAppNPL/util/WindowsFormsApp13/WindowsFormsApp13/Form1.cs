using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using WindowsFormsApp13.Models;

namespace WindowsFormsApp13
{
    public partial class Form1 : Form
    {
        List<Calificacion> calificaciones = new List<Calificacion>();
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int puntuacion = Convert.ToInt32(textBox2.Text);
            string contenido = textBox1.Text.Replace("\r","").Replace("\n", "").Replace("\t", "");

            calificaciones.Add(new Calificacion{
                Puntuacion = puntuacion,
                Contenido = contenido
            });
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                FileStream fs = new FileStream(saveFileDialog1.FileName, FileMode.OpenOrCreate, FileAccess.Write);
                StreamWriter sw = new StreamWriter(fs);
                foreach (Calificacion c in calificaciones)
                {
                    sw.WriteLine(c.ToString());
                }
                sw.Close();
            }
        }
    }
}
