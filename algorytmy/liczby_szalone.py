'''
Algorytm do sprawdzania liczb szalonych
Krystian Mankiewicz 03.04.2024
'''

def czySzalona(a):
    l = [0] * 10

    while a > 0:
        l[a % 10] += 1
        if l[a % 10] > a % 10:
            return False
        a //= 10

    return True


def main():
    print("Progam do sprawdzenia liczb szalonych\n")

    tak = 't'

    while tak != 'n':
        liczba = int(input("Podaj liczbe do sprawdzenia: "))

        if czySzalona(liczba):
            print("Tak")
        else:
            print("Nie")

        tak = input("Czy kontynować? (n - nie): ")

    print("Dziękuje za korzystanie z programu")


if __name__ == "__main__":
    main()