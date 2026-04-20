from src.fake_banco import fake_db

def get_data(item_id):
    print(f"[API] Buscando usuário {item_id}")
    return fake_db.get(item_id)

def update_data(item_id, message):
    print(f"[API] Atualizando usuário {item_id}")
    fake_db[item_id]["mensagem"] = message
