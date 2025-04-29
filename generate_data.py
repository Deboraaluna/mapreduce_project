import random
import string

def generate_random_word(length=5):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

# para gerar um arquivo de texto com 10.000 linhas, cada linha com 10 palavras aleatórias ;)
with open('data.txt', 'w', encoding='utf-8') as f:
    for _ in range(10000):  
        line = ' '.join(generate_random_word() for _ in range(10)) 
        f.write(line + '\n')

print("Arquivo data.txt gerado com sucesso!")
