# 🔐 Implementação do Algoritmo RSA em Python

Este projeto é uma implementação didática do algoritmo **RSA (Rivest–Shamir–Adleman)** desenvolvida em Python, com ênfase em **matemática aplicada**.  
O objetivo principal é mostrar como conceitos matemáticos fundamentais (como teoria dos números, aritmética modular e criptografia de chave pública) podem ser utilizados para construir um sistema de criptografia do zero.

---

## ✨ Funcionalidades

- **Pré-processamento de mensagens**:
  - Remoção de acentos.
  - Conversão de caracteres em códigos numéricos personalizados.

- **Geração de chaves**:
  - Seleção de dois números primos grandes usando o **Teste de Miller-Rabin**.
  - Criação da chave pública `n = p * q`.
  - Definição do expoente público `e` coprimo a φ(n).
  - Cálculo do expoente privado `d` via **Algoritmo Euclidiano Estendido**.

- **Codificação (Criptografia)**:
  - Transformação da mensagem em blocos numéricos.
  - Elevação modular usando `c = m^e mod n`.

- **Decodificação (Descriptografia)**:
  - Cálculo da chave privada `d`.
  - Recuperação da mensagem original usando `m = c^d mod n`.

---

## 🧮 Fundamentos Matemáticos

O RSA combina vários conceitos de **matemática aplicada**:

1. **Números primos grandes**  
   - Selecionados por meio do **Teste de Miller-Rabin** (teste probabilístico de primalidade).

2. **Máximo Divisor Comum (MDC)**  
   - Usado para garantir que `e` e φ(n) sejam coprimos (via **Algoritmo de Euclides**).

3. **Algoritmo Euclidiano Estendido**  
   - Permite calcular o inverso modular de `e` em relação a φ(n), encontrando `d`.

4. **Aritmética Modular**  
   - Operações de exponenciação modular (`pow(base, exp, mod)`).

5. **Teoria dos Blocos**  
   - Divisão da mensagem em blocos menores que `n` para garantir segurança e compatibilidade.

---

## 📂 Estrutura do Código

- `RSA` → Classe principal que implementa todas as etapas.
  - **Pré-processamento**: `_remover_acentos`, `pre_transforma_frase`.
  - **Criptografia**: `codificar()`.
  - **Descriptografia**: `decodificar()`.
  - **Geradores de chave**: `gerar_chaves_privadas()`, `gerar_chave_publica()`.
  - **Algoritmos matemáticos**: `algoritimo_euclidiano()`, `algoritimo_euclidiano_estendido()`, `teste_miller_rabin()`.

---

## 🚀 Exemplo de Uso

```python
from RSA_IC import RSA

# Inicializa o sistema
rsa = RSA()

# Mensagem original
mensagem = "MATEMATICA APLICADA"

# Criptografia
mensagem_codificada = rsa.codificar(mensagem)
print("Mensagem codificada:", mensagem_codificada)

# Descriptografia
mensagem_decodificada = rsa.decodificar()
print("Mensagem decodificada:", mensagem_decodificada)

