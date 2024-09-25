using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace ZadaniaButtony
{
    /// <summary>
    /// Logika interakcji dla klasy MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void btnPowieksz_Click(object sender, RoutedEventArgs e)
        {
            btnPowieksz.Width += btnPowieksz.Width * 0.2;
            btnPowieksz.Height += btnPowieksz.Height * 0.2;

        }
        bool change = false;
        private void btnZablokuj_Click(object sender, RoutedEventArgs e)
        {
            Button[] buttons = { btnPowieksz, button1, button2 };

            foreach (Button button in buttons)
            {
                button.IsEnabled = change; 
            }

            change = !change; 

        }

        private void button1_Click(object sender, RoutedEventArgs e)
        {
            button1.Visibility = Visibility.Hidden;
            button2.Visibility = Visibility.Visible;
            
        }

        private void button2_Click(object sender, RoutedEventArgs e)
        {
            button1.Visibility = Visibility.Visible;
            button2.Visibility = Visibility.Hidden;
        }
    }
}
