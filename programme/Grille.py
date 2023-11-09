import numpy as np
import random
import sys

sys.setrecursionlimit(2000)
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
        for i in range(self.matrice.shape[0]):
            for j in range (self.matrice.shape[1]):
                self.matrice[i,j]='O'

        
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
        
        
    def nombre_bombe_autour(self,case):
        
        grilliade=self
        count=0
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if [case[0]+i,case[1]+j] in grilliade.liste_bombe:
                        count+=1
                
        return count
         
        
    def afficher_matrice(self):
        
        custom_format = np.array2string(self.matrice, separator=', ', formatter={'all': lambda x: str(x)})

        print(custom_format)
        
        
    def devoiler_matrice(self):
        
        
        rtyu=self.matrice
        
        for case_bombe in self.liste_bombe:
            
            x,y=case_bombe
            
            self.matrice[x,y]="B"
        
        self.afficher_matrice()
        
        self.matrice=rtyu
        

        
        
    def faire_zone(self,case):
        
        liste_bombe=self.liste_bombe
        self.matrice[case[0],case[1]]=self.nombre_bombe_autour(case)
        liste_zero=[]
        for i in [-1,1,0]:
            for j in [-1,0,1]:
                if [case[0]+i,case[1]+j] not in liste_bombe and case[0]+i<self.matrice.shape[0] and case[1]+j>=0 and case[0]+i>=0 and case[1]+j<self.matrice.shape[0]:
                    if(self.nombre_bombe_autour([case[0]+i,case[1]+j])==0):
                        self.matrice[case[0]+i,case[1]+j]='X'
                        liste_zero.append([case[0]+i,case[1]+j])
                    else:
                        if i!=j:
                            self.matrice[case[0]+i,case[1]+j]=self.nombre_bombe_autour([case[0]+i,case[1]+j])       
                            
                          
            

        
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
    

        
        
