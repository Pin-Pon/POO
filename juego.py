import random
import time

class Game():
    def __init__(self):
        self.secuencia_puntos = [0,15,30,40]
        self.puntos_j1 = 0 #posicion en la lista...del jugador
        self.puntos_j2 = 0
        
        self.deuce = False
        self.ganador = None

    def ganador_punto(self):
        return random.randint(1,2)

    def jugar_game(self):
        ganador = self.ganador_punto()
        print("> Punto ganado por JUGADOR %s" % (ganador)) 

        puntos_antes_del_game = getattr(self,"puntos_j"+str(ganador))

        if self.deuce:
            if self.puntos_j1 > self.puntos_j2 and ganador==1:
                setattr(self,"puntos_j" + str (ganador),puntos_antes_del_game+1)
                print("GANO EL JUGADOR 1")
            elif self.puntos_j1 >self.puntos_j2 and ganador ==2:
                self.puntos_j1 = self.puntos_j1 -1
            elif self.puntos_j2 > self.puntos_j1 and ganador==2:
                setattr(self,"puntos_j"+str(ganador),puntos_antes_del_game+1)
                print("GANO EL JUGADOR 2")
            elif self.puntos_j2 > self.puntos_j1 and ganador ==1:
                self.puntos_j2 = self.puntos_j2 -1
            else:
                setattr(self,"puntos_j"+str(ganador),puntos_antes_del_game+1)
                print("Ventaja jugador %s" % (ganador))
        else:
            setattr(self,"puntos_j"+str(ganador),puntos_antes_del_game+1)  

        self.check_deuce()                            
    
    def check_deuce(self):
        if not self.deuce and (self.puntos_j1 == self.puntos_j2 == len(self.secuencia_puntos)-1):
            self.deuce= True

    def fin(self):
        es_fin = False

        x = (self.puntos_j1 > self.puntos_j2 and self.puntos_j1 == len(self.secuencia_puntos)) or (self.puntos_j2 > self.puntos_j1 and self.puntos_j2 >= len(self.secuencia_puntos))   

        if not self.deuce and (x):
            es_fin = True
        if self.deuce and ((self.puntos_j1 > self.puntos_j2 and self.puntos_j1 == len(self.secuencia_puntos)+1) or (self.puntos_j2> self.puntos_j1 and self.puntos_j2 >= len(self.secuencia_puntos)+1)):
            es_fin = True

        if es_fin:
            if self.puntos_j1 > self.puntos_j2:
                self.ganador = 1
            else:
                self.ganador = 2
        return es_fin 
    def ver_puntuacion(self):
        if self.deuce and self.puntos_j1 > self.puntos_j2:
            ptos_j1 = "V"
        elif self.puntos_j1 < len(self.secuencia_puntos)-1:
            ptos_j1 = self.secuencia_puntos[self.puntos_j1]
        else:
            ptos_j1 = self.secuencia_puntos[len(self.secuencia_puntos)-1]
        if self.deuce and self.puntos_j2 > self.puntos_j1:
            ptos_j2= "V"
        elif self.puntos_j2 < len(self.secuencia_puntos)-1:
            ptos_j2 = self.secuencia_puntos[self.puntos_j2]
        else:
            ptos_j2 = self.secuencia_puntos[len(self.secuencia_puntos)-1]

        print("=========================") 
        print("JUGADOR 1 | %s" % (ptos_j1)) 
        print("JUGADOR 2 | %s" % (ptos_j2)) 
        print("===========================")    

g = Game()
while not g.fin():
    g.jugar_game()
    g.ver_puntuacion()
    time.sleep(2)
print("Fin del game")
print("GANADOR")    
print("JUGADOR"+ str(g.ganador))





 













g = Game()

g.jugar_game()