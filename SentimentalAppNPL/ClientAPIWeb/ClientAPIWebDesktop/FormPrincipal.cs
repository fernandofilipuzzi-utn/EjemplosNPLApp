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


            tbComentario.Text = "Esta crítica será útil para aquellos que quieran ver, además de una película de ciencia ficción, una parábola política propia del autor de la hipnótica “Asalto a la comisaría del Distrito 13” (1976). Son varias las películas en las que el cine estadounidense se ha preocupado de los estragos causados por los las crisis cíclicas del capitalismo y sus efectos sobre la clase trabajadora, pero pocas veces se ha realizado una película en la cual la crítica se extienda a todo el sistema, con su clasismo y sus mecanismos de control y alienación. En este sentido, la película merece un diez. Pero ojo, como las fabulaciones del protagonista de Memento no debemos convertirnos en esclavos de nuestras teorías; no es necesario que acabemos creyéndonos nuestras propias fantasías.";
        }

        async private void button1_Click(object sender, EventArgs e)
        {
            string baseUrl = "http://localhost:5000/calificaciones";

            using (HttpClient httpClient = new HttpClient())
            {
                try
                {
                    var listaCriticas = new List<Critica>();

                    listaCriticas.Add(new Critica()
                    {
                        Id = 1,
                        Comentario = tbComentario.Text.Replace("\r", "").Replace("\n", "").Replace("\"", "")
                    });


                    string jsonData = JsonConvert.SerializeObject(listaCriticas);

                    var content = new StringContent(jsonData, Encoding.UTF8, "application/json");

                    HttpResponseMessage response = await httpClient.PostAsync(baseUrl, content);

                    if (response.IsSuccessStatusCode)
                    {
                        string responseContent = await response.Content.ReadAsStringAsync();

                        List<Critica> listaRespuesta = JsonConvert.DeserializeObject<List<Critica>>(responseContent);

                        tbRespuesta.Text = "Respuesta de la API:\r\n";
                        foreach (var critica in listaRespuesta)
                        {
                            tbRespuesta.Text += critica.ToString() + "\r\n";
                        }
                    }
                    else
                    {
                        tbRespuesta.Text = "Error en la solicitud: " + response.StatusCode;
                    }
                }
                catch (Exception ex)
                {
                    tbRespuesta.Text = "Error: " + ex.Message;
                }
            }
        }
    }
}
