class Case:
    def __init__(self, etat, ligne, colonne, type):
        self.etat = etat
        self.ligne= ligne
        self.colonne= colonne
        self.type= type
        
    
    @property
    def afficher_attribut(self):
        print('Etat' ,self.etat)
        print("Ligne",self.ligne)
        print("Colonne", self.colonne)
        print("type",self.type)
        

    def GetEtat(self):
        return self.etat
    
    def SetEtat(self,valeur):
        print("Avant ",self.etat)
        self.etat=valeur
        print("Apres ",self.etat)
        
    
    
# mon_objet=Case("non decouvert",14,19,"Mine")
# mon_objet.afficher_attribut()

# mon_objet.SetEtat(False)


