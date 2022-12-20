import sqlalchemy as s
from sqlalchemy import select
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import count

engine = s.create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'

    id_cliente = s.Column(s.Integer, primary_key=True, autoincrement=True)
    nome = s.Column(s.String(20), nullable=False)
    cpf = s.Column(s.String(11), nullable=False, unique=True)
    endereco = s.Column(s.String(25), nullable=False)

    conta = relationship('Conta', back_populates='cliente')

    def __repr__(self):
        return f'id_cliente={self.id_cliente}\nnome={self.nome}\ncpf={self.cpf}\nendereco={self.endereco}'

class Conta(Base):
    __tablename__ = 'conta'

    id_conta = s.Column(s.Integer, primary_key=True, autoincrement=True)
    tipo = s.Column(s.String(20), nullable=False)
    agencia = s.Column(s.String(5), nullable=False, unique=True)
    nro_conta = s.Column(s.Integer, nullable=False, unique=True)
    saldo = s.Column(s.Float, nullable=False)
    id_cliente = s.Column(s.Integer, s.ForeignKey('cliente.id_cliente'))

    cliente = relationship('Cliente', back_populates='conta')

    def __repr__(self):
        return f'id_conta={self.id_conta}\ntipo={self.tipo}\nagencia={self.agencia}\nnro_conta={self.nro_conta}' \
               f'\nsaldo={self.saldo}\nid_cliente={self.id_cliente}'

Base.metadata.create_all(engine)

with Session(engine) as session:
    cliente_01 = Cliente(
        nome='Pedro Cardoso',
        cpf='78965412345',
        endereco='Rua Salvador 25',
        conta=[Conta(
            tipo='Conta Poupança',
            agencia='0001',
            nro_conta='123-7',
            saldo=2500
            )]
    )
    cliente_02 = Cliente(
        nome='Rafael Peixoto',
        cpf='12365478942',
        endereco='Rua Campinas 102',
        conta=[Conta(
            tipo='Conta Corrente',
            agencia='0010',
            nro_conta='321-5',
            saldo=5000
        )]
    )
    cliente_03 = Cliente(
        nome='João Pereira',
        cpf='52463518795',
        endereco='Rua Goiânia 1325',
        conta=[Conta(
            tipo='Conta Corrente',
            agencia='0020',
            nro_conta='852-3',
            saldo=10000
        )]
    )
    cliente_04 = Cliente(
        nome='Matheus Carvalho',
        cpf='54397851463',
        endereco='Rua Santiago 96',
        conta=[Conta(
            tipo='Conta Salário',
            agencia='0017',
            nro_conta='761-1',
            saldo=1500
        )]
    )
    cliente_05 = Cliente(
        nome='Adriano Santos',
        cpf='96325874154',
        endereco='Rua Natal 54',
        conta=[Conta(
            tipo='Conta Poupança',
            agencia='0006',
            nro_conta='542-9',
            saldo=20000
        )]
    )
    cliente_06 = Cliente(
        nome='Pedro Silva',
        cpf='15795348625',
        endereco='Rua Rio Branco 2365',
        conta=[Conta(
            tipo='Conta Corrente',
            agencia='0027',
            nro_conta='953-6',
            saldo=7400
        )]
    )
    cliente_07 = Cliente(
        nome='João Barbosa',
        cpf='75195385297',
        endereco='Rua Alagoas 7',
        conta=[Conta(
            tipo='Conta Corrente',
            agencia='0025',
            nro_conta='458-3',
            saldo=5500
        )]
    )
    cliente_08 = Cliente(
        nome='Breno Dias',
        cpf='95175396312',
        endereco='Rua Brasília 13',
        conta=[Conta(
            tipo='Conta Corrente',
            agencia='0725',
            nro_conta='634-5',
            saldo=3750
        )]
    )
    cliente_09 = Cliente(
        nome='Matheus Souza',
        cpf='14796365241',
        endereco='Rua Amazonas 22',
        conta=[Conta(
            tipo='Conta Poupança',
            agencia='0305',
            nro_conta='520-5',
            saldo=15000
        )]
    )
    cliente_10 = Cliente(
        nome='Maria Vasconcelos',
        cpf='96478525695',
        endereco='Rua Rio de Janeiro 47',
        conta=[Conta(
            tipo='Conta Corrente',
            agencia='5305',
            nro_conta='201-7',
            saldo=50000
        )]
    )
    cliente_11 = Cliente(
        nome='Fernanda Carvalho',
        cpf='45871973628',
        endereco='Rua Amapá 63',
        conta=[Conta(
            tipo='Conta Corrente',
            agencia='1327',
            nro_conta='254-8',
            saldo=75600
        )]
    )
    cliente_12 = Cliente(
        nome='Paula Guimarães',
        cpf='95175345796',
        endereco='Rua Santa Catarina 27',
        conta=[Conta(
            tipo='Conta Salário',
            agencia='0508',
            nro_conta='997-8',
            saldo=3000
        )]
    )
    cliente_13 = Cliente(
        nome='Ana Barbosa',
        cpf='15320096582',
        endereco='Rua São Paulo 987',
        conta=[Conta(
            tipo='Conta Corrente',
            agencia='0989',
            nro_conta='556-1',
            saldo=12500
        )]
    )
    cliente_14 = Cliente(
        nome='Bianca Siqueira',
        cpf='22654397520',
        endereco='Rua Bahia 41',
        conta=[Conta(
            tipo='Conta Corrente',
            agencia='3879',
            nro_conta='721-3',
            saldo=7400
        )]
    )
    cliente_15 = Cliente(
        nome='Julia Pereira',
        cpf='12085246397',
        endereco='Rua Minas Gerais 2',
        conta=[Conta(
            tipo='Conta Poupança',
            agencia='0183',
            nro_conta='258-3',
            saldo=120000
        )]
    )
    cliente_16 = Cliente(
        nome='Carolina Sampaio',
        cpf='14851679542',
        endereco='Rua Belo Horizonte 91',
        conta=[Conta(
            tipo='Conta Corrente',
            agencia='1122',
            nro_conta='335-4',
            saldo=26000
        )]
    )

    session.add_all([cliente_01, cliente_02, cliente_03, cliente_04, cliente_05, cliente_06, cliente_07, cliente_08,
                     cliente_09, cliente_10, cliente_11, cliente_12, cliente_13, cliente_14, cliente_15, cliente_16])
    session.commit()


def query(stmt):
    for results in session.scalars(stmt):
        print('*' * 15)
        print(results)
        print('*' * 15)

def query_with_connection(stmt):
    connection = engine.connect()
    results = connection.execute(stmt).fetchall()
    for result in results:
        print('*' * 15)
        print(result)
        print('*' * 15)


# Dados das pessoas que possuem Conta Salário
stmt_01 = select(Conta).where(Conta.tipo.in_(['Conta Salário']))
query(stmt_01)
# print(stmt_01)


# Números de conta em ordem decrescente de saldo
stmt_02 = select(Conta.nro_conta).order_by(Conta.saldo.desc())
query(stmt_02)
# print(stmt_02)

# Nomes, números da conta e saldos maiores que R$10.000 ordenados por saldo em ordem crescente
stmt_03 = select(Cliente.nome, Conta.nro_conta, Conta.saldo).join_from(Cliente, Conta).where(Conta.saldo >= 10000).order_by(Conta.saldo.asc())
query_with_connection(stmt_03)
# print(stmt_03)

#Total de cada tipo de conta
stmt_04 = select(count(Cliente.nome), Conta.tipo).join_from(Cliente, Conta).group_by(Conta.tipo)
query_with_connection(stmt_04)
# print(stmt_04)
