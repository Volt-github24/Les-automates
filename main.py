"""
Ce qu'il faut savoir de la calsse Automate() :

1. L'alphabet est une LISTE de tous les symboles du langage reconnu
2. L'ensemble des etats, Q, c'est egalement une liste des differents etats de l'automate, donc une LISTE DE LISTE.
3. L'etat initial, est une LISTE DE LISTE, (d'au moins une liste), si la liste n'a qu'une seule liste alors, 
   alors cet automate n'a qu'un seul etat initial, maintenant si cette une seule liste n'a qu'un seul element, alors l'etat initial
   est un sous ensemble d'un seul etat..
4. Pareil pour l'etat final.
5. Un etat qi maintenant est une simple LISTE d'un ou plusieurs elements, si cette liste a un seul element alors cet etat est un 
   sous ensemble d'un seul etat
6. La fonction de transition prend donc en entree, une liste d'elements, un str ( le symbole ) et retourne une liste de liste, j'explique :
   un etat est materialisé par une liste d'elements, ca peut etre plus d'un element(dans le cas d'un determinisé), 
   le symbole est tout simplement un caractere de l'alphabet à lire. La liste de le liste retournee est tout simplement la liste
   des differents etats ou la transition peut nous emmener, la premiere liste est pour contenir ces differents etats, la deuxieme
   est pour chacun des etats ou ca nous mene
7. Le dictionnaire transactions est un dictionnaire materialisant les transitions de l'automate, un element du dictionnaire est 
   tel que la cle est un tuple contenant deux elements, le premiere est un tuple, qui a tous les elements de l'etat et l'autre
   element est le symbole lu, maintenant la valeur est est une liste de liste donc la liste des etats aux quels ca mene

"""

# classe automate
class Automate():

	
	# Constructeur de la classe
	def __init__(self):
		
		self.alphabet = []
		self.etats = []
		self.etats_initiaux = []
		self.etats_finaux = []
		self.transitions = {}

	
	# fonction de transition
	def f_transitions(self, etat:list, symbole:str) -> list:

		for trans in self.transitions: # je parcours les transitions
			if list(trans[0]) == etat and trans[1] == symbole: # si je tombe sur un transition telle que l'etat est celui que je passe en entree, et le symbole ce lui que je passe en entree
				return self.transitions[trans] # alors je prends l'etat au quel ca mene et je le retourne
		return []

	
	# fonction permettant de savoir si un automate est accessible
	def est_accessible(self)->bool:

		for q in self.etats:
			print(q)
			states = self.etats_initiaux
			print(states, "--------------------------------------")
			for state in states:
				for s in self.alphabet:
					print(states, "deuxieme tour")
					if len(states) != 0:
						etat = self.f_transitions(state,s)
						if q in etat:
							break
						else:
							for qi in etat:
								if qi not in self.etats_finaux:
									states.append(qi)
					else:
						return False
				states.pop(0)
		return True	

	
	# fonction permettant de savoir si un automate est co-accessible
	def est_coaccessible(self)->bool:
		pass

	
	# fonction permettant de savoir si un automate est emondé	
	def est_emonde(self)->bool:
		
		if self.est_accessible() and self.est_coaccessible:
			return True
		return False


	# fonction permettant de savoir si un automate contient des epsilonnes-transitions
	def est_epsilone_non_deterministe(self)->bool:
		
		for trans in self.transitions.keys():
			if trans[1] == 'e' :
				return True
		return False

	
	# fonction permettant de savoir si un automate est non-deterministe
	def est_non_deterministe(self)->bool:
		
		for trans in self.transitions.values():
			if len(trans) > 1:
				return True
		
		if len(self.etats_initiaux) > 1:
			return True

		return False

	
	# fonction permettant de savoir si un automate est deterministe
	def est_deterministe(self)->bool:
		
		for trans in self.transitions.values():
			if len(trans) > 1:
				return False
	
		if len(self.etats_initiaux) > 1:
			return False

		return True


	# fonction permettant de savoir si un automate est complet
	def est_complet(self)->bool:
		
		for etat in self.etats:
			for char in self.alphabet:
				if (tuple(etat),char) not in self.transitions.keys():
					return False
		return True


	# fonction qui retourne toutes les natures d'un automate
	def nature(self)->str:
		
		nature = []
		"""
		if self.est_accessible():
			nature.append("accessible")
		
		if self.est_coaccessible():
			nature.append("co-accessible")

		if self.est_emonde():
			nature.append("émondé")"""
		
		if self.est_epsilone_non_deterministe():
			nature.append("e-AFN")

		if self.est_non_deterministe():
			nature.append("AFN")

		if self.est_deterministe():
			nature.append("AFD")

		if self.est_complet():
			nature.append("Complet")

		return "Cet automate est : " + ", ".join(nature)


	# fonction permettant de creer un automate
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

# exemple de ce à quoi doit ressembler le dictionnaire des transitions
A_transitions = {
			((0,),'b'):[[0]], 
			((0,),'a'):[[1]],
			((1,),'b'):[[1]],
			((1,),'a'):[[2]],
			#((2,),'b'):[[2]],
			((2,),'b'):[[2],[3]],
			((2,),'a'):[[0]],
			((3,),'b'):[[3]],
			((3,),'a'):[[0]]
		}

A.create(alphabet=['a','b'], etats=[[0], [1], [2], [3]], etats_initiaux=[[0]], etats_finaux=[[3]], transitions = A_transitions)

# j'instancie la classe et je cree un automate B (la c'est comme un automate qu'on a minimisé)
B = Automate()

# exemple de ce à quoi doit ressembler le dictionnaire des transitions
B_transitions = {
			(('1-6',),'b'):[['1-6']],
			(('1-6',),'a'):[['2-7']], 
			(('2-7',),'b'):[['2-7']],
			(('2-7',),'a'):[['3-8']],
			(('3-8',),'b'):[['3-8']],
			(('3-8',),'a'):[['4-9']],
			(('4-9',),'b'):[['4-9']],
			(('4-9',),'a'):[['0-5']],
			(('0-5',),'b'):[['0-5']]
		}

B.create(alphabet=['a','b'], etats=[['1-6'], ['2-7'], ['3-8'], ['4-9'], ['0-5']], etats_initiaux=[['1-6']], etats_finaux=[['0-5']], transitions = B_transitions)



### DEFINITIONS DES FONCTIONS SUR LES AUTOMATES

# 1. determinisation d'un automate
def determinisation(A:Automate) -> Automate:

	if A.est_deterministe():
		return A

	else:
		
		tous_les_etats_du_determinise = []	
		toutes_les_transitions_du_determinise = {}	

		etat_initial_du_determinise = []
		for etat in A.etats_initiaux:
			for num_etat in etat:
				etat_initial_du_determinise.append(num_etat)
		
		tous_les_etats_du_determinise.append(etat_initial_du_determinise)
		etat_initial_du_determinise = [etat_initial_du_determinise]
		
		for etat in tous_les_etats_du_determinise:
			
			for character in A.alphabet:
				nouvel_etat_pour_charactere = []
				
				for numero_etat in etat:
					
					liste_des_etats = A.f_transitions([numero_etat], character)
					
					for e in liste_des_etats: 
						for num_etat in e:
							if num_etat not in nouvel_etat_pour_charactere: nouvel_etat_pour_charactere.append(num_etat)
				if nouvel_etat_pour_charactere not in tous_les_etats_du_determinise:
					if len(nouvel_etat_pour_charactere) != 0:
						tous_les_etats_du_determinise.append(nouvel_etat_pour_charactere)

				if len(nouvel_etat_pour_charactere) != 0:	
					toutes_les_transitions_du_determinise[(tuple(etat),character)]=[nouvel_etat_pour_charactere]
			

		etats_finaux_du_determinise = []
		for etat in tous_les_etats_du_determinise:
			for etat_final in A.etats_finaux: # ici aussi
				for num_etat in etat_final:
					if num_etat in etat:
						if etat not in etats_finaux_du_determinise: etats_finaux_du_determinise.append(etat)
		etats_finaux_du_determinise = [etats_finaux_du_determinise]
			
		A_prime = Automate()
		A_prime.create(alphabet=A.alphabet, etats=tous_les_etats_du_determinise, etats_initiaux=etat_initial_du_determinise, 
		etats_finaux=etats_finaux_du_determinise, transitions = toutes_les_transitions_du_determinise)
		

		return A_prime


# 2. completion d'un automate
def completion(A:Automate) -> Automate:

	if A.est_complet():
		return A
	
	else:
		A_prime = Automate()
		A_prime = A
		A_prime.etats.append(['puit'])
		for etat in A_prime.etats:
			for char in A_prime.alphabet:
				if (tuple(etat),char) not in A_prime.transitions.keys():
					A_prime.transitions[(tuple(etat),char)]=[['puit']]

		for char in A_prime.alphabet:
			A_prime.transitions[(tuple(['puit']),char)]=[['puit']]
		return A_prime


# 3. non-determinisation d'un automate
def non_determinisation(A:Automate) -> Automate:

	if A.est_non_deterministe():
		return A
	
	else:
		A_prime = Automate()
		A_prime = A
		A_prime.etats.append(['N'])
		etat_cible = A_prime.etats_initiaux[0]
		
		dictionnaire_transitions_copie = dict(A_prime.transitions)
		
		for trans_etat_et_symbole, etat in dictionnaire_transitions_copie.items():

			print(dictionnaire_transitions_copie)

			if trans_etat_et_symbole[0] == tuple(etat_cible) :
				A_prime.transitions[(tuple(['N']),trans_etat_et_symbole[1])] = etat
				
			
			if etat == [etat_cible]:
				A_prime.transitions[tuple(trans_etat_et_symbole[0]),trans_etat_et_symbole[1]].append(['N'])

		return A_prime


# 4. reconnaissance d'un mot par un automate
def reconnaissance(A:Automate, mot:str) -> bool:

	if A.est_deterministe():
		
		etat = A.etats_initiaux[0]
		for char in mot:
			if char not in A.alphabet:
				return False
			etat = A.f_transitions(etat,char)[0]
			if len(etat) == 0 or etat == ['puit']:
				return False
		if etat in A.etats_finaux:
			return True
		return False
	
	else:
		pile = []
		for chaque_etat_initial in A.etats_initiaux:
			pile.append((chaque_etat_initial, 0))
		
		while len(pile) > 0:
			etat_actuel, indice_actuel_du_mot = pile.pop()
			if indice_actuel_du_mot == len(mot):
				if etat_actuel in A.etats_finaux:
					return True
			else:
				etats_possibles_pour_cette_transition = A.f_transitions(etat_actuel, mot[indice_actuel_du_mot])
				for chaque_etat in etats_possibles_pour_cette_transition:
					if len(chaque_etat) != 0 and chaque_etat != ['puit']:
						pile.append((chaque_etat,indice_actuel_du_mot+1))
		
		return False			




print(A.nature())
print(reconnaissance(A,'bbbbaaabaab'))

