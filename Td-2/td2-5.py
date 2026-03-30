import csv

class GestionnaireEtudiants:
    def __init__(self):
        self.etudiants = []

    def ajouter_etudiant(self, etudiant):
        self.etudiants.append(etudiant)

    def sauvegarder_csv(self, nom_fichier):
        with open(nom_fichier, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Nom", "Prénom", "Email"])
            for e in self.etudiants:
                writer.writerow([e.id_etudiant, e.nom, e.prenom, e.email])

    def charger_csv(self, nom_fichier):
        self.etudiants = []
        with open(nom_fichier, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                etu = Etudiant(
                    id_etudiant=row["ID"],
                    nom=row["Nom"],
                    prenom=row["Prénom"],
                    email=row["Email"],
                    mot_de_passe="temp"
                )
                self.etudiants.append(etu)

    def trouver_etudiant_par_email(self, email):
        for e in self.etudiants:
            if e.email == email:
                return e
        return None


# Exemple d’utilisation
if __name__ == "__main__":
    # On suppose que la classe Etudiant est définie ailleurs
    etu1 = Etudiant(1, "Dupont", "Jean", "jean.dupont@example.com", "secret123")
    etu2 = Etudiant(2, "Durand", "Marie", "marie.durand@example.com", "mdp456")

    gestion = GestionnaireEtudiants()
    gestion.ajouter_etudiant(etu1)
    gestion.ajouter_etudiant(etu2)

    gestion.sauvegarder_csv("etudiants.csv")

    gestion.charger_csv("etudiants.csv")
    etu_trouve = gestion.trouver_etudiant_par_email("marie.durand@example.com")
    if etu_trouve:
        print("Étudiant trouvé :", etu_trouve.nom, etu_trouve.prenom)
