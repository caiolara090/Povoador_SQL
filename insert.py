import random
import string

existing_usernames = []

def generate_random_username(existing_usernames):
    while True:
        username = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
        if username not in existing_usernames:
            return username

def generate_random_name():
    names = ['John', 'Alice', 'Bob', 'Emily', 'David', 'Olivia', 'Paula', 'Mario', 'Pedro', 'Augusto', 'Joana', 'Lucy',
             'Mary', 'Peter', 'Lucas', 'Caio', 'Luiz Fernando', 'Thales', 'Victor', 'Julio']
    sobrenomes = [
    "Silva",
    "Santos",
    "Oliveira",
    "Pereira",
    "Souza",
    "Rodrigues",
    "Almeida",
    "Lima",
    "Ferreira",
    "Ribeiro",
    "Carvalho",
    "Gomes",
    "Martins",
    "Costa",
    "Sousa"
]

    carac = ["!!", ".", "_", "-"]

    return random.choice(names) + random.choice(carac) + random.choice(sobrenomes)

def generate_random_age():
    return random.randint(18, 60)

def generate_random_email():
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com']
    username = generate_random_username(existing_usernames)
    domain = random.choice(domains)
    return f"{username}@{domain}"

def generate_random_telephone():
    return random.randint(10000000, 99999999)

def generate_random_saldo():
    return random.randint(0, 1000)

def generate_insert_command(existing_usernames):
    username = generate_random_username(existing_usernames)
    nome = generate_random_name()
    idade = generate_random_age()
    email = generate_random_email()
    telefone = generate_random_telephone()
    saldo = generate_random_saldo()

    insert_command = f"INSERT INTO `usuario` VALUES ('{username}', '{nome}', {idade}, '{email}', {telefone}, {saldo});\n"
    existing_usernames.add(username)
    return insert_command

def generate_insert_commands_file(num_commands, file_name):
    existing_usernames = set()
    with open(file_name, 'w') as file:
        for _ in range(num_commands):
            insert_command = generate_insert_command(existing_usernames)
            file.write(insert_command)

generate_insert_commands_file(100, 'insert_commands.txt')
