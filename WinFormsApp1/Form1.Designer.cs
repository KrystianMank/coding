namespace WinFormsApp1
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            textBoxRNG = new TextBox();
            buttonLosuj = new Button();
            textBoxInput = new TextBox();
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            textBoxProby = new TextBox();
            labelNapisKoniec = new Label();
            SuspendLayout();
            // 
            // textBoxRNG
            // 
            textBoxRNG.Location = new Point(69, 118);
            textBoxRNG.Name = "textBoxRNG";
            textBoxRNG.ReadOnly = true;
            textBoxRNG.Size = new Size(125, 27);
            textBoxRNG.TabIndex = 0;
            // 
            // buttonLosuj
            // 
            buttonLosuj.Location = new Point(189, 164);
            buttonLosuj.Name = "buttonLosuj";
            buttonLosuj.Size = new Size(94, 29);
            buttonLosuj.TabIndex = 1;
            buttonLosuj.Text = "Losuj";
            buttonLosuj.UseVisualStyleBackColor = true;
            buttonLosuj.Click += buttonLosuj_Click;
            // 
            // textBoxInput
            // 
            textBoxInput.Location = new Point(168, 30);
            textBoxInput.Name = "textBoxInput";
            textBoxInput.Size = new Size(125, 27);
            textBoxInput.TabIndex = 2;
            textBoxInput.Text = "1";
            textBoxInput.TextChanged += textBoxInput_TextChanged;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(157, 7);
            label1.Name = "label1";
            label1.Size = new Size(162, 20);
            label1.TabIndex = 3;
            label1.Text = "Liczba do wylosowania";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(69, 95);
            label2.Name = "label2";
            label2.Size = new Size(136, 20);
            label2.TabIndex = 4;
            label2.Text = "Wylosowana liczba";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(303, 95);
            label3.Name = "label3";
            label3.Size = new Size(87, 20);
            label3.TabIndex = 5;
            label3.Text = "Liczba prób";
            // 
            // textBoxProby
            // 
            textBoxProby.Location = new Point(291, 118);
            textBoxProby.Name = "textBoxProby";
            textBoxProby.ReadOnly = true;
            textBoxProby.Size = new Size(125, 27);
            textBoxProby.TabIndex = 6;
            // 
            // labelNapisKoniec
            // 
            labelNapisKoniec.AutoSize = true;
            labelNapisKoniec.Location = new Point(49, 219);
            labelNapisKoniec.Name = "labelNapisKoniec";
            labelNapisKoniec.Size = new Size(0, 20);
            labelNapisKoniec.TabIndex = 7;
            labelNapisKoniec.Click += label4_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(486, 253);
            Controls.Add(labelNapisKoniec);
            Controls.Add(textBoxProby);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(textBoxInput);
            Controls.Add(buttonLosuj);
            Controls.Add(textBoxRNG);
            Name = "Form1";
            Text = "Form1";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private TextBox textBoxRNG;
        private Button buttonLosuj;
        private TextBox textBoxInput;
        private Label label1;
        private Label label2;
        private Label label3;
        private TextBox textBoxProby;
        private Label labelNapisKoniec;
    }
}
