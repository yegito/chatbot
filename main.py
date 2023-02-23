import nltk
from nltk.chat.util import Chat, reflections

# Definir perguntas e respostas
pairs = [
    ['oi', ['Olá!', 'Oi!', 'Olá, como posso ajudar?']],
    ['tudo bem?', ['Estou bem, obrigado! E você?', 'Tudo certo, e com você?', 'Estou bem, obrigado por perguntar.']],
    ['qual é o seu nome?', ['Meu nome é ChatBot.']],
    ['o que você faz?', ['Eu sou um chatbot e posso responder perguntas ou ajudá-lo com informações.']],
    ['adeus', ['Tchau!', 'Até logo!', 'Foi bom falar com você!']],
    ['obrigado', ['De nada!', 'Sempre à disposição.', 'Fico feliz em ajudar.']]
]

# Inicia o chatbot
def chatbot():
    print('Olá! Eu sou um chatbot. Como posso ajudá-lo hoje?')
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

# Inicia o chatbot
if __name__ == '__main__':
    chatbot()
