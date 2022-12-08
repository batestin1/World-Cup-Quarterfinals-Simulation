#!/usr/local/bin/python3

###################################################################################################
#                                                                                                 #
# SCRIPT FILE: main.py                                                                            #
# CREATION DATE: 07/12/2022                                                                       #
# HOUR: 10:10                                                                                     #
# DISTRIBUTION USED: UBUNTU                                                                       #
# OPERATIONAL SYSTEM: DEBIAN                                                                      #
#                                                                             DEVELOPED BY: BATES #
###################################################################################################
#                                                                                                 #
# SUMMARY: SIMULATION OF WORLD CUP OF SOCCER                                                      #
#                                                                                                 #
###################################################################################################

# variables

from datetime import date, timedelta
import random
import time
import os


def present_a():
    chave_a = ['brasil', random.randint(0,6), 'croacia', random.randint(0,6)]
    chave_b = ['holanda', random.randint(0,6), 'argentina', random.randint(0,6)]
    chave_c= ['inglaterra', random.randint(0,6), 'franca', random.randint(0,6)]
    chave_d = ['marrocos', random.randint(0,6), 'portugal', random.randint(0,6)]
    ast = "-*-"*20
    print(ast)
    time.sleep(1)
    print('SIMULADOR FINAL DA COPA DO MUNDO\n')
    print(ast)
    time.sleep(1)
    print(f"""
SELEÇÕES PARTICIPANTES
{ast}
CHAVE 1:
{chave_a[0].upper()} vs {chave_a[2].upper()}
{ast}
CHAVE 2:
{chave_b[0].upper()} vs {chave_b[2].upper()}
{ast}
CHAVE 3:
{chave_c[0].upper()} vs {chave_c[2].upper()}
{ast}
CHAVE 4:
{chave_d[0].upper()} vs {chave_d[2].upper()}
{ast}
""")
    time.sleep(4)
    


def quart():
    chave_a = ['brasil', random.randint(0,6), 'croacia', random.randint(0,6)]
    chave_b = ['holanda', random.randint(0,6), 'argentina', random.randint(0,6)]
    chave_c= ['inglaterra', random.randint(0,6), 'franca', random.randint(0,6)]
    chave_d = ['marrocos', random.randint(0,6), 'portugal', random.randint(0,6)]
    global semi_a
    global semi_b
    global third
    global final
    semi_a = []
    semi_b = []
    print("JOGO 1\n")
    if chave_a[1] > chave_a[3]:
        print("-PLACAR-\n")
        print(f"{chave_a[0].upper()} ({chave_a[1]}) vs ({chave_a[3]}) {chave_a[2].upper()}\n")
        print(f"Vitoria de {chave_a[0].upper()} \n")
        print(f"---------------------------------------------------------------------------\n")
        semi_a.append(chave_a[0])
    elif chave_a[1] < chave_a[3]:
        print("-PLACAR-\n")
        print(f"{chave_a[0].upper()} ({chave_a[1]}) vs ({chave_a[3]}) {chave_a[2].upper()}\n")
        print(f"Vitoria de {chave_a[2].upper()} \n")
        print(f"---------------------------------------------------------------------------\n")
        semi_a.append(chave_a[2])
    elif chave_a[1] == chave_a[3]:
        print("-PLACAR-\n")
        print(f"{chave_a[0].upper()} ({chave_a[1]}) vs ({chave_a[3]}) {chave_a[2].upper()}\n")
        print(f"EMPATE \n")
        print(f"PENALTIS \n")
        print(f"---------------------------------------------------------------------------\n")
        while chave_a[1] == chave_a[3]:
            chave_a = ['brasil', random.randint(0,6), 'croacia', random.randint(0,6)]
            break
        if chave_a[1] > chave_a[3]:
            print("-PLACAR-\n")
            print(f"{chave_a[0].upper()} ({chave_a[1]}) vs ({chave_a[3]}) {chave_a[2].upper()}\n")
            print(f"Vitoria de {chave_a[0].upper()} \n")
            semi_a.append(chave_a[0])
            print(f"---------------------------------------------------------------------------\n")
        elif chave_a[1] < chave_a[3]:
            print("-PLACAR-\n")
            print(f"{chave_a[0].upper()} ({chave_a[1]}) vs ({chave_a[3]}) {chave_a[2].upper()}\n")
            print(f"Vitoria de {chave_a[2].upper()} \n")
            print(f"---------------------------------------------------------------------------\n")
            semi_a.append(chave_a[2])
    else:
        print("erro")

    print("JOGO 2\n")
    if chave_b[1] > chave_b[3]:
        print("-PLACAR-\n")
        print(f"{chave_b[0].upper()} ({chave_b[1]}) vs ({chave_b[3]}) {chave_b[2].upper()}\n")
        print(f"Vitoria de {chave_b[0].upper()} \n")
        semi_a.append(chave_b[0])
        print(f"---------------------------------------------------------------------------\n")
    elif chave_b[1] < chave_b[3]:
        print("-PLACAR-\n")
        print(f"{chave_b[0].upper()} ({chave_b[1]}) vs ({chave_b[3]}) {chave_b[2].upper()}\n")
        print(f"Vitoria de {chave_b[2].upper()} \n")
        semi_a.append(chave_b[2])
        print(f"---------------------------------------------------------------------------\n")
    elif chave_b[1] == chave_b[3]:
        print("-PLACAR-\n")
        print(f"{chave_b[0].upper()} ({chave_b[1]}) vs ({chave_b[3]}) {chave_b[2].upper()}\n")
        print(f"EMPATE \n")
        print(f"PENALTIS \n")
        print(f"---------------------------------------------------------------------------\n")
        while chave_b[1] == chave_b[3]:
            chave_b = ['holanda', random.randint(0,6), 'argentina', random.randint(0,6)]
            break
        if chave_b[1] > chave_b[3]:
            print("-PLACAR-\n")
            print(f"{chave_b[0].upper()} ({chave_b[1]}) vs ({chave_b[3]}) {chave_b[2].upper()}\n")
            print(f"Vitoria de {chave_b[0].upper()} \n")
            semi_a.append(chave_b[0])
            print(f"---------------------------------------------------------------------------\n")
        elif chave_b[1] < chave_b[3]:
            print("-PLACAR-\n")
            print(f"{chave_b[0].upper()} ({chave_b[1]}) vs ({chave_b[3]}) {chave_b[2].upper()}\n")
            print(f"Vitoria de {chave_b[2].upper()} \n")
            semi_a.append(chave_b[2])
            print(f"---------------------------------------------------------------------------\n")
    else:
        print("erro")

    print("JOGO 3\n")
    if chave_c[1] > chave_c[3]:
        print("-PLACAR-\n")
        print(f"{chave_c[0].upper()} ({chave_c[1]}) vs ({chave_c[3]}) {chave_c[2].upper()}\n")
        print(f"Vitoria de {chave_c[0].upper()} \n")
        semi_b.append(chave_c[0])
        print(f"---------------------------------------------------------------------------\n")
    elif chave_c[1] < chave_c[3]:
        print("-PLACAR-\n")
        print(f"{chave_c[0].upper()} ({chave_c[1]}) vs ({chave_c[3]}) {chave_c[2].upper()}\n")
        print(f"Vitoria de {chave_c[2].upper()} \n")
        semi_b.append(chave_c[2])
        print(f"---------------------------------------------------------------------------\n")
    elif chave_c[1] == chave_c[3]:
        print("-PLACAR-\n")
        print(f"{chave_c[0].upper()} ({chave_c[1]}) vs ({chave_c[3]}) {chave_c[2].upper()}\n")
        print(f"EMPATE \n")
        print(f"PENALTIS \n")
        print(f"---------------------------------------------------------------------------\n")
        while chave_c[1] == chave_c[3]:
            chave_c= ['inglaterra', random.randint(0,6), 'franca', random.randint(0,6)]
            break
        if chave_c[1] > chave_c[3]:
            print("-PLACAR-\n")
            print(f"{chave_c[0].upper()} ({chave_c[1]}) vs ({chave_c[3]}) {chave_c[2].upper()}\n")
            print(f"Vitoria de {chave_c[0].upper()} \n")
            semi_b.append(chave_c[0])
            print(f"---------------------------------------------------------------------------\n")
        elif chave_c[1] < chave_c[3]:
            print("-PLACAR-\n")
            print(f"{chave_c[0].upper()} ({chave_c[1]}) vs ({chave_c[3]}) {chave_c[2].upper()}\n")
            print(f"Vitoria de {chave_c[2].upper()} \n")
            semi_a.append(chave_c[2])
            print(f"---------------------------------------------------------------------------\n")
    else:
        print("erro")

    print("JOGO 4\n")
    if chave_d[1] > chave_d[3]:
        print("-PLACAR-\n")
        print(f"{chave_d[0].upper()} ({chave_d[1]}) vs ({chave_d[3]}) {chave_d[2].upper()}\n")
        print(f"Vitoria de {chave_d[0].upper()} \n")
        semi_b.append(chave_d[0])
        print(f"---------------------------------------------------------------------------\n")
    elif chave_d[1] < chave_d[3]:
        print("-PLACAR-\n")
        print(f"{chave_d[0].upper()} ({chave_d[1]}) vs ({chave_d[3]}) {chave_d[2].upper()}\n")
        print(f"Vitoria de {chave_c[2].upper()} \n")
        semi_b.append(chave_d[2])
        print(f"---------------------------------------------------------------------------\n")
    elif chave_d[1] == chave_d[3]:
        print("-PLACAR-\n")
        print(f"{chave_d[0].upper()} ({chave_d[1]}) vs ({chave_d[3]}) {chave_d[2].upper()}\n")
        print(f"EMPATE \n")
        print(f"PENALTIS \n")
        print(f"---------------------------------------------------------------------------\n")
        while chave_d[1] == chave_d[3]:
            chave_d = ['marrocos', random.randint(0,6), 'portugal', random.randint(0,6)]
            break
        if chave_d[1] > chave_d[3]:
            print("-PLACAR-\n")
            print(f"{chave_d[0].upper()} ({chave_d[1]}) vs ({chave_d[3]}) {chave_d[2].upper()}\n")
            print(f"Vitoria de {chave_d[0].upper()} \n")
            semi_b.append(chave_d[0])
            print(f"---------------------------------------------------------------------------\n")
        elif chave_d[1] < chave_d[3]:
            print("-PLACAR-\n")
            print(f"{chave_d[0].upper()} ({chave_d[1]}) vs ({chave_d[3]}) {chave_d[2].upper()}\n")
            print(f"Vitoria de {chave_d[2].upper()} \n")
            semi_b.append(chave_d[2])
            print(f"---------------------------------------------------------------------------\n")
    else:
        print('erro')
    time.sleep(4)
    


def present_b():
    global semi_a
    global semi_b
    global third
    global final

    ast = "-*-"*20

    print(f"""
    SEMIFINALISTAS
    CHAVE 1:
    {semi_a[0].upper()} vs {semi_a[1].upper()}

    CHAVE 2:
    {semi_b[0].upper()} vs {semi_b[1].upper()}
    """)
    time.sleep(1)
    time.sleep(4)
    


def semi():
    global semi_a
    global semi_b
    global third
    global final_
    goals_a = random.randint(0,6)
    goals_b = random.randint(0,6)
    semi_a.insert(1,goals_a)
    semi_a.insert(3,goals_b)
    goals_c = random.randint(0,6)
    goals_d = random.randint(0,6)
    semi_b.insert(1,goals_c)
    semi_b.insert(3,goals_d)

    final_ = []
    third = []

    if semi_a[1] > semi_a[3]:
        print("-PLACAR-\n")
        print(f"{semi_a[0].upper()} ({semi_a[1]}) vs ({semi_a[3]}) {semi_a[2].upper()}\n")
        print(f"Vitoria de {semi_a[0].upper()} \n")
        print(f"---------------------------------------------------------------------------\n")
        final_.append(semi_a[0])
        third.append(semi_a[2])
    elif semi_a[1] < semi_a[3]:
        print("-PLACAR-\n")
        print(f"{semi_a[0].upper()} ({semi_a[1]}) vs ({semi_a[3]}) {semi_a[2].upper()}\n")
        print(f"Vitoria de {semi_a[2].upper()} \n")
        print(f"---------------------------------------------------------------------------\n")
        final_.append(semi_a[2])
        third.append(semi_a[0])
    elif semi_a[1] == semi_a[3]:
        print("-PLACAR-\n")
        print(f"{semi_a[0].upper()} ({semi_a[1]}) vs ({semi_a[3]}) {semi_a[2].upper()}\n")
        print(f"EMPATE \n")
        print(f"PENALTIS \n")
        print(f"---------------------------------------------------------------------------\n")
        while semi_a[1] == semi_a[3]:
            goals_c = random.randint(0,6)
            goals_d = random.randint(0,6)
            semi_b.insert(1,goals_c)
            semi_b.insert(3,goals_d)
            goals_a = random.randint(0,6)
            goals_b = random.randint(0,6)
            semi_a.insert(1,goals_a)
            semi_a.insert(3,goals_b)
            break
        if semi_a[1] > semi_a[3]:
            print("-PLACAR-\n")
            print(f"{semi_a[0].upper()} ({semi_a[1]}) vs ({semi_a[3]}) {semi_a[2].upper()}\n")
            print(f"Vitoria de {semi_a[0].upper()} \n")
            print(f"---------------------------------------------------------------------------\n")
            final_.append(semi_a[0])
            third.append(semi_a[2])
        elif semi_a[1] < semi_a[3]:
            print("-PLACAR-\n")
            print(f"{semi_a[0].upper()} ({semi_a[1]}) vs ({semi_a[3]}) {semi_a[2].upper()}\n")
            print(f"Vitoria de {semi_a[2].upper()} \n")
            print(f"---------------------------------------------------------------------------\n")
            final_.append(semi_a[2])
            third.append(semi_a[0])
    else:
        print("erro")

    if semi_b[1] > semi_b[3]:
        print("-PLACAR-\n")
        print(f"{semi_b[0].upper()} ({semi_b[1]}) vs ({semi_b[3]}) {semi_b[2].upper()}\n")
        print(f"Vitoria de {semi_b[0].upper()} \n")
        print(f"---------------------------------------------------------------------------\n")
        final_.append(semi_b[0])
        third.append(semi_b[2])
    elif semi_b[1] < semi_b[3]:
        print("-PLACAR-\n")
        print(f"{semi_b[0].upper()} ({semi_b[1]}) vs ({semi_b[3]}) {semi_b[2].upper()}\n")
        print(f"Vitoria de {semi_b[2].upper()} \n")
        print(f"---------------------------------------------------------------------------\n")
        final_.append(semi_b[2])
        third.append(semi_b[0])
    elif semi_b[1] == semi_b[3]:
        print("-PLACAR-\n")
        print(f"{semi_b[0].upper()} ({semi_b[1]}) vs ({semi_b[3]}) {semi_b[2].upper()}\n")
        print(f"EMPATE \n")
        print(f"PENALTIS \n")
        print(f"---------------------------------------------------------------------------\n")
        while semi_b[1] == semi_b[3]:
            goals_c = random.randint(0,6)
            goals_d = random.randint(0,6)
            semi_b.insert(1,goals_c)
            semi_b.insert(3,goals_d)
            goals_a = random.randint(0,6)
            goals_b = random.randint(0,6)
            semi_a.insert(1,goals_a)
            semi_a.insert(3,goals_b)
            break
        if semi_b[1] > semi_b[3]:
            print("-PLACAR-\n")
            print(f"{semi_b[0].upper()} ({semi_b[1]}) vs ({semi_b[3]}) {semi_b[2].upper()}\n")
            print(f"Vitoria de {semi_b[0].upper()} \n")
            final_.append(semi_b[0])
            third.append(semi_b[2])
            print(f"---------------------------------------------------------------------------\n")
        elif semi_b[1] < semi_b[3]:
            print("-PLACAR-\n")
            print(f"{semi_b[0].upper()} ({semi_b[1]}) vs ({semi_b[3]}) {semi_b[2].upper()}\n")
            print(f"Vitoria de {semi_b[2].upper()} \n")
            print(f"---------------------------------------------------------------------------\n")
            final_.append(semi_b[2])
            third.append(semi_b[0])
    else:
        print("erro")

    time.sleep(4)
    

def present_c():
    global semi_a
    global semi_b
    global third
    global final_

    ast = "-*-"*20

    print(f"""
    FINALISTAS
    {final_[0].upper()} vs {final_[1].upper()}

    DECISÃO DE TERCEIRO LUGAR:
    {third[0].upper()} vs {third[1].upper()}
    """)

def final():
        
    global semi_a
    global semi_b
    global third
    global final_
    goals_a = random.randint(0,6)
    goals_b = random.randint(0,6)
    final_.insert(1,goals_a)
    final_.insert(3,goals_b)
    goals_c = random.randint(0,6)
    goals_d = random.randint(0,6)
    third.insert(1,goals_c)
    third.insert(3,goals_d)

    if final_[1] > final_[3]:
        print("-PLACAR-\n")
        print(f"{final_[0].upper()} ({final_[1]}) vs ({final_[3]}) {final_[2].upper()}\n")
        print(f"---------------------------------------------------------------------------\n")
        print(f"O CAMPEÃO É {final_[0].upper()} \n")
        print(f"O VICE CAMPEÃO É {final_[2].upper()} \n")
        print(f"---------------------------------------------------------------------------\n")
    elif final_[1] < final_[3]:
        print("-PLACAR-\n")
        print(f"{final_[0].upper()} ({final_[1]}) vs ({final_[3]}) {final_[2].upper()}\n")
        print(f"---------------------------------------------------------------------------\n")
        print(f"O CAMPEÃO É {final_[2].upper()} \n")
        print(f"O VICE CAMPEÃO É {final_[0].upper()} \n")
        print(f"---------------------------------------------------------------------------\n")
    elif final_[1] == final_[3]:
        print("-PLACAR-\n")
        print(f"{final_[0].upper()} ({final_[1]}) vs ({final_[3]}) {final_[2].upper()}\n")
        print(f"EMPATE \n")
        print(f"PENALTIS \n")
        print(f"---------------------------------------------------------------------------\n")
        while final_[1] == final_[3]:
            goals_a = random.randint(0,6)
            goals_b = random.randint(0,6)
            final_.insert(1,goals_a)
            final_.insert(3,goals_b)
            goals_c = random.randint(0,6)
            goals_d = random.randint(0,6)
            third.insert(1,goals_c)
            third.insert(3,goals_d)
            break
        if final_[1] > final_[3]:
            print("-PLACAR-\n")
            print(f"{final_[0].upper()} ({final_[1]}) vs ({final_[3]}) {final_[2].upper()}\n")
            print(f"O CAMPEÃO É {final_[0].upper()} \n")
            print(f"O VICE CAMPEÃO É {final_[2].upper()} \n")
            print(f"---------------------------------------------------------------------------\n")
        elif final_[1] < final_[3]:
            print("-PLACAR-\n")
            print(f"{final_[0].upper()} ({final_[1]}) vs ({final_[3]}) {final_[2].upper()}\n")
            print(f"O CAMPEÃO É {final_[2].upper()} \n")
            print(f"O VICE CAMPEÃO É {final_[0].upper()} \n")
            print(f"---------------------------------------------------------------------------\n")
    else:
        print("erro")

    if third[1] > third[3]:
        print("-PLACAR-\n")
        print(f"{third[0].upper()} ({third[1]}) vs ({third[3]}) {third[2].upper()}\n")
        print(f"---------------------------------------------------------------------------\n")
        print(f"O TERCEIRO LUGAR É {third[0].upper()} \n")
        print(f"O QUARTO LUGAR É {third[2].upper()} \n")
        print(f"---------------------------------------------------------------------------\n")
    elif third[1] < third[3]:
        print("-PLACAR-\n")
        print(f"{third[0].upper()} ({third[1]}) vs ({third[3]}) {third[2].upper()}\n")
        print(f"---------------------------------------------------------------------------\n")
        print(f"O TERCEIRO LUGAR É {third[2].upper()} \n")
        print(f"O QUARTO LUGAR É {third[0].upper()} \n")
        print(f"---------------------------------------------------------------------------\n")
    elif third[1] == third[3]:
        print("-PLACAR-\n")
        print(f"{third[0].upper()} ({third[1]}) vs ({third[3]}) {third[2].upper()}\n")
        print(f"EMPATE \n")
        print(f"PENALTIS \n")
        print(f"---------------------------------------------------------------------------\n")
        while third[1] == third[3]:
            goals_a = random.randint(0,6)
            goals_b = random.randint(0,6)
            final.insert(1,goals_a)
            final.insert(3,goals_b)
            goals_c = random.randint(0,6)
            goals_d = random.randint(0,6)
            third.insert(1,goals_c)
            third.insert(3,goals_d)
            break
        if third[1] > third[3]:
            print("-PLACAR-\n")
            print(f"{third[0].upper()} ({third[1]}) vs ({third[3]}) {third[2].upper()}\n")
            print(f"---------------------------------------------------------------------------\n")
            print(f"O TERCEIRO LUGAR É {third[0].upper()} \n")
            print(f"O QUARTO LUGAR É {third[2].upper()} \n")
            print(f"---------------------------------------------------------------------------\n")
        elif third[1] < third[3]:
            print("-PLACAR-\n")
            print(f"{third[0].upper()} ({third[1]}) vs ({third[3]}) {third[2].upper()}\n")
            print(f"---------------------------------------------------------------------------\n")
            print(f"O TERCEIRO LUGAR É {third[2].upper()} \n")
            print(f"O QUARTO LUGAR É {third[0].upper()} \n")
            print(f"---------------------------------------------------------------------------\n")
    else:
        print("erro")

if __name__== '__main__':
    present_a()
    quart()
    present_b()
    semi()
    present_c()
    final()

