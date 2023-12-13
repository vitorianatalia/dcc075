
from criptografia import cifra_cesar, cifra_vigenere, cifra_transposicao, decifra_vigenere, decifra_transposicao, aplica_cifra

def ataque_forca_bruta_cesar(texto_cifrado):
    for chave_teste in range(26):
        tentativa = cifra_cesar(texto_cifrado, -chave_teste)
        print(f"Chave {chave_teste}: {tentativa}")

def ataque_forca_bruta_vigenere(texto_cifrado):
    for chave_teste in range(1, len(texto_cifrado)):
        tentativa = decifra_vigenere(texto_cifrado, "A" * chave_teste)  # Supõe chave composta apenas por 'A'
        print(f"Tentativa com chave de tamanho {chave_teste}: {tentativa}")

def ataque_forca_bruta_transposicao(texto_cifrado):
    for chave_teste in range(1, len(texto_cifrado)):
        tentativa = decifra_transposicao(texto_cifrado, list(range(1, chave_teste + 1)))
        print(f"Tentativa com chave {list(range(1, chave_teste + 1))}: {tentativa}")

if __name__ == '__main__':
    with open('cifrado.txt', 'r') as arquivo:
        texto_cifrado = arquivo.read()
    ataque_forca_bruta_transposicao(texto_cifrado)
    ataque_forca_bruta_vigenere(texto_cifrado)
    ataque_forca_bruta_cesar(texto_cifrado)
