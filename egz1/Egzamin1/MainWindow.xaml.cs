using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
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

namespace Egzamin1
{
    /// <summary>
    /// Logika interakcji dla klasy MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            labelCena.Content = "Cena: 1 zł";
            image.Source = new BitmapImage(new Uri(@"Resources/pocztowka.png", UriKind.Relative));
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            if (radioPoczt.IsChecked == true)
            {
                labelCena.Content = "Cena: 1 zł";
                image.Source = new BitmapImage(new Uri(@"Resources/pocztowka.png", UriKind.Relative));
            }
            else if (radioList.IsChecked == true)
            {
                labelCena.Content = "Cena: 1,5 zł";
                image.Source = new BitmapImage(new Uri(@"Resources/list.png", UriKind.Relative));
            }
            else
            {
                labelCena.Content = "Cena: 10 zł";
                image.Source = new BitmapImage(new Uri(@"Resources/paczka.png", UriKind.Relative));
            }
        }

        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
            string kodPocztowy = textBoxKodPocztowy.Text;
            string email = textBoxEmail.Text;
            string ulica = textBoxUlica.Text;
            string miasto = textBoxMiasto.Text;


            Regex regexKodPocztowy = new Regex(@"^\d{5}$");
            Regex regexEmail = new Regex(@"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$");

            if (kodPocztowy.Length == 0 || email.Length == 0 || ulica.Length == 0 || miasto.Length == 0)
            {
                MessageBox.Show("Dane adresowe nie zostały wprowadzone", "Niepowodzenie", MessageBoxButton.OK, MessageBoxImage.Warning);
            }
            else
            {
                if (kodPocztowy.Length == 5)
                {
                    if (regexKodPocztowy.IsMatch(kodPocztowy))
                    {
                        if (!regexEmail.IsMatch(email))
                        {
                            MessageBox.Show("Nieprawidłowy email", "Niepowodzenie", MessageBoxButton.OK, MessageBoxImage.Warning);
                        }
                        else
                        {
                            MessageBox.Show("Dane przesyłki zostały wprowadzone", "Powodzenie", MessageBoxButton.OK, MessageBoxImage.Information);
                        }
                    }
                    else
                    {
                        MessageBox.Show("Kod pocztowy powinien się składać z samych cyfr", "Niepowodzenie", MessageBoxButton.OK, MessageBoxImage.Warning);

                    }
                }
                else
                {
                    MessageBox.Show("Nieprawidłowa liczba cyfr w kodzie pocztowym", "Niepowodzenie", MessageBoxButton.OK, MessageBoxImage.Warning);
                }
            }


            

            

        }
    }
}
