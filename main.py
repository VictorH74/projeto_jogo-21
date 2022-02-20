import random
from replit import clear
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
dealer_cards = []

user_balance = 900
dealer_balance = 900

value_on_the_table = 0

op2 = False
acima_de_21 = False
houve_erro = False

def apostar(amount):
  # Quantidade que deseja apostar

  global user_balance
  global dealer_balance
  global value_on_the_table
  global houve_erro

  if (user_balance - amount) >= 0 and (dealer_balance - amount) >= 0:
    user_balance -= amount
    dealer_balance -= amount
    value_on_the_table += (amount * 2)
  else:
    houve_erro = True

def someone_won(balance):
  # Informe o saldo de quem ganhou
  # para acrescentar o valor de mesa na conta
  return balance + value_on_the_table

def hint():
  # Informar um vetor de cartas

  user_cards.append(random.choice(cards))
 


def stand():
  global op2
  op2 = True

def show_deck(player_cards):
  # Retorna uma string com as cartas do jogador informado

  cards_str = ""

  if player_cards == user_cards:
    for card in player_cards:
      cards_str += f"[{card}]"
  else:
    for card in player_cards:
      if player_cards.index(card) == 0 and not op2:
        cards_str += "[?]"
      else:
        cards_str += f"[{card}]"

  return cards_str


options = {1: hint, 2: stand}

def verificar(cards):
  global acima_de_21
  # Verificar o total das cartas do jogador informado

  total = 0
  for value in cards:
    total += value

  if total > 21:
    acima_de_21 = True
  else:
    return total


def balance(balance):
  if balance <= 0:
    return False
  else:
    return True

########################################################

while user_balance > 0 and dealer_balance > 0:

  user_cards = []
  dealer_cards = []
  acima_de_21 = False
  houve_erro = False
  op2 = False
  value_on_the_table = 0

  for i in range(2):
    user_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))

  print("LOGO\n")
  print(f"Seu saldo: {user_balance}")
  print(f"Saldo do comp.: {dealer_balance}")
  apostar(int(input("\nQuanto deseja apostar:\n$")))

  if not houve_erro:
    while not acima_de_21 and not op2:
      clear()
      print("LOGO\n")
      print(f"Valor da aposta em mesa: ${value_on_the_table}\n")
      print(f"Seu Deck: {show_deck(user_cards)}")
      print(f"Deck do computador: {show_deck(dealer_cards)}\n")

      operation = int(input("1.Tirar carta do deck\n2.Jogar cartas na mesa\n"))
      if operation > 0 and operation < 3:
        options_function = options[operation]
        options_function()
        verificar(user_cards)
      else:
        print("\n** Opçao numerica nao reconhecido **")
    #FIM DO SEGUNDO WHILE

    if acima_de_21:
      print("Bust")
      dealer_balance = someone_won(dealer_balance)
    elif op2:
      clear()
      print(f"Seu Deck: {show_deck(user_cards)}")
      print(f"Deck do computador: {show_deck(dealer_cards)}\n")
      if verificar(user_cards) > verificar(dealer_cards):
        print("Voce Ganhou!!")
        user_balance = someone_won(user_balance)
      else:
        print("Computador ganhou")
        dealer_balance = someone_won(dealer_balance)
  
  else:
    print("\n** Erro ao inserir valor da aposta **")

  input("Clique [ENTER] para continuar\n")
  clear()

#FIM DO PRIMEIRO WHILE

if user_balance <= 0:
 print("Computador ganhou")
else:
 print("Voce ganhou!")




