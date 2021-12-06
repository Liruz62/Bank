# Bibliothèques utilisées

from tkinter import *
from tkinter.ttk import Combobox
from tkinter.messagebox import *
import threading
from Compte import Compte
from Manager import manager

# Gestion de la fenetre
class Transfert(Tk):
    # Constructeur de la fenêtre
    def __init__(self):
        Tk.__init__(self)
        self.title("Transfert")
        self.geometry("300x150")
        self.attributes("-topmost", True)

        self.label = Label(self, text="Transfert", bg="orange")
        self.label.grid(row=0, column=1)


        #Texte User
        self.user = Label(self, text="Utilisateur :")
        self.user.grid(row=1)

        #Valeur de nom
        self.value = StringVar()
        self.nom = Entry(self, width=30)
        self.nom.grid(row=1, column=1)

        #Texte Amount
        self.amount = Label(self, text="Solde :")
        self.amount.grid(row=3)

        #Valeur de solde
        self.value2 = StringVar()
        self.montant = Entry(self, width=30)
        self.montant.grid(row=3, column=1)
        
        #Texte Destinataire
        self.destinataire = Label(self, text="Destinataire :")
        self.destinataire.grid(row=2)

        #Valeur de Desinataire
        self.value3 = StringVar()
        self.desti = Entry(self, width=30)
        self.desti.grid(row=2, column=1)
        
        #Bouton Valider
        self.bouton = Button(self, text="Valider")
        self.bouton.grid(row=4, column=1)
        self.bouton.bind('<Button-1>', self.clic)

    def clic(self, evt):
        f = open("logs.txt", "a")
        user = self.nom.get()
        montant = self.montant.get()
        desti = self.desti.get()
        destinataire = manager.recuperer_compte(self.desti.get())
        compte = manager.recuperer_compte(self.nom.get())
        texte = str(user) + " vous avez fait un transfert de : " + str(montant) + " €" + " à " + str(desti) + "\n"
        texte2 = str(user) + " n'a pas assez de fonds !"
        if compte.etat == 0:
            return showerror("Action invalide", "Le compte courant est désactivé")
        if not compte:
            return showerror("Action invalide", "Le compte n'existe pas")
        if destinataire.etat == 0:
            return showerror("Action invalide", "Le compte destinataire est désactivé")
        if not compte:
            return showerror("Action invalide", "Le compte destinataire n'existe pas")
        if not montant.isnumeric():
            return showerror("Action invalide", "La valeur entrée n'est pas correcte")
        if compte.solde == 0:
            return showerror("Action invalide", texte2)
        res = compte.transfert(destinataire, int(montant))
        if res:
            showerror("Erreur", res)
            return
        showinfo("Transferer de l'argent", texte)
        f.write(str(texte))
        f.close()


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

    fenetre = Transfert()
    fenetre.mainloop()
    print('Le programme se termnine maintenant....')