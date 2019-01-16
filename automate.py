import random as rd
import os
import time
import matplotlib.pyplot as plt


def afficherGrille():
    global grille

    for i in range(len(grille)):
        print(grille[i])


def placer(x, y):
    global grille

    grille[y][x] = 1


def checkDirection(direction, y, x):
    global grille
    global h
    global w

    if direction == 3 and grille[y][pacman(x + 1, w)] == 0:
        #print("3")
        return True

    elif direction == 1 and grille[y][pacman(x - 1, w)] == 0:
        #print("1")
        return True

    elif direction == 4 and grille[pacman(y + 1, h)][x] == 0:
        #print("4")
        return True

    elif direction == 2 and grille[pacman(y - 1, h)][x] == 0:
        #print("2")
        return True
    else:
        return False


def cellCounter():
    global grille

    cells = 0

    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if grille[i][j] == 1:
                cells += 1
            else:
                continue
    return cells

def pacman(x, lx) :
    if x > lx - 1:
        return x - lx
    elif x < 0 :
        return x + lx
    else:
        return x

rd.seed(None)

h = 21
w = 21

cellCount = [1]

grille = [[0 for i in range(w)] for i in range(h)]

placer(10, 10)


lsti = list(range(len(grille)))

#rd.shuffle(lsti)

loop = 50

passage = [0, 0, 0, 0]

courbeY = list(range(0, loop + 1))

afficherGrille()

cellLst = []
for u in range(25) :
    for k in range(loop):
        rd.shuffle(lsti)
        for j in lsti:
            lstj = list(range(len(grille[j])))
            rd.shuffle(lstj)
            #print(lsti, "\n", lstj)
            for i in lstj:
                #grille[i][j] += 1
                if grille[i][j] > 0:
                    direction = rd.randint(1, 4)
                    #print("Direction : ", direction)
                    passage[direction - 1] += 1
                    #print(checkDirection(direction, i, j))
                    if checkDirection(direction, i, j):
                        proba = rd.uniform(0.0, 1.0)

                        if proba > 0.3:
                            try:
                                if direction == 3:
                                    grille[i][pacman(j + 1, w)] = 1
                                    grille[i][j] = 0
                                    #print("Pacman : ", pacman(j + 1, w), "  ", j)

                                elif direction == 1:
                                    grille[i][pacman(j - 1, w)] = 1
                                    grille[i][j] = 0
                                    #print("Pacman : ", pacman(j - 1, w), "  ", j)

                                elif direction == 4:
                                    grille[pacman(i + 1, w)][j] = 1
                                    grille[i][j] = 0
                                    #print("Pacman : ", pacman(i + 1, w), "  ", i)

                                elif direction == 2:
                                    grille[pacman(i - 1, w)][j] = 1
                                    grille[i][j] = 0
                                    #print("Pacman : ", pacman(i - 1, w), "  ", i)

                            except :
                                pass

                        if proba <= 0.3:
                            try:
                                if direction == 3:
                                    grille[i][pacman(j + 1, w)] = 1
                                    #passage[2] += 1

                                if direction == 1:
                                    grille[i][pacman(j - 1, w)] = 1
                                    #passage[0] += 1

                                if direction == 4:
                                    grille[pacman(i + 1, h)][j] = 1
                                    #passage[3] += 1

                                if direction == 2:
                                    grille[pacman(i - 1, h)][j] = 1
                                    #passage[1] += 1
                            except IndexError:
                                pass

    cellCount.append(cellCounter())
    cellLst.append(cellCount)
    """
    os.system("clear")
    afficherGrille()
    print("\n")
    time.sleep(0.2)
    """
#os.system("clear")
#afficherGrille()
#print(passage[0], passage[1], passage[2], passage[3])



"""
plt.plot(courbeY, cellCount)
plt.show()
"""
