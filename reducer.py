import redis
import json
import os
import time  # IMPORTANTE: para usar sleep

def reduzir(nome_arquivo):
    try:
        with open(f'reducer_inputs/{nome_arquivo}', 'r', encoding='utf-8') as f:
            dados = json.load(f)

        resultado_final = {palavra: sum(valores) for palavra, valores in dados.items()}

        os.makedirs('reducer_outputs', exist_ok=True)
        with open(f'reducer_outputs/{nome_arquivo.replace("input", "output").replace(".json", ".txt")}', 'w', encoding='utf-8') as f:
            for palavra, contagem in resultado_final.items():
                f.write(f"{palavra}: {contagem}\n")

        print(f"Redução concluída para {nome_arquivo}. Resultados salvos em 'reducer_outputs/{nome_arquivo.replace('input', 'output').replace('.json', '.txt')}'")

    except Exception as e:
        print(f"Erro ao processar o arquivo {nome_arquivo}: {e}")

def main():
    r = redis.Redis()
    while True:
        tarefa = r.lpop('reducer_tasks')
        if tarefa is None:
            time.sleep(0.5)  # Espera meio segundo e tenta de novo!
            continue
        
        tarefa = tarefa.decode('utf-8')
        print(f"Recebendo tarefa para reduzir: {tarefa}")
        try:
            reduzir(tarefa)
            r.publish('reducer_done', tarefa)
            print(f"Tarefa {tarefa} reduzida com sucesso.")
        except Exception as e:
            print(f"Erro ao reduzir {tarefa}: {e}")

if __name__ == "__main__":
    main()
