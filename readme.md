# Gerador de Dados de Loja para Business Intelligence

Este projeto tem como objetivo gerar dados fictícios para uma loja, permitindo a criação de cenários para análise de Business Intelligence (BI) e desenvolvimento de relatórios. Inclui várias entidades relacionadas ao funcionamento de uma loja, como vendas, produtos, clientes, colaboradores, fornecedores, entre outros.

## Estrutura do Projeto

### 1. Entidades e Dados Gerados
O projeto gera os seguintes dados:

- **Lojas:** Contém informações sobre lojas físicas e online.
- **Produtos:** Catálogo de produtos, com categorias, preços e custos.
- **Clientes:** Perfil dos clientes, incluindo idade, género e histórico de compras.
- **Colaboradores:** Detalhes sobre a equipa de trabalho, como função e desempenho.
- **Fornecedores:** Dados de fornecedores, incluindo custo de transporte e prazos de entrega.
- **Campanhas:** Informações sobre campanhas de marketing e o impacto nas vendas.
- **Vendas:** Registo de transações realizadas, incluindo canal de venda.
- **Devoluções:** Histórico de devoluções com motivo e detalhes do cliente.
- **Custos Operacionais:** Gastos mensais como rendas, energia, e manutenção.
- **Stock:** Gestão de inventário de produtos.
- **Histórico de Preços:** Variações de preços ao longo do tempo.
- **Avaliações de Produtos:** Feedback dos clientes sobre os produtos.

### 2. Base de Dados SQL
O projeto inclui um script SQL que define a estrutura da base de dados com tabelas normalizadas e relações entre elas. As principais tabelas incluem:

- `Lojas`
- `Produtos`
- `Clientes`
- `Vendas`
- `Colaboradores`
- `Campanhas`
- `Devolucoes`
- `Fornecedores`
- `Custos_Operacionais`
- `Stock`
- Outras tabelas auxiliares para suportar funcionalidades avançadas.

### 3. Ferramentas e Tecnologias Utilizadas
- **Python:** Para geração de dados e simulação de cenários.
- **Bibliotecas Python:** 
  - `pandas` para manipulação de dados.
  - `faker` para geração de nomes e descrições fictícias.
  - `random` para criar variações nos dados.
- **SQLite:** Para criar e gerir a base de dados.
- **GitHub:** Para controlo de versão e colaboração.

## Como Usar

### 1. Pré-requisitos
- Python 3.8 ou superior.
- Bibliotecas instaladas: `pandas`, `faker`.

Instala as bibliotecas com:
```bash
pip install pandas faker
