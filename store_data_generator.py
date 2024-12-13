import random
import pandas as pd
from faker import Faker
import numpy as np
from datetime import datetime, timedelta
import random
import sqlite3
import os

# Inicializar o gerador de dados fictícios
fake = Faker('pt_PT')

conn = sqlite3.connect('vendas_lojas.db')
cursor = conn.cursor()

if not os.path.exists("vendas_lojas.db"):
    with open("dados.sql") as f:
        cursor.executescript(f.read())

conn.commit()

n_lojas = 5

regions_cities = {
    "Norte": [
        "Porto", "Braga", "Vila Nova de Gaia", "Viana do Castelo", "Bragança", 
        "Guimarães", "Póvoa de Varzim", "Barcelos", "Vila Real", "Maia", "Gondomar", 
        "Vila Nova de Famalicão", "Espinho", "Paredes", "Valongo", "Santo Tirso", "Trofa", 
        "Penafiel", "Fafe", "Lousada", "Paços de Ferreira", "Marco de Canaveses", "Cabeceiras de Basto", 
        "Amarante", "Felgueiras", "Baião", "Vizela", "Vila Verde", "Esposende", "Póvoa de Lanhoso", 
        "Celorico de Basto", "Mondim de Basto", "Montalegre", "Cabeceiras de Basto", "Terras de Bouro", 
        "Vieira do Minho", "Vila Pouca de Aguiar", "Vila do Conde", "Arcos de Valdevez", "Caminha", 
        "Melgaço", "Monção", "Paredes de Coura", "Ponte da Barca", "Ponte de Lima", "Valença", 
        "Vila Nova de Cerveira", "Amares", "Barcelos", "Braga", "Cabeceiras de Basto", 
        "Celorico de Basto", "Esposende", "Fafe", "Guimarães", "Póvoa de Lanhoso",
        "Terras de Bouro", "Vieira do Minho", "Vila Nova de Famalicão", "Vizela", "Vila Verde"
    ],
    "Centro": [
        "Coimbra", "Aveiro", "Leiria", "Viseu", "Castelo Branco", "Caldas da Rainha", 
        "Cantanhede", "Tomar", "Ovar", "Figueira da Foz", "Aveiro", "Guarda", "Covilhã", 
        "Fátima", "Gouveia", "Mangualde", "Mira", "Miranda do Corvo", "Montemor-o-Velho", 
        "Murtosa", "Nelas", "Oliveira de Azeméis", "Oliveira do Bairro", "Oliveira do Hospital", 
        "Ourem", "Penacova", "Penalva do Castelo", "Penamacor", "Penela", "Penedono", "Peniche", 
        "Pombal", "Porto de Mós", "Proença-a-Nova", "Resende", "S. Pedro do Sul", "Sabugal", "Seia", 
        "Sernancelhe", "Sertã", "Sever do Vouga", "Sines", "Tábua", "Tondela", "Trancoso", "Vagos", 
        "Vale de Cambra", "Vila de Rei", "Vila Nova de Paiva", "Vila Nova de Poiares", "Vila Velha de Ródão", 
        "Viseu", "Vouzela", "Águeda", "Albergaria-a-Velha", "Anadia", "Arouca", "Aveiro", "Castelo de Paiva", 
        "Espinho", "Estarreja", "Ílhavo", "Mealhada", "Murtosa", "Oliveira de Azeméis", "Oliveira do Bairro", "Ovar", 
        "Santa Maria da Feira", "São João da Madeira", "Sever do Vouga", "Vagos", "Vale de Cambra", "Alcobaça", "Alvaiázere", 
        "Ansião", "Batalha", "Bombarral", "Caldas da Rainha", "Castanheira de Pêra", "Figueiró dos Vinhos", "Leiria", "Marinha Grande", 
        "Nazaré", "Óbidos", "Pedrógão Grande", "Peniche", "Pombal", "Porto de Mós", "Soure", "Almeida", "Aguiar da Beira", "Albergaria-a-Velha", 
        "Alcanena", "Alcobaça", "Alenquer", "Almeirim", "Alvaiázere", "Anadia", "Ansião", "Arganil", "Arouca", "Aveiro", "Azambuja", "Batalha", 
        "Bombarral", "Cabeceiras de Basto", "Caldas da Rainha", "Cantanhede", "Carregal do Sal", "Castanheira de Pêra", "Castelo Branco", 
        "Castelo de Paiva", "Castro Daire", "Chamusca", "Coimbra", "Condeixa-a-Nova", "Coruche", "Covilhã", "Espinho", "Estarreja", "Fafe", 
        "Figueira da Foz", "Figueiró dos Vinhos", "Fundão", "Góis", "Gouveia", "Guarda", "Idanha-a-Nova", "Ílhavo", "Lamego", "Leiria", "Lousã", 
        "Mangualde", "Mealhada", "Mira", "Miranda do Corvo", "Mirandela", "Mogadouro", "Moimenta da Beira", "Mortágua", "Murtosa", "Nelas", 
        "Oliveira de Azeméis", "Oliveira de Frades", "Oliveira do Bairro", "Oliveira do Hospital", "Ourém", "Ovar", "Pampilhosa da Serra", 
        "Paredes", "Pedrógão Grande", "Penacova", "Penalva do Castelo", "Penamacor", "Penela", "Peniche"
    ],
    "Lisboa e Vale do Tejo": [
        "Lisboa", "Sintra", "Cascais", "Oeiras", "Vila Franca de Xira", 
        "Loures", "Setúbal", "Almada", "Amadora", "Odivelas", "Mafra", 
        "Torres Vedras", "Palmela", "Sesimbra", "Barreiro", "Montijo", 
        "Alcochete", "Azambuja", "Arruda dos Vinhos", "Sobral de Monte Agraço", 
        "Vila Nova de Santo André", "Grândola", "Santiago do Cacém", "Sines",
        "Alcácer do Sal", "Montemor-o-Novo", "Coruche", "Benavente", "Cartaxo",
        "Rio Maior", "Alenquer", "Arruda dos Vinhos", "Azambuja", "Cadaval",
        "Lourinhã", "Sobral de Monte Agraço", "Torres Vedras", "Amadora", "Cascais",
        "Lisboa", "Loures", "Mafra", "Odivelas", "Oeiras", "Sintra", "Vila Franca de Xira",
        "Alenquer", "Arruda dos Vinhos", "Azambuja", "Cadaval", "Lourinhã", "Sobral de Monte Agraço",
        "Torres Vedras", "Alcochete", "Almada", "Barreiro", "Moita", "Montijo", "Palmela", "Seixal",
        "Sesimbra", "Setúbal", "Alcácer do Sal", "Grândola", "Santiago do Cacém", "Sines", "Alcochete",
        "Almada", "Amadora", "Barreiro", "Cascais", "Lisboa", "Loures", "Mafra", "Moita", "Montijo",
        "Odivelas", "Oeiras", "Palmela", "Seixal", "Setúbal", "Sintra", "Vila Franca de Xira", "Alenquer"
    ],
    "Alentejo": [
        "Évora", "Beja", "Portalegre", "Sines", "Aljustrel", "Almodôvar", "Alvito", "Arraiolos", 
        "Barrancos", "Castro Verde", "Cuba", "Estremoz", "Ferreira do Alentejo", "Mértola", "Mora", 
        "Moura", "Odemira", "Oliveira do Hospital", "Ourique", "Ponte de Sor", "Portel", "Redondo", 
        "Reguengos de Monsaraz", "Santiago do Cacém", "Serpa", "Sousel", "Vendas Novas", "Viana do Alentejo", 
        "Vidigueira", "Vila Viçosa"
    ],
    "Algarve": [
        "Faro", "Albufeira", "Tavira", "Loulé", "Lagos", "Portimão", "Vila Real de Santo António",
        "Silves", "Olhão", "Lagoa", "Monchique", "São Brás de Alportel", "Alcoutim", "Castro Marim",
        "Aljezur", "Vila do Bispo"
    ],
    "Regiões Autónomas": [
        "Funchal", "Ponta Delgada", "Angra do Heroísmo",
        "Horta", "Santa Cruz da Graciosa", "Velas", "Lajes das Flores",
        "Vila do Porto", "Santa Cruz das Flores", "Vila Franca do Campo",
        "Angra do Heroísmo", "Horta", "Lajes do Pico", "Machico",
        "Ponta Delgada", "Praia da Vitória", "Ribeira Grande",
        "Santa Cruz da Graciosa", "Santa Cruz das Flores", "Velas",
        "Vila do Porto", "Vila Franca do Campo", "Vila do Corvo",
    ],
}

# Adjetivos ou temas para campanhas
adjetivos = [
    "Inovadora", "Sustentável", "Elegante", "Exclusiva", "Rápida", "Confiável",
    "Fresca", "Moderna", "Simples", "Impactante", "Premium", "Personalizada",
    "Divertida", "Acessível", "Saudável", "Criativa", "Original", "Inteligente",
    "Económica", "Ecológica", "Sazonal", "Atemporal", "Confortável", "Clássica",
    "Descontraída", "Desportiva", "Sensual", "Sofisticada", "Tecnológica", "Única",
    "Versátil", "Vibrante", "Vintage", "Atemporal", "Chique", "Colorida", "Elegante",
    "Estilosa", "Feminina", "Masculina", "Neutra", "Jovem", "Adulto", "Infantil",
]

# Substantivos relacionados a campanhas
substantivos = [
    "Oferta", "Promoção", "Evento", "Desconto", "Campanha", "Festival", 
    "Semana", "Oportunidade", "Sensação", "Estilo", "Verão", "Inverno",
    "Primavera", "Outono", "Coleção", "Lançamento", "Novidade", "Tendência",
    "Moda", "Estação", "Dia", "Noite", "Hora", "Minuto", "Segundo",
    "Preço", "Valor", "Presente", "Surpresa", "Desafio", "Concurso",
    "Sorteio", "Prémio", "Troféu", "Recompensa", "Brinde", "Vantagem",
    "Benefício", "Qualidade", "Conforto", "Estilo", "Design", "Marca",
    "Assinatura", "Assinatura", "Experiência", "Viagem", "Destino",
]

# Temas ou palavras relacionadas
temas = [
    "Digital", "Familiar", "Online", "Global", "Nacional", 
    "Local", "De Luxo", "Inovação", "Ecológica",
    "Sustentável", "Urbana", "Rural", "Desportiva",
    "Fitness", "Gourmet", "Cultural", "Artística",
    "Tecnológica", "Clássica", "Retro", "Vintage",
     "Tradicional", "Contemporânea"
]

def gerar_nome_campanha():
    return f"Campanha {random.choice(adjetivos)} {random.choice(substantivos)} {random.choice(temas)}"

def save_data(table, df):
    df.to_sql(table, conn, if_exists='replace', index=False)
    print(f"Tabela {table} criada com sucesso!")
    # df.to_csv(csv, index=False)

def save_all_to_json(tables):
    for table in tables:
        df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
        df.to_json(f"JSON/{table}.json", orient="records")

# Função para gerar datas aleatórias dentro de um intervalo de 10 anos (2014-2024)
def random_date(start_year=2014, end_year=2024):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_seconds = random.randint(0, 86399)  # Number of seconds in a day
    return start_date + timedelta(days=random_days, seconds=random_seconds)

def gerar_nome_campanha_por_canal(canal):
    prefixos = {
        "Redes Sociais": "Conectada",
        "Email Marketing": "Direta",
        "Google Ads": "Alvo",
        "Influenciadores": "Viral",
        "TV": "Clássica",
    }
    tema = random.choice(["Impacto", "Promoção", "Campanha"])
    return f"{prefixos.get(canal, 'Inovadora')} {tema} {random.choice(temas)}"


# Função para gerar uma data de fim sempre posterior à data de início
def random_campaign_dates(start_year=2014, end_year=2024):
    start_date = random_date(start_year, end_year)  # Gerar a data de início
    # A data de fim deve ser posterior à data de início, então garantimos isso
    delta_days = random.randint(15, 365)  # Garantir pelo menos 1 dia de diferença
    delta_seconds = random.randint(1, 86399)  # Garantir pelo menos 1 segundo de diferença
    end_date = start_date + timedelta(days=delta_days, seconds=delta_seconds)
    return start_date, end_date

# STOCK
stock = []
for i in range(1, 1001):
    item_stock = {
        "Produto_ID": random.randint(1, 1000),
        "Quantidade em stock": random.randint(21, 1000),
        "Nível Mínimo": random.randint(5, 20),
        "Nível Máximo": random.randint(200, 1000),
        "Tempo Médio de Entrega (dias)": random.randint(1, 30),
    }
    stock.append(item_stock)

# df_stock = pd.DataFrame(stock)
# df_stock.to_csv("Stock.csv", index=False)

# FORNECEDORES
fornecedores = []
for i in range(1, 101):
    regiao = random.choice(list(regions_cities.keys()))
    cidade = random.choice(regions_cities[regiao])

    fornecedor = {
        "Fornecedor_ID": i,
        "Nome": fake.company(),
        "Histórico de Fornecimento": random.randint(1, 100),
        "Custo de Transporte": round(random.uniform(50, 500), 2),
        "Prazo Médio de Entrega (dias)": random.randint(1, 15),
        "Cidade": cidade,
    }
    fornecedores.append(fornecedor)

# df_fornecedores = pd.DataFrame(fornecedores)
# df_fornecedores.to_csv("Fornecedores.csv", index=False)

# CUSTOS OPERACIONAIS
custos_operacionais = []
for i in range(1, 101):
    custo = {
        "Custo_ID": i,
        "Loja_ID": random.randint(1, n_lojas),
        "Tipo de Custo": random.choice(["Renda", "Energia", "Salários", "Manutenção"]),
        "Valor Mensal": round(random.uniform(500, 10000), 2),
        "Data": random_date(),
    }
    custos_operacionais.append(custo)

# df_custos = pd.DataFrame(custos_operacionais)
# df_custos.to_csv("Custos_Operacionais.csv", index=False)

# COLABORADORES
colaboradores = []
for i in range(1, 501):
    regiao = random.choice(list(regions_cities.keys()))
    cidade = random.choice(regions_cities[regiao])
    colaborador = {
        "Colaborador_ID": i,
        "Loja_ID": random.randint(1, n_lojas),
        "Nome": fake.name(),
        "Função": random.choice(["Vendedor", "Gerente", "Caixa", "Operário"]),
        "Horas Trabalhadas Semanais": random.randint(20, 40),
        "Avaliação de Desempenho": round(random.uniform(1, 5), 2),
        "Vendas Realizadas": random.randint(10, 200),
        "Naturalidade": cidade,
    }
    colaboradores.append(colaborador)

# df_colaboradores = pd.DataFrame(colaboradores)
# df_colaboradores.to_csv("Colaboradores.csv", index=False)

# SATISFAÇÃO DO CLIENTE
satisfacao = []
for i in range(1, 1001):
    feedback = {
        "Cliente_ID": random.randint(1, 1000),
        "Inquérito_ID": i,
        "Pontuação": random.randint(1, 5),
        "Comentário": fake.sentence(),
        "Data do Inquérito": random_date(),
    }
    satisfacao.append(feedback)

# df_satisfacao = pd.DataFrame(satisfacao)
# df_satisfacao.to_csv("Satisfacao.csv", index=False)

# LOJAS
lojas = []
for i in range(1, 5):
    regiao = random.choice(list(regions_cities.keys()))
    cidade = random.choice(regions_cities[regiao])
    
    loja = {
        "Loja_ID": i,
        "Nome": f"Loja {fake.company()}",
        "Região": regiao,
        "Cidade": cidade,
        "Tipo": random.choice(["Física", "Online"]),
    }
    lojas.append(loja)

# Criar DataFrame para a tabela de lojas
# df_lojas = pd.DataFrame(lojas)
# df_lojas.to_csv("Lojas.csv", index=False)

# PRODUTOS
produtos = []
for i in range(1, 1001):
    produto = {
        "Produto_ID": i,
        "Nome": f"{fake.word().capitalize()} {fake.word().capitalize()}",
        "Categoria": random.choice(
            ["Roupas Masculinas", "Roupas Femininas", "Acessórios", "Calçado"]
        ),
        "Preço": round(random.uniform(20, 100), 2),
        "Custo_Aquisição": round(random.uniform(10, 50), 2),
    }
    produtos.append(produto)

# VENDAS
vendas = []
for i in range(1, 20001):
    venda = {
        "Venda_ID": i,
        "Loja_ID": random.randint(1, n_lojas),
        "Produto_ID": random.randint(1, 1000),
        "Cliente_ID": random.randint(1, 1000),
        "Colaborador_ID": random.randint(1, 500),
        "Quantidade": random.randint(1, 100),
        "Preço Unitário": round(random.uniform(2, 1000), 2),
        "Data da Venda": random_date(),
        "Canal de Venda": random.choice(["Física", "Online"]),
    }
    vendas.append(venda)

# DEVOLUÇÕES
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
        "Data da Devolução": random_date(),
    }
    devolucoes.append(devolucao)

# CLIENTES
clientes = []
for i in range(1, 1001):
    regiao = random.choice(list(regions_cities.keys()))
    cidade = random.choice(regions_cities[regiao])
    cliente = {
        "Cliente_ID": i,
        "Nome": fake.name(),
        "Idade": random.randint(18, 70),
        "Género": random.choice(["M", "F"]),
        "Cidade": cidade,
        "Canal de Compra": random.choice(["Física", "Online"]),
        "Total de Compras": round(random.uniform(100, 1000), 2),
    }
    clientes.append(cliente)

# CAMPANHAS
campanhas = []
df_vendas = pd.DataFrame(vendas)
for i in range(1, 2000):
    data_inicio, data_fim = random_campaign_dates()
    canal = random.choice(["Redes Sociais", "Email Marketing", "Google Ads", "Influenciadores", "TV"])
    store_id = random.randint(1, 1000)
    vendas_geradas = df_vendas[(df_vendas["Data da Venda"] >= data_inicio) & (df_vendas["Data da Venda"] <= data_fim) & (df_vendas["Loja_ID"] == store_id)]["Quantidade"].sum()
    campanha = {
        "Campanha_ID": i,
        "Loja_ID": store_id,
        "Nome": gerar_nome_campanha_por_canal(canal),
        "Canal": canal,
        "Investimento": round(random.uniform(200, 1000), 2),
        "Vendas Geradas": vendas_geradas,
        "Data de Início": data_inicio,
        "Data de Fim": data_fim,
    }
    campanhas.append(campanha)

# HISTÓRICO DE VENDAS
historico_vendas = []
for i in range(1, 10001):
    historico = {
        "Venda_ID": i,
        "Loja_ID": random.randint(1, n_lojas),
        "Produto_ID": random.randint(1, 1000),
        "Cliente_ID": random.randint(1, 1000),
        "Colaborador_ID": random.randint(1, 500),
        "Quantidade": random.randint(1, 100),
        "Preço Unitário": round(random.uniform(2, 1000), 2),
        "Data da Venda": random_date(2014, 2021),
        "Canal de Venda": random.choice(["Física", "Online"]),
    }
    historico_vendas.append(historico)

# Avaliação de Produtos
avaliacoes = []
for i in range(1, 1001):
    avaliacao = {
        "Produto_ID": i,
        "Avaliação": round(random.uniform(1, 5), 2),
        "Comentário": fake.sentence(),
    }
    avaliacoes.append(avaliacao)

# Pedidos de Compra
pedidos_compra = []
for i in range(1, 1001):
    pedido = {
        "Pedido_ID": i,
        "Fornecedor_ID": random.randint(1, 100),
        "Produto_ID": random.randint(1, 1000),
        "Quantidade": random.randint(10, 100),
        "Data do Pedido": random_date(2014, 2021),
    }
    pedidos_compra.append(pedido)   

# Criar DataFrames para as tabelas e salvar em CSV
df_lojas = pd.DataFrame(lojas)
df_produtos = pd.DataFrame(produtos)
df_vendas = pd.DataFrame(vendas)
df_devolucoes = pd.DataFrame(devolucoes)
df_clientes = pd.DataFrame(clientes)
df_campanhas = pd.DataFrame(campanhas)
df_stock = pd.DataFrame(stock)
df_fornecedores = pd.DataFrame(fornecedores)
df_custos = pd.DataFrame(custos_operacionais)
df_colaboradores = pd.DataFrame(colaboradores)
df_satisfacao = pd.DataFrame(satisfacao)
df_hist_vendas = pd.DataFrame(historico_vendas)
df_avaliacoes = pd.DataFrame(avaliacoes)
df_pedidos_compra = pd.DataFrame(pedidos_compra)

# Salvar os DataFrames como arquivos CSV
df_lojas.to_csv("CSV/Lojas.csv", index=False)
df_produtos.to_csv("CSV/Produtos.csv", index=False)
df_vendas.to_csv("CSV/Vendas.csv", index=False)
df_devolucoes.to_csv("CSV/Devolucoes.csv", index=False)
df_clientes.to_csv("CSV/Clientes.csv", index=False)
df_campanhas.to_csv("CSV/Campanhas.csv", index=False)
df_stock.to_csv("CSV/Stock.csv", index=False)
df_fornecedores.to_csv("CSV/Fornecedores.csv", index=False)
df_custos.to_csv("CSV/Custos_Operacionais.csv", index=False)
df_colaboradores.to_csv("CSV/Colaboradores.csv", index=False)
df_satisfacao.to_csv("CSV/Satisfacao.csv", index=False)
df_hist_vendas.to_csv("CSV/Historico_Vendas.csv", index=False)
df_avaliacoes.to_csv("CSV/Avaliacoes.csv", index=False)
df_pedidos_compra.to_csv("CSV/Pedidos_Compra.csv", index=False)

# Salvar os DataFrames como tabelas no banco de dados
save_data("Lojas", df_lojas)
save_data("Produtos", df_produtos)
save_data("Vendas", df_vendas)
save_data("Devolucoes", df_devolucoes)
save_data("Clientes", df_clientes)
save_data("Campanhas", df_campanhas)
save_data("Stock", df_stock)
save_data("Fornecedores", df_fornecedores)
save_data("Custos_Operacionais", df_custos)
save_data("Colaboradores", df_colaboradores)
save_data("Satisfacao", df_satisfacao)
save_data("Historico_Vendas", df_hist_vendas)
save_data("Avaliacoes", df_avaliacoes)
save_data("Pedidos_Compra", df_pedidos_compra)

# Salvar todos os dados em arquivos JSON
save_all_to_json(["Lojas", "Produtos", "Vendas", "Devolucoes", "Clientes", "Campanhas", "Stock", 
                  "Fornecedores", "Custos_Operacionais", "Colaboradores", "Satisfacao", "Historico_Vendas", "Avaliacoes", "Pedidos_Compra"])

print("Dados gerados e salvos com sucesso!")
conn.close()

