'''
Algorytm liczby Smitha
Krystian Mankiewicz 13.03.2024
'''


def sumaCyfr(liczba):
    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba //= 10

    return suma


def czyLiczbaSmitha(a):
    suma = 0
    b = a
    i = 2
    while i <= (b / 2):
        while a % i == 0:
            suma += sumaCyfr(i)
            a //= i
        i += 1

    if suma == sumaCyfr(b):
        return True
    else:
        return False


def main():
    print("=" * 50)
    print("Program do testowania algorytmu sprawdzania liczb Smitha")
    print("=" * 50)

    tak = 't'

    while tak != 'n':
        liczba = int(input("Podaj liczbe do sprawdzenia: "))
        if czyLiczbaSmitha(liczba):
            print("Liczba należy do zbioru liczb Smitha")
        else:
            print("Liczba nie należy do zbioru")
        tak = input("Czy kontynować? (n - nie): ")

    print("Dziękuje za korzystanie z programu")


if __name__ == "__main__":
    main()
