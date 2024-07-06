#!/usr/bin/env python
# coding: utf-8
def criptografar(texto):
    substituicoes = {'A': 'あ', 'B': 'い', 'C': 'う', 'D': 'え', 'E': 'お', 'F': 'か', 'G': 'き', 'H': 'く', 'I': 'け', 'J': 'こ',
                     'K': 'さ', 'L': 'し', 'M': 'す', 'N': 'せ', 'O': 'そ', 'P': 'た', 'Q': 'ち', 'R': 'つ', 'S': 'て', 'T': 'と',
                     'U': 'な', 'V': 'に', 'W': 'ぬ', 'X': 'ね', 'Y': 'の', 'Z': 'ん'}
    
    texto_criptografado = ''.join(substituicoes.get(letra.upper(), letra) for letra in texto)
    return texto_criptografado

def descriptografar(texto_criptografado):
    substituicoes = {'あ': 'A', 'い': 'B', 'う': 'C', 'え': 'D', 'お': 'E', 'か': 'F', 'き': 'G', 'く': 'H', 'け': 'I', 'こ': 'J',
                     'さ': 'K', 'し': 'L', 'す': 'M', 'せ': 'N', 'そ': 'O', 'た': 'P', 'ち': 'Q', 'つ': 'R', 'て': 'S', 'と': 'T',
                     'な': 'U', 'に': 'V', 'ぬ': 'W', 'ね': 'X', 'の': 'Y', 'ん': 'Z'}
    
    texto = ''.join(substituicoes.get(letra, letra) for letra in texto_criptografado)
    return texto

tipo=int(input("Digite o que deseja fazer: (1 para Criptografar, 2 para Descriptogrfar)"))

if tipo ==1:
    meutexto=input("Digite o texto para Criptografar:")
    texto_criptografado = criptografar(meutexto)
    print("Texto Criptografado:", texto_criptografado)
  
elif tipo==2:
    meutexto=input("Digite o texto para Descriptografar:")
    texto_descriptografado = descriptografar(meutexto)
    print("Texto Descriptografado:", texto_descriptografado)
else: 
    print("Opção inválida")
