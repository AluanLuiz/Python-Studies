import random as rd

def key_create():
    carac_min = "qwertyuiopasdfghjklzxcvbnm"
    carac_max = "QWERTYUIOPASDFGHJKLZXCVBNM"
    carac_special = "!@#$%&*?<>+-=_"
    numeros = "0123456789"
    
    f1 = rd.randint(1, digitos - 3)
    f2 = rd.randint(1, digitos - f1 - 2)
    f3 = rd.randint(1, digitos - f1 - f2 - 1)
    f4 = digitos - f1 - f2 - f3
    
    key = []
    
    for _ in range(f1):
        letras_min = rd.choice(carac_min)
        key.append(letras_min)
    for _ in range(f2):
        letras_max = rd.choice(carac_max)
        key.append(letras_max)
    for _ in range(f3):
        special = rd.choice(carac_special)
        key.append(special)
    for _ in range(f4):
        numero = rd.choice(numeros)
        key.append(numero)
    
    rd.shuffle(key)
    final_key = "".join(key)    
    
    return final_key
    
    
digitos = int(input("Digite o numero de caracteres da chave: "))
result = key_create()
print(result)