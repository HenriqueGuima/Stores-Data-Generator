import random
import pandas as pd
from faker import Faker
import numpy as np
from datetime import datetime, timedelta

# Inicializar o gerador de dados fictícios
fake = Faker()

portuguese_cities = [
    "Lisbon",
    "Porto",
    "Amadora",
    "Braga",
    "Coimbra",
    "Funchal",
    "Vila Nova de Gaia",
    "Aveiro",
    "Setúbal",
    "Évora",
    "Leiria",
    "Faro",
    "Albufeira",
    "Cascais",
    "Ponta Delgada",
    "Viseu",
    "Beja",
    "Évora",
    "Guimarães",
    "Sintra",
    "Maia",
    "Oeiras",
    "Caldas da Rainha",
    "Viana do Castelo",
    "Bragança",
    "Santarém",
    "Castelo Branco",
    "Vila Real",
    "Póvoa de Varzim",
    "Tavira",
    "Angra do Heroísmo",
    "Sesimbra",
    "Loulé",
    "Vila do Conde",
    "Sines",
    "Monção",
    "Tomar",
    "Vila Franca de Xira",
    "Ovar",
    "Celorico de Basto",
    "Aljezur",
    "Peniche",
    "Cantanhede",
    "Alcobaça",
    "Gondomar",
    "S. João da Madeira",
    "Loures",
    "Barcelos",
    "Mirandela",
    "Caminha",
    "Aljustrel",
    "Paredes",
    "Matosinhos",
]


# Função para gerar datas aleatórias dentro de um intervalo de 10 anos (2014-2024)
def random_date(start_year=2014, end_year=2024):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)


# Função para gerar uma data de fim sempre posterior à data de início
def random_campaign_dates(start_year=2014, end_year=2024):
    start_date = random_date(start_year, end_year)  # Gerar a data de início
    # A data de fim deve ser posterior à data de início, então garantimos isso
    delta_days = random.randint(1, 30)  # Garantir pelo menos 1 dia de diferença
    end_date = start_date + timedelta(days=delta_days)
    return start_date, end_date


# Tabela de Lojas (já criada anteriormente)
lojas = []
for i in range(1, 1001):
    loja = {
        "Loja_ID": i,
        "Nome da Loja": f"Loja {fake.word().capitalize()}",
        "Região (NUTS II)": random.choice(
            ["Norte", "Centro", "Lisboa e Vale do Tejo", "Alentejo", "Algarve"]
        ),
        "Cidade": random.choice(portuguese_cities),
        "Tipo de Loja (Física/Online)": random.choice(["Física", "Online"]),
    }
    lojas.append(loja)

# Tabela de Produtos (já criada anteriormente)
produtos = []
for i in range(1, 1001):
    produto = {
        "Produto_ID": i,
        "Nome do Produto": f"{fake.word().capitalize()} {fake.word().capitalize()}",
        "Categoria": random.choice(
            ["Roupas Masculinas", "Roupas Femininas", "Acessórios", "Calçado"]
        ),
        "Preço": round(random.uniform(20, 100), 2),
        "Custo de Aquisição": round(random.uniform(10, 50), 2),
    }
    produtos.append(produto)

# Tabela de Vendas (1000 registros)
vendas = []
for i in range(1, 1001):
    venda = {
        "Venda_ID": i,
        "Loja_ID": random.randint(1, 1000),
        "Produto_ID": random.randint(1, 1000),
        "Cliente_ID": random.randint(1, 1000),
        "Quantidade": random.randint(1, 20),
        "Preço Unitário": round(random.uniform(20, 100), 2),
        "Data de Início": random_date(),
        "Data de Fim": random_date(),
        "Canal de Venda": random.choice(["Física", "Online"]),
    }
    vendas.append(venda)

# Tabela de Devoluções (1000 registros)
devolucoes = []
for i in range(1, 1001):
    devolucao = {
        "Devolução_ID": i,
        "Venda_ID": random.randint(1, 1000),
        "Produto_ID": random.randint(1, 1000),
        "Cliente_ID": random.randint(1, 1000),
        "Quantidade": random.randint(1, 5),
        "Motivo da Devolução": random.choice(
            ["Tamanho Inadequado", "Defeito no Produto", "Expectativa não atendida", "Outros", "Arrependimento", "Desistência", "Troca",]
        ),
        "Data da Devolução": fake.date_this_year(),
    }
    devolucoes.append(devolucao)

# Tabela de Clientes (1000 registros)
clientes = []
for i in range(1, 1001):
    cliente = {
        "Cliente_ID": i,
        "Nome": fake.name(),
        "Idade": random.randint(18, 70),
        "Gênero": random.choice(["M", "F"]),
        "Cidade": random.choice(portuguese_cities),
        "Canal de Compra": random.choice(["Física", "Online"]),
        "Total de Compras": round(random.uniform(100, 1000), 2),
    }
    clientes.append(cliente)

# Tabela de Campanhas (1000 registros)
campanhas = []
for i in range(1, 1001):
    data_inicio, data_fim = random_campaign_dates()

    campanha = {
        "Campanha_ID": i,
        "Nome da Campanha": f"{fake.word().capitalize()} {fake.word().capitalize()}",
        "Canal": random.choice(
            [
                "Redes Sociais",
                "Email Marketing",
                "Google Ads",
                "Influenciadores",
                "TV",
                "Rádio",
                "Outros",
                "SMS",
                "WhatsApp",
                "Telegram",
                "LinkedIn",
            ]
        ),
        "Investimento": round(random.uniform(200, 1000), 2),
        "Vendas Geradas": random.randint(1000, 10000),
        "Data de Início": data_inicio,
        "Data de Fim": data_fim,
    }
    campanhas.append(campanha)

# Criar DataFrames para as tabelas e salvar em CSV
df_lojas = pd.DataFrame(lojas)
df_produtos = pd.DataFrame(produtos)
df_vendas = pd.DataFrame(vendas)
df_devolucoes = pd.DataFrame(devolucoes)
df_clientes = pd.DataFrame(clientes)
df_campanhas = pd.DataFrame(campanhas)

# Salvar os DataFrames como arquivos CSV
df_lojas.to_csv("Lojas.csv", index=False)
df_produtos.to_csv("Produtos.csv", index=False)
df_vendas.to_csv("Vendas.csv", index=False)
df_devolucoes.to_csv("Devolucoes.csv", index=False)
df_clientes.to_csv("Clientes.csv", index=False)
df_campanhas.to_csv("Campanhas.csv", index=False)

print("Dados gerados e salvos com sucesso!")
