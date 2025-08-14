import unicodedata
import random
from teste import is_prime
class RSA:
    _dicionario_letras = {
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
        'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21,
        'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27,
        'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33,
        'Y': 34, 'Z': 35, ' ': 99
    }

    def __init__(self):
        self.frase = ""
        self._keyPrivate1 = int()
        self._keyPrivate2 = int()
    # Parte 1 - Pré codificação
    ## Método para remover acesntos da string
    def _remover_acentos(self, texto):
        nfkd = unicodedata.normalize('NFD', texto)
        return ''.join(c for c in nfkd if unicodedata.category(c) != 'Mn')

    ## Método que converte a frase em string de números
    def pre_transforma_frase(self, frase):
        self.frase = self._remover_acentos(frase).upper()
        frase_pre_codificacao = []
        for letra in self.frase:
            if letra in self._dicionario_letras:
                frase_pre_codificacao.append(self._dicionario_letras[letra])
        return ''.join(map(str, frase_pre_codificacao))  # string contínua
    
    def gerar_primos(self):
        flag = 0
        while flag != 2:
            possible_key = random.randint(10**150, 10**200)
            if self.teste_miller_primo(possible_key) and flag == 0:
                flag+=1
                self._keyPrivate1 = possible_key
            elif self.teste_miller_primo(possible_key) and flag == 1:
                flag+=1
                self._keyPrivate2 = possible_key
        return self._keyPrivate1, self._keyPrivate2
                  
    def teste_miller_primo(self,n):
        return True
    
    ## Método que faz a blocagem com base na chave gerada por dois primos
    def pre_blocagem(self):
        numero_primo1, numero_primo2 = self.gerar_primos()
        chave = numero_primo1 * numero_primo2
        frase_pre_codificacao = self.pre_transforma_frase("Paraty é linda")
        blocos = []
        i = 0
        while i < len(frase_pre_codificacao):
            bloco_atual = frase_pre_codificacao[i]
            j = i + 1
            while j < len(frase_pre_codificacao):
                bloco_potencial = frase_pre_codificacao[i : j+1]
                if int(bloco_potencial) < chave:
                    bloco_atual = bloco_potencial
                    j = j + 1
                else:
                    break
            blocos.append(bloco_atual)
            i += len(bloco_atual)
        return blocos
