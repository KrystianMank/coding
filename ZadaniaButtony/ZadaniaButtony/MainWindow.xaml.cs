using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
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

        private void btnZablokuj_Click(object sender, RoutedEventArgs e)
        {
            
        }
    }
}
