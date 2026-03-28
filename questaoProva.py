# Peça ao usuário um time, caso um dos times for Flamengo, printar "Maior Do RJ",
# se for Palmeiras, printar "Sem Mundial", Se for PSG, printar "Time favorito de PP"


time = input("Digite um time: ")

if time == "Flamengo" or time == 'Palmeiras' or time == 'PSG':
    print('Esse time é famoso')
else:
    print("Seu time é desconhecido.")
