# FastAPI Multitenant

Exemplo de aplicação multitenant com estratégia de isolamento de banco de dados único com múltiplos schemas. Conteúdo apresentado na Python Sul 2022. [Apresentação de slides](https://docs.google.com/presentation/d/1goJIzpQUDE0mAkSAJhVkxil5AGlAkP4M4TmxdI3cGhc/edit?usp=sharing)

## Pré-requisitos

* Python 3.8+
* Docker
* Docker-compose

## Instalação

Clone o repositório e crie um virtual env.

```bash
virtualenv venv
source venv/bin/activate
```

Instale as dependências

```bash
pip install -r requirements.txt
```

Inicialize o docker com a instância do Postgres

```bash
docker-compose up -d
```

Modifique o arquivo `/etc/hosts` com domínios de exemplo:

```
127.0.0.1	meudominio.com.br
127.0.0.1	cia_a.meudominio.com.br
127.0.0.1	cia_b.meudominio.com.br
127.0.0.1	cia_c.meudominio.com.br
```

## Execução

```bash
uvicorn main:app --port 9000 --reload
```

## Acessando a documentação da API

http://cia_a.meudominio.com.br:9000/docs
