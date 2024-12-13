-- Tabela de Lojas
CREATE TABLE Lojas (
    Loja_ID INT PRIMARY KEY,
    Nome TEXT,
    Regiao TEXT,
    Cidade TEXT,
    Tipo TEXT
);

-- Tabela de Produtos
CREATE TABLE Produtos (
    Produto_ID INT PRIMARY KEY,
    Nome TEXT,
    Categoria TEXT,
    Preco REAL,
    Custo_Aquisicao REAL
);

-- Tabela de Vendas
CREATE TABLE Vendas (
    Venda_ID INT PRIMARY KEY,
    Loja_ID INT,
    Produto_ID INT,
    Cliente_ID INT,
    Colaborador_ID INT,
    Quantidade INT,
    Preco_Unitario REAL,
    Data TEXT,
    Canal TEXT,
    FOREIGN KEY (Loja_ID) REFERENCES Lojas(Loja_ID),
    FOREIGN KEY (Produto_ID) REFERENCES Produtos(Produto_ID),
    FOREIGN KEY (Cliente_ID) REFERENCES Clientes(Cliente_ID),
    FOREIGN KEY (Colaborador_ID) REFERENCES Colaboradores(Colaborador_ID)
);

-- Tabela de Clientes
CREATE TABLE Clientes (
    Cliente_ID INT PRIMARY KEY,
    Nome TEXT,
    Idade INT,
    Genero TEXT,
    Cidade TEXT,
    Canal_Compra TEXT,
    Total_Compras REAL
);

-- Colaborador_ID,Loja_ID,Nome,Função,Horas Trabalhadas Semanais,Avaliação de Desempenho,Vendas Realizadas,Naturalidade

CREATE TABLE Colaboradores (
    Colaborador_ID INT PRIMARY KEY,
    Loja_ID INT,
    Nome TEXT,
    Funcao TEXT,
    Horas_Trabalhadas_Semanais INT,
    Avaliacao_Desempenho REAL,
    Vendas_Realizadas INT,
    Naturalidade TEXT,
    FOREIGN KEY (Loja_ID) REFERENCES Lojas(Loja_ID)
);

-- Tabela de Campanhas
CREATE TABLE Campanhas (
    Campanha_ID INT PRIMARY KEY,
    Nome TEXT,
    Canal TEXT,
    Investimento REAL,
    Vendas_Geradas INT,
    Data_Inicio TEXT,
    Data_Fim TEXT
);

-- Custo_ID,Tipo de Custo,Valor Mensal,Data
CREATE TABLE Custos_Operacionais (
    Custo_ID INT PRIMARY KEY,
    Loja_ID INT,
    Tipo_Custo TEXT,
    Valor_Mensal REAL,
    Data TEXT,
    FOREIGN KEY (Loja_ID) REFERENCES Lojas(Loja_ID)
);

-- Devolução_ID,Venda_ID,Produto_ID,Cliente_ID,Quantidade,Motivo da Devolução,Data da Devolução
CREATE TABLE Devolucoes (
    Devolucao_ID INT PRIMARY KEY,
    Venda_ID INT,
    Produto_ID INT,
    Cliente_ID INT,
    Quantidade INT,
    Motivo_Devolucao TEXT,
    Data_Devolucao TEXT,
    FOREIGN KEY (Venda_ID) REFERENCES Vendas(Venda_ID),
    FOREIGN KEY (Produto_ID) REFERENCES Produtos(Produto_ID)
);

-- Fornecedor_ID,Nome,Histórico de Fornecimento,Custo de Transporte,Prazo Médio de Entrega (dias),Cidade
CREATE TABLE Fornecedores (
    Fornecedor_ID INT PRIMARY KEY,
    Nome TEXT,
    Historico_Fornecimento TEXT,
    Custo_Transporte REAL,
    Prazo_Medio_Entrega INT,
    Cidade TEXT
);

CREATE TABLE Stock (
    Produto_ID INT PRIMARY KEY,
    Quantidade INT,
    Max INT,
    Min INT,
    Tempo_Entrega TEXT,
    FOREIGN KEY (Produto_ID) REFERENCES Produtos(Produto_ID)
);

CREATE TABLE Price_History (
    Produto_ID INT,
    Preco REAL,
    Data_Inicio TEXT,
    Data_Fim TEXT,
    FOREIGN KEY (Produto_ID) REFERENCES Produtos(Produto_ID)
);

CREATE TABLE Cliente_Produto (
    Cliente_Produto_ID INT PRIMARY KEY,
    Cliente_ID INT,
    Produto_ID INT,
    Ultima_Compra TEXT,
    FOREIGN KEY (Cliente_ID) REFERENCES Clientes(Cliente_ID),
    FOREIGN KEY (Produto_ID) REFERENCES Produtos(Produto_ID)
);

CREATE TABLE Product_Reviews (
    Review_ID INT PRIMARY KEY,
    Produto_ID INT,
    Avaliacao REAL,
    Comentario TEXT,
    Data TEXT,
    FOREIGN KEY (Produto_ID) REFERENCES Produtos(Produto_ID)
);

CREATE TABLE Campanha_Produto (
    Campanha_Produto_ID INT PRIMARY KEY,
    Campanha_ID INT,
    Produto_ID INT,
    Quantidade INT,
    FOREIGN KEY (Campanha_ID) REFERENCES Campanhas(Campanha_ID),
    FOREIGN KEY (Produto_ID) REFERENCES Produtos(Produto_ID)
);

CREATE TABLE Orders (
    Order_ID INT PRIMARY KEY,
    Cliente_ID INT,
    Produto_ID INT,
    Quantidade INT,
    Preco_Unitario REAL,
    Data_Inicio TEXT,
    Data_Fim TEXT,
    Status TEXT,
    FOREIGN KEY (Cliente_ID) REFERENCES Clientes(Cliente_ID),
    FOREIGN KEY (Produto_ID) REFERENCES Produtos(Produto_ID)
);

CREATE TABLE Clientes_Campanhas (
    Cliente_Campanha_ID INT PRIMARY KEY,
    Cliente_ID INT,
    Campanha_ID INT,
    Metricas TEXT,
    Vendas_Geradas INT,
    FOREIGN KEY (Cliente_ID) REFERENCES Clientes(Cliente_ID),
    FOREIGN KEY (Campanha_ID) REFERENCES Campanhas(Campanha_ID)
);
