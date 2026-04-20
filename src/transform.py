from src.ai_fake_mensagem import mensagens
import random

def generate_message(nome):
    mensagem = random.choice(mensagens)
    return f"{nome}, {mensagem}"