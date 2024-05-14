import re

def word_token(text):
    return re.findall("[\w']+", text)

print(word_token("oui c'est une phrase cool"))
print(word_token("On peut Se 4x4 que c'est une phrase cool"))
print(word_token("la vie vaut la peine, de vivre"))
print(word_token("Que dire de la vie"))