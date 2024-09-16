namespace WinFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        int proby = 0;
        private void buttonLosuj_Click(object sender, EventArgs e)
        {
            proby++;
            int liczbaDoWylosowania = Convert.ToInt32(textBoxInput.Text);
            Random random = new Random();
            int rand = 0;
            if (liczbaDoWylosowania < 0)
            {
                rand = random.Next(liczbaDoWylosowania - 10, -1);
            }
            else
            {
                rand = random.Next(0, liczbaDoWylosowania + 10);
            }

            textBoxRNG.Text = rand.ToString();
            if (liczbaDoWylosowania == rand)
            {
                labelNapisKoniec.Text = "By wylosowaæ podan¹ liczbê potrzeba by³o Ci " + proby + " prób";
            }
            else
            {
                textBoxProby.Text = proby.ToString();
            }
        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void textBoxInput_TextChanged(object sender, EventArgs e)
        {
            textBoxRNG.Clear();
            textBoxProby.Clear();
            labelNapisKoniec.Text = "";
            proby = 0;
        }
    }
}
