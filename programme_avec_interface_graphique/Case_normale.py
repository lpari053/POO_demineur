from Case import Case

class Case_normale(Case,object):
    def __init__(self, etat, ligne, colonne, type):
        super(Case_normale,self).__init__(etat, ligne, colonne, type)
        self.type="Case Normale"
        
        
    def demine(self):
        self.SetEtat('decouvert')
        
