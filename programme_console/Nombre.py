from Case import Case

class Nombre(Case):
    def __init__(self, etat, ligne, colonne, type, nombre_bombe):
        Case.__init__(self,etat, ligne, colonne, type)
        self.type="Nombre"
        self.nombre_bombe=nombre_bombe
                 
    
    def GetNombre_bombe(self):
        
        print('le nombre de bombe de cette case est',self.nombre_bombe)
        
        return self.nombre_bombe

 
    def demine_chiffre(self):
        self.SetEtat('decouvert')
    

mon_nombre=Nombre(True,12,6,"Nombre",3)
mon_nombre.GetNombre_bombe()
mon_nombre.demine_chiffre()