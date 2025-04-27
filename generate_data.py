import random
import string

# Função para gerar palavras aleatórias
def generate_random_word(length=5):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

# Criar o arquivo data.txt
with open('data.txt', 'w', encoding='utf-8') as f:
    for _ in range(10000):  # Gera 10.000 linhas, você pode aumentar ou diminuir
        line = ' '.join(generate_random_word() for _ in range(10))  # 10 palavras por linha
        f.write(line + '\n')

print("Arquivo data.txt gerado com sucesso!")
