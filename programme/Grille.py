import numpy as np
import random

class Grille:
 
    def __init__(self,difficulte):
        
        self.difficulte=difficulte
        
        if (self.difficulte==1):
            
                self.nombre_ligne=5
                self.nombre_colonne=5
                self.combien_bombe=5
                
        if (self.difficulte==2):
        
            self.nombre_ligne=10
            self.nombre_colonne=10
            self.combien_bombe=10
            
            
        if (self.difficulte==3):
                
            self.nombre_ligne=20
            self.nombre_colonne=20
            self.combien_bombe=20


        self.matrice=np.zeros((self.nombre_ligne,self.nombre_colonne),dtype=object)
        

        
    def generation_matrice(self,case_dep):
        
        liste_bombe=[]
        print(liste_bombe)
        
        for i in range(self.combien_bombe):
            
            casie=[random.randint(0, self.nombre_ligne-1),random.randint(0, self.nombre_ligne-1)]
            
            if casie!=case_dep:
            
                liste_bombe.append(casie)
            
            else:
                i=i-1
            
        self.liste_bombe=liste_bombe
            

            
        
    def afficher_matrice(self):
        
        custom_format = np.array2string(self.matrice, separator=', ', formatter={'all': lambda x: str(x)})

        print(custom_format)
        
        
    def devoiler_matrice(self):
        
        for case_bombe in self.liste_bombe:
            
            x,y=case_bombe
            
            self.matrice[x,y]="B"
        
        self.afficher_matrice()
        
        
    def fini_ou_non(self):
        grilliade=self
        plus_de_zero=np.isin(grilliade.matrice,0)
        a=grilliade.matrice
        ou_drapeau=np.where(a=='D')
        liste_drapeau= [list(x) for x in zip(ou_drapeau[0], ou_drapeau[1])]
        
        
        
        if liste_drapeau==grilliade.liste_bombe:
            
            print("Vous avez gagne")
            
            return True
            
        else:
            
            return False
    

        
        
