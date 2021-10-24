def lst_int_numbers():
    '''
    Citeste o lista de numere intregi
    :return:
    '''

    lst_str = input("Introduceti numerele intregi: ").split(" ")
    lst_int = []
    for nr in lst_str:
        lst_int.append(int(nr))
    return lst_int

def is_palindrome(n):
    '''
    Functie care determina daca numarul este palindrom
    :param n:
    :return:
    '''
    clona = n
    ogl = 0
    while clona > 0:
        ogl = ogl * 10 + clona % 10
        clona = clona // 10
    if n == ogl:
        return True
    elif n != ogl:
        return False

def test_is_palindrome():
    assert is_palindrome(75457) ==  True
    assert is_palindrome(543) == False

def get_longest_all_palindromes(lst):
    """
    determina subsecventa cea mai lunga de palindroame
    """
    l = len(lst)
    result = []
    for i in range (l):
        for j in range (i,l):
            all_palindromes = True
            for el in lst[i:j+1]:
                if is_palindrome(el) == False:
                    all_palindromes = False
                    break
            if all_palindromes:
                if j-i+1 >len(result):
                    result = lst[i:j+1]
    return result
def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([4322, 76567, 98789, 121, 7, 4322]) == [76567, 98789, 121, 7]
    assert get_longest_all_palindromes([432, 6543]) == []


def nr_div(n):
    """
    determina numarul de divizori ai unui nr
    """
    k = 0
    for i in range (1,n+1):
        if n % i == 0:
            k = k + 1
    return k

def test_nr_div():
    assert nr_div(16) == 5
    assert nr_div(28) == 6

def get_longest_same_div_count(lst):
    """
    determina cea mai lunga subsecv de numere care au acelasi nr de divizori
    """
    l = len(lst)
    result = []
    for i in range (l):
        for j in range (i,l):
            k = nr_div(lst[i])
            same_div_count = True
            for num in lst[i:j+1]:
                if nr_div(num) != k :
                    same_div_count = False
                    break
            if same_div_count:
                if j-i+1 >len(result):
                    result = lst[i:j+1]
    return result
def test_get_longest_same_div_count():
    assert get_longest_same_div_count([12, 3, 5, 7, 24]) == [3, 5, 7]
    assert get_longest_same_div_count([6, 8, 10, 3, 13]) == [6, 8, 10]
    assert get_longest_same_div_count([3, 12, 28, 32, 7]) == [12, 28, 32]

def is_prime(n):
        '''
          Returneaza True daca numarul este prim, iar Flase in caz contrar
          :return:
          '''
        for i in range(2, n // 2):
            if n % i == 0:
                return False
        return True

def test_is_prime():
        assert is_prime(7) == True
        assert is_prime(82) == False

def only_primes(lst: list) -> bool:
        # verifica daca toate numerele din lst sunt prime
        for i in lst:
            if is_prime(i) == False: return False
        return True

def get_longest_all_primes(lst: list) -> list:
        """
        determina cea mai lunga secventa dintr-o lista in care toate numerele sunt prime
        param. lst - lista
        return - o lista ce contine cea mai lunga secventa in care toate numerele sunt prime
        """
        result = []
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                if len(lst[i: j + 1]) > len(result) and only_primes(lst[i: j + 1]) == True:
                    result = lst[i: j + 1]
        return result


def show_menu():
    print ('''
    1. Citire numere intregi
    2. Determina cea mai lunga secventa cu prop ca numerele sunt palindroame
    3. Determina cea mai lunga secventa cu prop ca numerele au acelasi nr de divizori
    4. Determina cea mai lunga secventa cu prop ca toate numerele sunt prime
    x. Iesire
    ''')

def main():
    lst = []
    while True:
        show_menu()
        cmd = input ("Introduceti comanda dvs: ")
        if cmd == '1':
            lst = lst_int_numbers()
        elif cmd == '2':
            print(get_longest_all_palindromes(lst))
        elif cmd == '3':
            print(get_longest_same_div_count(lst))
        elif cmd == '4':
            print(get_longest_all_primes(lst))
        elif cmd == 'x':
            break
        else:
            print ("Comanda invalida")


def run_tests():
    test_is_palindrome()
    test_get_longest_all_palindromes()
    test_nr_div()
    test_get_longest_same_div_count()
    test_is_prime()

if __name__ == '__main__':
    run_tests()
    main()