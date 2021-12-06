class Compte():
    liste = {}
    def __init__(self, ide, nom, solde = 0, etat = 1):
        self.ide = ide
        self.nom = nom
        self.solde = solde
        self.etat = etat
        Compte.liste[self.nom] = self.solde
        
    
        #-----------------------
        #récupération de l'état du compte
        #-----------------------
        
    def get_etat(self):
        if self.etat == 1:
            return "Activé"
        return "Désactivé"
        

        #-----------------------
        #méthode de dépot d'argent sur le compte
        #-----------------------
    
    def deposer(compte ,argent):
        """
        Fonction permettant d'ajouter un montant à la solde du compte
        :param (int) : nombre entier indiquant le montant à ajouter
        :return :
        :Effet de bord:
        :CU : (None)
        
        >>> lucas = Compte('GUGLIELMETTI' , 3000000)
        >>> lucas.deposer(100)
        >>> lucas.solde
        3000100
        
        """
        compte.solde = compte.solde + argent
        l = list(Compte.liste.keys())
        Compte.liste[l[compte.ide]] = compte.solde
        print(compte.solde)
        
        #-----------------------
        #méthode de retrait d'argent sur le compte
        #-----------------------

    def retirer(compte, argent):
        """
        Fonction permettant de retirer un montant à la solde du compte
        :param (int) : nombre entier indiquant le montant à retirer
        :return : chaîne de caractères si le montant à retirer est plus grand que la solde
        :Effet de bord:
        :CU : La solde doit être supérieure au montant à retirer
        
        >>> lucas = Compte('GUGLIELMETTI' , 3000000)
        >>> lucas.retirer(100)
        >>> lucas.solde
        2999900
        
        """
        if argent <= compte.solde:
            compte.solde = compte.solde - argent
            l = list(Compte.liste.keys())
            Compte.liste[l[compte.ide]] = compte.solde
            print(compte.solde)
            
        #-----------------------
        #récupération du compte (méthode manager est plus pratique) 
        #-----------------------

    def get_compte(compte):
        """
        Fonction qui récupère la solde du compte
        :param () : 
        :return : solde du compte
        :Effet de bord:
        :CU : (None)
        
        >>> lucas = Compte('GUGLIELMETTI' , 3000000)
        >>> lucas.get_compte() 
        3000000
        
        """
        return compte.solde

    def set_compte(self, solde):
        """
        Fonction qui modifie la solde par une nouvelle valeur en paramètre
        :param (int) : nombre entier qui correspond à la nouvelle solde
        :return : châine de caractères si la valeur entrée n'est pas un entier
        :Effet de bord:
        :CU : La valeur en entrée doi être un entier
        
        >>> lucas = Compte('GUGLIELMETTI' , 3000000)
        >>> lucas.set_compte(100)
        >>> lucas.solde
        100
        
        >>> lucas = Compte('GUGLIELMETTI' , 3000000)
        >>> lucas.set_compte('toto')
        "Cette valeur n'est pas acceptable"
        
        """
        if solde == int:
            self.solde = solde
        else:
            print("Operation Impossible")
            
        #-----------------------
        #méthode de transfert d'argent sur le compte
        #-----------------------

    def transfert(self, destinataire, valeurs):
        """
        Fonction transfert qui prend une somme de la solde d'un compte pour la déposer dans un autre
        :param (int) : montant à transférer
        :param (str) : client à qui transférer l'argent
        :return : 
        :Effet de bord:
        :CU : (none)
        
        dict_clients['Tintin'].transfert(115, dict_clients['Milou'])
        >>> dict_clients['Tintin'].solde
        1905
        >>> dict_clients['Milou'].solde
        2135
        
        """
        if valeurs <= self.solde:
            self.retirer(valeurs)
            destinataire.deposer(valeurs)
        else:
            print("Operation Impossible")
            
        #-----------------------
        #méthode de dépot d'argent sur le compte
        #-----------------------

    def __del__(self):
        """
        Fonction permettant la supression d'un Objet de la classe Compte
        """
