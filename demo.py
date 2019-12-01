from sense_hat import SenseHat
from FrameList import FrameList, Frame
import time

class SenseHatEncodator(SenseHat):
    
    def __init__(self):
        super().__init__()
        
    def display_msg(self):
        self.show_message("Merci d'entrer le mot de passe.")
        #A faire par Lucas
        
    def register_message(self):
        self.show_message("Veuillez entrer le message.")
        numbers = r
        
    def type_message(self):
        #Non fini
        """
        pre : -
        """
        self.show_message("Entrez le message. > pour aide")
        start = True
        while start():
            event = self.wait_for_event
            if event.direction == "right":
                self.show_message("Vous pouver")
        
    def show_registered_message(self):
        """
        pre : -
        post : si un message existe, affiche celui-ci.
        Sinon, affiche un message d'erreur.
        """
        if message_exists():
            with open("message.txt", "r") as file:
                a = file.readlines()
                for line in a:
                    self.show_message(line)
        
        else:
            self.show_message("There is no message", text_colour=[255, 0, 0])
        
def message_exists():
    """
    pre : -
    post : retourne True si un message est deja enregistre, False sinon
    """
    try:
        with open("message.txt", "r") as file:
            if file.readlines()[0].strip() == "" and len(file.readlines()) == 1:     #Si le fichier message est vide.
                return False
            else:
                return True
    except FileNotFoundError:
        return False    #On retourne False si le fichier message.txt n'existe pas.

def register_message(content):
    """
    pre : content est une liste de strings.
    post : cree un nouveau fichier message.txt avec comme contenu "content"
    qui ecrase l'ancien fichier message.txt si ce dernier existait.
    """
    with open("message.txt", "w") as file:
        file.writelines(content)
        
def handle_wait_for_event(event):
    """
    pre : event est un objet SenseHat.stick.
    post : retourne le nouveau Frame a afficher.
    Ne gere pour le moment que les mouvements gauche droite du joistick.
    """
    if event.action != "released":
        if event.direction == "right":
            return current_frame.next()
        if event.direction == "left":
            return current_frame.last()
        
if __name__ == "__main__":
    #Creation des FrameLists qui composent les menus (à remplacer plus tard)
    main_menu = FrameList()
    (a, b) = (Frame(cargo = "Lire le message", up = "display_msg"),\
              Frame(cargo = "Nouveau message", up = "register_message"))
    main_menu.add_last(a)
    main_menu.add_last(b)
    #Creation du SenseHat
    s = SenseHatEncodator()
    #Programme principal
    running = True
    current_menu = main_menu
    current_frame = a
    message_showed = True
    while running:
        if message_showed:    #Empeche les inputs ne changeant pas le message afficher de faire celui-ci se repeter.
            s.show_message(text_string = str(current_frame), scroll_speed = 0.05)
        event = s.stick.wait_for_event()
        print(event)
        rcf = handle_wait_for_event(event)
        if rcf == None:       #Si current_frame ne change pas, on ne réaffiche pas le meme Frame.
            message_showed = False
        else:
            message_showed = True
            current_frame = rcf