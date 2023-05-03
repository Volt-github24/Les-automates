"""
Bout de code pour la construction d'un automate

"""

# classe automate
class Automate():

	def __init__(self):
		
		self.alphabet = []
		self.etats = []
		self.etats_initiaux = []
		self.etats_finaux = []
		self.transitions = {}

	def f_transitions(self, etats:list, symbole:str) -> list:

		for etat in etats:
			print(etat)

	def est_accessible(self)->bool:
		pass

	def est_coaccessible(self)->bool:
		pass

	def est_emonde(self)->bool:
		pass

	def est_epsilone_non_deterministe(self)->bool:
		pass

	def est_non_deterministe(self)->bool:
		pass

	def est_deterministe(self)->bool:
		pass
	
	def est_complet(self)->bool:
		pass

	def nature(self)->str:
		
		nature = []
		
		if self.est_accessible:
			nature.append("accessible")
		
		if self.est_coaccessible:
			nature.append("co-accessible")

		if self.est_emonde:
			nature.append("emonde")
		
		if self.est_epsilone_non_deterministe:
			nature.append("e-AFN")

		if self.est_non_deterministe:
			nature.append("AFN")

		if self.est_deterministe:
			nature.append("AFD")

		if self.est_complet:
			nature.append("Complet")

		return "Cet automate est : " + ", ".join(nature)


	def create(self, alphabet:list, etats:list, etats_initiaux:list, 
		etats_finaux:list, transitions:dict):

		self.alphabet = alphabet
		self.etats = etats
		self.etats_initiaux = etats_initiaux
		self.etats_finaux = etats_finaux
		self.transitions = transitions

### TESTS

# j'instancie la classe et je cree un automate
A = Automate()

transitions = {(0,'b'):0, 
				(0,'a'):1,
				(1,'b'):1,
				(1,'a'):2,
				(2,'b'):2,
				(2,'b'):3,
				(2,'0'):0,
				(3,'b'):3,
				(3,'a'):0,}

A.create(['a','b'], [0,1,2,3], [0], [3], transitions)

print(A.nature())

