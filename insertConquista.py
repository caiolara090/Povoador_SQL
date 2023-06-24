import random
from datetime import date

# Lista de tipos de itens
tipos = ['Arma', 'Equipamento', 'Poder', 'Consumível']

codigos = [1, 104, 134, 277, 366, 388, 408, 586, 725, 870, 928, 1000, 1289, 1629, 1787, 1838, 1986, 2000, 2314, 2405, 2426, 2536, 2552, 2589, 2656, 2708, 2917, 3000, 3184, 3333, 3382, 3394, 3452, 3463, 3483, 3496, 3497, 3498, 3534, 3663, 3699, 3714, 3768, 3781, 3791, 4000, 4002, 4042, 4103, 4246, 4446, 4667, 4700, 4722, 4752, 4806, 4996, 5000, 5185, 5202, 5258, 5401, 5518, 5833, 5955, 6247, 6310, 6411, 6441, 6601, 6613, 6699, 6729, 6748, 6845, 7095, 7239, 7380, 7438, 7513, 7670, 7714, 7734, 7749, 7776, 8112, 8285, 8455, 8485, 8501, 8509, 8516, 8585, 8710, 8793, 8881, 8887, 8889, 9013, 9192, 9255, 9343, 9528, 9756, 9822, 9897]

#codigos = [1000, 2000, 3000, 4000]

# Gerar unidades de itens
def gerar_unidades(num_unidades):
    unidades = []
    
    for _ in range(num_unidades):
        nome_item = f'Conquista-{random.randint(1, 100)}'
        jogo_codigo = random.choice(codigos)  # Considerando que existam 5 jogos na tabela
        tipo = random.choice(tipos)
        imagem = random.randint(100, 800)
        descricao = f'Descrição de {nome_item}'
        
        unidade = (nome_item, jogo_codigo, descricao, imagem)
        unidades.append(unidade)
    
    return unidades

# Gerar 10 unidades de itens aleatórios
unidades_geradas = gerar_unidades(50)

# Gerar comandos INSERT em SQL
insert_commands = []
for unidade in unidades_geradas:
    insert_command = "INSERT INTO `conquista` VALUES"
    insert_command += f"('{unidade[0]}', {unidade[1]}, '{unidade[2]}', '{unidade[3]}');"
    insert_commands.append(insert_command)

# Escrever comandos INSERT no arquivo
with open("insert_commands.txt", "w") as file:
    for insert_command in insert_commands:
        file.write(insert_command + "\n")
