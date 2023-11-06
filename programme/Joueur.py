from Grille import Grille
from Case_normale import Case_normale
from Mine import Mine


import numpy as np
class Joueur:
    
    def __init__(self):
        
        self.etat_jeu=" pret a jouer"
        

    def demarrage(self):
        
        print("Demarrer")
        
        
    def GetEtat_jeu(self):
        return self.etat_jeu
        
    
    
    def choix_difficulte(self):
        
        print("Veuillez choisir une difficlte entre 1 2 et 3, ", self.nom) 
        
        difficulte=input()
        
        self.grille=Grille(difficulte)

        grilliade=self.grille
        
        grilliade.afficher_matrice()
        
        
    def choix_case_depart(self):
        
        grilliade=self.grille
        
        difficulte=grilliade.difficulte
        
        
        if difficulte==1:
            maxou=5
            
        if difficulte==2:
            maxou=10
            
        if difficulte==3:
            maxou=20
        
        print("Veuillez choisir une case de depart en ligne entre 1 et , ",maxou) 
        
        case_dep_x=input()
        
        print("Veuillez choisir une case de depart en colonne entre 1 et , ",maxou) 
        
        case_dep_y=input()
        
        self.case_depart=Case_normale("decouvert",int(case_dep_x)-1,int(case_dep_y)-1,"Case_normale")
        
        grilliade.matrice[int(case_dep_x)-1,int(case_dep_y)-1]="X"
        
        grilliade.afficher_matrice()
        
        grilliade.generation_matrice([int(case_dep_x)-1,int(case_dep_y)-1])
        
        
        self.etat_jeu='en jeu'
        

        
        
    def choix_click(self):
        
        grilliade=self.grille
        
        
        difficulte=grilliade.difficulte
        
        
        if difficulte==1:
            maxou=5
            
        if difficulte==2:
            maxou=10
            
        if difficulte==3:
            maxou=20
        
        print("Voulez vous mettre un drapeau( mettre 1) ou deminer (mettre 0)")
        action=input()
        
        if action=='O' or action==0:
            
            print("Quelle case voulez vous deminer en x entre 1 et ",maxou)
            
            x=input()
            
            
            print("Quelle case voulez vous deminer en y entre 1 et ",maxou)
            
            y=input()
            
            case=[x-1,y-1]
            
            
            
            
            if case in grilliade.liste_bombe:
                
                choisi=Mine('decouvert',x-1,y-1,'Mine')
                
                choisi.explose()
                
                grilliade.matrice[x-1,y-1]="B"
                
                self.etat_jeu='perdu'
                
                
            else:
                
                liste_bombe=grilliade.liste_bombe
                count_bombe=0
                for k in [-1,0,1]:
                    for l in [-1,0,1]:
                        try:
                            f=[x-1+k,y-1+l]
                            
                            if f in liste_bombe:
                                count_bombe+=1
                            
                        except:
                            pass
                
                grilliade.matrice[x-1,y-1]=count_bombe
                
                
        if action==1:
            
            print("Quelle case voulez vous mettre un drapeau en x entre 1 et ",maxou)
            
            x=input()
            
            
            print("Quelle case voulez vous mettre un drapeau en y entre 1 et ",maxou)
            
            y=input()
            
            case=[x-1,y-1]
            
            if grilliade.matrice[x-1,y-1]=='D':
                
                print('Voulez vous enlevez le drapeau ? Oui (marquez 0) Non (marquez 1)')
                
            
                act=input()
                
                if act==0 :
                    
                    grilliade.matrice[x-1,y-1]=0
                    
            
            
            grilliade.matrice[x-1,y-1]='D'
            
            
        grilliade.afficher_matrice()
        
        # grilliade.devoiler_matrice()
    
        r_etat=grilliade.fini_ou_non()
        
        if r_etat==True:
            self.etat_jeu='gagne'
            
        
    def fini(self):
        
        if self.etat_jeu=='perdu':
            print('vous avez perdu aaaaaaaaaaaaaaa')
            
            self.grille.devoiler_matrice()
            return True
        
        elif self.etat_jeu=='gagne':
            return True
        
        
        else :
            return False
    
    
    def jeu(self):
        
        
        print('Bienvenue dans le demineur,\n Quelle est votre nom ?')
        nom=raw_input()
        moi=self
        
        self.nom=nom
        self.etat_jeu='debut'
        
        moi.choix_difficulte()
        
        moi.choix_case_depart()
        
        moi.etat_jeu='joue'
        
        count=0
        
        while moi.fini()==False:
            moi.choix_click()
            
            if moi.fini()==True:
                break
        
            
        


# moi=Joueur("debut","Laura")
# moi.choix_difficulte()
# moi.choix_case_depart()
# moi.choix_click()
# moi.choix_click()


moi=Joueur()

moi.jeu()