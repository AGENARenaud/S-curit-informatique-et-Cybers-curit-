import random
import string
import csv
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

class Etudiant:
    def __init__(self, id_etudiant, nom, prenom, email, mot_de_passe=None):
        self.id_etudiant = id_etudiant
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.mot_de_passe = mot_de_passe or self.generer_mot_de_passe()

    def generer_mot_de_passe(self, longueur=12):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(caracteres) for _ in range(longueur))


class GestionnaireEtudiants:
    def __init__(self):
        self.etudiants = []

    def ajouter_etudiant(self, etudiant):
        self.etudiants.append(etudiant)

    def lister_etudiants(self):
        for e in self.etudiants:
            print(f"{e.id_etudiant} - {e.nom} {e.prenom} ({e.email}) | MDP: {e.mot_de_passe}")

    def sauvegarder_csv(self, nom_fichier):
        with open(nom_fichier, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Nom", "Prénom", "Email", "Mot de passe"])
            for e in self.etudiants:
                writer.writerow([e.id_etudiant, e.nom, e.prenom, e.email, e.mot_de_passe])

    def charger_csv(self, nom_fichier):
        self.etudiants = []
        with open(nom_fichier, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                etu = Etudiant(row["ID"], row["Nom"], row["Prénom"], row["Email"], row["Mot de passe"])
                self.etudiants.append(etu)

    def trouver_etudiant_par_email(self, email):
        for e in self.etudiants:
            if e.email == email:
                return e
        return None


def generer_pdf_etudiants(etudiants, nom_fichier):
    c = canvas.Canvas(nom_fichier, pagesize=A4)
    largeur, hauteur = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, hauteur - 50, "Liste des étudiants et mots de passe")

    y = hauteur - 100
    c.setFont("Helvetica", 12)

    for e in etudiants:
        ligne = f"ID: {e.id_etudiant} | Nom: {e.nom} {e.prenom} | Email: {e.email} | Mot de passe: {e.mot_de_passe}"
        c.drawString(50, y, ligne)
        y -= 20
        if y < 50:
            c.showPage()
            c.setFont("Helvetica", 12)
            y = hauteur - 50

    c.save()
    print(f"✅ PDF généré : {nom_fichier}")


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
    print("7. Export PDF")
    print("0. Quitter")


def main():
    gestionnaire = GestionnaireEtudiants()
    while True:
        afficher_menu()
        choix = input("Choix: ")

        if choix == "1":
            print("Mot de passe généré :", Etudiant(0, "", "", "").generer_mot_de_passe())

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

        elif choix == "7":
            fichier = input("Nom du fichier PDF: ")
            generer_pdf_etudiants(gestionnaire.etudiants, fichier)

        elif choix == "0":
            print("Au revoir !")
            break

        else:
            print("Choix invalide, réessayez.")


if __name__ == "__main__":
    main()
