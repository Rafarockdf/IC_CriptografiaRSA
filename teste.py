import math
import random
def is_prime(num): 
    if num < 2: 
        return False 
    if num in [2, 3, 5, 7]: 
        return True 
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0: 
        return False 
 
    # Testa divisores de 7 até a raiz quadrada de num 
    for i in range(7, int(math.sqrt(num)) + 1, 2): 
        if num % i == 0: 
            return False 
 
    return True 


def gerar_primos():
        n = random.randint(10**150, 10**200)
        print(n)
        return is_prime(n),n
    
teste = (False,0)
while teste[0] != True:
    teste = gerar_primos()
    print(teste)