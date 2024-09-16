namespace WinFormsApp2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            
        }
        int moveX = 0;
        int moveY = 0;
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            Random random = new Random();
            int rand1 = random.Next(-1, 1);


            Pen pen = new Pen(Color.Black);
            Font font = new Font(Font.OriginalFontName, Font.Size);
            Brush brush = new SolidBrush(Color.Black);
            e.Graphics.DrawEllipse(pen, (pictureBox1.Width / 2) - 25 + moveX, (pictureBox1.Height / 2) - moveX, 100, 50);
           // e.Graphics.DrawString("DVD", font, brush, (pictureBox1.Width / 2) + moveX, (pictureBox1.Height / 2) + moveY);
        }


        private void timer1_Tick(object sender, EventArgs e)
        {
            //System.Windows.Forms.Timer timer = new System.Windows.Forms.Timer();
            
            moveX += 25;
            moveY += 25;

        }

        private void buttonStart_Click(object sender, EventArgs e)
        {
            timer1.Start();
        }
    }
}
