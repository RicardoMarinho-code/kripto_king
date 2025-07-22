import telebot
from datetime import datetime
import time
import threading

API_TOKEN = '8073455529:AAFSQq2mUNxPCqWF_HZ1c2zdkLHo5pysphU'
bot = telebot.TeleBot(API_TOKEN)

usuarios = {}

# Thread para alertas
def alerta_automatico():
    while True:
        hora_atual = datetime.now().strftime('%H:%M')
        for uid, user in usuarios.items():
            if user.get("alerta") == hora_atual:
                nome = user.get("nome", "investidor")
                msg = f"""Olá, {nome}!
⏰ Já são {hora_atual} e aqui estão suas sugestões de hoje com IA:

🟢 **Bitcoin (BTC)** – Forte como sempre, bom para estabilidade  
🟢 **Polygon (MATIC)** – Alta adoção em DeFi, volume saudável  
🟠 **Shiba Inu (SHIB)** – Movimento de alta, mas altíssimo risco  
🟣 **NeuralX (NX)** – Nova moeda ligada à IA. Projeto ainda não auditado.

Deseja ver projeções da IA ou comprar?
"""
                bot.send_message(uid, msg, parse_mode='Markdown')
        time.sleep(60)

threading.Thread(target=alerta_automatico, daemon=True).start()

@bot.message_handler(commands=['start'])
def start(msg):
    uid = msg.chat.id
    usuarios[uid] = {"etapa": "login_email"}
    bot.send_message(uid, "👋 Olá! Bem-vindo ao *Kripto King* — sua corretora inteligente com IA.\n\nPara começarmos, digite seu e-mail de login:", parse_mode='Markdown')

@bot.message_handler(func=lambda m: usuarios.get(m.chat.id, {}).get("etapa") == "login_email")
def pegar_email(msg):
    uid = msg.chat.id
    usuarios[uid]["email"] = msg.text
    usuarios[uid]["etapa"] = "login_senha"
    bot.send_message(uid, "🔐 Agora, digite sua senha:")

@bot.message_handler(func=lambda m: usuarios.get(m.chat.id, {}).get("etapa") == "login_senha")
def pegar_senha(msg):
    uid = msg.chat.id
    usuarios[uid]["senha"] = msg.text
    usuarios[uid]["etapa"] = "nome"
    bot.send_message(uid, "✅ Conta verificada com sucesso!\n\nComo posso chamá-lo?")

@bot.message_handler(func=lambda m: usuarios.get(m.chat.id, {}).get("etapa") == "nome")
def pegar_nome(msg):
    uid = msg.chat.id
    usuarios[uid]["nome"] = msg.text
    usuarios[uid]["etapa"] = "corretora"
    bot.send_message(uid, f"""🚀 Perfeito, {msg.text}! Agora selecione sua corretora:

Binance
Coinbase
Safe
OKX""")

@bot.message_handler(func=lambda m: usuarios.get(m.chat.id, {}).get("etapa") == "corretora")
def pegar_corretora(msg):
    uid = msg.chat.id
    usuarios[uid]["corretora"] = msg.text
    usuarios[uid]["etapa"] = "painel"
    mostrar_painel(uid)

def mostrar_painel(uid):
    nome = usuarios[uid]["nome"]
    bot.send_message(uid, f"Conseguimoos acessar sua conta na corretora {usuarios[uid]['corretora']} com sucesso, {nome}!\n\n")
    bot.send_message(uid, f"""

Você escolheu a corretora: Coinbase!                     
                     
🔒 *Painel do Investidor CriptoSmartIA*
Bem-vindo, {nome}!

Escolha uma opção:
1️⃣ Ver sugestões de hoje  
2️⃣ Consultar carteira   
3️⃣ Configurar alertas por horário  
4️⃣ Perfil de investidor  
5️⃣ Ativar IA SmartTrade (Beta)  
6️⃣ Importar histórico da corretora  
7️⃣ Integrar com API de preço (em breve)  
8️⃣ Comprar criptos

(Digite apenas o número da opção)""", parse_mode='Markdown')

@bot.message_handler(func=lambda m: usuarios.get(m.chat.id, {}).get("etapa") == "painel")
def opcoes_painel(msg):
    uid = msg.chat.id
    escolha = msg.text.strip()

    if escolha == "1":
        nome = usuarios[uid]["nome"]
        msg = f"""🔍 *Sugestões de Hoje com IA* — para você, {nome}

🟢 Ethereum (ETH) – Estável, grande volume  
🟢 Chainlink (LINK) – Forte integração com DeFi  
🟠 Degen Coin – Risco extremo, mas potencial x100  
🔴 TestX (TX) – Sinal de queda, evite por ora

Quer configurar alertas ou comprar?"""
        bot.send_message(uid, msg, parse_mode='Markdown')

    elif escolha == "2":
        bot.send_message(uid, """📊 *Carteira*:

- BTC: 0,053 
- MATIC: 10916,934066609516  
- SHIB: 4042992,8362753433
- Saldo USD: $9166,60
""", parse_mode='Markdown')

    elif escolha == "3":
        usuarios[uid]["etapa"] = "config_alerta"
        bot.send_message(uid, "⏰ Digite o horário para receber sugestões (formato HH:MM):")

    elif escolha == "4":
        bot.send_message(uid, """👤 *Perfil de Investidor*:

- Tipo: Moderado  
- Preferência: Criptos com utilidade real  
- Risco aceito: Médio  
- Última atualização: Hoje
""", parse_mode='Markdown')

    elif escolha == "5":
        bot.send_message(uid, "🤖 *IA SmartTrade* ativada! (emulando inteligência preditiva para compras automáticas fictícias)")

    elif escolha == "6":
        bot.send_message(uid, "🔄 Importação de histórico em andamento...")

    elif escolha == "7":
        bot.send_message(uid, "🔌 Integração com API de preços ainda em desenvolvimento. Aguarde futuras atualizações!")

    elif escolha == "8":
        bot.send_message(uid, "💰 Digite o nome da cripto e valor em USD que deseja comprar:")

    else:
        bot.send_message(uid, "❓ Opção inválida. Digite de 1 a 8.")

@bot.message_handler(func=lambda m: usuarios.get(m.chat.id, {}).get("etapa") == "config_alerta")
def configurar_alerta(msg):
    uid = msg.chat.id
    try:
        hora = datetime.strptime(msg.text, '%H:%M')
        usuarios[uid]["alerta"] = msg.text
        usuarios[uid]["etapa"] = "painel"
        bot.send_message(uid, f"⏰ Alerta configurado com sucesso para {msg.text} todos os dias!")
        mostrar_painel(uid)
    except:
        bot.send_message(uid, "Formato inválido. Tente HH:MM (ex: 09:30).")

# Rodar o bot
bot.polling()