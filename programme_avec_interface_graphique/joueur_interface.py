from Grille import Grille
from Case_normale import Case_normale
from Mine import Mine


import numpy as np

import sys

class Joueur:
    
    def __init__(self):
        
        self.etat_jeu="pret a jouer"
        

    def demarrage(self):
        
        print("Demarrer")
        
        
    def GetEtat_jeu(self):
        return self.etat_jeu
        
    
    
    def choix_difficulte(self,difficulte):
        
        if int(difficulte) in [1,2,3]:
        
            self.grille=Grille(int(difficulte))
    
            
        print('difficulte choisi')
        
        
    def choix_case_depart(self,case_dep_x,case_dep_y):
        
        grilliade=self.grille
        
        self.case_depart=Case_normale("decouvert",int(case_dep_x),int(case_dep_y),"Case_normale")
       
        grilliade.matrice[int(case_dep_x),int(case_dep_y)]="X"
        
        
        grilliade.generation_matrice([int(case_dep_x),int(case_dep_y)])
        
        grilliade.faire_zone([int(case_dep_x),int(case_dep_y)])

        self.etat_jeu='en jeu'

        print('case_depart_choisi')
        
    def mettre_drapeau(self,x,y):

        grilliade=self.grille
        
        if grilliade.matrice[x,y]=='D':
            
            grilliade.matrice[x,y]=0

        grilliade.matrice[x,y]='D'

        if len(np.where(grilliade.matrice=='D'))==len(grilliade.liste_bombe):
            r_etat=grilliade.fini_ou_non()
        
            if r_etat==True:
                self.etat_jeu='gagne'
                
            else:
                self.etat_jeu='perdu'

        print('drapeau')


    def mettre_bombe(self,x,y):

        grilliade=self.grille

        case=[x,y]
            
        if case in grilliade.liste_bombe:
            
            choisi=Mine('decouvert',x,y,'Mine')
            
            choisi.explose()
            
            grilliade.matrice[x,y]="B"
            
            self.etat_jeu='perdu'
   
        else:
            
            liste_bombe=grilliade.liste_bombe
            count_bombe=0
            for k in [-1,0,1]:
                for l in [-1,0,1]:
                    try:
                        f=[x+k,y+l]
                        
                        if f in liste_bombe:
                            count_bombe+=1
                        
                    except:
                        pass
            
            grilliade.matrice[x,y]=count_bombe


        if len(np.where(grilliade.matrice=='D'))==len(grilliade.liste_bombe):
            r_etat=grilliade.fini_ou_non()
        
            if r_etat==True:
                self.etat_jeu='gagne'
                
            else:
                self.etat_jeu='perdu'

        print("bombe")
      


    def choix_click(self):
        
        grilliade=self.grille
        
        
        difficulte=grilliade.difficulte
        
        
        if difficulte==1:
            maxou=5
            
        if difficulte==2:
            maxou=10
            
        if difficulte==3:
            maxou=20
        
        print("Voulez vous mettre un drapeau( mettre 1) ou deminer (mettre 0) ou arreter (mettre 3)")
        action=input()
        
        if action==3 or action=='3':
            self.etat_jeu='abandon'
        
  
        if action=='O' or action==0 or action=='0':
            
            print("Quelle case voulez vous deminer en x entre 1 et ",maxou)
            
            x=int(input())
            
            
            print("Quelle case voulez vous deminer en y entre 1 et ",maxou)
            
            y=int(input())
            
            case=[x,y]
            
            if case in grilliade.liste_bombe:
                
                choisi=Mine('decouvert',x,y,'Mine')
                
                choisi.explose()
                
                grilliade.matrice[x,y]="B"
                
                self.etat_jeu='perdu'
                
                
            else:
                
                liste_bombe=grilliade.liste_bombe
                count_bombe=0
                for k in [-1,0,1]:
                    for l in [-1,0,1]:
                        try:
                            f=[x+k,y+l]
                            
                            if f in liste_bombe:
                                count_bombe+=1
                            
                        except:
                            pass
                
                grilliade.matrice[x,y]=count_bombe
                
                
        elif action==1 or action=='1':
            
            print("Quelle case voulez vous mettre un drapeau en x entre 1 et ",maxou)
            
            x=int(input())
            
            
            print("Quelle case voulez vous mettre un drapeau en y entre 1 et ",maxou)
            
            y=int(input())
            
            case=[x,y]
            
            if grilliade.matrice[x,y]=='D':
                
                print('Voulez vous enlevez le drapeau ? Oui (marquez 0) Non (marquez 1)')
                
            
                act=input()
                
                if act==0 :
                    
                    grilliade.matrice[x,y]=0
                    
            
            
            grilliade.matrice[x,y]='D'
       
        if len(np.where(grilliade.matrice=='D'))==len(grilliade.liste_bombe):
            r_etat=grilliade.fini_ou_non()
        
            if r_etat==True:
                self.etat_jeu='gagne'
                
            else:
                self.etat_jeu='perdu'
            
        
    def fini(self):
        
        if self.etat_jeu=='perdu':
            print('vous avez perdu ahahahaha')
            
            self.grille.devoiler_matrice()
            return True
        
        elif self.etat_jeu=='gagne':
            return True
        
        elif self.etat_jeu=='abandon':
            print('vous avez abandonne')
            self.grille.devoiler_matrice()
            return True
        
        else :
            return False
    
    
    # def jeu(self):
        
        
    #     print('Bienvenue dans le demineur,\n Quelle est votre nom ?')
    #     nom=input()
    #     moi=self
        
    #     self.nom=nom
    #     self.etat_jeu='debut'
        
    #     moi.choix_difficulte()
        
    #     moi.choix_case_depart()
        
    #     moi.etat_jeu='joue'
        
    #     count=0
        
    #     while moi.fini()==False:
    #         moi.choix_click()
            
    #         if moi.fini()==True:
    #             break
        
            
        


# moi=Joueur()

# moi.jeu()