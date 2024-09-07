def contar_letra_a(s):
    return s.lower().count('a')

texto = input("Digite algo: ")
quantidade = contar_letra_a(texto)
if quantidade > 0:
    print(f"A letra 'a' (maiúscula ou minúscula) aparece {quantidade} vez(es) na string.")
else:
    print("A letra 'a' não aparece na string.")
