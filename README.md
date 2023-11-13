# Calculadora de Ganho de Capital

Este projeto implementa uma calculadora de ganho de capital para operações de compra e venda de ações. 
O objetivo é calcular o imposto devido sobre o lucro das operações de venda, seguindo as regras fiscais aplicáveis.

## Descrição do Desafio

O desafio consiste em criar uma calculadora que possa processar uma sequência de operações de compra e venda de ações e calcular o imposto devido com base no lucro obtido. 
As operações devem ser processadas em ordem e o cálculo do imposto deve considerar o preço médio ponderado das ações e a compensação de prejuízos acumulados.

## Regras do Ganho de Capital

1. **Cálculo de Imposto**: O imposto é 20% sobre o lucro obtido na operação de venda cujo preço de venda é superior ao preço médio ponderado de compra.
2. **Lucro ou Prejuízo**: O lucro ocorre quando o preço de venda é maior do que o preço médio ponderado. Se for menor, resulta em prejuízo.
3. **Preço Médio Ponderado**: É recalculado a cada operação de compra.
4. **Compensação de Prejuízos**: Prejuízos podem ser usados para reduzir o lucro tributável de vendas futuras até que sejam totalmente compensados.
5. **Isenção de Imposto**: Não há imposto a pagar se o valor total da operação de venda for menor ou igual a R$ 20.000,00.
6. **Operações de Compra**: Não geram imposto.
7. **Quantidade de Ações**: Não é permitido vender mais ações do que o disponível em carteira.

## Implementação

A implementação consiste nas seguintes etapas:

### Passo 1: Estrutura da Classe

Definição da classe `CapitalGainCalculator` com propriedades para armazenar o custo acumulado, a quantidade total de ações e os prejuízos acumulados.

### Passo 2: Método de Atualização do Preço Médio

Implementação do método `update_average_price` que recalcula o preço médio ponderado a cada compra de ações.

### Passo 3: Cálculo de Lucro ou Prejuízo

Desenvolvimento da lógica para calcular o lucro ou prejuízo a cada venda, comparando o preço de venda com o preço médio ponderado.

### Passo 4: Aplicação das Regras Fiscais

Aplicação da taxa de imposto sobre o lucro e utilização de prejuízos acumulados para ajustar o lucro tributável.

### Passo 5: Tratamento da Isenção

Verificação do valor total da operação para aplicar a regra de isenção de imposto.

### Passo 6: Cálculo do Imposto Devido

Cálculo do imposto devido após a aplicação de todas as regras fiscais e compensação de prejuízos.

### Passo 7: Reset do Estado

Reinicialização do estado da calculadora quando todas as ações são vendidas.

### Passo 8: Testes Unitários

Testes unitários criados para validar a lógica de cálculo do imposto e garantir que a calculadora esteja funcionando conforme o esperado.

## Execução dos Testes

Instruções sobre como executar os testes unitários e verificar se a implementação está correta.

## Exemplos de Casos de Teste

### Caso #1
Operações de compra e venda onde as vendas não resultam em imposto devido ao valor total ser menor que R$ 20.000,00.

- Entrada:
  ```json
  [{"operation": "buy", "unit-cost": 10.00, "quantity": 100},
  {"operation": "sell", "unit-cost": 15.00, "quantity": 50},
  {"operation": "sell", "unit-cost": 15.00, "quantity": 50}]

- Saida:
  ```json
  [{"tax": 0},{"tax": 0},{"tax": 0}]

### Caso #2
Neste caso, há uma compra e duas vendas, com a primeira venda resultando em lucro e a segunda em prejuízo.

- Entrada:
  ```json
  [{"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
  {"operation": "sell", "unit-cost": 20.00, "quantity": 5000},
  {"operation": "sell", "unit-cost": 5.00, "quantity": 5000}]

- Saida:
  ```json
  [{"tax": 0.00}, {"tax": 10000.00}, {"tax": 0.00}]
  
### Caso #1 + Caso #2
Neste caso, há uma compra e duas vendas, com a primeira venda resultando em lucro e a segunda em prejuízo.

- Entrada:
  ```json
  [{"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
  {"operation": "sell", "unit-cost": 20.00, "quantity": 5000},
  {"operation": "sell", "unit-cost": 5.00, "quantity": 5000}]

- Saida:
  ```json
  [{"tax": 0.00}, {"tax": 10000.00}, {"tax": 0.00}]
  
### Caso #3
Este caso apresenta uma compra seguida por duas vendas, uma resultando em prejuízo e outra em lucro que precisa considerar o prejuízo anterior para o cálculo do imposto.

- Entrada:
  ```json
  [{"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
  {"operation": "sell", "unit-cost": 5.00, "quantity": 5000},
  {"operation": "sell", "unit-cost": 20.00, "quantity": 3000}]

- Saida:
  ```json
  [{"tax": 0.00}, {"tax": 10000.00}, {"tax": 0.00}]

### Caso #4
Compra de ações seguida por uma venda sem lucro ou prejuízo e outra venda com lucro.

- Entrada:
  ```json
  [{"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
  {"operation": "buy", "unit-cost": 25.00, "quantity": 5000},
  {"operation": "sell", "unit-cost": 15.00, "quantity": 10000},
  {"operation": "sell", "unit-cost": 25.00, "quantity": 5000}]

- Saida:
  ```json
  [{"tax": 0.00}, {"tax": 0.00}, {"tax": 0.00}, {"tax": 10000.00}]
  
### Caso #5
Operações de compra e venda onde a venda final é lucrativa, exigindo o pagamento do imposto.

- Entrada:
  ```json
  [{"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
  {"operation": "buy", "unit-cost": 25.00, "quantity": 5000},
  {"operation": "sell", "unit-cost": 15.00, "quantity": 10000},
  {"operation": "sell", "unit-cost": 25.00, "quantity": 5000}]

- Saida:
  ```json
  [{"tax": 0.00}, {"tax": 0.00}, {"tax": 0.00}, {"tax": 10000.00}]
  
### Caso #6
Compra de ações seguida por vendas com prejuízo e lucro, com imposto devido na venda final.

- Entrada:
  ```json
  [{"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
  {"operation": "sell", "unit-cost": 2.00, "quantity": 5000},
  {"operation": "sell", "unit-cost": 20.00, "quantity": 2000},
  {"operation": "sell", "unit-cost": 20.00, "quantity": 2000},
  {"operation": "sell", "unit-cost": 25.00, "quantity": 1000}]

- Saida:
  ```json
  [{"tax": 0.00}, {"tax": 0.00}, {"tax": 0.00}, {"tax": 0.00}, {"tax": 3000.00}]

### Caso #7
Várias operações de compra e venda, com impostos calculados com base no lucro líquido após compensar prejuízos anteriores.

- Entrada:
  ```json
  [{"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
  {"operation": "sell", "unit-cost": 2.00, "quantity": 5000},
  {"operation": "sell", "unit-cost": 20.00, "quantity": 2000},
  {"operation": "sell", "unit-cost": 20.00, "quantity": 2000},
  {"operation": "sell", "unit-cost": 25.00, "quantity": 1000},
  {"operation": "buy", "unit-cost": 20.00, "quantity": 10000},
  {"operation": "sell", "unit-cost": 15.00, "quantity": 5000},
  {"operation": "sell", "unit-cost": 30.00, "quantity": 4350}]

- Saida:
  ```json
  [{"tax": 0.00}, {"tax": 10000.00}, {"tax": 0.00}]

### Caso #8
Este caso apresenta uma compra seguida por duas vendas, uma resultando em prejuízo e outra em lucro que precisa considerar o prejuízo anterior para o cálculo do imposto.

- Entrada:
  ```json
  [{"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
  {"operation": "sell", "unit-cost": 5.00, "quantity": 5000},
  {"operation": "sell", "unit-cost": 20.00, "quantity": 3000}]
  
- Saida:
  ```json
  [{"tax": 0.00}, {"tax": 10000.00}, {"tax": 0.00}]
  
### Caso #8
Este caso ilustra uma série de compras e vendas que resultam em lucros substanciais, exigindo cálculos de impostos significativos.
As operações de venda neste caso resultam em um lucro elevado, com o imposto sendo uma porcentagem significativa do retorno. 
É crucial que a calculadora de ganho de capital aplique as regras corretamente para garantir a precisão do imposto devido.

- Entrada:
  ```json
  [{"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
  {"operation": "sell", "unit-cost": 50.00, "quantity": 10000},
  {"operation": "buy", "unit-cost": 20.00, "quantity": 10000},
  {"operation": "sell", "unit-cost": 50.00, "quantity": 10000}]

- Saida:
  ```json
  [{"tax": 0.00}, {"tax": 80000.00}, {"tax": 0.00}, {"tax": 60000.00}]

## Conclusão
Este projeto é uma representação da minha dedicação em construir o desafio para uma Calculadora de Ganho de Capital.