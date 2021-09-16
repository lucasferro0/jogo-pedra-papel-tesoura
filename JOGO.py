import random
import time
import os

tupla = ("pedra", "papel", "tesoura")

# FUNÇÕES
def limpar():
  os.system("clear")

def jogador():
  print("Escolha sua jogada.")
  print("pedra[1]\npapel[2]\ntesoura[3]\n")
  player = input("Sua jogada: ")
  if player == "1":
    escolha_jogador = tupla[0]
  elif player == "2":
    escolha_jogador = tupla[1]
  elif player == "3":
    escolha_jogador = tupla[2]
  else:
    while (player != "1") and (player != "2") and (player != "3"):
      limpar()
      time.sleep(1)
      print("Opção inválida. Digite novamente após 5 segundos.\n")
      time.sleep(5)
      print("Escolha sua jogada.")
      print("pedra[1]\npapel[2]\ntesoura[3]\n")
      player = input("Sua jogada: ")
      if player == "1":
        escolha_jogador = tupla[0]
      elif player == "2":
        escolha_jogador = tupla[1]
      elif player == "3":
        escolha_jogador = tupla[2]
      else:
        limpar()

  return escolha_jogador

def computador():
  escolha_computador = random.choice(tupla)
  return escolha_computador

# OPÇÃO DE CONTINUAR OU NÃO NO JOGO
def continuar():
  continuos = input("\nDeseja continuar jogando [s/n] ? ").lower()
  if continuos == "s":
    limpar()
    start()
  elif continuos == "n":
    limpar()
  else:
    limpar()
    while continuos != "s" and continuos != "n":
      time.sleep(1)
      print("Opção inválida. Digite novamente após 5 segundos.\n")
      time.sleep(5)
      continuos = input("Deseja continuar jogando [s/n] ? ").lower()
      if continuos == "s":
        limpar()
        start()  # REINICIAR O JOGO
      elif continuos == "n":
        limpar()
      else:
        limpar()
# INICIAR O JOGO
def start():
    manual = jogador()
    pc = computador()
    if manual == pc:
      limpar()
      print("Empate !\nVocê jogou",manual,"\nComputador jogou",pc+".")
      print("\n\nReiniciando o jogo ...")
      time.sleep(5)
      limpar()
      start()  # REINICIAR O JOGO
    # JOGADOR PERDER
    elif manual == "pedra" and pc == "papel":
      limpar()
      print("Você jogou",manual+".")
      print("Computador jogou",pc+".")
      print("VOCÊ PERDEU.")
      continuar()
    elif manual == "papel" and pc == "tesoura":
      limpar()
      print("Você jogou",manual+".")
      print("Computador jogou",pc+".")
      print("VOCÊ PERDEU.")
      continuar()
    elif manual == "tesoura" and pc == "pedra":
      limpar()
      print("Você jogou",manual+".")
      print("Computador jogou",pc+".")
      print("VOCÊ PERDEU.")
      continuar()
    # JOGADOR GANHAR
    elif manual == "papel" and pc == "pedra":
      limpar()
      print("Você jogou",manual+".")
      print("Computador jogou",pc+".")
      print("VOCÊ GANHOU !!!.")
      continuar()
    elif manual == "tesoura" and pc == "papel":
      limpar()
      print("Você jogou",manual+".")
      print("Computador jogou",pc+".")
      print("VOCÊ GANHOU !!!.")
      continuar()
    elif manual == "pedra" and pc == "tesoura":
      limpar()
      print("Você jogou",manual+".")
      print("Computador jogou",pc+".")
      print("VOCÊ GANHOU !!!.")
      continuar()
    else:
      limpar()
      print("Opção inválida. Digite novamente após 5 segundos.")
      time.sleep(5)
      limpar()
      start()  # REINICIAR O JOGO

# INÍCIO DO JOGO
start()