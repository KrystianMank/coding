'''
Algorytm do sprawdzania liczb gładkich
Krystian Mankiewicz 20.03.2024
'''


def stopienGladkowsci(a):
    a_copy = a
    for i in range(2, int(a/2)):
        while a_copy % i == 0:
            a_copy /= i
        if a_copy == 1:
            return i
    return a


def main():
    print("Progam do sprawdzenia liczb gładkich\n")

    tak = 't'

    while tak != 'n':
        liczba = int(input("Podaj liczbe do sprawdzenia: "))

        print(f"Stopien gładkości K = {stopienGladkowsci(liczba)}")

        tak = input("Czy kontynować? (n - nie): ")

    print("Dziękuje za korzystanie z programu")


if __name__ == "__main__":
    main()