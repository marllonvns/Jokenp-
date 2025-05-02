import random

user_score = 0
boot_score = 0

options = ["r", "t", "p"]
nomes_options = {
    "r": "Pedra",
    "t": "Tesoura",
    "p": "Papel"
}

while True:
    userEscolha = input("Escolha R(Pedra)/T(Tesoura)/P(Papel) ou Q(Sair): ").lower()
    if userEscolha == "q":
        break

    if userEscolha not in options:
        continue

    bootEscolha = random.choice(options)

    print(f"A escolha do computador foi: {bootEscolha}")

    if userEscolha == bootEscolha:
        print("Empate!")
    elif userEscolha == "r" and bootEscolha == "t":
        print("Parabens, Você ganhou!!!")
        user_score = user_score +1

    elif userEscolha == "t" and bootEscolha == "p":
        print("Parabens, Você ganhou!!!")
        user_score = user_score +1

    elif userEscolha == "p" and bootEscolha == "r":
        print("Parabens, Você ganhou!!!")
        user_score = user_score +1

    else:
        print("Perdeu, seja melhor na proxima:)")
        boot_score = boot_score + 1

print(f"Sua pontuação final foi: {user_score}")
print(f"A pontuaçâo do computador foi: {boot_score}")

if user_score > boot_score:
    print("!!PARABENS, VOCÊ GANHOU!!")

elif user_score == boot_score:
    print("Empate:(")

else:
    print("Você é muito ruim, PERDEDOR HAHAHAHAHA")
    