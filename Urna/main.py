import graphics as gf
from graphics import *
import pygame
pygame.init()
from urnaLib import *

win = gf.GraphWin("Urna Eleitoral", 1200, 600)
img = Image(Point(500, 300),
            "public/img/urna-eletronica.gif")
img.draw(win)
votosTotaisEleitor = []
finalTotal = False
senha = "netinho"
while True:
    drawUrna(win)
    votosEleitor = []
    brancoTeste = False
    candidatoPara = 0
    testeNulo = False
    teste = 0
    teste2 = 0
    acabou = False
    votosVotados = []
    votos = []
    cont = 0
    posGov = 1
    try:
        final.undraw()
    except:
        pass
    if finalTotal:
        win.close()
        break
    while True:
        if posGov == 1 and candidatoPara == 0:
            formatacao = gf.Image(gf.Point(294, 315),
                                  "public/img/background.gif")
            numeroTexto = gf.Text(gf.Point(190, 288), "NUMERO:")
            numeroTexto.draw(win)
            partidoTexto = gf.Text(gf.Point(180, 365), "PARTIDO:")
            partidoTexto.draw(win)

            seuVotoPara = gf.Text(gf.Point(360-40, 222), "DEPUTADO FEDERAL")
            seuVotoPara.setSize(17)
            seuVotoPara.draw(win)
            candidatoPara += 1
            candidato = "depFederal"
            numeros = manipularArqNum(candidato)
            numeroVoto(len(numeros[0]), win)
        elif posGov == 2 and candidatoPara == 0:
            gf.Image(gf.Point(294, 281), "public/img/background.gif").draw(win)
            seuVotoPara.undraw()
            seuVotoPara = gf.Text(gf.Point(360-40, 222), "SENADOR")
            seuVotoPara.setSize(17)
            seuVotoPara.draw(win)
            candidatoPara += 1
            try:
                if testeNulo:
                    votoNulo.undraw()
            except:
                pass
            testeNulo = False
            candidato = "senador"
            numeros = manipularArqNum(candidato)
            numeroVoto(len(numeros[0]), win)
        elif posGov == 3 and candidatoPara == 0:
            gf.Image(gf.Point(294, 281), "public/img/background.gif").draw(win)
            seuVotoPara.undraw()
            seuVotoPara = gf.Text(gf.Point(360-40, 222), "PRESIDENTE")
            seuVotoPara.setSize(16)
            seuVotoPara.draw(win)
            candidatoPara += 1
            try:
                if testeNulo:
                    votoNulo.undraw()
            except:
                pass
            testeNulo = False
            candidato = "presidentes"
            numeros = manipularArqNum(candidato)
            numeroVoto(len(numeros[0]), win)
        clique = win.getMouse()
        voto = numeroClick(clique.getX(), clique.getY())
        try:
            if acabou and voto in "1234567890l":
                voto = ""
        except:
            voto = ""
        if brancoTeste and voto not in ["Confirma", "Corrige"]:
            voto = ""
        if type(voto) == type("a"):
            try:
                if int(voto) in range(0, 10):
                    numeroChoose = gf.Text(gf.Point(249+(cont*30), 285),
                                           (numeroClick(clique.getX(), clique.getY())))
                    votosVotados.append(numeroChoose)
                    numeroChoose.setSize(20)
                    numeroChoose.draw(win)
                    votos.append(numeroClick(clique.getX(), clique.getY()))
                    cont += 1
                    if cont == len(numeros[0]):
                        acabou = True
            except:
                if voto == "Corrige":
                    for val in (votosVotados):
                        try:
                            val.undraw()
                            votoNulo.undraw()
                        except:
                            continue
                    try:
                        nome.undraw()
                        partido.undraw()
                        imgCandidato.undraw()
                    except:
                        pass
                    if teste2 > 0:
                        try:
                            partidoTexto.draw(win)
                        except:
                            pass
                    cont = 0
                    votos = []
                    acabou = False
                    teste = 0
                    teste2 = 0
                    brancoTeste = False
                    try:
                        formatacao.undraw()
                        branco.undraw()
                        partidoTexto.draw(win)
                        numeroTexto.draw(win)
                    except:
                        pass
                elif voto == "Confirma" and len(votos) > 0:
                    musicaClick(True)
                    for val in (votosVotados):
                        val.undraw()
                    try:
                        nome.undraw()
                        partido.undraw()
                        imgCandidato.undraw()
                    except:
                        pass
                    if teste2 > 0:
                        try:
                            partidoTexto.draw(win)
                        except:
                            pass
                    votosEleitor.append(votos)
                    cont = 0
                    votos = []
                    posGov += 1
                    testeNulo = True
                    acabou = False
                    teste = 0
                    teste2 = 0
                    candidatoPara = 0
                    brancoTeste = False
                    try:
                        formatacao.undraw()
                        branco.undraw()
                        partidoTexto.draw(win)
                        numeroTexto.draw(win)
                    except:
                        pass
                elif voto == "Branco" and len(votos) < 1:
                    brancoTeste = True
                    formatacao = gf.Image(gf.Point(294, 315),
                                          "public/img/background.gif")
                    formatacao.draw(win)
                    votos.append(voto)
                    partidoTexto.undraw()
                    numeroTexto.undraw()
                    branco = gf.Text(gf.Point(370, 300), "VOTO EM BRANCO")
                    branco.setSize(30)
                    branco.draw(win)
                elif voto == "Fim" and posGov == 1:
                    entrada = gf.Entry(gf.Point(1100, 380), 15)
                    entrada.draw(win)
                    digitePass = gf.Text(
                        gf.Point(1080, 360), "Digite a senha:")
                    digitePass.draw(win)
                    cliqueEmQlq = gf.Text(gf.Point(1100, 415), "ENTER")
                    cliqueEmQlq.draw(win)
                    rectangleEnter = gf.Rectangle(
                        gf.Point(1040, 400), gf.Point(1160, 430))
                    rectangleEnter.draw(win)
                    win.getMouse()
                    textoentrada = entrada.getText()
                    if textoentrada == senha:
                        finalTotal = True
                        entrada.undraw()
                        digitePass.undraw()
                        cliqueEmQlq.undraw()
                        rectangleEnter.undraw()
                        if len(votosEleitor) == 1:
                            votosEleitor.append(["0"])
                            votosEleitor.append(["0"])
                            votosTotaisEleitor.append(votosEleitor)
                        if len(votosEleitor) == 2:
                            votosEleitor.append(["0"])
                            votosTotaisEleitor.append(votosEleitor)
                        break
                    else:
                        finalTotal = False
                        entrada.undraw()
                        cliqueEmQlq.undraw()
                        digitePass.undraw()
                        rectangleEnter.undraw()
        if ("").join(votos) in numeros and teste == 0:
            numCand = ("").join(votos)
            try:
                votoNulo.undraw()
                partidoTexto.draw(win)
            except:
                pass
            nome = manipularArqNome(candidato, ("").join(votos))
            nome = gf.Text(gf.Point(263, 320), nome)
            nome.setSize(16)
            nome.draw(win)

            partido = manipularArqPart(candidato, ("").join(votos))
            partido = gf.Text(gf.Point(250, 365), partido)
            partido.setSize(16)
            partido.draw(win)
            teste += 1
            imgCandidato = Image(Point(
                550, 240), f"public/img/{numCand}.gif")
            imgCandidato.draw(win)
        if ("").join(votos) not in numeros and len(votos) > 0 and teste2 != 1 and brancoTeste == False:
            votoNulo = gf.Text(gf.Point(360, 354), "VOTO NULO")
            votoNulo.setSize(35)
            votoNulo.draw(win)
            teste2 += 1
            partidoTexto.undraw()
        if len(votosEleitor) == 3:
            formatacaoFim1 = gf.Image(gf.Point(300, 405),
                                      "public/img/background.gif")
            formatacaoFim1.draw(win)
            formatacaoFim2 = gf.Image(gf.Point(220, 405),
                                      "public/img/background.gif")
            formatacaoFim2.draw(win)
            formatacaoFim3 = gf.Image(gf.Point(234, 246),
                                      "public/img/background.gif")
            formatacaoFim3.draw(win)
            try:
                votoNulo.undraw()
            except:
                pass
            partidoTexto.undraw()
            numeroTexto.undraw()
            seuVotoPara.undraw()
            formatacao.draw(win)
            drawUrnaFim(win)
            animation = ["■□□□□□□□□□", "■■□□□□□□□□", "■■■□□□□□□□", "■■■■□□□□□□", "■■■■■□□□□□",
                         "■■■■■■□□□□", "■■■■■■■□□□", "■■■■■■■■□□", "■■■■■■■■■□", "■■■■■■■■■■"]
            for i in range(len(animation)):
                anim = gf.Text(gf.Point(370, 320), animation[i])
                anim.setSize(35)
                anim.setFill("green")
                anim.draw(win)
                time.sleep(0.1)
                anim.undraw()
            final = gf.Text(gf.Point(370, 320), "FIM")
            final.setSize(35)
            final.draw(win)
            pygame.mixer.music.load("public/sound/urnaFim.wav")
            pygame.mixer.music.play()
            time.sleep(1)
            votosTotaisEleitor.append(votosEleitor)
            break

numerosDeEleitores = len(votosTotaisEleitor)


arq = open("./src/votos.txt", "r")
lista = arq.read()
arq.close()
lista = lista.split("\n")

listadeVotos = [{"Branco": 0, "Nulo": 0}, {
    "Branco": 0, "Nulo": 0}, {"Branco": 0, "Nulo": 0}]
nulos = 0
brancos = 0
cont = 0
for votos in votosTotaisEleitor:
    valida = validaVoto(votos)
    valida = valida[::-1]
    for val in valida:
        if val == "Nulo":
            listadeVotos[cont]["Nulo"] += 1
        elif val == "Branco":
            listadeVotos[cont]["Branco"] += 1
        else:
            if len(val) == 2:
                if val in listadeVotos[0]:
                    listadeVotos[0][val] += 1
                else:
                    listadeVotos[0][val] = 1
            elif len(val) == 3:
                if val in listadeVotos[1]:
                    listadeVotos[1][val] += 1
                else:
                    listadeVotos[1][val] = 1
            else:
                if val in listadeVotos[2]:
                    listadeVotos[2][val] += 1
                else:
                    listadeVotos[2][val] = 1
        cont += 1
    cont = 0

votosPresidente = listadeVotos[0]
votosSenador = listadeVotos[1]
votosDep = listadeVotos[2]

word1 = 'Presidentes - Numero de Votos - Percentual\n'
word2 = '\nSenadores - Numero de Votos - Percentual\n'
word3 = '\nDeputados Federais - Numero de Votos - Percentual\n'

for val in votosPresidente:
    candidato = "presidentes"
    if numerosDeEleitores == 0:
        word1 += f"{descobrirArqNome(candidato,val)} - {votosPresidente[val]} - 0%"+"\n"
    else:
        word1 += f"{descobrirArqNome(candidato,val)} - {votosPresidente[val]} - {round((votosPresidente[val]*100)/numerosDeEleitores,2)}%"+"\n"
for val in votosSenador:
    candidato = "senador"
    if numerosDeEleitores == 0:
        word2 += f"{descobrirArqNome(candidato,val)} - {votosSenador[val]} - 0%"+"\n"
    else:
        word2 += f"{descobrirArqNome(candidato,val)} - {votosSenador[val]} - {round((votosSenador[val]*100)/numerosDeEleitores,2)}%"+"\n"
for val in votosDep:
    candidato = "depFederal"
    if numerosDeEleitores == 0:
        word3 += f"{descobrirArqNome(candidato,val)} - {votosDep[val]} - 0%"+"\n"
    else:
        word3 += f"{descobrirArqNome(candidato,val)} - {votosDep[val]} - {round((votosDep[val]*100)/numerosDeEleitores,2)}%"+"\n"

gigaString = word1 + word2 + word3
arq = open("./src/votos.txt", "w")
arq.write(gigaString)
arq.close()
