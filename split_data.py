def dividir_arquivo():
    with open('data.txt', 'r', encoding='utf-8') as file:
        linhas = file.readlines()

    partes = len(linhas) // 10
    for i in range(10):
        with open(f'chunks/chunk{i}.txt', 'w', encoding='utf-8') as chunk_file:
            chunk_file.writelines(linhas[i*partes : (i+1)*partes])

if __name__ == "__main__":
    dividir_arquivo()
