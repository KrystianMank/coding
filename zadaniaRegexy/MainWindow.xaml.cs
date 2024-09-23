using System;
using System.Collections.Generic;
using System.Diagnostics.CodeAnalysis;
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

namespace zadaniaRegexy
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

        private void btnWypiszDaty_Click(object sender, RoutedEventArgs e)
        {
            string textZDatami = textBoxTextZDatami.Text;
            Regex regex = new Regex(@"(\d{2})-(\d{2})-(\d{4})");

            MatchCollection matchCollection = regex.Matches(textZDatami);

            foreach (Match match in matchCollection)
            {
                if (match.Success)
                {
                    labelDaty.Content += match.Value+"\n";
                }
            }
        }

        private void btnSprawdzPesel_Click(object sender, RoutedEventArgs e)
        {
            string pesel = textBoxPesel.Text;
            Regex regex = new Regex(@"^\d{11}$");
            int[] wagi = { 1, 3, 7, 9, 1, 3, 7, 9, 1, 3 };
            int[] liczba = new int[11];
            int suma = 0;

            if (regex.IsMatch(pesel))
            {
                // Konwersja cyfr PESEL na tablicę liczb
                for (int i = 0; i < 11; i++)
                {
                    liczba[i] = pesel[i] - '0'; // Bezpośrednia konwersja znaku na liczbę
                }

                // Obliczanie sumy kontrolnej
                for (int i = 0; i < 10; i++)
                {
                    suma += liczba[i] * wagi[i];
                }
                suma = suma % 10;
                suma = 10 - suma;

                // Sprawdzenie sumy kontrolnej z ostatnią cyfrą PESEL
                if (suma == liczba[10])
                {
                    MessageBox.Show("Numer PESEL poprawny", "Poprawność numeru PESEL", MessageBoxButton.OK, MessageBoxImage.Information);
                }
                else
                {
                    MessageBox.Show("Numer PESEL niepoprawny", "Poprawność numeru PESEL", MessageBoxButton.OK, MessageBoxImage.Warning);
                }
            }
            else
            {
                MessageBox.Show("Wprowadź poprawny numer PESEL składający się z 11 cyfr.", "Błąd", MessageBoxButton.OK, MessageBoxImage.Error);
            }

        }

        private void btnUsunSpacje_Click(object sender, RoutedEventArgs e)
        {
            string tekst = textBoxSpacje.Text;
            Regex regex = new Regex(@"\s+");

            string nowyTekst = regex.Replace(tekst, " ");
            textBoxBezSpacji.Text = nowyTekst;
        }

        private void btnDopasuj_Click(object sender, RoutedEventArgs e)
        {
            string tekst = textBoxTekst.Text;
            Regex regex = new Regex(@"[A-Z][a-z]*");

            MatchCollection matchCollection = regex.Matches(tekst);

            foreach (Match match in matchCollection)
            {
                if (match.Success)
                {
                    textBoxDopasowanie.Text += match.Value + "\n";
                }
            }
        }

        private void btnAdresyURL_Click(object sender, RoutedEventArgs e)
        {
            string tekst = textBoxTekstZAdresami.Text;
            Regex regex = new Regex(@"https?:\/\/(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}(\/\S*)?");

            MatchCollection matchCollection = regex.Matches(tekst);

            foreach (Match match in matchCollection)
            {
                if (match.Success)
                {
                    textBoxAdresyURL.Text += match.Value + "\n";
                }
            }
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            string tekst = textBoxNumerBankowy.Text;
            string numer = Regex.Replace(tekst, "-","");
            int[] wynik = new int[16];
            int suma = 0;
            
            for(int i = 0; i<numer.Length; i++)
            {
                wynik[i] = (numer[i] - '0');
                if (i % 2 == 0)
                {
                    wynik[i] *= 2;
                    if (wynik[i] > 9) wynik[i] -= 9;
                }
                suma += wynik[i];
            }
            if(suma % 10 == 0)
            {
                MessageBox.Show("Numer karty kredytowej poprawny", "Poprawność numeru", MessageBoxButton.OK, MessageBoxImage.Information);
            }
            else
            {
                MessageBox.Show("Numer karty kredytowej niepoprawny", "Poprawność numeru", MessageBoxButton.OK, MessageBoxImage.Warning);

            }


            MessageBox.Show($"{suma}", "ddd", MessageBoxButton.OK, MessageBoxImage.Error);
        }
    }

}
