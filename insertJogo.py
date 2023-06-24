import random

def generate_random_game():
    classificacoes_indicativas = [0, 6, 12, 16, 18]
    desenvolvedores = ["Desenvolvedor1", "Desenvolvedor2", "Desenvolvedor3"]
    publicadores = ["Publicador1", "Publicador2", "Publicador3"]
    adjectives = ["Amazing", "Fantastic", "Epic", "Awesome", "Incredible", "Legendary", "Spectacular", "Majestic", "Glorious", "Marvelous", "Thrilling", "Unforgettable", "Stunning", "Exhilarating", "Breathtaking"]
    nouns = ["Game", "Adventure", "World", "Quest", "War", "Journey", "Saga", "Legend", "Realm", "Battle", "Champion", "Hero", "Epic", "Masterpiece", "Warrior"]

    nome = generate_random_name(adjectives, nouns)
    classificacao_indicativa = random.choice(classificacoes_indicativas)
    desenvolvedor = random.choice(desenvolvedores)
    publicador = random.choice(publicadores)
    preco = round(random.uniform(0.99, 59.99), 2)

    game = {
        'codigo': random.randint(1, 10000),
        'nome': nome,
        'classificacao_indicativa': classificacao_indicativa,
        'desenvolvedor': desenvolvedor,
        'publicador': publicador,
        'preco': preco
    }

    return game

def generate_random_name(adjectives, nouns):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    name = f"{adjective} {noun}"

    return name

def generate_insert_command(game):
    insert_command = "INSERT INTO `jogo` VALUES "
    insert_command += f"('{game['codigo']}','{game['nome']}', {game['classificacao_indicativa']}, '{game['desenvolvedor']}', '{game['publicador']}', {game['preco']});"

    return insert_command

def generate_games(num_games):
    games = []

    for _ in range(num_games):
        game = generate_random_game()
        games.append(game)

    return games

def generate_insert_commands_file(games, file_name):
    with open(file_name, 'w') as file:
        for game in games:
            insert_command = generate_insert_command(game)
            file.write(insert_command + '\n')

num_games = 100
games = generate_games(num_games)
generate_insert_commands_file(games, 'insert_commands.txt')
