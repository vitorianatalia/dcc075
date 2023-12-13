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

def cifra_transposicao(texto, chave):
    num_colunas = len(chave)
    num_linhas = -(-len(texto) // num_colunas)
    matriz = [[' ' for _ in range(num_colunas)] for _ in range(num_linhas)]

    for i, char in enumerate(texto):
        linha = i // num_colunas
        coluna = i % num_colunas
        matriz[linha][coluna] = char

    texto_cifrado = ''
    for num in chave:
        indice_chave = num - 1
        for linha in matriz:
            texto_cifrado += linha[indice_chave]

    return texto_cifrado

def decifra_transposicao(texto_cifrado, chave):
    num_colunas = len(chave)
    num_linhas = -(-len(texto_cifrado) // num_colunas)
    matriz = [[' ' for _ in range(num_colunas)] for _ in range(num_linhas)]

    chars_per_column = [0] * num_colunas
    for i in range(len(texto_cifrado)):
        coluna = i % num_colunas
        chars_per_column[coluna] += 1

    index = 0
    for coluna in sorted(range(num_colunas), key=lambda x: chave[x]):
        for linha in range(chars_per_column[coluna]):
            if index < len(texto_cifrado):
                matriz[linha][coluna] = texto_cifrado[index]
                index += 1

    texto_decifrado = ''
    for i in range(num_linhas):
        for j in chave:
            texto_decifrado += matriz[i][j-1]

    return texto_decifrado.rstrip()

def aplica_cifra(algoritmo, texto_original, chave_correta, *args):
    texto_cifrado = algoritmo(texto_original, chave_correta, *args)
    if algoritmo == cifra_cesar:
        texto_decifrado = algoritmo(texto_cifrado, -chave_correta)
    elif algoritmo == cifra_vigenere:
        texto_decifrado = decifra_vigenere(texto_cifrado, chave_correta)
    else:
        texto_decifrado = decifra_transposicao(texto_cifrado, chave_correta)
    return texto_cifrado, texto_decifrado



with open('file.txt', 'r') as arquivo:
    conteudo = arquivo.read()

texto_original = "Algoritmo combinado de Cifra de Cesar e Cifra de Vigenere"
#texto_original = conteudo

chave_cesar_correta = 3
chave_vigenere_correta = "CHAVE_DCC"
chave_transposicao_correta = [3, 1, 2]
print("chave", chave_transposicao_correta)

texto_cifrado_cesar, texto_decifrado_cesar = aplica_cifra(cifra_cesar, texto_original, chave_cesar_correta)
texto_cifrado_vigenere, texto_decifrado_vigenere = aplica_cifra(cifra_vigenere, texto_cifrado_cesar, chave_vigenere_correta)
texto_cifrado_transposicao, texto_decifrado_transposicao = aplica_cifra(cifra_transposicao, texto_cifrado_vigenere, chave_transposicao_correta)

print("\nIniciando criptografia...\n")
print("Texto original: ", texto_original)
print("Passo 1: Cifra de Cesar -- ", texto_cifrado_cesar)
print("Passo 2: Cifra de Vigenere -- ", texto_cifrado_vigenere)
print("Passo 3: Cifra de Transposicao -- ", texto_cifrado_transposicao)
print("\nIniciando descriptografia...\n")
print("Passo 1: Cifra de Transposicao -- ", texto_decifrado_transposicao)
print("Passo 2: Cifra de Vigenere -- ", texto_decifrado_vigenere)
print("Passo 3: Cifra de Cesar -- ", texto_decifrado_cesar)
print("\nTaxa de sucesso: ", "100%" if texto_original == texto_decifrado_cesar else "0%")

