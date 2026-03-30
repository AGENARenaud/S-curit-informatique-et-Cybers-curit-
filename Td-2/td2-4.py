import hashlib
import os

class Etudiant:
    def __init__(self, id_etudiant, nom, prenom, email, mot_de_passe):
        self.id_etudiant = id_etudiant
        self.nom = nom
        self.prenom = prenom
        self.email = email
        # On stocke le mot de passe sous forme hashée avec un sel
        self.salt = os.urandom(16)
        self.mot_de_passe_hash = self._hash_mot_de_passe(mot_de_passe)

    def _hash_mot_de_passe(self, mot_de_passe: str) -> str:
        """Hash du mot de passe avec SHA-256 et un sel."""
        h = hashlib.sha256()
        h.update(self.salt + mot_de_passe.encode('utf-8'))
        return h.hexdigest()

    def verifier_mot_de_passe(self, mot_de_passe_tente: str) -> bool:
        """Vérifie si le mot de passe fourni correspond au hash stocké."""
        h = hashlib.sha256()
        h.update(self.salt + mot_de_passe_tente.encode('utf-8'))
        return h.hexdigest() == self.mot_de_passe_hash

    def changer_mot_de_passe(self, ancien_mdp: str, nouveau_mdp: str) -> bool:
        """Change le mot de passe si l'ancien est correct."""
        if self.verifier_mot_de_passe(ancien_mdp):
            self.salt = os.urandom(16)  # Nouveau sel pour plus de sécurité
            self.mot_de_passe_hash = self._hash_mot_de_passe(nouveau_mdp)
            return True
        return False


# Exemple d'utilisation
if __name__ == "__main__":
    etu = Etudiant(1, "Dupont", "Jean", "jean.dupont@example.com", "monSecret123")
    print("Vérification correcte :", etu.verifier_mot_de_passe("monSecret123"))
    print("Vérification incorrecte :", etu.verifier_mot_de_passe("mauvaisMDP"))

    # Changement de mot de passe
    if etu.changer_mot_de_passe("monSecret123", "nouveauMDP456"):
        print("Mot de passe changé avec succès !")
        print("Vérification nouveau :", etu.verifier_mot_de_passe("nouveauMDP456"))
