from Compte import Compte


class Manager:
    def __init__(self) -> None:
        self.comptes = []
        self.ide = 0

    def recuperer_compte(self, nom):
        for compte in self.comptes:
            if compte.nom == nom:
                return compte

    def ajouter_compte(self, nom, montant):
        self.comptes.append(Compte(self.ide, nom, montant))
        self.ide += 1
        
    def comptes_non_actif(self):
        l = []
        for compte in self.comptes:
            if compte.etat == 0:
                l.append(compte)
                
    def comptes_actifs(self):
        l = []
        for compte in self.comptes:
            if compte.etat == 1:
                l.append(compte)
                
manager = Manager()
