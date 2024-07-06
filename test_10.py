# Cifra de césar modificada

def criptografar(texto):
    substituicoes = {'A': 'あ', 'B': 'い', 'C': 'う', 'D': 'え', 'E': 'お', 'F': 'か', 'G': 'き', 'H': 'く', 'I': 'け', 'J': 'こ',
                     'K': 'さ', 'L': 'し', 'M': 'す', 'N': 'せ', 'O': 'そ', 'P': 'た', 'Q': 'ち', 'R': 'つ', 'S': 'て', 'T': 'と',
                     'U': 'な', 'V': 'に', 'W': 'ぬ', 'X': 'ね', 'Y': 'の', 'Z': 'ん', '1':'一', '2':'二','3':'三', '4':'四',
                     '5':'五','6':'六','7':'七','8':'八','9':'九','0':'零'}
  
    
    texto_criptografado = ''.join(substituicoes.get(letra.upper(), letra) for letra in texto)
    return texto_criptografado

def descriptografar(texto_criptografado):
    substituicoes = {'あ': 'A', 'い': 'B', 'う': 'C', 'え': 'D', 'お': 'E', 'か': 'F', 'き': 'G', 'く': 'H', 'け': 'I', 'こ': 'J',
                     'さ': 'K', 'し': 'L', 'す': 'M', 'せ': 'N', 'そ': 'O', 'た': 'P', 'ち': 'Q', 'つ': 'R', 'て': 'S', 'と': 'T',
                     'な': 'U', 'に': 'V', 'ぬ': 'W', 'ね': 'X', 'の': 'Y', 'ん': 'Z','一':'1','二':'2','三':'3','四':'4',
                     '五':'5','六':'6','七':'7','八':'8','九':'9','零':'0'}
    
    
    texto = ''.join(substituicoes.get(letra, letra) for letra in texto_criptografado)
    return texto

tipo=int(input("Digite o que deseja fazer: (1 para Criptografar, 2 para Descriptogrfar)"))

def cifrarcesar(texto):
    cipher = ''
    for char in texto:
        if char.isalpha():
            char = char.upper()
            code = ord(char) + 3
            if code > ord('Z'):
                code = ord('A')
            cipher += chr(code)
        elif char.isdigit():
            code = ord(char) + 3
            if code > ord('9'):
                code = ord('0')
            cipher += chr(code)
        else:
            # Keep other characters unchanged (like spaces, punctuation, etc.)
            cipher += char
    return cipher

def descifrarcesar(texto):
    cipher = ''
    for char in texto:
        if char.isalpha():
            char = char.upper()
            code = ord(char) - 3
            if code < ord('A'):
                code = ord('Z')
            cipher += chr(code)
        elif char.isdigit():
            code = ord(char) - 3
            if code < ord('0'):
                code = ord('9')
            cipher += chr(code)
        else:
            # Keep other characters unchanged (like spaces, punctuation, etc.)
            cipher += char
    return cipher


if tipo ==1:
    meutexto=input("Digite o texto para Criptografar:")
    meutexto=cifrarcesar(meutexto)
    
    
    texto_criptografado = criptografar(meutexto)
    print("Texto Criptografado:", texto_criptografado)
  
elif tipo==2:
    
    meutexto=input("Digite o texto para Descriptografar:")
    texto_descriptografado = descriptografar(meutexto)
    
    
    texto_descriptografado=descifrarcesar(texto_descriptografado)

    print("Texto Descriptografado:", texto_descriptografado)
else: 
    print("Opção inválida")