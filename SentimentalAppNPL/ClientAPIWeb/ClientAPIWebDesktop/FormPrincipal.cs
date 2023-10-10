using ClientAPIWebDesktop.Modelos;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ClientAPIWebDesktop
{
    /// <summary>
    /// Ejemplo sencillo GET http
    /// </summary>
    public partial class FormPrincipal : Form
    {
        public FormPrincipal()
        {
            InitializeComponent();


            textBox1.Text = "es genial, parece impresionante\r\n" +
                            "es bueno, regular";
        }

        async private void button1_Click(object sender, EventArgs e)
        {
            string baseUrl = "http://192.168.1.186:5000/calificaciones";

            using (HttpClient httpClient = new HttpClient())
            {
                try
                {
                    var mensaje = textBox1.Text.Split('\n');
                    var listaCriticas = new List<Critica>();

                    int contador = 1;

                    foreach (var mensajeLine in mensaje)
                    {
                        var critica = new Critica
                        {
                            Id = contador,
                            Mensaje = mensajeLine.Replace("\r",""),
                            Calificacion = 0 // Valor inicial para Evaluación
                        };

                        listaCriticas.Add(critica);
                        contador++;
                    }

                    string jsonData = JsonConvert.SerializeObject(listaCriticas);

                    var content = new StringContent(jsonData, Encoding.UTF8, "application/json");

                    HttpResponseMessage response = await httpClient.PostAsync(baseUrl, content);

                    if (response.IsSuccessStatusCode)
                    {
                        string responseContent = await response.Content.ReadAsStringAsync();

                        List<Critica> listaRespuesta = JsonConvert.DeserializeObject<List<Critica>>(responseContent);

                        textBox2.Text = "Respuesta de la API:\r\n";
                        foreach (var critica in listaRespuesta)
                        {
                            textBox2.Text += critica.ToString() + "\r\n";
                        }
                    }
                    else
                    {
                        textBox2.Text = "Error en la solicitud: " + response.StatusCode;
                    }
                }
                catch (Exception ex)
                {
                    textBox2.Text = "Error: " + ex.Message;
                }
            }
        }
    }
}
