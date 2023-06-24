import random

categorias_jogos = [
    "Ação",
    "Aventura",
    "RPG",
    "Estratégia",
    "Esportes",
    "Corrida",
    "Puzzle",
    "Simulação",
    "FPS",
    "Luta",
    "Plataforma",
    "Tiro em terceira pessoa",
    "Survival Horror",
    "Mundo aberto",
    "RPG de ação",
    "Hack and slash",
    "Musical",
    "Casual",
    "Jogo de cartas",
    "Jogo de tabuleiro",
    "Raciocínio",
    "Quiz",
    "MMO",
    "Realidade virtual",
    "Construção",
    "Esportes radicais",
    "Combate aéreo",
    "Stealth",
    "Educativo",
    "Party game"
]

def gerar_comando_insert(codigo_jogo, categoria_jogo):
    comando = "INSERT INTO `categoria_jogo` VALUES ('{}', '{}');\n".format(codigo_jogo, categoria_jogo)
    return comando

# Número de comandos de inserção que você deseja gerar
num_comandos = 20

codigo_jogos = [1, 104, 134, 277, 366, 388, 408, 586, 725, 870, 928, 1000, 1289, 1629, 1787, 1838, 1986, 2000, 2314, 2405, 2426, 2536, 2552, 2589, 2656, 2708, 2917, 3000, 3184, 3333, 3382, 3394, 3452, 3463, 3483, 3496, 3497, 3498, 3534, 3663, 3699, 3714, 3768, 3781, 3791, 4000, 4002, 4042, 4103, 4246, 4446, 4667, 4700, 4722, 4752, 4806, 4996, 5000, 5185, 5202, 5258, 5401, 5518, 5833, 5955, 6247, 6310, 6411, 6441, 6601, 6613, 6699, 6729, 6748, 6845, 7095, 7239, 7380, 7438, 7513, 7670, 7714, 7734, 7749, 7776, 8112, 8285, 8455, 8485, 8501, 8509, 8516, 8585, 8710, 8793, 8881, 8887, 8889, 9013, 9192, 9255, 9343, 9528, 9756, 9822, 9897]

with open("comandos_insert.txt", "w") as arquivo:
    for _ in range(num_comandos):
        codigo_jogo = random.choice(codigo_jogos)
        categoria_jogo = random.choice(categorias_jogos)
        comando_insert = gerar_comando_insert(codigo_jogo, categoria_jogo)
        arquivo.write(comando_insert)
