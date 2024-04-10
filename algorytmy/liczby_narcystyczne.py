'''
Algorytm sprawdzania liczb narcystycznych
Krystian Mankiewicz 10.04.2024
'''


def dlugosc(a, dl=1):
    if a > 9:
        return dlugosc(a / 10, dl + 1)
    else:
        return dl


def czyNarcystyczna(a):
    suma = 0
    dl = dlugosc(a)
    for i in range(0, dl, 1):
        suma += pow(int(a / pow(10, i)) % 10, dl)
    if suma == a:
        return True
    else:
        return False

def main():
    print("=" * 50)
    print("Program do testowania algorytmu sprawdzania liczb narcystycznych")
    print("=" * 50)

    tak = 't'

    while tak != 'n':
        liczba = int(input("Podaj liczbe do sprawdzenia: "))
        if czyNarcystyczna(liczba):
            print("Liczba jest narcystyczna")
        else:
            print("Liczba nie jest narcystyczna")
        tak = input("Czy kontynować? (n - nie): ")

    print("Dziękuje za korzystanie z programu")


if __name__ == "__main__":
    main()
