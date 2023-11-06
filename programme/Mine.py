from Case import Case

class Mine(Case,object):
    def __init__(self, etat, ligne, colonne, type):
        super(Mine,self).__init__(etat, ligne, colonne, type)
        self.type="Mine"
         
        
    def explose(self):
        
        self.SetEtat("explose")
        
        # print('VOUS AVEZ PERDU AHAHAHA VOUS ETES NUL')
        
    
# mon_mine=Mine(True,14,19,"Mine")
# mon_mine.explose()