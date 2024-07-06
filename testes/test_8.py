def vigenere_encrypt(plaintext, keyword):
    encrypted_text = ""
    keyword = keyword.upper()
    keyword_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(keyword[keyword_index]) - ord('A')
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += encrypted_char
            keyword_index = (keyword_index + 1) % len(keyword)
        else:
            encrypted_text += char

    return encrypted_text

def vigenere_decrypt(ciphertext, keyword):
    decrypted_text = ""
    keyword = keyword.upper()
    keyword_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(keyword[keyword_index]) - ord('A')
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted_text += decrypted_char
            keyword_index = (keyword_index + 1) % len(keyword)
        else:
            decrypted_text += char

    return decrypted_text

# Solicitar ao usuário o texto a ser criptografado e a palavra-chave
plaintext = input("Digite o texto a ser criptografado: ")
keyword = input("Digite a palavra-chave: ")

# Criptografar
ciphertext = vigenere_encrypt(plaintext, keyword)
print("Texto cifrado:", ciphertext)

# Descriptografar
decrypted_text = vigenere_decrypt(ciphertext, keyword)
print("Texto descriptografado:", decrypted_text)