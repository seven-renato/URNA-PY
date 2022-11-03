import graphics as gf
from graphics import *
import pygame
pygame.init()


def descobrirArqNome(candidato, num):
    if num in ["Branco", "Nulo"]:
        return num
    arq = open(f"./src/{candidato}.csv", "r", encoding="utf-8")
    lista = arq.read()
    arq.close()
    lista = lista.split("\n")
    candidatos = []
    for val in lista:
        candidatos.append(val.split(";"))
    for val in candidatos:
        if num in val:
            return val[0]


def validaVoto(array):
    arq1 = open("./src/depFederal.csv", "r", encoding="utf-8")
    arq2 = open("./src/senador.csv", "r", encoding="utf-8")
    arq3 = open("./src/presidentes.csv", "r", encoding="utf-8")
    lista1 = arq1.read().split("\n")[1:]
    lista2 = arq2.read().split("\n")[1:]
    lista3 = arq3.read().split("\n")[1:]
    depf = []
    sen = []
    pres = []
    arq1.close()
    arq2.close()
    arq3.close()
    for val in lista1:
        depf.append(val.split(";")[2])
    for val in lista2:
        sen.append(val.split(";")[2])
    for val in lista3:
        pres.append(val.split(";")[2])
    votos = []
    cont = 0
    for val in array:
        if val[0] == "Branco":
            votos.append("Branco")
        elif "".join(val) in depf and len(val) == 4 and cont == 0:
            votos.append("".join(val))
        elif "".join(val) in sen and len(val) == 3 and cont == 1:
            votos.append("".join(val))
        elif "".join(val) in pres and len(val) == 2 and cont == 2:
            votos.append("".join(val))
        else:
            votos.append("Nulo")
        cont += 1
    return votos


def musicaClick(Bool):
    if Bool:
        pygame.mixer.music.load("public/sound/urnaClick.wav")
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.load("public/sound/clickMouse.wav")
        pygame.mixer.music.play()


def numeroVoto(lenght, win):
    cont = 0
    while cont < lenght:
        rectangleVote = gf.Rectangle(
            Point(236+(cont*30), 305), Point(263+(cont*30), 264))
        rectangleVote.draw(win)
        cont += 1


def numeroClick(posX, posY):
    if posY in range(230, 260):
        if posX in range(670, 715):
            musicaClick(False)
            return ("1")
        elif posX in range(734, 780):
            musicaClick(False)
            return ("2")
        elif posX in range(799, 845):
            musicaClick(False)
            return ("3")
    elif posY in range(276, 310):
        if posX in range(672, 719):
            musicaClick(False)
            return ("4")
        elif posX in range(738, 784):
            musicaClick(False)
            return ("5")
        elif posX in range(804, 850):
            musicaClick(False)
            return ("6")
    elif posY in range(324, 358):
        if posX in range(675, 723):
            musicaClick(False)
            return ("7")
        elif posX in range(742, 789):
            musicaClick(False)
            return ("8")
        elif posX in range(808, 855):
            musicaClick(False)
            return ("9")
    elif posY in range(372, 409):
        if posX in range(745, 793):
            musicaClick(False)
            return ("0")
    elif posY in range(424, 464):
        if posX in range(745, 805):
            musicaClick(False)
            return "Corrige"
        elif posX in range(668, 729):
            musicaClick(False)
            return "Branco"
    if posY in range(413, 462):
        if posX in range(819, 880):            
            return "Confirma"
    if posY in range(251, 326):
        if posX in range(1030, 1170):
            return "Fim"


def drawUrna(win):
    seuVotoPara = gf.Text(gf.Point(234, 193), "SEU VOTO PARA: ")
    seuVotoPara.draw(win)
    lineVoto = gf.Line(gf.Point(133, 404), gf.Point(602, 404))
    lineVoto.draw(win)
    lineVoto.setWidth(2)
    glossarioVotoAperta = gf.Text(gf.Point(190, 400+15), "Aperta a tecla:")
    glossarioVotoAperta.setSize(10)
    glossarioVotoConfirma = gf.Text(
        gf.Point(255, 420+15), "CONFIRMA para PROSSEGUIR")
    glossarioVotoConfirma.setSize(10)
    glossarioVotoCorrige = gf.Text(
        gf.Point(265, 440+15), "CORRIGE para REINICIAR este voto")
    glossarioVotoCorrige.setSize(10)
    glossarioVotoAperta.draw(win)
    glossarioVotoConfirma.draw(win)
    glossarioVotoCorrige.draw(win)
    termina = gf.Rectangle(gf.Point(1030, 251), gf.Point(1170, 326))
    termina.setFill("red")
    termina.draw(win)
    terminaText = gf.Text(gf.Point(1100, 290), "TERMINAR VOTAÇÃO")
    terminaText.setFill("white")
    terminaText.setSize(10)
    terminaText.draw(win)


def drawUrnaFim(win):
    lineVoto = gf.Line(gf.Point(133, 404), gf.Point(602, 404))
    lineVoto.draw(win)
    lineVoto.setWidth(2)
    lineVoto.setFill(gf.color_rgb(217, 217, 217))


def manipularArqNum(candidato):
    arq = open(f"./src/{candidato}.csv", "r", encoding="utf-8")
    lista = arq.read()
    arq.close()
    lista = lista.split("\n")
    candidatos = []
    for val in lista:
        candidatos.append(val.split(";"))
    numeros_Possiveis = []
    for val in candidatos:
        try:
            numeros_Possiveis.append(val[2])
        except:
            continue
    return numeros_Possiveis


def manipularArqNome(candidato, num):
    arq = open(f"./src/{candidato}.csv", "r", encoding="utf-8")
    lista = arq.read()
    arq.close()
    lista = lista.split("\n")
    candidatos = []
    for val in lista:
        candidatos.append(val.split(";"))
    for val in candidatos:
        if num in val:
            return val[0]


def manipularArqPart(candidato, num):
    arq = open(f"./src/{candidato}.csv", "r", encoding="utf-8")
    lista = arq.read()
    arq.close()
    lista = lista.split("\n")
    candidatos = []
    for val in lista:
        candidatos.append(val.split(";"))
    for val in candidatos:
        if num in val:
            return val[1]
