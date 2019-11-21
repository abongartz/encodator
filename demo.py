from sense_hat import SenseHat
import time

s = SenseHat()

def message_exists():
    """
    pre : -
    post : retourne True si un message est deja enregistre, False sinon
    """
    try:
        with open("message.txt", "r") as file:
            if file.readlines() == []:     #Si le fichier message est vide.
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
        
def type_message(s):
    #Non fini
    """
    pre : s est un SenseHat
    """
    s.show_message("Entrez le message. > pour aide")
    start = True
    while start():
        event = s.wait_for_event
        if event.direction == "right":
            s.show_message("Vous pouver")
    