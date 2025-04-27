import redis
import json
import os

def mapear(chunk_file):
    resultado = {}

    # Verifica se o arquivo de entrada existe
    file_path = f'chunks/{chunk_file}'
    if not os.path.exists(file_path):
        print(f"Arquivo {file_path} não encontrado!")
        return

    print(f"Iniciando mapeamento para {chunk_file}...")

    # Lê o arquivo e processa as palavras
    with open(file_path, 'r', encoding='utf-8') as f:
        for linha in f:
            palavras = linha.strip().split()
            for palavra in palavras:
                palavra = palavra.lower()  # Normaliza para minúsculas
                if palavra in resultado:
                    resultado[palavra] += 1
                else:
                    resultado[palavra] = 1

    # Cria a pasta de resultados intermediários, se necessário
    os.makedirs('intermediate', exist_ok=True)

    # Salva o arquivo de resultados intermediários
    output_file = f'intermediate/{chunk_file}_map.json'
    with open(output_file, 'w', encoding='utf-8') as out:
        json.dump(resultado, out, ensure_ascii=False, indent=4)

    print(f"Mapeamento concluído para {chunk_file}, resultados salvos em {output_file}")

def main():
    r = redis.Redis()

    while True:
        tarefa = r.lpop('mapper_tasks')
        if tarefa is None:
            print("Não há mais tarefas para processar.")
            break
        
        tarefa = tarefa.decode('utf-8')
        print(f"Iniciando mapeamento para {tarefa}")
        try:
            mapear(tarefa)
            # Após o mapeamento, publica a tarefa como concluída no Redis
            print(f"Publicando 'mapper_done' para {tarefa}...")
            r.publish('mapper_done', tarefa)  
            print(f"Tarefa {tarefa} concluída.")
        except Exception as e:
            print(f"Erro ao processar {tarefa}: {e}")
            # Mesmo em caso de erro, publica a tarefa como concluída para não travar o sistema
            r.publish('mapper_done', tarefa)  
            print(f"Tarefa {tarefa} marcada como concluída, mesmo com erro.")
            
if __name__ == "__main__":
    main()
