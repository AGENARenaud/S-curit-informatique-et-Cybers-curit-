import random
import string

def generer_mdp_simple(longueur=8):
    lettres = string.ascii_letters  # contient 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    mdp = ''.join(random.choice(lettres) for _ in range(longueur))
    return mdp

# Exemple d'utilisation
if __name__ == "__main__":
    print(generer_mdp_simple())

 