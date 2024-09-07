from fibonacci.fibonacci import Fibonacci
from letter_a_counter.letter_a_counter import LetterACounter
from sum_calculator.sum_calculator import SumCalculator
from sequence_completer.sequence_completer import SequenceCompleter
from switch_lamp.switch_lamp import SwitchLampMapping

def main():
    # Verificar número na sequência de Fibonacci
    numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
    checker = Fibonacci(numero)
    print(checker.check_number())

    # Contar letras 'a' em uma string
    texto = input("Digite uma string: ")
    counter = LetterACounter(texto)
    print(counter.report())

    # Calcular o valor de SOMA
    indice = 12
    calculator = SumCalculator(indice)
    print("O valor de SOMA é:", calculator.calculate_sum())

    # Completar as sequências
    print("Próximo número da sequência a:", SequenceCompleter.complete_sequence_a())
    print("Próximo número da sequência b:", SequenceCompleter.complete_sequence_b())
    print("Próximo número da sequência c:", SequenceCompleter.complete_sequence_c())
    print("Próximo número da sequência d:", SequenceCompleter.complete_sequence_d())
    print("Próximo número da sequência e:", SequenceCompleter.complete_sequence_e())
    print("Próximo número da sequência f:", SequenceCompleter.complete_sequence_f())

    # Identificar interruptores e lâmpadas
    mapping = SwitchLampMapping()
    results = mapping.identify_lamps()
    for switch, lamp in results.items():
        print(f"{switch} controla a {lamp}.")

if __name__ == "__main__":
    main()
