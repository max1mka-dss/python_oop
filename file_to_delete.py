  # Генерация перестановок
def gen_bin (M, prefix="") -> object:
    """выводит все перестановки"""
    if M == 0:
        print(prefix)
        return
    gen_bin(M-1,prefix+"0")
    gen_bin(M-1,prefix+"1")
def generate_numbers (n:int , m:int, prefix = None):
    """Генерирует все числа(с лидирующими незначащими нулями в N-ричной системе счисления N<=10
    длины M"""
    if m == 0:
        print(prefix)
        return
    prefix = prefix or []
    for digit in range (n):
        prefix.append(digit)
        generate_numbers(n,m- 1,prefix)
        prefix.pop()
#gen_bin(3 )
generate_numbers(3,3)

def generate_permutations(N:int, M:int, prefix = None):
    """Генерация всех перестановок N чисел в M позициях, с префиксом prefix"""