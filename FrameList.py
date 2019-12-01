class FrameList:
    """
    Liste chainee de Frames.
    """
    def __init__(self):
        """
        pre : -
        post : initialise un objet FrameList.
        self.__lenght est le nombre de Frames que contient self.
        self.__head est le premier Frame de self.
        self.__tail_end est le dernier Frame de self.
        """
        self.__lenght = 0
        self.__head = None
        self.__tail_end = None
        
    def head(self):
        return self.__head
    
    def tail_end(self):
        return self.__tail_end
    
    def lenght(self):
        return self.__lenght
        
    def add_last(self, frame):
        """
        pre : frame est un Frame dont les attributs __next et __last sont None.
        post : ajoute Frame a self.
        Ce Frame sera reference par l'ancien Frame self.__tail_end et deviendra le nouveau self.__tail_end
        """
        #Si le LinkedList est vide
        if self.head() == None:
            self.__head = frame
            self.__tail_end = frame
        #Sinon, on attache frame au reste du LinkedList
        else:
            self.tail_end().setnext(frame)
            frame.setlast(self.tail_end())
            self.__tail_end = frame
        self.__lenght += 1
    
class Frame:
    def __init__(self, cargo = None, nxt = None, last = None, up = None, down = None):
        """
        pre : -
        post : initialise un objet Frame.
        self.__cargo est le contenu du Frame, c'est ce qui est retourne par la methode __str__(self).
        self.__last et self.__next peuvent etre des objets Frames.
        self.__up et self.__down peuvent etre des objets FrameList.
        """
        self.__cargo = cargo
        self.__last = last
        self.__next = nxt
        self.__up = up
        self.__down = down
        
    def __str__(self):
        return str(self.__cargo)
    
    def last(self):
        return self.__last
    
    def next(self):
        return self.__next
    
    def up(self):
        return self.__up
    
    def down(self):
        return self.__down
    
    def setnext(self, nxt):
        self.__next = nxt
        
    def setlast(self, last):
        self.__last = last