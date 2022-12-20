from pymongo import MongoClient
from pymongo.server_api import ServerApi
import pprint

client = MongoClient("mongodb+srv://<username>:<password>@cluster0.m0fjl5a.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.test_database
# Ao criar um cluster no Mongo Atlas, a própria aplicação nos dá as variáveis "client" e "db" para testar o banco de
# dados inicializado. A string na instância de "MongoClient" também é fornecida.

novos_clientes = [
        {"nome": "Pedro Cardoso",
        "cpf": "78965412345",
        "endereco": "Rua Salvador 25",
        "nro_conta": "123-7",
        "tipo": "Conta Corrente",
        "agencia": "0001",
        "saldo": 2500},

        {"nome": "Rafael Peixoto",
        "cpf": "12365478942",
        "endereco": "Rua Campinas 102",
        "nro_conta": "321-5",
        "tipo": "Conta Corrente",
        "agencia": "0010",
        "saldo": 5000},

        {"nome": "João Pereira",
        "cpf": "52463518795",
        "endereco": "Rua Goiânia 1325",
        "nro_conta": "852-3",
        "tipo": "Conta Corrente",
        "agencia": "0020",
        "saldo": 10000},

        {"nome": "Edna Silva",
        "cpf": "48625319742",
        "endereco": "Rua Petrópolis 325",
        "nro_conta": "252-3",
        "tipo": "Conta Corrente",
        "agencia": "1030",
        "saldo": 10000},

        {"nome": "Matheus Carvalho",
        "cpf": "54397851463",
        "endereco": "Rua Santiago 96",
        "nro_conta": "761-1",
        "tipo": "Conta Salário",
        "agencia": "0017",
        "saldo": 1500},

        {"nome": "Adriano Santos",
        "cpf": "96325874154",
        "endereco": "Rua Natal 54",
        "nro_conta": "542-9",
        "tipo": "Conta Poupança",
        "agencia": "0006",
        "saldo": 20000},

        {"nome": "Pedro Silva",
        "cpf": "15795348625",
        "endereco": "Rua Rio Branco 2365",
        "nro_conta": "953-6",
        "tipo": "Conta Corrente",
        "agencia": "0027",
        "saldo": 7400},

        {"nome": "João Barbosa",
        "cpf": "75195385297",
        "endereco": "Rua Alagoas 7",
        "nro_conta": "458-3",
        "tipo": "Conta Corrente",
        "agencia": "0025",
        "saldo": 5500},

        {"nome": "Breno Dias",
        "cpf": "95175396312",
        "endereco": "Rua Brasília 13",
        "nro_conta": "634-5",
        "tipo": "Conta Corrente",
        "agencia": "0725",
        "saldo": 3750},

        {"nome": "Matheus Souza",
        "cpf": "14796365241",
        "endereco": "Rua Amazonas 22",
        "nro_conta": "520-5",
        "tipo": "Conta Poupança",
        "agencia": "0001",
        "saldo": 15000},

        {"nome": "Maria Vasconcelos",
        "cpf": "96478525695",
        "endereco": "Rua Rio de Janeiro 47",
        "nro_conta": "201-7",
        "tipo": "Conta Corrente",
        "agencia": "5305",
        "saldo": 50000},

        {"nome": "Fernanda Carvalho",
        "cpf": "45871973628",
        "endereco": "Rua Amapá 63",
        "nro_conta": "254-8",
        "tipo": "Conta Corrente",
        "agencia": "1327",
        "saldo": 75600},

        {"nome": "Paula Guimarães",
        "cpf": "95175345796",
        "endereco": "Rua Santa Catarina 27",
        "nro_conta": "997-8",
        "tipo": "Conta Salário",
        "agencia": "0508",
        "saldo": 2500},

        {"nome": "Ana Barbosa",
        "cpf": "15320096582",
        "endereco": "Rua São Paulo 987",
        "nro_conta": "556-1",
        "tipo": "Conta Corrente",
        "agencia": "0989",
        "saldo": 12500},

        {"nome": "Bianca Siqueira",
        "cpf": "22654397520",
        "endereco": "Rua Bahia 41",
        "nro_conta": "721-3",
        "tipo": "Conta Corrente",
        "agencia": "3879",
        "saldo": 7400},

        {"nome": "Julia Pereira",
        "cpf": "12085246397",
        "endereco": "Rua Minas Gerais 2",
        "nro_conta": "258-3",
        "tipo": "Conta Poupança",
        "agencia": "0183",
        "saldo": 120000},

        {"nome": "Carolina Sampaio",
        "cpf": "14851679542",
        "endereco": "Rua Belo Horizonte 91",
        "nro_conta": "335-4",
        "tipo": "Conta Corrente",
        "agencia": "1122",
        "saldo": 26000
        }]



clientes = db.clientes
# result = clientes.insert_many(novos_clientes)  # Irá sempre inserir os novos clientes a cada vez que rodar o código.

# Dados dos clientes que possuem conta salário
for cliente in clientes.find({"tipo": "Conta Salário"}):
        print('*'*30)
        pprint.pprint(cliente)
        print('*'*30)

# Total de clientes com saldo de R$10.000,00
print(clientes.count_documents({"saldo": 10000}))

# Busca específica por nome
pprint.pprint(clientes.find_one({"nome": "João Barbosa"}))