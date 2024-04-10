'''
Algorytm do sprawdzania czy liczba jest doskonala
Krystian Mankiewicz 13.03.2024
'''


def czyDoskonala(liczba):
    if liczba < 1:
        return False
    suma = 0
    i = 1
    while i < liczba:
        if liczba % i == 0:
            suma += i
        i += 1

    if suma == liczba:
        return True
    else:
        return False


def main():
    print("Progam do sprawdzenia czy liczba jest doskonała\n")

    tak = 't'

    while tak != 'n':
        liczba = int(input("Podaj liczbe do sprawdzenia: "))
        if czyDoskonala(liczba):
            print("Liczba jest doksonala")
        else:
            print("Liczba nie jest doskonala")
        tak = input("Czy kontynować? (n - nie): ")

    print("Dziękuje za korzystanie z programu")


if __name__ == "__main__":
    main()