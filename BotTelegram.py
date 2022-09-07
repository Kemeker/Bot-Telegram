#importa a biblioteca telebot
import telebot


#variavel que chama a API
CHAVE_API = "5642696200:AAFLDJr8PSSD0Zi2rEvzROCDeSyfrkbvedg"

#Cria uma variavel chamada bot e atribui o token API
bot = telebot.TeleBot(CHAVE_API)


# Comando para para Opçao1
@bot.message_handler(commands=["Opcao1"]) 

#Funçao que vai fazer com que o bot responda caso for escolhido a opçao1, ele apresenta esse link
def opcao1(mensagem): 
    print(mensagem)
    bot.send_message(mensagem.chat.id, "Link das caixas https://docs.google.com/spreadsheets/d/1OluIwMpEBWe5lABNuk7lyzGE9S8kU_vzEVXYQOo8I7c/edit?usp=sharing")


# comando para Opçao2
@bot.message_handler(commands=["Opcao2"])


# ainda nao foi definido uma funçao para essa opçao, mas vai ser ( sair)
def opcao2(mensagem): 
    pass

# 2º funçao
# Essa funçao e executada logo apos a primeira e vai verficar se e true ou false ou seja
# se o usuario cliclou em Opcao1 ou Opcao2
def verificar(mensagem):

    return True    


# vai ler a opçao escolhida pelo usuario se e verdadeira ou falta e passar para a funçao escolhida    
@bot.message_handler(func=verificar)


# 1º funçao
# Assim que o usuario iniciar uma interaçao com o bot essa funçao e acionada e apresenta o texto 
# com as seguintes opçoes ( Opcao1 e Opcao2)
def responder(mensagem):
    texto = """
    Escolha a opçao para continuar:
    /Opcao1 abrir as caixas da rede
    /Opcao2 sair"""
    bot.reply_to(mensagem, texto)    




bot.polling()