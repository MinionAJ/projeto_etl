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
projeto_etl/
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── api_cliente.py
│   ├── ai_fake_mensagem.py
│   ├── fake_banco.py
│   ├── input.csv
│   ├── output.csv
│   └── main.py
│
├── descricao.txt
└── README.md
```

---

## 🧪 Como executar o projeto

### 1. Clonar repositório

```bash
git clone https://github.com/MinionAJ/projeto_etl.git
cd projeto_etl
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
5
6
12
17
22
```

---

## 📄 Exemplo de saída (`output.csv`)

```csv
id,nome,mensagem
1,Ana,"-- Ana, seu futuro merece segurança — comece a investir com quem entende do assunto."
2,Bruno,"-- Bruno, temos uma surpresa esperando por você."
3,Carlos,"-- Carlos, segurança, rentabilidade e praticidade em um só lugar."
4,Daniela,"-- Daniela, olá! Temos novidades incríveis para você."
5,Marcos,"-- Marcos, sentimos sua falta! Volte e confira o que preparamos."
6,Fernanda,"-- Fernanda, invista hoje e conquiste mais liberdade financeira amanhã."
12,Juliana,"-- Juliana, diversifique seus investimentos e aumente suas oportunidades de lucro."
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

CORRÊA, A.J.C.
[https://linkedin.com](https://www.linkedin.com/in/adilsonjosecamposcorrea87/)
[https://github.com](https://github.com/MinionAJ)

