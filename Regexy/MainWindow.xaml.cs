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
using System.Text.RegularExpressions;

namespace Regexy
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

        private void replaceMethod_Click(object sender, RoutedEventArgs e)
        {
            string tekst = textBoxReplace.Text;
            string zmienionyTekst = Regex.Replace(tekst, @"czerwony|biały", "czarny");
            labelWynik.Content = zmienionyTekst;
        }

        private void btnKodPocztowy_Click(object sender, RoutedEventArgs e)
        {
            string kodPocztowy = textBoxKodPocztowy.Text;
            Regex regex = new Regex(@"^\d{2}-\d{3}$");
            if (regex.IsMatch(kodPocztowy))
            {
                MessageBox.Show("Kod pocztowy poprawny", "Poprawność kodu pocztowego", MessageBoxButton.OK, MessageBoxImage.Information);
            }
            else
            {
                MessageBox.Show("Kod pocztowy niepoprawny", "Poprawność kodu pocztowego", MessageBoxButton.OK, MessageBoxImage.Warning);

            }
        }

        private void btnEmail_Click(object sender, RoutedEventArgs e)
        {
            string email = textBoxEmail.Text;
            Regex regex = new Regex(@"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$");
            if (regex.IsMatch(email))
            {
                MessageBox.Show("Email poprawny", "Poprawność emailu", MessageBoxButton.OK, MessageBoxImage.Information);
            }
            else
            {
                MessageBox.Show("Email niepoprawny", "Poprawność emailu", MessageBoxButton.OK, MessageBoxImage.Warning);

            }
        }

        private void btnTelefony_Click(object sender, RoutedEventArgs e)
        {
            string telefony = textBoxTelefony.Text;
            Regex regex = new Regex(@"\d{3}-\d{3}-\d{3}");

            MatchCollection matchCollection = regex.Matches(telefony);
            foreach (Match match in matchCollection)
            {
                MessageBox.Show($"Telefon:{match.Value}", "Znajdowanie numerów telefonu", MessageBoxButton.OK, MessageBoxImage.Information);
            }
        }

        private void textBoxDaty_TextChanged(object sender, TextChangedEventArgs e)
        {

        }

        private void btnDaty_Click(object sender, RoutedEventArgs e)
        {
            string data = textBoxDaty.Text;

            Regex regex = new Regex(@"(\d{4})-(\d{2})-(\d{2})");

            string zamiana = "$3-$2-$1";

            string nowaData = regex.Replace(data, zamiana);

            MessageBox.Show($"{nowaData}", "Zmiana kolejności", MessageBoxButton.OK, MessageBoxImage.Information);
        }

        private void btnUsunSpacje_Click(object sender, RoutedEventArgs e)
        {
            string tekstZSpacjami = textBoxSpacje.Text;

            Regex regex = new Regex(@"\s+");

            string nowyTekst = regex.Replace(tekstZSpacjami, " ");

            MessageBox.Show($"{nowyTekst}", "Nowy tekst", MessageBoxButton.OK, MessageBoxImage.Information);
        }

        private void btnDzielenieTekstu_Click(object sender, RoutedEventArgs e)
        {
            string tekstDoPodzielenia = textBoxDzielenie.Text;

            string[] tablica = Regex.Split(tekstDoPodzielenia, @",");

            foreach (string s in tablica)
            {
                labelWyrazy.Content += s +"\n";
            }
        }
    }
}
