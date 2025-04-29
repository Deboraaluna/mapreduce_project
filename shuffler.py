import json
import os
import hashlib

def carregar_intermediarios():
    dados = {}

    for nome_arquivo in os.listdir('intermediate'):
        if nome_arquivo.endswith('_map.json'):
            with open(f'intermediate/{nome_arquivo}', 'r', encoding='utf-8') as f:
                parcial = json.load(f)
                for palavra, contagem in parcial.items():
                    if palavra not in dados:
                        dados[palavra] = []
                    dados[palavra].append(contagem)

    return dados

def particionar_para_reducers(dados, num_reducers=3):
    reducers = [{} for _ in range(num_reducers)]

    for palavra, contagens in dados.items():
        idx = int(hashlib.sha1(palavra.encode()).hexdigest(), 16) % num_reducers
        reducers[idx][palavra] = contagens

    os.makedirs('reducer_inputs', exist_ok=True)
    for i, conteudo in enumerate(reducers):
        with open(f'reducer_inputs/reducer_input_{i}.json', 'w', encoding='utf-8') as f:
            json.dump(conteudo, f)

def main():
    dados = carregar_intermediarios()

    particionar_para_reducers(dados)

if __name__ == "__main__":
    main()
    print("✅ Shuffle concluído! Dados prontos para os reducers.")
    print("🗂️ Arquivos de entrada para reducers criados em 'reducer_inputs'.")
    print("🔄 Pronto para iniciar os reducers!")
    print("🎉 Tudo pronto!")
    print("Resultado em 'final/final_result.txt'!")
    