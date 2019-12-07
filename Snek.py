from sense_hat import SenseHat
import time

class Snek:
    
    def __init__(self):
        """
        pre : -
        post : initialise un objet Snek ou
        self.__head est le premier SnekPart du Snek.
        self.__tail est le dernier SnekPart du Snek.
        """
        self.__head = None
        self.__tail = None
        
    def gethead(self):
        return self.__head
    
    def gettail(self):
        return self.__tail
    
    def add_last(self, s):
        """
        pre : s est un SnekPart
        post : ajoute le SnekPart s a la fin de Snek
        """
        pass
        
    def move(self, extend = False):
        """
        pre : extend est un boolean
        post : deplace le Snek et l'allonge de 1 si extend = True
        """
        pass
    
    def run(self):
        """
        pre : self.__head != de None
        post : commence un jeu de snake.
        Retourne la position de la tete lors de la mort du Snek.
        """
        pass
    
class SnekPart:
    
    def __init__(self, pos, heading, next = None):
        """
        pre : pos est une liste.
        heading est un string valant n, s, e ou w
        post: self.__pos est la position du SnekPart dans la matrice de led.
        self.__heading est l'orientation du SnekPart (n = north, s = south, e = east et w = east)
        self.__next peut etre le SnekPart suivant celui-ci.
        """
        self.__pos = pos
        self.__heading = heading
        self.__next = next
        
    def getpos(self):
        return self.__pos
    
    def getheading(self):
        return self.__heading
    
    def getnext(self):
        return self.__next
    
    def setpos(self, npos):
        self.__pos = npos
        
    def setheading(self, nheading):
        self.__heading = nheading
        
    def setnext(self, nnext):
        self.__next = nnext