import redis
import time
import os
import shuffler  # Importa o script shuffler que você já criou

def iniciar_mappers(r):
    print("👉 Iniciando mappers...")
    for i in range(10):  # chunk0.txt até chunk9.txt
        r.rpush('mapper_tasks', f'chunk{i}.txt')
        print(f"Tarefa de mapeamento para 'chunk{i}.txt' enfileirada.")
    print("✅ Tarefas de mappers enviadas.")

def esperar_mappers(r):
    print("⏳ Aguardando mappers terminarem...")
    pubsub = r.pubsub()
    pubsub.subscribe('mapper_done')
    contador = 0
    while contador < 10:
        mensagem = pubsub.get_message()
        if mensagem and mensagem['type'] == 'message':
            contador += 1
            print(f"📦 Mapper finalizado ({contador}/10)")
        else:
            print("Nenhuma mensagem recebida. Aguardando...")
        time.sleep(1)  # Ajuste o tempo de espera para um intervalo mais longo
    print("✅ Todos os mappers terminaram!")

def iniciar_reducers(r, num_reducers=3):
    print("👉 Iniciando reducers...")
    for i in range(num_reducers):
        r.rpush('reducer_tasks', f'reducer_input_{i}.json')
        print(f"Tarefa de redução para 'reducer_input_{i}.json' enfileirada.")
    print("✅ Tarefas de reducers enviadas.")

def esperar_reducers(r, num_reducers=3):
    print("⏳ Aguardando reducers terminarem...")
    pubsub = r.pubsub()
    pubsub.subscribe('reducer_done')
    contador = 0
    while contador < num_reducers:
        mensagem = pubsub.get_message()
        if mensagem and mensagem['type'] == 'message':
            contador += 1
            print(f"🛠️ Reducer finalizado ({contador}/{num_reducers})")
        else:
            print("Nenhuma mensagem recebida. Aguardando...")
        time.sleep(1)  # Ajuste o tempo de espera para um intervalo mais longo
    print("✅ Todos os reducers terminaram!")

def juntar_resultados():
    print("🧩 Juntando resultados finais...")
    os.makedirs('final', exist_ok=True)
    os.makedirs('reducer_outputs', exist_ok=True)  # Garantir que o diretório de saídas do reducer exista

    with open('final/final_result.txt', 'w', encoding='utf-8') as final_file:
        for nome in os.listdir('reducer_outputs'):
            with open(f'reducer_outputs/{nome}', 'r', encoding='utf-8') as parcial:
                final_file.write(parcial.read())
    print("🏁 Resultado final gerado em 'final/final_result.txt'.")

def main():
    os.makedirs('final', exist_ok=True)  # Cria a pasta final se não existir
    os.makedirs('reducer_outputs', exist_ok=True)  # Cria a pasta reducer_outputs se não existir
    r = redis.Redis()  # Conecta ao Redis

    # Inicia os mappers
    iniciar_mappers(r)
    
    # Espera os mappers finalizarem
    esperar_mappers(r)

    # Executa o shuffle para criar inputs dos reducers
    shuffler.main()  # Executa o shuffle para criar inputs dos reducers

    # Inicia os reducers
    iniciar_reducers(r)

    # Espera os reducers finalizarem
    esperar_reducers(r)

    # Junta os resultados finais
    juntar_resultados()

    print("\n🎉 Tudo pronto! Resultado em 'final/final_result.txt'!")

if __name__ == "__main__":
    main()
#
# In this code, we have added print statements to provide feedback on the progress of each step.                
