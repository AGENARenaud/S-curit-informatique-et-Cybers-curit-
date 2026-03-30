import random
import string
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
        self.etudiants.append(etudiant)

    def lister_etudiants(self):
        for e in self.etudiants:
            print(f"{e.id_etudiant} - {e.nom} {e.prenom} ({e.email})")

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
                etu = Etudiant(row["ID"], row["Nom"], row["Prénom"], row["Email"])
                self.etudiants.append(etu)

    def trouver_etudiant_par_email(self, email):
        for e in self.etudiants:
            if e.email == email:
                return e
        return None


def generer_mot_de_passe(longueur=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longueur))


def audit_securite(gestionnaire):
    print("Audit de sécurité :")
    print(f"Nombre d'étudiants enregistrés : {len(gestionnaire.etudiants)}")
    emails = [e.email for e in gestionnaire.etudiants]
    doublons = set([email for email in emails if emails.count(email) > 1])
    if doublons:
        print("⚠️ Emails en double :", doublons)
    else:
        print("✅ Aucun doublon d'email détecté.")


def afficher_menu():
    print("\n=== Menu Principal ===")
    print("1. Générer mot de passe")
    print("2. Ajouter étudiant")
    print("3. Lister étudiants")
    print("4. Sauvegarder")
    print("5. Charger")
    print("6. Audit sécurité")
    print("0. Quitter")


def main():
    gestionnaire = GestionnaireEtudiants()
    while True:
        afficher_menu()
        choix = input("Choix: ")

        if choix == "1":
            print("Mot de passe généré :", generer_mot_de_passe())

        elif choix == "2":
            id_etudiant = input("ID: ")
            nom = input("Nom: ")
            prenom = input("Prénom: ")
            email = input("Email: ")
            etu = Etudiant(id_etudiant, nom, prenom, email)
            gestionnaire.ajouter_etudiant(etu)
            print("✅ Étudiant ajouté.")

        elif choix == "3":
            gestionnaire.lister_etudiants()

        elif choix == "4":
            fichier = input("Nom du fichier CSV: ")
            gestionnaire.sauvegarder_csv(fichier)
            print("✅ Sauvegarde effectuée.")

        elif choix == "5":
            fichier = input("Nom du fichier CSV: ")
            gestionnaire.charger_csv(fichier)
            print("✅ Chargement effectué.")

        elif choix == "6":
            audit_securite(gestionnaire)

        elif choix == "0":
            print("Au revoir !")
            break

        else:
            print("Choix invalide, réessayez.")


if __name__ == "__main__":
    main()
