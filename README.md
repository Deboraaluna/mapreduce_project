# MapReduce Project

Este projeto implementa o modelo de programação MapReduce para processar grandes volumes de dados de forma distribuída.

## Pré-requisitos

Certifique-se de ter os seguintes itens instalados em sua máquina:
- [Git](https://git-scm.com/)
- [Python 3.x](https://www.python.org/downloads/) (ou outra linguagem usada no projeto)

## Clonando o repositório

Para clonar este repositório, execute o seguinte comando no terminal:

```bash
git clone https://github.com/seu-usuario/mapreduce_project.git
cd mapreduce_project
```

## Instalando dependências

O projeto utiliza Python, instale as dependências com:

```bash
pip install -r 
```

## Executando o projeto

1. Certifique-se de que os dados de entrada estão no diretório correto ou configure o caminho no código.
2. Execute o script principal:

```bash
python main.py
```

Substitua `main.py` pelo nome do arquivo principal do projeto, se necessário.

## Estrutura do projeto

- `main.py`: Arquivo principal para execução do projeto.
- `mapper.py`: Implementação da função Map.
- `reducer.py`: Implementação da função Reduce.
- `data/`: Diretório para armazenar os dados de entrada e saída.

## Para Rodar

- `redis-cli`: Execute esse arquivo Arquivo que está dentro do diretório onde o Redis foi instalado.

![exemplo redis-cli](img\redis-cli.png)

- `start_all.bat`: Depois dê dois cliques nesse arquivo .bat localizado dentro da pasta do projeto, dessa forma esse scrip vai rodar toda aplicação evitando perder tempo rodando varios terminais manualmente.
- 'obs': você só irar seguir para o próximo passo quando o `start_all.bat` tiver retornando "NENHUMA MENSSAGEM RECEBIDA...

![exemplo Nenhuma msg recebida](img\arquivo_bat.png)

- `redis-cli`: Feito os passos anteriores, volte para o terminal redis-cli que voce abriu e digite o comando a seguir 10x mudando apenas a numeração contida em "chunks".
# EXEMPLO:
PUBLISH mapper_done "chunk0.txt"
 -ENTER
PUBLISH mapper_done "chunk1.txt"
-ENTER
 PUBLISH mapper_done "chunk2.txt"
 -ENTER
 "               "
 E assim por diante até...
  PUBLISH mapper_done "chunk9.txt"
  ## DICA: OLHAR A IMG 1
- `start_all.bat`: Por fim, procure nas abas do arquivo bat gerou a que estava retornando "NENHUMA MENSSAGEM ENCONTRADA..., terá atualizado e irá estar carregando e rodando o restante do que é necessário na aplicação.

![exemplo - aplicação rodou e gerou todos os arquivos](img\bat_concluido.png)


## Contribuindo

Sinta-se à vontade para abrir issues ou enviar pull requests. Toda contribuição é bem-vinda!

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato

Se tiver dúvidas, entre em contato pelo e-mail: deboraffcruz@gmail.com