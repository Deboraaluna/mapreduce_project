import redis
import time
import os
import shuffler

def iniciar_mappers(r):
    for i in range(10):
        r.rpush('mapper_tasks', f'chunk{i}.txt')

def esperar_mappers(r):
    contador = 0
    while contador < 10:
        mensagem = r.pubsub().get_message()
        if mensagem and mensagem['type'] == 'message':
            contador += 1
        time.sleep(0.5)

def iniciar_reducers(r, num_reducers=3):
    for i in range(num_reducers):
        r.rpush('reducer_tasks', f'reducer_input_{i}.json')

def esperar_reducers(r, num_reducers=3):
    contador = 0
    while contador < num_reducers:
        mensagem = r.pubsub().get_message()
        if mensagem and mensagem['type'] == 'message':
            contador += 1
        time.sleep(0.5)

def juntar_resultados():
    with open('final/final_result.txt', 'w', encoding='utf-8') as final_file:
        for nome in os.listdir('reducer_outputs'):
            with open(f'reducer_outputs/{nome}', 'r', encoding='utf-8') as parcial:
                final_file.write(parcial.read())

def main():
    os.makedirs('final', exist_ok=True)
    r = redis.Redis()
    
    iniciar_mappers(r)
    esperar_mappers(r)

    shuffler.main()

    iniciar_reducers(r)
    esperar_reducers(r)

    juntar_resultados()
    print("✅ Tudo pronto! Resultado final em final/final_result.txt")

if __name__ == "__main__":
    main()



