from database.db import db
from model.trainer import Trainer
from model.pokemon import Pokemons
from app import app
from flask import request, jsonify
import json
import requests

# use_requests
# recebe como parametro o nome ou id do pokemon e busca na poke API
def use_requests(pokemon_id):
    pokemon_url = 'https://pokeapi.co/api/v2/pokemon/' + str(pokemon_id)
    response = requests.get(pokemon_url)
    json_response = json.loads(response.text)
    return json_response


@app.route('/trainer/<id>/pokemon/<pokemon_id>', methods=['GET'])
def get_trainer_pokemon(id, pokemon_id):

    # Verifica se o id informado pertence a um treinador
    # Caso não exista, retorna 404.
    Trainer.query.get_or_404(id)

    # verifica se o pokemon já exite para o treinador informado
    # utlizando a chave composta trainer_id e pokemon_id
    pokemon = Pokemons.query.get_or_404((id, pokemon_id))

    # chama o metodo use_requests passando como parametro o id do pokemon
    pokemon_result = use_requests(pokemon.pokemon_id)
    
    # criando um novo objeto para armazenar e atualizar as informações
    # da requisição e do retorno da pokeAPI.
    pokemon_data = {
        "id": pokemon.trainer_id,
        "name": pokemon_result['name'],
        "level": pokemon.level,
        "pokemon_data": pokemon_result
    }
    # converte o objeto criado em json para o retorno
    return jsonify(pokemon_data)


@app.route('/trainer/<id>/pokemon', methods=['GET'])
def get_pokemon_data(id):

    # Verifica se o id informado pertence a um treinador
    # Caso não exista, retorna 404.
    Trainer.query.get_or_404(id)

    # pega os registros na tabela da classe Pokemons e compara o id
    # com o id passado na requisição pela url
    pokemons_owned = Pokemons.query.filter(Pokemons.trainer_id == id).all()

    # cria um array vazio de pokemons_owned
    pokemons_owned_result = []

    # laço criado para pegar todas as informações 
    for pokemon in pokemons_owned:

        # criando um novo objeto para armazenar e atualizar as informações
        # da requisição e do retorno da pokeAPI.
        api_result = use_requests(pokemon.pokemon_id)
        pokemon_data = {
            "id": pokemon.trainer_id,
            "name": api_result['name'],
            "level": pokemon.level,
            "pokemon_data": api_result
        }

        # adiciona pokemon_data ao array vazio
        pokemons_owned_result.append(pokemon_data)

    #converte o objeto criado em json para o retorno   
    return jsonify(pokemons_owned_result)


@app.route('/trainer/<id>/pokemon', methods=['POST'])
def add_pokemon_trainer(id):
    # Verifica se o id informado pertence a um treinador
    # Caso não exista, retorna 404.
    Trainer.query.get_or_404(id)
    
    # Lê o body enviado junto a requisição
    body = request.get_json()

    # chama o metodo use_requests passando como parametro o nome do pokemon
    result_pokemon = use_requests(body['name'])

    # verifica se o id passado na requisição é diferente do id retornado da API.
    # se o id for diferente, retorna informando que o Id está incorreto. 
    if body['pokemon_id'] != result_pokemon['id']:
        return 'Incorrect pokemon id', 400

    # verifica se o pokemon já exite para o treinador informado
    # utlizando a chave composta trainer_id e pokemon_id
    pokemon = Pokemons.query.get((id, result_pokemon['id']))
    if pokemon:
        return "Pokemon already exits", 400

    # cria conexão no banco instanciando a classe Pokemons acessando a tabela relacionada
    # passando como parâmetro o body da requisição e o ID que recebe da PokeAPI
    db.session.add(
        Pokemons(body['name'], body['level'], result_pokemon['id'], id))
    db.session.commit()

    # criando um novo objeto para armazenar e atualizar as informações
    # da requisição e do retorno da pokeAPI.
    pokemon = Pokemons.query.get((id, result_pokemon['id']))
    pokemon_added = {
        "id": pokemon.trainer_id,
        "name": result_pokemon['name'],
        "level": pokemon.level,
        "pokemon_data": result_pokemon
    }

    # converte o objeto criado em json para o retorno
    return jsonify(pokemon_added)


@app.route('/trainer/<id>', methods=['GET'])
def get_trainer(id):

    # Verifica se o id informado pertence a um treinador
    # Caso não exista, retorna 404
    trainer = Trainer.query.get_or_404(id)

    # deleta a propriedade _sa_instance_state do objeto trainer
    del trainer.__dict__['_sa_instance_state']
    
    # Retira espaços dos atributos
    # https://stackoverflow.com/questions/8907788/iterating-over-a-dictionary-in-python-and-stripping-white-space
    clean_trainer = { k:str(v).strip() for k, v in trainer.__dict__.items()}
    clean_trainer['id'] = int(id)


    # converte o objeto criado em json para o retorno
    return jsonify(clean_trainer)


@app.route('/trainer', methods=['GET'])
def get_all_trainers():
    # cria um array vazio de trainers
    trainers = []

    # laço de repetição criado acessar todos os registros da tabela da classe Trainer
    # e adicionar os registros no array trainers
    for trainer in db.session.query(Trainer).all():
        del trainer.__dict__['_sa_instance_state']

        # Retira espaços dos atributos
        # https://stackoverflow.com/questions/8907788/iterating-over-a-dictionary-in-python-and-stripping-white-space
        clean_trainer = { k:str(v).strip() for k, v in trainer.__dict__.items()}
        clean_trainer['id'] = trainer.id
        trainers.append(clean_trainer)
        
    # converte o objeto criado em json para o retorno    
    return jsonify(trainers)


@app.route('/trainer', methods=['POST'])
def create_trainer():

    # Lê o body enviado junto a requisição
    body = request.get_json()

    # cria conexão no banco instanciando a classe Trainer acessando a tabela relacionada
    # passando como parâmetro o body da requisição.
    db.session.add(Trainer(body['nickname'], body['first_name'], body['last_name'],
                           body['email'], body['password'], body['team']))
    db.session.commit()
    return "trainer created"


@app.route('/trainer/<id>', methods=['DELETE'])
def delete_trainer(id):

    # realiza uma query de pesquisa do id na tabela da classe Trainer
    # e compara com o id passado na requisição pela url e deleta o registro.
    Trainer.query.filter(Trainer.id == id).delete()

    # busca os pokemons do treinador e deleta.
    Pokemons.query.filter(Pokemons.trainer_id == id).delete()

    db.session.commit()
    return "trainer deleted"