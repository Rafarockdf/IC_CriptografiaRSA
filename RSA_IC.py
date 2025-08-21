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
        self.__keyPrivate1 = int()
        self.__keyPrivate2 = int()
    
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
            if self.teste_miller_rabin(possible_key) and flag == 0:
                flag+=1
                self.__keyPrivate1 = possible_key
            elif self.teste_miller_rabin(possible_key) and flag == 1:
                flag+=1
                self.__keyPrivate2 = possible_key
        return self.__keyPrivate1, self.__keyPrivate2
                  
    import random

    # A função está fora de uma classe para ser mais fácil de testar.
    # Se quiser usar em uma classe, adicione o "self" como primeiro argumento.
    def teste_miller_rabin(self,n, k_testes=5):
        """
        Executa o Teste de Miller-Rabin k_testes vezes para aumentar a confiança.
        """
        if n == 2 or n == 3:
            return True
        if n <= 1 or n % 2 == 0:
            return False

        # Executa o teste várias vezes com diferentes testemunhas
        for _ in range(k_testes):
            if not self._miller_rabin_passo_a_passo(n):
                return False # Se falhar uma vez, é definitivamente composto
        if self.__keyPrivate1 > 0:
            self.__keyPrivate2 = n
        else:
            self.__keyPrivate1 = n
        return True # Se passar em todos os testes, é muito provavelmente primo

    def _miller_rabin_passo_a_passo(self,n):

        # 1. Decompor n-1 em 2^k * q
        q = n - 1
        k = 0
        while q % 2 == 0:
            q //= 2
            k += 1

        # 2. Escolher uma testemunha aleatória 'a'
        testemunha = random.randint(2, n - 2)

        # 3. Calcular x = testemunha^q mod n
        x = pow(testemunha, q, n)

        # 4. Verificar a primeira condição: se x for 1 ou n-1, o número passa no teste
        if x == 1 or x == n - 1:
            return True

        # 5. Se não, continuar elevando ao quadrado k-1 vezes
        for _ in range(k - 1):
            x = pow(x, 2, n)
            

            if x == n - 1:
                return True
            if x == 1:
                return False

        return False


    
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
