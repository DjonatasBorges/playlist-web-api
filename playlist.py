from flask import Flask, jsonify, request
import requests

playlist = Flask(__name__)

musicas = [
    {
        "musica": "In the End",
        "estilo": "New Metal",
        "id": 0
    },
    {
        "musica": "Eu bebo se beija",
        "estilo": "Sertanejo Universitário",
        "id": 1
    },
    {
        "musica": "Menino da Porteira",
        "estilo": "Sertanejo Raiz",
        "id": 2
    },
    {
        "musica": "Dependente",
        "estilo": "Pagode",
        "id": 3
    },
    {
        "musica": "Jesus Chorou",
        "estilo": "Rap",
        "id": 4
    }
]


@playlist.route('/musicas')
def obter_musicas():
    return jsonify(musicas)


@playlist.route('/musicas/<int:indice>', methods=['GET'])
def obter_musicas_por_id(indice):
    try:
        if musicas[indice] is not None:
            return jsonify(musicas[indice])
    except:
        return jsonify(f'A música de núnero {indice} não esta disponível. A playlist está com {len(musicas)} músicas até o momento. Lembramos que a música começa no índice 0', 404)


@playlist.route('/musicas', methods=['POST'])
def postar_musica():
    musica = request.get_json()
    musicas.append(musica)
    return jsonify(musica, 200)


@playlist.route('/musicas/<int:indice>', methods=['PUT'])
def repost(indice):
    repostagem = request.get_json()
    musicas[indice].update(repostagem)

    return jsonify(musicas[indice], 200)


@playlist.route('/musicas/<int:indice>', methods=['DELETE'])
def deletar(indice):
    try:
        if musicas[indice] is not None:
            deletada = musicas[indice]['musica']
            del musicas[indice]
            return jsonify(f'A música {deletada} foi deletada', 200)
    except:
        return jsonify('Não foi possível encontrar a música para exclusão', 404)


playlist.run(port=9999, host='localhost', debug=True)