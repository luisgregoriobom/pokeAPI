# PokeAPI

# Objetivo
O objetivo desse projeto é demonstrar meus conhecimentos adquiridos em áreas ao desenvolvimento back-end em Python! 

# Detalhes: 
O projeto baseia-se na <a href="https://pokeapi.co/">PokeAPI</a> para desenvolver uma aplicação que ofereça o CRUD de um novo recurso <b>TRAINER</b>

# O que foi desenvolvido:
- [x] CRUD do recurso Trainer
- [x] <a href="https://pokeapi.co/">PokeAPI</a> consumida
- [x] Readme com instruções de como instalar, fazer funcionar e etc.

# Tecnologias
O projeto em Python foi desenvolvido com o framework <b>FLASK</b>, o motivo da escolha do framework foi por conta deste framework fornecer ao desenvolvedor as necessidades básicas para o desenvolvimento web de um jeito simples e fácil! 

Docker foi usado para facilitar a instalação do banco postgress e adminer e também o deployment para aws! 

# Como utilizar este projeto:

Devemos ter no computador, como pré-requisito Python3, Docker e o pip instalados! 

<h1>  Para Windows: </h1>
Devemos começar instalando o <b>Terminal WSL Ubuntu</b> no windows, para isso podemos abrir o <b>PowerShell</b> como administrador rodando o comando:

```
$ wsl.exe --install
```
Esse simples comando instala o subsistema e também o Ubuntu como distribuição padrão junto com o kernel mais recente no dispositivo.

<p>

Com esse comando você pode atualizar o kernel. O Ubuntu aparecerá após a reinicialização.
```
$ wsl --update
``` 
<p>
 
Clonar repositório:
```
$ git clone https://github.com/luisgregoriobom/pokeAPI.git
```
<p>
 
E na sequencia instalaremos o postgreSQL
 
```
$ sudo apt-get install postgresql
``` 
<p> 
Abrir o docker e rodar os seguintes comandos no seu terminal wsl:
 
```
$ cd trainerapp
``` 
```
$ export DATABASE_URL="postgresql://username:userpass@localhost:5433/pokemon"
``` 
```
$ docker build -t trainer_image .
```
```
$ docker-compose -f docker-compose-dev.yml up -d.
```

Agora acessamos a pasta do diretorio PokeAPI:

```
$ cd PokeAPI
``` 
<p>
Para instalar as dependências necessárias do projeto, rode o comando no seu terminal, dentro da pasta raiz do projeto:
 
```
$ pip install -r requirements.txt
``` 
<p>
 
Feito isso, rodar o comando
 
```
$ flask run
```

# Endpoints
Para testar as requisições, utilize o endereço: 
<p>
http://ec2-34-203-236-97.compute-1.amazonaws.com:5001/

<h3> ENDPOINTS DISPONÍVEIS: </h3>

 
- [x] GET - /trainer<id>/pokemon/<pokemon_id> - Retorna o Treinador e o Pokemon pelo id
- [x] GET - /trainer<id>/pokemon - Retorna o Treinador com seus Pokemons
- [x] GET - /trainer/<id> - Retorna o Treinador
- [x] GET - /trainer - Retorna todos os Treinadores
- [x] POST - /trainer - Cria um treinador
- [x] POST - /trainer<id>/pokemon - Adiciona um pokemon a um treinador existente
- [x] DELETE - /trainer/<id> - Deleta um treinador

# Banco de Dados
URL: http://ec2-34-203-236-97.compute-1.amazonaws.com:8080/
<p>
Para acessar ao banco, utilize esses requisitos na tela de login:
<p>
<b>SISTEMA:</b> PostgresSQL
<p>
<b>USUARIO:</b> username
<p>
<b>PASSWORD:</b> userpass
<p>
Clique em <b> ENTRAR </b>


