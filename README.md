# 🚀 ETL Pipeline com Python (CSV + API Fake)

Projeto de estudo de Engenharia de Dados que implementa um pipeline ETL completo utilizando Python, simulando integração entre CSV, API e geração de mensagens.

---

## 📌 Sobre o projeto

Este projeto simula um fluxo real de engenharia de dados:

* Leitura de dados via CSV
* Consumo de API (fake)
* Transformação de dados (geração de mensagens)
* Atualização de dados via API
* Exportação do resultado final

---

## 🧠 Arquitetura do Pipeline

```text
CSV → Extract → Transform → Load → API Fake
```

---

## ⚙️ Tecnologias utilizadas

* Python
* Pandas
* Requests (simulado)
* Random (simulação de IA)

---

## 📂 Estrutura do projeto

```bash
.
├── input.csv
├── output.csv
└── main.py
```

---

## 🧪 Como executar o projeto

### 1. Clonar repositório

```bash
git clone https://github.com/seu-usuario/etl-python-estudo.git
cd etl-python-estudo
```

---

### 2. Instalar dependências

```bash
pip install pandas
```

---

### 3. Executar

```bash
python main.py
```

---

## 📄 Exemplo de entrada (`input.csv`)

```csv
id
1
2
3
4
```

---

## 📄 Exemplo de saída (`output.csv`)

```csv
id,nome,mensagem
1,Ana,"Ana, Temos novidades incríveis para você 🎉"
2,Bruno,"Bruno, Aproveite nossas ofertas exclusivas hoje!"
```

---

## 🔄 Fluxo do ETL

1. Lê o CSV com IDs
2. Busca dados na API fake
3. Gera mensagem aleatória
4. Atualiza os dados
5. Salva resultado final em CSV

---

## ⚠️ Tratamento de erros

* IDs não encontrados são ignorados
* Logs exibidos no console
* Lista de IDs inválidos gerada ao final

---

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido com foco em aprendizado prático de:

* Engenharia de Dados
* Integração de sistemas
* Estruturação de pipelines ETL
* Boas práticas em Python

---

## 🚀 Próximos passos

* [ ] Separar em módulos (extract, transform, load)
* [ ] Adicionar logs estruturados
* [ ] Implementar paralelismo
* [ ] Substituir API fake por API real
* [ ] Integrar com IA (OpenAI)

---

## 👨‍💻 Autor

Seu Nome
https://linkedin.com
https://github.com

