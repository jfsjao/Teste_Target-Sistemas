# 🚀 Desafio Técnico - Desenvolvedor de Sistemas Jr. | Target

Este repositório contém as soluções para o **Desafio Técnico da Target**, resolvidas em **Python**.  
O projeto aborda desafios de **lógica de programação** e **análise de dados** utilizando **JSON, XML e manipulação de strings**.

---

## 📌 Sobre o Projeto
O código principal está no arquivo [`main.py`](./main.py), que contém a implementação das **cinco questões do desafio**, abrangendo **estruturas de repetição, análise de dados e manipulação de strings**.

Cada função no código resolve um dos desafios propostos, garantindo um código **organizado, modular e reutilizável**.

---

## 📌 Tecnologias Utilizadas
- **Python 3.x** 🐍
- **Pandas** (para análise de dados)
- **XML.etree.ElementTree** (para manipulação de arquivos XML)
- **JSON** (para leitura de dados estruturados)
- **Estruturas de controle e repetição (loops, condicionais, funções)**

---

## 📌 Como Executar o Projeto
### 🔹 **1. Clonar o repositório**
```bash
git clone https://github.com/seu-usuario/desafio-target.git
cd desafio-target
```

### 🔹 **2. Instalar as dependências**
Antes de rodar o projeto, instale as dependências listadas no `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 🔹 **3. Executar o programa**
Para rodar o código e visualizar os resultados, execute:

```bash
python main.py
```

---

## 📌 Descrição das Questões
### ✅ **1. Cálculo da variável SOMA**
O programa executa um **loop de soma incremental** de `1` até `13`, acumulando o resultado final.

🔹 **Saída esperada:**
```bash
Resultado da soma: 91
```

---

### ✅ **2. Verificação de número na sequência de Fibonacci**
Dado um número fornecido pelo usuário, o programa verifica se ele pertence à **sequência de Fibonacci**.

🔹 **Exemplo de entrada e saída:**
```bash
Digite um número para verificar na sequência de Fibonacci: 13
O número 13 pertence à sequência de Fibonacci.
```

---

### ✅ **3. Análise de faturamento diário**
O programa lê arquivos `JSON` e `XML` contendo faturamento diário e retorna:

✔ O **menor faturamento diário**  
✔ O **maior faturamento diário**  
✔ A **quantidade de dias com faturamento acima da média**  

🔹 **Exemplo de saída esperada:**
```bash
🔹 Processando dados de faturamento (JSON)...
Menor valor de faturamento: R$ 373.78
Maior valor de faturamento: R$ 48924.24
Número de dias acima da média: 10
```
```bash
🔹 Processando dados de faturamento (XML)...
Menor valor de faturamento: R$ 3071.33
Maior valor de faturamento: R$ 48275.30
Número de dias acima da média: 12
```

---

### ✅ **4. Cálculo do percentual de faturamento por estado**
Com base em dados fornecidos, o programa **calcula o percentual de cada estado no faturamento total**.

🔹 **Saída esperada:**
```bash
Percentual de faturamento por estado:
SP: 37.53%
RJ: 20.30%
MG: 16.18%
ES: 15.03%
Outros: 10.97%
```

---

### ✅ **5. Inversão de string**
O programa **inverte uma string sem usar funções prontas como `.reverse()`**.

🔹 **Exemplo de entrada e saída:**
```bash
Digite uma string para inverter: python
String invertida: nohtyp
```

---

## 📌 Estrutura do Projeto
```
desafio-target/
│── dados.json              # Dados de faturamento diário (JSON)
│── dados.xml               # Dados de faturamento diário (XML)
│── main.py                 # Código principal do desafio
│── README.md               # Documentação do projeto
│── requirements.txt        # Dependências do projeto
```

---

## 📌 Autor
🔹 Desenvolvido por **João Felipe**  
🔹 LinkedIn: [seu-linkedin](https://www.linkedin.com/in/joao-silva-jfs/)  
🔹 GitHub: [seu-github](https://github.com/jfsjao)

---

🚀 **Se gostou do projeto, deixe uma ⭐ no repositório!**  
