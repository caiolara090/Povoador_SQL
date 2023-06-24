import random

# Lista de nomes de publicadoras famosas
publicadoras = ['Electronic Arts', 'Ubisoft', 'Activision', 'Nintendo', 'Square Enix', 'Rockstar Games', 'Bethesda Softworks', 'Capcom', 'Sony Interactive Entertainment', 'Microsoft Studios']

# Lista de nomes de desenvolvedores famosos
desenvolvedores = ['Naughty Dog', 'CD Projekt Red', 'Valve Corporation', 'BioWare', 'Blizzard Entertainment', 'FromSoftware', 'Epic Games', 'Gearbox Software', 'Bungie', 'Konami']

# Lista de jogos disponíveis
jogos = [    "The Forgotten Realms Expansion",
    "Rise of the Titans DLC",
    "Shadows Edge: The Dark Awakening",
    "Lost City Chronicles: Secrets Unveiled",
    "Eternal Kingdoms: Reign of Legends",
    "Mystic Isles: Enchanted Quest",
    "Cybernetic Revolution: Future Warfare",
    "Ancient Prophecies: Uncharted Realms",
    "Frostfall: Arctic Expeditions",
    "Legends of Valor: Epic Trials"]

# Gera um valor de saldo aleatório
def gerar_saldo():
    return random.randint(0, 100)

#codigos = [1, 104, 134, 277, 366, 388, 408, 586, 725, 870, 928, 1000, 1289, 1629, 1787, 1838, 1986, 2000, 2314, 2405, 2426, 2536, 2552, 2589, 2656, 2708, 2917, 3000, 3184, 3333, 3382, 3394, 3452, 3463, 3483, 3496, 3497, 3498, 3534, 3663, 3699, 3714, 3768, 3781, 3791, 4000, 4002, 4042, 4103, 4246, 4446, 4667, 4700, 4722, 4752, 4806, 4996, 5000, 5185, 5202, 5258, 5401, 5518, 5833, 5955, 6247, 6310, 6411, 6441, 6601, 6613, 6699, 6729, 6748, 6845, 7095, 7239, 7380, 7438, 7513, 7670, 7714, 7734, 7749, 7776, 8112, 8285, 8455, 8485, 8501, 8509, 8516, 8585, 8710, 8793, 8881, 8887, 8889, 9013, 9192, 9255, 9343, 9528, 9756, 9822, 9897]


codigos = [1000, 2000, 3000, 4000, 1, 104, 134, 277]
# Gera comandos INSERT aleatórios
def gerar_inserts(num_inserts):
    inserts = []
    
    for _ in range(num_inserts):
        nome = random.choice(jogos)
        codigo_jogo = random.choice(codigos)
        publi_dlc = random.choice(publicadoras)
        desenvolvedor_dlc = random.choice(desenvolvedores)
        preco = round(random.uniform(1, 100), 2)
        saldo = gerar_saldo()
        
        insert_command = f"INSERT INTO `dlc` VALUES "
        insert_command += f"('{nome}', {codigo_jogo}, '{publi_dlc}', '{desenvolvedor_dlc}', {preco});"
        
        inserts.append(insert_command)
    
    return inserts

# Define o número de comandos INSERT a serem gerados
num_inserts = 10

# Gera os comandos INSERT
inserts_gerados = gerar_inserts(num_inserts)

# Escreve os comandos INSERT no arquivo
with open("insert_commands.txt", "w") as file:
    for insert_command in inserts_gerados:
        file.write(insert_command + "\n")
