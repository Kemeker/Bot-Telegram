import telebot



CHAVE_API = "5642696200:AAFLDJr8PSSD0Zi2rEvzROCDeSyfrkbvedg"

bot = telebot.TeleBot(CHAVE_API)



@bot.message_handler(commands=["Opcao1"])
def opcao1(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, "Link das caixas https://docs.google.com/spreadsheets/d/1OluIwMpEBWe5lABNuk7lyzGE9S8kU_vzEVXYQOo8I7c/edit?usp=sharing")

@bot.message_handler(commands=["Opcao2"])
def opcao2(mensagem):
    pass

def verificar(mensagem):

    return True    
    
@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha a opçao para continuar:
    /Opcao1 abrir as caixas da rede
    /Opcao2 sair"""
    bot.reply_to(mensagem, texto)    




bot.polling()