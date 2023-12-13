import unittest

from criptografia import cifra_cesar, cifra_vigenere, cifra_transposicao, decifra_vigenere, decifra_transposicao, aplica_cifra

class TestCifras(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open('file.txt', 'r') as arquivo:
            cls.conteudo = arquivo.read()

    def test_cifra_cesar(self):
        texto_original = self.conteudo
        chave_correta = 3

        texto_cifrado = cifra_cesar(texto_original, chave_correta)
        texto_decifrado = cifra_cesar(texto_cifrado, -chave_correta)

        self.assertEqual(texto_decifrado, texto_original)

    def test_cifra_vigenere(self):
        texto_original = self.conteudo
        chave_correta = "KEY"

        texto_cifrado = cifra_vigenere(texto_original, chave_correta)
        texto_decifrado = decifra_vigenere(texto_cifrado, chave_correta)

        self.assertEqual(texto_decifrado, texto_original)

    def test_cifra_transposicao(self):
        texto_original = "Hello World!"
        chave_correta = [3, 1, 2]

        texto_cifrado = cifra_transposicao(texto_original, chave_correta)
        texto_decifrado = decifra_transposicao(texto_cifrado, chave_correta)

        self.assertEqual(texto_decifrado, texto_original)

    def test_aplica_cifra(self):
        texto_original = "Hello World!"
        chave_cesar_correta = 3
        chave_vigenere_correta = "KEY"
        chave_transposicao_correta = [3, 1, 2]

        texto_cifrado, texto_decifrado = aplica_cifra(cifra_cesar, texto_original, chave_cesar_correta)
        self.assertEqual(texto_decifrado, texto_original)

        texto_cifrado, texto_decifrado = aplica_cifra(cifra_vigenere, texto_original, chave_vigenere_correta)
        self.assertEqual(texto_decifrado, texto_original)

        texto_cifrado, texto_decifrado = aplica_cifra(cifra_transposicao, texto_original, chave_transposicao_correta)
        self.assertEqual(texto_decifrado, texto_original)

if __name__ == '__main__':
    unittest.main()
