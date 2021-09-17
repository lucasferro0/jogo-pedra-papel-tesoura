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
    contabilizado = contabilizar()
    exibir_resultado(contabilizado)
    # LIMPANDO DADOS DE VITÓRIAS
    arquivo = open("users_ganhar.txt", "w")
    arquivo.close()
    # LIMPANDO DADOS DE DERROTAS
    arquivo = open("users_perder.txt", "w")
    arquivo.close()
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
        contabilizado = contabilizar()
        exibir_resultado(contabilizado)
        # LIMPANDO DADOS DE VITÓRIAS
        arquivo = open("users_ganhar.txt", "w")
        arquivo.close()
        # LIMPANDO DADOS DE DERROTAS
        arquivo = open("users_perder.txt", "w")
        arquivo.close()
      else:
        limpar()
def login():
  nome = input("Digite seu nome: ")
  return nome
def recorde_ganhar():
  arquivo = open("users_ganhar.txt", "a")
  arquivo.write(nome+"\n")
  arquivo.close()
def recorde_perder():
  arquivo = open("users_perder.txt", "a")
  arquivo.write(nome+"\n")
  arquivo.close()

def contabilizar():
  # VITÓRIAS
  arquivo = open("users_ganhar.txt", "r")
  v = 0
  for e in arquivo:
    v += 1
  arquivo.close()

  # DERROTAS
  arquivo = open("users_perder.txt", "r")
  d = 0
  for e in arquivo:
    d += 1
  arquivo.close()
  return (v, d)

def exibir_resultado(contabilizado):
  venceu = contabilizado[0]
  perdeu = contabilizado[1]
  final = venceu - perdeu
  final = str(final)
  print(nome+", sua pontuação foi:", final+".")

# INICIAR O JOGO
def start():
    manual = jogador()
    pc = computador()
    if manual == pc:
      limpar()
      print("Empate !\n\nVocê jogou",manual,"\nComputador jogou",pc+".")
      print("\n\nReiniciando o jogo ...")
      time.sleep(5)
      limpar()
      start()  # REINICIAR O JOGO
    # JOGADOR PERDER
    elif manual == "pedra" and pc == "papel":
      limpar()
      print("========================")
      print("Você jogou",manual+".")
      print("Computador jogou",pc+".")
      print("========================")
      print("VOCÊ PERDEU.")
      print("========================")
      recorde_perder()
      continuar()
    elif manual == "papel" and pc == "tesoura":
      limpar()
      print("========================")
      print("Você jogou",manual+".")
      print("Computador jogou",pc+".")
      print("========================")
      print("VOCÊ PERDEU.")
      print("========================")
      recorde_perder()
      continuar()
    elif manual == "tesoura" and pc == "pedra":
      limpar()
      print("========================")
      print("Você jogou",manual+".")
      print("Computador jogou",pc+".")
      print("========================")
      print("VOCÊ PERDEU.")
      print("========================")
      recorde_perder()
      continuar()
    # JOGADOR GANHAR
    elif manual == "papel" and pc == "pedra":
      limpar()
      print("========================")
      print("Você jogou",manual+".")
      print("Computador jogou",pc+".")
      print("========================")
      print("VOCÊ GANHOU !!!.")
      print("========================")
      recorde_ganhar()
      continuar()
    elif manual == "tesoura" and pc == "papel":
      limpar()
      print("========================")
      print("Você jogou",manual+".")
      print("Computador jogou",pc+".")
      print("========================")
      print("VOCÊ GANHOU !!!.")
      print("========================")
      recorde_ganhar()
      continuar()
    elif manual == "pedra" and pc == "tesoura":
      limpar()
      print("========================")
      print("Você jogou",manual+".")
      print("Computador jogou",pc+".")
      print("========================")
      print("VOCÊ GANHOU !!!.")
      print("========================")
      recorde_ganhar()
      continuar()
    else:
      limpar()
      print("Opção inválida. Digite novamente após 5 segundos.")
      time.sleep(5)
      limpar()
      start()  # REINICIAR O JOGO

# INÍCIO DO JOGO
nome = login()
# RESETANDO OS ARQUIVOS
arquivo = open("users_ganhar.txt", "w")
arquivo.close()
arquivo = open("users_perder.txt", "w")
arquivo.close()
limpar()
# JOGO
start()
