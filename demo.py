from sense_hat import SenseHat
import time

class SenseHatEncodator(SenseHat):
    
    def __init__(self):
        super().__init__()
        self.__menu = {0 : "Help", 1 : "Lire le message", 2 : "Nouveau message", "Lire le message" : "$display_msg",\
                       "Nouveau message" : "$register_message"}
        
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
                
    def show_number(self, num):
        """
        pre : num est un entier positif a un chiffre.
        Des images .png de tous les chiffres doivent exister dans un meme dossier.
        Si ce dernier n'est pas le meme que celui du programme, il doit etre
        defini au depart par une variable pic_dir.
        pic_dir doit se terminer par un "/" ou un "\".
        post : affiche une image du chiffre "num".
        """
        #Si pic_dir n'est pas defini, path est un string vide
        try:
            path = pic_dir
        except NameError:
            path = ""
        filename = "{0}{1}.png".format(path, num)
        self.load_image(filename)
        
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
        
if __name__ == "__main__":
    pass