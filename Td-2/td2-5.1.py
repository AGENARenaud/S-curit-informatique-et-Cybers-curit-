import csv

class Etudiant:
    def __init__(self, id_etudiant, nom, prenom, email):
        self.id_etudiant = id_etudiant
        self.nom = nom
        self.prenom = prenom
        self.email = email

class GestionnaireEtudiants:
    def __init__(self):
        self.etudiants = []

    def ajouter_etudiant(self, etudiant):
        """Ajoute un étudiant à la liste."""
        self.etudiants.append(etudiant)

    def sauvegarder_csv(self, nom_fichier):
        """Sauvegarde la liste des étudiants dans un fichier CSV."""
        with open(nom_fichier, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            # En-têtes
            writer.writerow(["ID", "Nom", "Prénom", "Email"])
            # Données
            for e in self.etudiants:
                writer.writerow([e.id_etudiant, e.nom, e.prenom, e.email])

    def charger_csv(self, nom_fichier):
        """Charge les étudiants depuis un fichier CSV."""
        self.etudiants = []
        with open(nom_fichier, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                etu = Etudiant(
                    id_etudiant=row["ID"],
                    nom=row["Nom"],
                    prenom=row["Prénom"],
                    email=row["Email"]
                )
                self.etudiants.append(etu)

    def trouver_etudiant_par_email(self, email):
        """Recherche un étudiant par son email."""
        for e in self.etudiants:
            if e.email == email:
                return e
        return None


# Exemple d’utilisation
if __name__ == "__main__":
    gestion = GestionnaireEtudiants()

    # Création de deux étudiants
    etu1 = Etudiant(1, "Dupont", "Jean", "jean.dupont@example.com")
    etu2 = Etudiant(2, "Durand", "Marie", "marie.durand@example.com")

    # Ajout dans le gestionnaire
    gestion.ajouter_etudiant(etu1)
    gestion.ajouter_etudiant(etu2)

    # Sauvegarde dans un fichier CSV
    gestion.sauvegarder_csv("etudiants.csv")

    # Recharge depuis le fichier CSV
    gestion.charger_csv("etudiants.csv")

    # Recherche par email
    etu_trouve = gestion.trouver_etudiant_par_email("marie.durand@example.com")
    if etu_trouve:
        print("Étudiant trouvé :", etu_trouve.nom, etu_trouve.prenom)
