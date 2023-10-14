using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Runtime.Serialization.Formatters.Binary;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using EditorDataSet.Models;

namespace EditorDataSet
{
    public partial class Form1 : Form
    {
        List<Calificacion> calificaciones = new List<Calificacion>();
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string path = Application.StartupPath;
            FileStream fs = null;
            BinaryFormatter bf = new BinaryFormatter();

            try
            {
                fs = new FileStream(Path.Combine(path, "datos.dat"), FileMode.Open, FileAccess.Read);
                calificaciones = bf.Deserialize(fs) as List<Calificacion>;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
            finally
            {
                if (fs != null) fs.Close();
            }

            if (calificaciones == null)
                calificaciones = new List<Calificacion>();
        }

        private void btnAgregarValoracion_Click(object sender, EventArgs e)
        {
            int puntuacion = Convert.ToInt32(nupValoracion.Value);
            string contenido = tbComentario.Text.Replace("\r", "").Replace("\n", "").Replace("\t", "");

            calificaciones.Add(new Calificacion
            {
                Puntuacion = puntuacion,
                Contenido = contenido
            });

            nupValoracion.Value = 0;
            tbComentario.Clear();
        }


        private void btnExportar_Click(object sender, EventArgs e)
        {
            saveFileDialog1.Title = "Exportando las críticas";
            saveFileDialog1.Filter = "Fichero json|*.json";

            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                FileStream fs = null;
                StreamWriter sw = null;

                try
                {
                    fs = new FileStream(saveFileDialog1.FileName, FileMode.Create, FileAccess.Write);
                    sw = new StreamWriter(fs);

                    string pathDir = Path.GetDirectoryName(saveFileDialog1.FileName);

                    sw.WriteLine("[");

                    int n = 0;
                    foreach (Calificacion c in calificaciones)
                    {
                        string contenido = c.Contenido.Replace("\"", "\\\"").Replace("\r", "").Replace("\n", "").Replace("(", "").Replace("\n", "").Replace(")", "");
                        contenido = contenido.Length > 500 ? contenido.Substring(0, 500) : contenido;
                        sw.WriteLine($"{{\"comentario\" : \"{contenido}\",\"valoracion\":{c.Puntuacion}}}");
                        n++;
                        if (n < calificaciones.Count) sw.Write(',');
                    }
                    sw.WriteLine("]");
                    sw.Close();
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);
                }
                finally
                {
                    if (fs != null)
                    {
                        if (sw != null) sw.Close();
                        fs.Close();
                        fs.Dispose();
                    }
                }
            }
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            string path = Application.StartupPath;
            FileStream fs = null;
            BinaryFormatter bf = new BinaryFormatter();

            try
            {
                fs = new FileStream(Path.Combine(path, "datos.dat"), FileMode.Create,
                                                                       FileAccess.Write);
                bf.Serialize(fs, calificaciones);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
            finally
            {
                if (fs != null) fs.Close();
            }
        }
    }
}
