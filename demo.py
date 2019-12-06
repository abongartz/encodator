from sense_hat import SenseHat
from subprocess import call
from FrameList import FrameList, Frame
import time

class SenseHatEncodator(SenseHat):
    
    def __init__(self):
        super(SenseHatEncodator, self).__init__()
        
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
            
    def display_proto_message(self):
        """
        pre : -
        post : affiche le message contenu dans le fichier "proto-message.txt".
        Affiche un message d'erreur s'il n'y en a pas.
        """
        try:
            with open("proto-message.txt", "r") as file:
                proto_message = file.readlines[0]
                if proto_message.strip() == "":
                    self.show_message("Aucun message enregistre", scroll_speed = 0.05)
                else:
                    self.show_message(proto_message, scroll_speed = 0.05)
        except FileNotFoundError:
            self.show_message("Aucun message enregistre", scroll_speed = 0.05)
        
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
        
def handle_wait_for_event(event, frame, s):
    """
    pre : event est un objet SenseHat.stick.
    frame est un objet Frame.
    s est un SenseHatEncodator.
    post : retourne le nouveau Frame a afficher.
    Ne gere pour le moment que les mouvements gauche droite du joistick.
    """
    to_return = None
    if event.action != "released":
        if event.direction == "right":
            to_return = frame.next()
        elif event.direction == "left":
            to_return = frame.last()
        elif event.direction == "down" and frame.down() == None:
            call("sudo shutdown -h now", shell=True)    #TODO : ajouter une demande de confirmation
        elif event.direction == "up" and frame.up() != None:
            try:
                to_return = frame.up().head()
            except AttributeError:
                to_return = str(frame.up())
        elif event.direction == "down" and frame.down() != None:
            to_return = frame.down()
        if str(to_return)[0] == "$":
            handle_methods(to_return, frame, s)
            return None
        else:
            return to_return
            
def handle_methods(string, frame, s):
    """
    pre : string commence par $.
    frame est un Frame.
    s est un SenseHatEncodator
    post : execute la fonction designee par string
    """
    function = string[1:]
    if function == append_new_message:
        frame.append_new_message("proto-message.txt")
    if function == display_proto_message:
        s.display_proto_message()
        

if __name__ == "__main__":
    #Creation des FrameLists qui composent les menus (a remplacer plus tard)
    main_menu = FrameList()
    new_message_menu = FrameList()
    keyboard_menu = FrameList()
    keyboard_menu_frames = []
    for i in range(10):
        frame = Frame(cargo = i)    #TODO : define a up attribute here
        frame.setup("$append_new_message")
        keyboard_menu_frames.append(frame)
    (a1, a2, a3, a4) = (Frame(cargo = "Entrer un message", up = keyboard_menu), Frame(cargo = "Entrer le mot de passe"),\
                        Frame(cargo = "Voir le message", up = "$display_proto_message"), Frame(cargo = "Valider"))
    new_message_menu_frames = [a1, a2, a3, a4]
    (b, a) = (Frame(cargo = "Lire le message"),\
              Frame(cargo = "Nouveau message", up = new_message_menu))
    main_menu_frames = [a, b]
    
    keyboard_menu.setdown(a1)
    new_message_menu.setdown(a)
    
    for frame in keyboard_menu_frames:
        keyboard_menu.add_last(frame)
        
    for frame in new_message_menu_frames:
        new_message_menu.add_last(frame)
        
    for frame in main_menu_frames:
        main_menu.add_last(frame)
    #Creation du SenseHat
    s = SenseHatEncodator()
    #Programme principal
    running = True
    current_menu = main_menu
    current_frame = a
    message_showed = True
    while running:
        if message_showed:    #Empeche les inputs ne changeant pas le message afficher de faire celui-ci se repeter.
            if len(str(current_frame)) > 1:    #On separe les characteres des autres strings
                s.show_message(text_string = str(current_frame), scroll_speed = 0.05)
            else:
                s.show_letter(str(current_frame))
        event = s.stick.wait_for_event()
        print(event)
        rcf = handle_wait_for_event(event, current_frame, s)
        if rcf == None:       #Si current_frame ne change pas, on ne reaffiche pas le meme Frame.
            message_showed = False
        else:
            message_showed = True
            current_frame = rcf