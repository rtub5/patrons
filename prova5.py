# Made by Roger Bajona and Gerard Garcia, all rights reserved

def pedrapapertisores(q): #entrar en numeros
    import random,time
    mans = ["R","S","P"] 
    ma_ordinador = ()
    ma_persona =()
    puntuacio = 0
    puntuacio_jugador = 0
    victoria = 0
    print("Pedra paper tisores \n\n Per tisores escriu S, per pedra escriu R i per paper polsa P")

    # patrons

    llista_resultats = []

    llargada_llista = (0)

    llargada_patro = (3)

    m = 0

    n = 0

    posicio = ()

    patroutil = []

    espera = 0

    def preparar_llista():

        global llargada_llista,llista_resultats,ma_persona

        if ma_persona == "R":

            llargada_llista += 1
            llista_resultats.append(1)

        if ma_persona == "P":

            llargada_llista += 1
            llista_resultats.append(2)

        if ma_persona == "S":

            llargada_llista += 1
            llista_resultats.append(3)




    def suma(f,d): # f es la llargada del patro, es resta al numero llargada_patro
        global llista_resultats,llargada_patro
        # defineix la posició que es suma, te de començar per la inicial i acabar sent la ultima (recorrent un tram igual a la llargada del patro -f)
        guardat = 0
        lloc = d
        for n in range(1,int(llargada_patro-f)):
            sumat = int(llista_resultats[-lloc])
            guardat += sumat
            lloc += 1
        
        return guardat



    def nombres_patro(u,p): # per definir llargada patró i la posició
        global llargada_patro, llista_resultats
        lloc = p

        llista = []

        for n in range(1,int(llargada_patro-u)):
            llista.append(llista_resultats[-lloc])
            lloc += 1

        return llista


    def comprobacio(l, p, d):
        global llargada_patro, llista_resultats

        llocu = p
        llocd = d

        for i in range(1, llargada_patro-l):
            if llista_resultats[-llocu] != llista_resultats[-llocd]:
                return False
                break
            
            else:
                llocu += 1
                llocd += 1



    def patrons():
        parar = 0
        n = 1
        m = 1

        global llargada_patro,llargada_llista,llista_resultats,posicio, patroutil

        if llargada_llista < 12:
            return False
        else:
            if llargada_llista < 2000:

                llargada_patro = (int(llargada_llista/4))
            
            else: 
                llargada_patro = 500
        
        while n < (llargada_patro-3):#posicio, llargada etc
            posicio = 1

            if parar == 1:
                break
            while posicio < llargada_patro:
                m = 1
                if parar == 1:
                    break
                for i in range(1,llargada_patro):

                    if parar == 1:
                        break
                    
                    if suma(n,posicio) == suma(n,(posicio+m)): #no
                        
                        if comprobacio(n,posicio,(posicio+m)) != False:

                            #print("patro")
                            #print(suma(n,posicio), " i ", suma(n,(posicio+m)))
                            #print(llargada_patro - n)
                            print(nombres_patro(n,posicio), posicio)
                            print(nombres_patro(n,(posicio+m)), (posicio+m))
                            patroutil = (nombres_patro(n,posicio))
                            
                            return True
                            parar += 1

                    m += 1 

                posicio += 1
                
            n += 1
            

    def convertidor(n): #converteix de numeros a lletres
        if n == 1:
            return "R"
        if n == 2:
            return "P"
        if n == 3:
            return "S"

    def maguanyadora(n):
        if convertidor(n) == "R":
            return "P"

        if convertidor(n) == "P":
            return "S"

        if convertidor(n) == "S":
            return "R"

    tR = int(33) #afecta a la probabilitat de tindre P (mes gran mes probable) i a la de R (inversament proporcional a la R)

    tP = int(66) #afecta a la probabilitat de tindre R (mes gran mes probable) i a la de S (inversament proporcional a la R)

    almillor = input("\nA quants punts vols jugar? ")

    def probabilitat():
        global tP,tR
        if ma_persona == "P": # guanya S
            if tP > 10:
                tP -= 10
                if tP < tR:
                    tP =  ((tR - tP)+10)

        if ma_persona == "R": # guanya P
            if tP > tR:
                tR += 10
                
        if ma_persona == "S": # guanya R
            if tR > 5:
                tR -= 5
                if tR < 5:
                    tR = 5
            tP += 5
            if tP < tR:
                    tP = ((tR - tP)+10)
            if tP > 100:
                    tP = 95

    while victoria < 1:
        ma_persona = convertidor(q)
        preparar_llista()
        

        if llargada_llista >= 12:
            if espera < 1:
                if patrons() == True:
                    patrons()
                    if patroutil[0] == llista_resultats[-1]: # si l'ultim que s'ha tirat es igual al primer del patro

                        ma_ordinador = maguanyadora((int(patroutil[1]))) #per guanyar al jugador 

                        espera = llargada_patro

        else:
            ma_ordinador = random.randint(1,100)

            if ma_ordinador > 0 and ma_ordinador <= int(tR):
                ma_ordinador = "P"
            else:
                if ma_ordinador > int(tR) and ma_ordinador <= int(tP):
                    ma_ordinador = "R"
                else:
                    if ma_ordinador > int(tP) and ma_ordinador <= 100:
                        ma_ordinador = "S"
    

        if ma_ordinador == ma_persona:
#            print("Empat, els dos heu triat: ", ma_ordinador)
            probabilitat()

        else: 
            if ma_persona == "R":
                if ma_ordinador == "P":
                    puntuacio += 1
     #               print("L'ordinador guanya, ha triat:", ma_ordinador)
      #              print("\n", "Punts ordinador: ",puntuacio, "\n","Punts jugador: ", puntuacio_jugador)
                    probabilitat()
                
                else:
                    puntuacio_jugador += 1
       #             print("Tu guanyes, l'ordinador ha triat:", ma_ordinador)
        #            print("\n", "Punts ordinador: ",puntuacio, "\n","Punts jugador: ", puntuacio_jugador)
                    probabilitat()

            if ma_persona == "P":
                if ma_ordinador == "S":
                    puntuacio += 1
         #           print("L'ordinador guanya, ha triat:", ma_ordinador)
          #          print("\n","Punts ordinador: ",puntuacio, "\n","Punts jugador: ", puntuacio_jugador)
                    probabilitat()
                
                else:
                    puntuacio_jugador += 1
            #        print("Tu guanyes, l'ordinador ha triat:", ma_ordinador)
           #         print("\n","Punts ordinador: ",puntuacio, "\n","Punts jugador: ", puntuacio_jugador)
                    probabilitat()

            if ma_persona == "S":
                if ma_ordinador == "R":
                    puntuacio += 1
           #         print("L'ordinador guanya, ha triat:", ma_ordinador)
            #        print("\n","Punts ordinador: ",puntuacio, "\n","Punts jugador: ", puntuacio_jugador)
                    probabilitat()
                
                else:
                    puntuacio_jugador += 1
             #       print("Tu guanyes, l'ordinador ha triat:", ma_ordinador)
              #      print("\n","Punts ordinador: ",puntuacio, "\n","Punts jugador: ", puntuacio_jugador)
                    probabilitat()

        
        

            
        if (puntuacio_jugador) == (int(almillor)):
            victoria += 1
        
        if (puntuacio) == (int(almillor)):
            victoria += 1

        if espera > 0:
            espera -= 1
        

        
    if puntuacio > puntuacio_jugador:
        print("L'ordinador guanya")
    else:
        print("Tu guanyes")

    patrons()


    print (patroutil) # UTILITZAT 
    print (patroutil[0]) # PRIMER NUMERO PATROUTIL
    print("Llista:\n",llista_resultats)

    return ma_ordinador,puntuacio,("Ordinador") ,puntuacio_jugador, ("Contrari") #RETORNA LA MA QUE HA TIRAT 
    
                