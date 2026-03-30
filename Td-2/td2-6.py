import re

def evaluer_force_mot_de_passe(mot_de_passe: str) -> int:
    score = 0

    # 1. Longueur minimale
    if len(mot_de_passe) >= 12:
        score += 25
    else:
        return 0  # trop court → mot de passe faible

    # 2. Présence de majuscules, minuscules, chiffres, caractères spéciaux
    if re.search(r"[A-Z]", mot_de_passe):
        score += 15
    if re.search(r"[a-z]", mot_de_passe):
        score += 15
    if re.search(r"[0-9]", mot_de_passe):
        score += 15
    if re.search(r"[^A-Za-z0-9]", mot_de_passe):
        score += 15

    # 3. Pas de mots du dictionnaire (exemple simple : liste réduite)
    dictionnaire = ["password", "motdepasse", "bonjour", "admin", "qwerty"]
    if any(mot in mot_de_passe.lower() for mot in dictionnaire):
        score -= 30

    # 4. Pas de séquences simples
    sequences = ["123", "abc", "abcd", "000", "111"]
    if any(seq in mot_de_passe.lower() for seq in sequences):
        score -= 20

    # Normalisation du score entre 0 et 100
    score = max(0, min(100, score))
    return score


# Exemple d’utilisation
if __name__ == "__main__":
    tests = [
        "password123",
        "Bonjour123!",
        "Tr0ub4dor&3",
        "A1b2C3d4E5f6!",
        "abc123456789"
    ]
    for mdp in tests:
        print(mdp, "→ score:", evaluer_force_mot_de_passe(mdp))
