# Bibliothèques utilisées
from tkinter import *
from tkinter import font
from tkinter.messagebox import *
from time import time, ctime
from time import *
import threading
import Logs
from Compte import Compte
import nsi_dict_indien
from Manager import manager
import Transfert
import Listing
import Etat
import Del
import random
                
# Gestion de la fenetre
class Fenetre(Tk):

    #Variable
    menu_val = 1
    t = time()

    # Constructeur de la fenêtre
    def __init__(self, l_fct_stop, titre_fenetre = "Compte Bancaire", dim = (640, 480), couleur = "red", bg = '#FFC566'):
        Tk.__init__(self)
        self.l_fct = l_fct_stop
        self.title(titre_fenetre)
        self.couleur = couleur
        self.largeur = dim[0]
        self.hauteur = dim[1]
        dimension_fenetre = "%dx%d" % (self.largeur, self.hauteur)
        self.geometry(dimension_fenetre)
        f = open('logs.txt', "a")
        f.writelines("\n")
        date = ctime(Fenetre.t) + "\n"
        f.write(date)
        f.close()
        #Texte Informatif
        self.label = Label(self, text="Ouvrez vous un compte à la \nbanque populaire", bg="orange")
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
        self.amount.grid(row=2)

        #Valeur de solde
        self.value2 = StringVar()
        self.montant = Entry(self, width=30)
        self.montant.grid(row=2, column=1)
        
        #Bouton Valider
        self.bouton = Button(self, text="Valider")
        self.bouton.grid(row=3, column=1)
        self.bouton.bind('<Button-1>', self.clic_souris)
        
#___________________________________________________________________________________________________________
# -------------------------------------------Définition du menu---------------------------------------------
#___________________________________________________________________________________________________________
        menubar = Menu(self)
        
        #Menu Gérer le compte

        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="Accueil", command=self.accueil)
        menu1.add_command(label="Dépot d'Argent", command=self.depot)
        menu1.add_command(label="Retrait d'Argent", command=self.retrait)
        menu1.add_command(label="Transfert d'Argent", command=self.transfert)
        menu1.add_separator()
        menu1.add_command(label="Désactiver un Compte", command=self.desactiver)
        menu1.add_command(label="Réactiver un Compte", command=self.activer)
        menu1.add_command(label="Supprimer un Compte", command=self.detruire)
        menubar.add_cascade(label="Gérer le compte", menu=menu1)
        
        #Menu Infos
        
        menu2 = Menu(menubar, tearoff=0)
        menu2.add_command(label="Etat du Compte", command=self.etat)
        menu2.add_command(label="Liste des Comptes", command=self.listing)
        menu2.add_command(label="Logs", command=self.logs)
        menubar.add_cascade(label="Infos", menu=menu2)
        
        #Menu Aide

        menu3 = Menu(menubar, tearoff=0)
        menu3.add_command(label="A propos", command=lambda: showinfo("A propos de nous", "Nous sommes une banque ne développement, certaines maintenances peuvent avoir lieu, désolé du dérangement occasionnel."))
        menubar.add_cascade(label="Aide", menu=menu3)

        self.config(menu=menubar)

        # Initialisation de l'événement de gestion de la fermeture de la fenêtre graphique
        self.protocol("WM_DELETE_WINDOW", self.close)
        
        #------------------------------------------------
        #Fonctions usuelles
        #------------------------------------------------

    def hide_all(self):
        """
        Cache tout
        """
        self.value.set("")
        self.value2.set("")
        self.amount.config(text="")
        self.montant.grid_forget()
        self.bouton.grid(row=2, column=1)
        
    def recover_montant(self):
        """
        Replace l'input montant et met le texte pour dire ce que fait l'input + remise en place de bouton valider
        """
        self.amount.config(text="Solde :")
        self.montant = Entry(self, width=30)
        self.montant.grid(row=2, column=1)
        self.bouton.grid(row=3, column=1)
        self.value.set("")
        self.value2.set("")
        
    
        #--------------------------------------------------------------------------------------------------------
        #Affichage des onglets acceuil, dépot, retrait, désactiver, activer, détruire, état, et liste des comptes 
        #--------------------------------------------------------------------------------------------------------
        
    def accueil(self):
        """
        Permet l'affichage de l'onglet acceuil de la banque
        """
        Fenetre.menu_val = 1
        self.hide_all()
        self.recover_montant()
        self.label.config(text="Ouvrez vous un compte à la \nbanque populaire")
        self.user.config(text="Utilisateur :")
        self.amount.config(text="Solde :")

    def depot(self):
        """
        Permet l'affichage de l'onglet dépot d'argent
        """
        Fenetre.menu_val = 2
        self.hide_all()
        self.recover_montant()
        self.label.config(text="Déposer de l'argent vers \nson Compte")
        self.user.config(text="Compte :")
        self.amount.config(text="Montant :")

    def retrait(self):
        """
        Permet l'affichage de l'onglet retrait transfert d'argent
        """
        Fenetre.menu_val = 3
        self.hide_all()
        self.recover_montant()
        self.label.config(text="Retirer de l'argent \ndu compte")
        self.user.config(text="Compte :")
        self.amount.config(text="Montant :")

    def desactiver(self):
        """
        Permet l'affichage de l'onglet désactiver compte
        """
        Fenetre.menu_val = 4
        self.hide_all()
        self.label.config(text="Désactiver le compte")
        self.user.config(text="Compte :")

    def activer(self):
        """
        Permet l'affichage de l'onglet activer compte
        """
        Fenetre.menu_val = 5
        self.hide_all()
        self.label.config(text="Reactiver le compte")
        self.user.config(text="Compte :")
        
    def detruire(self):
        """
        Permet l'affichage de l'onglet détruire
        """
        Fenetre.menu_val = 6
        Del.Del()

    def etat(self):
        """
        Permet l'affichage de l'onglet état du compte
        """
        Etat.Etats()

    def listing(self):
        """
        Permet l'affichage de l'onglet liste des comptes
        """
        Fenetre.menu_val = 8
        Listing.Liste()
        
    def transfert(self):
        """
        Permet l'affichage de l'onglet transfert
        """
        Transfert.Transfert()

    def logs(self):
        """
        L'onglet logs sous forme de fichier texte
        """
        Logs.Logs()
        
        
#___________________________________________________________________________________________________________
# ---------------------------------------Mise en marche des onglets-----------------------------------------
#___________________________________________________________________________________________________________

    def clic_souris(self, evt):
        """
        Permet la création du compte ainsi que la mise en marche des différents onglets
        Et affiche l'action effectuée dans les logs
        """
        f = open('logs.txt', "a")
        user = self.nom.get()
        montant = self.montant.get()
        
        
        #-----------------------
        #Onglet d'acceuil, création du compte
        #-----------------------
        
        
        if Fenetre.menu_val == 1:
            # Quand on crée un compte
            if not montant.isnumeric():
                showerror("Action invalide", "La valeur entrée n'est pas correcte")
                return
            texte = "Compte de : " + str(user) + " ouvert avec succés." + "\n"
            manager.ajouter_compte(user, int(montant))
            print("Ouverture du compte avec succés - " + montant + "€ " + user + "\n")
            showinfo("Ouverture du compte", texte)
            f.write(str(texte))
            
            
        #-----------------------
        #Onglet dépot d'argent
        #-----------------------
            
            
        elif Fenetre.menu_val == 2:
            # Quand on veut déposer une somme d'argent
            texte = str(user) + " vous avez déposé : " + str(montant) + " €" + "\n"
            compte = manager.recuperer_compte(self.nom.get())
            if compte.etat == 0:
                return showerror("Action invalide", "Le compte courant est désactivé")
            if not compte:
                showerror("Action invalide", "Le compte n'existe pas")
                return
            if not montant.isnumeric():
                showerror("Action invalide", "La valeur entrée n'est pas correcte")
                return
            Compte.deposer(compte, int(montant))
            showinfo("Déposer de l'argent", texte)
            f.write(str(texte))
            
        #-----------------------
        #Onglet retrait d'argent
        #-----------------------
        
        elif Fenetre.menu_val == 3:
            # Quand on veut retirer de l'argent
            texte = str(user) + " vous avez fait un retrait de : " + str(montant) + " €" + "\n"
            compte = manager.recuperer_compte(self.nom.get())
            if compte.etat == 0:
                return showerror("Action invalide", "Le compte courant est désactivé")
            if not compte:
                return showerror("Action invalide", "Le compte n'existe pas")
            if not montant.isnumeric():
                return showerror("Action invalide", "La valeur entrée n'est pas correcte")
            if compte.solde < int(montant):
                return showerror("Action invalide" , "La solde est trop basse pour ce retrait")
            res = compte.retirer(int(montant))
            if res:
                showerror("Erreur", res)
                return
            showinfo("Retirer de l'argent", texte)
            f.write(str(texte))
            
        #-----------------------
        #Onglet désactiver le compte
        #-----------------------
            
        elif Fenetre.menu_val == 4:
            compte = manager.recuperer_compte(self.nom.get())
            
            if not compte:
                showerror("Action invalide" , "Impossible de désactiver ce compte : inexistant")
                return
            texte = "Compte : " + str(user) + " a été désactivé."
            if compte.etat == 0:
                return showerror("Erreur" , "Ce compte est déjà désactivé")
            showinfo("Desactivation compte", texte)
            
            compte.etat = 0
            
            
        #-----------------------
        #Onglet réactiver le compte
        #-----------------------
            
        elif Fenetre.menu_val == 5:
            texte = "Compte : " + str(user) + " a été réactivé."
            compte = manager.recuperer_compte(self.nom.get()) 
            if not compte:
                return showerror("Action invalide" , "Impossible de réactiver ce compte : inexistant")
            if compte.etat == 1:
                return showerror("Erreur" , "Ce compte est déjà actif")
            showinfo("Réactivation du compte", texte)
                
            compte.etat = 1
            
        #-----------------------
        #Onglet destruction du compte
        #-----------------------

        elif Fenetre.menu_val == 6:
            texte = str(user) + " votre compte a été détruit avec succés !"
            askyesno("Détruire son compte", "Voulez vous vraiment détruire votre compte ?")
            compte = manager.recuperer_compte(self.nom.get())
            l = list(Compte.liste.keys())
            
            if not compte:
                showerror("Action invalide" , "Impossible de supprimer ce compte : inexistant")
                return
            del compte.liste[l[compte.ide]]
            showinfo("Compte détruit" , texte)
        f.close()

            
#___________________________________________________________________________________________________________

    # Gestion de la fermeture de la fenetre
    def close(self):
        """
        """
        print ("Fermeture de l'interface Homme - Machine...")
        # Exécution des fonctions à exécuter à la fermeture de la fenêtre
        for fct in self.l_fct:
            fct
        self.destroy()
        
#___________________________________________________________________________________________________________
        

class Fils_Execution(threading.Thread):
    """
    """
    def __init__(self, tempo = 1):
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
            print ("Le thread s'est terminé proprement")
        print('Arrêt de la boucle Run....')
        self.stop()                       

    def stop(self):
        """
        Destruction du fil d'exécution
        """
        print("Destruction du fil d'exécution...")
        self.actif = False
        self.stopevent.set( )
        
#___________________________________________________________________________________________________________

# Programme principal
if __name__=='__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
    l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for n in range(21):
        f = random.choice(l)
        i = random.choice(l)
        user = (nsi_dict_indien.DICT_1[f] + nsi_dict_indien.DICT_2[i])
        manager.ajouter_compte(str(user), random.randint(500, 15000))
    pass

    # Fil d'exécution pouvant être utilisé pour l'exécution de scripts en parallèle de la vie de la fenêtre
    fil_1 = Fils_Execution(1)
    
    fenetre = Fenetre([fil_1.stop], 'Compte Bancaire', (300, 300), '#FFC566' )
    fenetre.mainloop()
    print('Merci d\'avoir utilisé la banque populaire !')