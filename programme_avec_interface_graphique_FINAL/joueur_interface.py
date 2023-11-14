"""""
CLASSE JOUEUR_INTERFACE

Cette classe est la classe qui defini le joueur et ses actions au sein du jeu.



Attribut :

        +etat_jeu
        +grille


"""""


from Grille import Grille
import numpy as np


class Joueur:
    #Initilaisation du joueur 

    def __init__(self):
        
        self.etat_jeu=False
                
        
    def GetEtat_jeu(self):
        return self.etat_jeu
        
    
    #Fonction qui initilise l'attribut de difficulte selon choix appelle dans interface
    def choix_difficulte(self,difficulte):
        
        if int(difficulte) in [1,2,3]:
        
            self.grille=Grille(int(difficulte))
    
        
    #Fonction qui prend les coordonne de case depart chosi dans l'interface pour generer la grille  
        
    def choix_case_depart(self,case_dep_x,case_dep_y):
        

        grilliade=self.grille
        
       
        grilliade.matrice[int(case_dep_x),int(case_dep_y)]="X"
        
        #Nusgenerons la matrice depuis la class Grille grace au coordonnes de case depart
        grilliade.generation_matrice([int(case_dep_x),int(case_dep_y)])
        
        #Nous adaptons la matrice autoiur de la case depart avec les numeros
        grilliade.faire_zone([int(case_dep_x),int(case_dep_y)])

        #Mise a jour etat de jeu 
        self.etat_jeu='en jeu'

    
    #Fonction de mise en drapeau selon choix dans l'interface par le joueur 
    def mettre_drapeau(self,x,y):

        grilliade=self.grille
        #Actualisation de la matrice pour mettre drapeau ou l'enlever si deja drapeau sur la case
        if grilliade.matrice[x,y]=='D':
            
            grilliade.matrice[x,y]='O'

        else:

            grilliade.matrice[x,y]='D'

        #test si ou â gagne ou non 
        if len(np.where(grilliade.matrice=='D'))==len(grilliade.liste_bombe):
            r_etat=grilliade.fini_ou_non()
            if r_etat==True:
                self.etat_jeu='gagne'
                
            else:
                self.etat_jeu='perdu'

        print('Vous avez mis un drapeau ')

    #Fonction demine selon choix dans l'interface par le joueur 
    def mettre_bombe(self,x,y):

        grilliade=self.grille

        case=[x,y]
            
        if case in grilliade.liste_bombe:
            
            #mise a jour de la grille
            grilliade.matrice[x,y]="B"
            
            self.etat_jeu='perdu'  
   
        else:
            
            grilliade.matrice[x,y]=grilliade.nombre_bombe_autour([x,y])


        if len(np.where(grilliade.matrice=='D'))==len(grilliade.liste_bombe):
            r_etat=grilliade.fini_ou_non()
            if r_etat==True:
                self.etat_jeu='gagne'
                
            else:
                self.etat_jeu='perdu'
                print('les drapeau sont pose au mauvaise endroit')


        grilliade.nouv_zone([x,y])

        print("Vous avez deminez")
      

            
        #Fonction qui indique si le jeu est termine ou non 
    def fini(self):
        
        if self.etat_jeu=='perdu':
            return True
        
        elif self.etat_jeu=='gagne':
            return True
        
        elif self.etat_jeu=='abandon':
            print('vous avez abandonne')
            self.grille.devoiler_matrice()
            return True
        
        else :
            return False
    
    
