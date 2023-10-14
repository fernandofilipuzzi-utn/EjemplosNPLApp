
namespace ClientAPIWebDesktop
{
    partial class FormPrincipal
    {
        /// <summary>
        /// Variable del diseñador necesaria.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpiar los recursos que se estén usando.
        /// </summary>
        /// <param name="disposing">true si los recursos administrados se deben desechar; false en caso contrario.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código generado por el Diseñador de Windows Forms

        /// <summary>
        /// Método necesario para admitir el Diseñador. No se puede modificar
        /// el contenido de este método con el editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            this.tbComentario = new System.Windows.Forms.TextBox();
            this.tbRespuesta = new System.Windows.Forms.TextBox();
            this.btnEnviar = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // tbComentario
            // 
            this.tbComentario.Location = new System.Drawing.Point(1, 2);
            this.tbComentario.Multiline = true;
            this.tbComentario.Name = "tbComentario";
            this.tbComentario.Size = new System.Drawing.Size(692, 189);
            this.tbComentario.TabIndex = 0;
            // 
            // tbRespuesta
            // 
            this.tbRespuesta.Location = new System.Drawing.Point(1, 197);
            this.tbRespuesta.Multiline = true;
            this.tbRespuesta.Name = "tbRespuesta";
            this.tbRespuesta.Size = new System.Drawing.Size(692, 158);
            this.tbRespuesta.TabIndex = 1;
            // 
            // btnEnviar
            // 
            this.btnEnviar.Location = new System.Drawing.Point(703, 29);
            this.btnEnviar.Name = "btnEnviar";
            this.btnEnviar.Size = new System.Drawing.Size(113, 44);
            this.btnEnviar.TabIndex = 2;
            this.btnEnviar.Text = "Enviar";
            this.btnEnviar.UseVisualStyleBackColor = true;
            this.btnEnviar.Click += new System.EventHandler(this.button1_Click);
            // 
            // FormPrincipal
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(828, 367);
            this.Controls.Add(this.btnEnviar);
            this.Controls.Add(this.tbRespuesta);
            this.Controls.Add(this.tbComentario);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Name = "FormPrincipal";
            this.Text = "Form Principal";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox tbComentario;
        private System.Windows.Forms.TextBox tbRespuesta;
        private System.Windows.Forms.Button btnEnviar;
    }
}

