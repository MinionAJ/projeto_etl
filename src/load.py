from src.extract import read_csv
from src.api_cliente import get_data
from src.api_cliente import update_data
from src.transform import generate_message
from src.fake_banco import fake_db
import pandas as pd

def run():
    df = read_csv()

    ids_invalidos = []
    resultados = []

    for _, row in df.iterrows():
        item_id = row["id"]

        print(f"\nProcessando ID: {item_id}")

        # 1. Buscar usuário
        data = get_data(item_id)

        if data is None:
            print(f"[ERRO] ID {item_id} não encontrado!")
            ids_invalidos.append(item_id)
            continue

        # 2. Gerar mensagem
        message = generate_message(data["nome"])

        # 3. Atualizar "API"
        update_data(item_id, message)

        # 4. Guardar resultado
        resultados.append({
            "id": item_id,
            "nome": data["nome"],
            "mensagem": message
        })

        print(f"Mensagem gerada: {message}")

    # =========================
    # SALVAR CSV FINAL
    # =========================
    df_saida = pd.DataFrame(resultados)
    df_saida.to_csv("output.csv", index=False)

    print("\nGerando arquivo output.csv\n..\n....\n..\n....")

    print("\nArquivo output.csv gerado com sucesso!")

    # =========================
    # LOG DE ERROS
    # =========================
    if ids_invalidos:
        print("\nIDs não encontrados:")
        print(ids_invalidos)


    print("\n=== RESULTADO FINAL DO BANCO ===")
    for user in fake_db.values():
        print(user)

    print("\n========= NOTA =============")

    print("Acesse o arquivo output.csv para visualizar\nas mensagens geradas na execução do programa.", end="")