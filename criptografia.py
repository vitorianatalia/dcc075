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
    texto_sem_espacos = ''.join(texto.split())
    print(chave)
    num_colunas = len(chave)
    num_linhas = -(-len(texto_sem_espacos) // num_colunas)
    matriz = [[' ' for _ in range(num_colunas)] for _ in range(num_linhas)]

    for i, char in enumerate(texto_sem_espacos):
        linha = i // num_colunas
        coluna = i % num_colunas
        matriz[linha][coluna] = char

    texto_cifrado = ''
    for coluna in range(num_colunas):
        indice_chave = chave.index(coluna + 1)
        texto_cifrado += ''.join(matriz[linha][indice_chave] for linha in range(num_linhas))
    

    texto_cifrado_final = ''
    j = 0
    for i, char in enumerate(texto):
        if char.isalpha():
            texto_cifrado_final += texto_cifrado[j]
            j += 1
        else:
            texto_cifrado_final += ' '

    return texto_cifrado_final

def decifra_transposicao(texto_cifrado, chave):
    texto_sem_espacos = ''.join(texto_cifrado.split())
    num_colunas = len(chave)
    num_linhas = -(-len(texto_sem_espacos) // num_colunas)
    matriz = [[' ' for _ in range(num_colunas)] for _ in range(num_linhas)]

    # Preencher a matriz com o texto cifrado
    for i, char in enumerate(texto_sem_espacos):
        linha = i % num_linhas
        coluna = i // num_linhas
        matriz[linha][coluna] = char

    # Criar a string decifrada ao ler a matriz por linhas usando a chave
    texto_decifrado = ''
    for linha in range(num_linhas):
        for coluna in range(num_colunas):
            texto_decifrado += matriz[linha][chave[coluna] - 1]

    texto_decifrado_final = ''
    j = 0
    for i, char in enumerate(texto_cifrado):
        if char.isalpha():
            texto_decifrado_final += texto_decifrado[j]
            j += 1
        else:
            texto_decifrado_final += ' '

    return texto_decifrado_final

def aplica_cifra(algoritmo, texto_original, chave_correta, *args):
    texto_cifrado = algoritmo(texto_original, chave_correta, *args)
    if algoritmo == cifra_cesar:
        texto_decifrado = algoritmo(texto_cifrado, -chave_correta)
    elif algoritmo == cifra_vigenere:
        texto_decifrado = decifra_vigenere(texto_cifrado, chave_correta)
    else:
        texto_decifrado = decifra_transposicao(texto_cifrado, chave_correta)
    return texto_cifrado, texto_decifrado

texto_original = "Algoritmo combinado de Cifra de Cesar e Cifra de Vigenere"
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

