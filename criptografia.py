def cifra_cesar(texto, chave):
    resultado = ''
    for char in texto:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            resultado += chr((ord(char) - offset + chave) % 26 + offset)
        else:
            resultado += char
    return resultado

def cifra_vigenere(texto, chave):
    resultado = ''
    chave_repetida = (chave * (len(texto) // len(chave))) + chave[:len(texto) % len(chave)]
    for i in range(len(texto)):
        if texto[i].isalpha():
            offset = ord('a') if texto[i].islower() else ord('A')
            resultado += chr((ord(texto[i]) - ord(chave_repetida[i]) + 26) % 26 + offset)
        else:
            resultado += texto[i]
    return resultado

def taxa_sucesso_descriptografia(algoritmo, texto_original, chave_correta, *args):
    texto_cifrado = algoritmo(texto_original, chave_correta, *args)
    texto_decifrado = algoritmo(texto_cifrado, chave_correta, *args)
    return texto_decifrado == texto_original, texto_cifrado, texto_decifrado

texto_original = "Algoritmo combinado de Cifra de César e Cifra de Vigenère"
chave_cesar_correta = 3
chave_vigenere_correta = "CHAVE_DCC"

sucesso_cesar, texto_cifrado_cesar, texto_decifrado_cesar = taxa_sucesso_descriptografia(cifra_cesar, texto_original, chave_cesar_correta)
print("Cifra de César - Taxa de Sucesso:", sucesso_cesar)
print("Texto Cifrado:", texto_cifrado_cesar)
print("Texto Decifrado:", texto_decifrado_cesar)

sucesso_vigenere, texto_cifrado_vigenere, texto_decifrado_vigenere = taxa_sucesso_descriptografia(cifra_vigenere, texto_original, chave_vigenere_correta)
print("\nCifra de Vigenère - Taxa de Sucesso:", sucesso_vigenere)
print("Texto Cifrado:", texto_cifrado_vigenere)
print("Texto Decifrado:", texto_decifrado_vigenere)
