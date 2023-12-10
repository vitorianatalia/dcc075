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
            resultado += chr((ord(texto[i]) + ord(chave_repetida[i]) - 2 * offset) % 26 + offset)
        else:
            resultado += texto[i]
    return resultado

def decifra_vigenere(texto, chave):
    resultado = ''
    chave_repetida = (chave * (len(texto) // len(chave))) + chave[:len(texto) % len(chave)]
    for i in range(len(texto)):
        if texto[i].isalpha():
            offset = ord('a') if texto[i].islower() else ord('A')
            resultado += chr((ord(texto[i]) - ord(chave_repetida[i]) + 26) % 26 + offset)
        else:
            resultado += texto[i]
    return resultado

def aplica_cifra(algoritmo, texto_original, chave_correta, *args):
    texto_cifrado = algoritmo(texto_original, chave_correta, *args)
    if algoritmo == cifra_cesar:
        texto_decifrado = algoritmo(texto_cifrado, -chave_correta)
    else:
        texto_decifrado = decifra_vigenere(texto_cifrado, chave_correta)
    return texto_cifrado, texto_decifrado

texto_original = "Algoritmo combinado de Cifra de Cesar e Cifra de Vigenere"
chave_cesar_correta = 3
chave_vigenere_correta = "CHAVE_DCC"

texto_cifrado_cesar, texto_decifrado_cesar = aplica_cifra(cifra_cesar, texto_original, chave_cesar_correta)
texto_cifrado_vigenere, texto_decifrado_vigenere = aplica_cifra(cifra_vigenere, texto_cifrado_cesar, chave_vigenere_correta)

print("Texto original: ", texto_original)
print("Passo 1: Cifra de Cesar -- ", texto_cifrado_cesar)
print("Passo 2: Cifra de Vigenere -- ", texto_cifrado_vigenere)
print("\nIniciando descriptografia...\n")
print("Passo 1: Cifra de Vigenere -- ", texto_decifrado_vigenere)
print("Passo 2: Cifra de Cesar -- ", texto_decifrado_cesar)
print("\nTaxa de sucesso: ", "100%" if texto_original == texto_decifrado_cesar else "0%")
