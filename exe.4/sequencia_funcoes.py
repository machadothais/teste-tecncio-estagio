def next_element_sequence_a():
    return 7 + 2

def next_element_sequence_b():
    return 64 * 2

def next_element_sequence_c():
    n = 6
    return n * n

def next_element_sequence_d():
    n = 10
    return n * n

def next_element_sequence_e():
    a, b = 5, 8
    return a + b

def next_element_sequence_f():
    return 19 + 1

def main():
    print("Próximo elemento da sequência a):", next_element_sequence_a())
    print("Próximo elemento da sequência b):", next_element_sequence_b())
    print("Próximo elemento da sequência c):", next_element_sequence_c())
    print("Próximo elemento da sequência d):", next_element_sequence_d())
    print("Próximo elemento da sequência e):", next_element_sequence_e())
    print("Próximo elemento da sequência f):", next_element_sequence_f())

if __name__ == "__main__":
    main()
