import unicodedata
import random
class RSA:
    _dicionario_letras = {
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
        'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21,
        'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27,
        'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33,
        'Y': 34, 'Z': 35, ' ': 99
    }

    def __init__(self):
        self.__fraseCodificada = ""
        self.__e = int()
        self.__keyPrivate1 = int()
        self.__keyPrivate2 = int()
        self.__keyPublic = int()
    
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
    
    def gerar_chaves_privadas(self):
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
    def gerar_chave_publica(self):
        numero_primo1, numero_primo2 = self.gerar_chaves_privadas()
        chave_publica = numero_primo1 * numero_primo2
        self.__keyPublic = chave_publica
        return self.__keyPublic
    
    def pre_blocagem(self, frase):
        chave_publica = self.gerar_chave_publica()
        frase_pre_codificacao = self.pre_transforma_frase(frase)
        
        # A string agora é uma lista de códigos de 2 dígitos
        lista_de_codigos = [frase_pre_codificacao[i:i+2] for i in range(0, len(frase_pre_codificacao), 2)]
        
        blocos = []
        bloco_atual = ""
        for codigo in lista_de_codigos:
            # Tenta adicionar o próximo código de 2 dígitos ao bloco atual
            bloco_potencial = bloco_atual + codigo
            if int(bloco_potencial) < chave_publica:
                bloco_atual = bloco_potencial
            else:
                # O bloco potencial ficou muito grande, então salvamos o anterior
                blocos.append(bloco_atual)
                # O código atual inicia um novo bloco
                bloco_atual = codigo
        
        # Adiciona o último bloco que estava sendo formado
        if bloco_atual:
            blocos.append(bloco_atual)
        print(blocos)
        return blocos
    
    def algoritimo_euclidiano(self,a,b):
        r = 1
        aux = 0
        while r != 0:
            r = a % b
            if r == 0:
                break
            aux = b
            b = r
            a = aux
        return b
    def algoritimo_euclidiano_estendido(self,a,b):
        x = [1,0]
        y = [0,1]
        x_completo = []
        y_completo = []
        r = 1
        abs = 1
        aux = 0
        auxX = 0
        auxY = 0
        num1 = a
        num2 = b
        while r != 0:
            r = a % b
            abs = a // b
            auxX = x[0] - (abs * x[1])
            x[0] = x[1]
            x[1] = auxX
            auxY = y[0] - (abs * y[1])
            y[0] = y[1]
            y[1] = auxY
            if r == 0:
                break
            x_completo.append(x[1])
            y_completo.append(y[1])
            aux = b
            b = r
            a = aux
        return x[0]
    def codificar(self,frase):
        mensagem_blocada = self.pre_blocagem(frase)
        bloco_codificado = []
        e = 1
        mdc = 0
        o_n = (self.__keyPrivate1 - 1) * (self.__keyPrivate2 - 1)
        while mdc != 1:
            e += 1
            mdc = self.algoritimo_euclidiano(e,o_n)
        self.__e = e
        for bloco in  mensagem_blocada:
            bloco_codificado.append(str(pow(int(bloco),e,self.__keyPublic)))
        self.__fraseCodificada = ' '.join(bloco_codificado)
        return self.__fraseCodificada
    
    def decodificar(self):
        mensagem_codificada = self.__fraseCodificada
        mensagem_blocada = mensagem_codificada.split(' ')

        bloco_decodificado = []
        
        o_n = (self.__keyPrivate1 - 1) * (self.__keyPrivate2 - 1)
        x = self.algoritimo_euclidiano_estendido(self.__e, o_n)
        d = int(x) % o_n

        # Decodifica cada bloco para seu valor numérico original
        for bloco in mensagem_blocada:
            if bloco:
                valor_decodificado = pow(int(bloco), d, self.__keyPublic)
                bloco_decodificado.append(str(valor_decodificado))

        # Junta todos os blocos decodificados para formar a string numérica gigante
        # Como os blocos foram criados corretamente, a junção agora também é correta!
        string_numerica_completa = "".join(bloco_decodificado)

        # Cria um dicionário invertido para busca rápida
        dicionario_valores = {str(v): k for k, v in self._dicionario_letras.items()}
        
        mensagem_decodificada_final = ""
        i = 0
        # Percorre a string numérica de 2 em 2 caracteres
        while i < len(string_numerica_completa):
            codigo_letra = string_numerica_completa[i:i+2]
            if codigo_letra in dicionario_valores:
                mensagem_decodificada_final += dicionario_valores[codigo_letra]
            i += 2

        return mensagem_decodificada_final
                    

            
