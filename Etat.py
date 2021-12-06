# Bibliothèques utilisées

from tkinter import *
from tkinter.ttk import Combobox
from tkinter.messagebox import *
import threading
from Compte import Compte
from Manager import manager

# Gestion de la fenetre
class Etats(Tk):
    # Constructeur de la fenêtre
    def __init__(self):
        Tk.__init__(self)
        self.title("Listing des Comptes")
        self.geometry("300x100")
        self.attributes("-topmost", True)

        self.label = Label(self, text="Etats des Comptes", bg="orange")
        self.label.pack()

        self.user = StringVar()
        l = list(Compte.liste.keys())
        self.liste_User = l
        self.liste = Combobox(self, textvariable=self.user, values=self.liste_User, state='readonly')
        self.liste.pack()

        #Bouton Valider
        self.valid = Button(self, text="Valider")
        self.valid.pack()
        self.valid.bind('<Button-1>', self.clic)

    def clic(self, evt):
        user = self.liste.get()
        print(user)
        compte = manager.recuperer_compte(user)
        if not compte:
            return print("Il y a pas de comptes")
        
        texte = "Nom : " + str(user) + "\n" + "Solde : " + str(compte.get_compte()) + "€" + "\n" + "statuts : " + compte.get_etat() 
        self.newwind("Etat du compte", texte)

    def newwind(self, titre, texte):
        showinfo(titre, texte)

        # Gestion de la fermeture de la fenetre
    def close(self):
        """
        """
        print("Interception de la fermeture de la fenetre par la croix")
        # Exécution des fonctions à exécuter à la fermeture de la fenêtre
        for fct in self.l_fct:
            fct
        self.destroy()


class Fils_Execution(threading.Thread):
    """
    """

    def __init__(self, tempo=1):
        """
        Constructeur d'un objet de type Thread afin de réaliser des opérations en dehors de l'objet Fenetre
        :param (int): temporisation en seconde de la boucle run
        :return (None):
        :Effet de bord (None):

        """
        threading.Thread.__init__(self)
        self.stopevent = threading.Event()
        self.tempo = tempo
        self.actif = True

    def run(self):
        """
        """
        i = 0
        print("Démarrage du fil d'exécution")
        while not self.stopevent.isSet():
            print("Fil d'éxécution :", i)
            i += 1
            self.stopevent.wait(self.temporisation)
            print("Le thread s'est terminé proprement")
        print('Arrêt de la boucle Run....')
        self.stop()  # on revient en mode arrêt

    def stop(self):
        """
        Destruction du fil d'exécution
        """
        print("Destruction du fil d'exécution...")
        self.actif = False
        self.stopevent.set()

# Programme principal


if __name__ == '__main__':
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
    pass

    # Fil d'exécution pouvant être utilisé pour l'exécution de scripts en parallèle de la vie de la fenêtre
    fil_1 = Fils_Execution(1)

    fenetre = Liste()
    fenetre.mainloop()
    print('Le programme se termnine maintenant....')