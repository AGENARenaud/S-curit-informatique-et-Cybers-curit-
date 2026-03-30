import random
import string

def generer_mdp_chiffres(longueur=10):
    if longueur < 2:
        raise ValueError("Le mot de passe doit avoir au moins 2 caractères pour inclure 2 chiffres.")

    lettres = string.ascii_letters  # majuscules + minuscules
    chiffres = string.digits        # 0-9

    # Assurer au moins 2 chiffres
    mdp = [random.choice(chiffres) for _ in range(2)]

    # Compléter avec lettres ou chiffres pour atteindre la longueur
    mdp += [random.choice(lettres + chiffres) for _ in range(longueur - 2)]

    # Mélanger pour éviter que les 2 chiffres soient toujours au début
    random.shuffle(mdp)

    return ''.join(mdp)

# Exemple d'utilisation
if __name__ == "__main__":
    print(generer_mdp_chiffres())
