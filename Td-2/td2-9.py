import csv, random, string, bcrypt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

class Etudiant:
    def __init__(self, id_etudiant, nom, prenom, email, mot_de_passe=None):
        self.id_etudiant = id_etudiant
        self.nom = nom
        self.prenom = prenom
        self.email = email
        if mot_de_passe:
            self.set_password(mot_de_passe)
        else:
            self.set_password(self.generer_mot_de_passe())

    def generer_mot_de_passe(self, longueur=12):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(caracteres) for _ in range(longueur))

    def set_password(self, mot_de_passe):
        salt = bcrypt.gensalt()
        self.hashed_password = bcrypt.hashpw(mot_de_passe.encode(), salt)
        self.mot_de_passe = mot_de_passe

    def verifier_password(self, mot_de_passe):
        return bcrypt.checkpw(mot_de_passe.encode(), self.hashed_password)


class GestionnaireEtudiants:
    def __init__(self):
        self.etudiants = []

    def ajouter_etudiant(self, etudiant):
        self.etudiants.append(etudiant)

    def lister_etudiants(self):
        for e in self.etudiants:
            print(f"{e.id_etudiant} - {e.nom} {e.prenom} ({e.email})")

    def sauvegarder_csv(self, nom_fichier):
        with open(nom_fichier, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Nom", "Prénom", "Email", "Mot de passe hashé"])
            for e in self.etudiants:
                writer.writerow([e.id_etudiant, e.nom, e.prenom, e.email, e.hashed_password.decode()])

    def charger_csv(self, nom_fichier):
        self.etudiants = []
        with open(nom_fichier, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                etu = Etudiant(row["ID"], row["Nom"], row["Prénom"], row["Email"], "temp")
                etu.hashed_password = row["Mot de passe hashé"].encode()
                self.etudiants.append(etu)

    def export_pdf(self, nom_fichier):
        c = canvas.Canvas(nom_fichier, pagesize=A4)
        largeur, hauteur = A4
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, hauteur - 50, "Liste des étudiants et mots de passe")
        y = hauteur - 100
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, "ID")
        c.drawString(100, y, "Nom")
        c.drawString(200, y, "Prénom")
        c.drawString(300, y, "Email")
        c.drawString(500, y, "Mot de passe")
        y -= 20
        c.setFont("Helvetica", 12)
        for e in self.etudiants:
            c.drawString(50, y, str(e.id_etudiant))
            c.drawString(100, y, e.nom)
            c.drawString(200, y, e.prenom)
            c.drawString(300, y, e.email)
            c.drawString(500, y, e.mot_de_passe)
            y -= 20
            if y < 50:
                c.showPage()
                c.setFont("Helvetica", 12)
                y = hauteur - 50
        c.save()
        print(f"✅ PDF généré : {nom_fichier}")

    def audit_securite(self):
        print("Audit de sécurité :")
        print(f"Nombre d'étudiants : {len(self.etudiants)}")
        emails = [e.email for e in self.etudiants]
        doublons = set([email for email in emails if emails.count(email) > 1])
        if doublons:
            print("⚠️ Emails en double :", doublons)
        else:
            print("✅ Aucun doublon d'email")
        for e in self.etudiants:
            if len(e.mot_de_passe) < 12:
                print(f"⚠️ Mot de passe faible pour {e.email}")

    def trouver_etudiant_par_email(self, email):
        for e in self.etudiants:
            if e.email == email:
                return e
        return None


def interface_admin():
    gestionnaire = GestionnaireEtudiants()
    while True:
        print("\n=== Menu Admin ===")
        print("1. Ajouter étudiant")
        print("2. Lister étudiants")
        print("3. Sauvegarder CSV")
        print("4. Charger CSV")
        print("5. Audit sécurité")
        print("6. Export PDF")
        print("7. Réinitialiser mot de passe")
        print("0. Quitter")
        choix = input("Choix: ")

        if choix == "1":
            id_etudiant = input("ID: ")
            nom = input("Nom: ")
            prenom = input("Prénom: ")
            email = input("Email: ")
            etu = Etudiant(id_etudiant, nom, prenom, email)
            gestionnaire.ajouter_etudiant(etu)
            print("✅ Étudiant ajouté.")
        elif choix == "2":
            gestionnaire.lister_etudiants()
        elif choix == "3":
            gestionnaire.sauvegarder_csv("etudiants.csv")
        elif choix == "4":
            gestionnaire.charger_csv("etudiants.csv")
        elif choix == "5":
            gestionnaire.audit_securite()
        elif choix == "6":
            gestionnaire.export_pdf("etudiants.pdf")
        elif choix == "7":
            email = input("Email de l'étudiant: ")
            etu = gestionnaire.trouver_etudiant_par_email(email)
            if etu:
                nouveau_mdp = etu.generer_mot_de_passe()
                etu.set_password(nouveau_mdp)
                print(f"✅ Mot de passe réinitialisé pour {email}: {nouveau_mdp}")
            else:
                print("❌ Étudiant introuvable.")
        elif choix == "0":
            break


if __name__ == "__main__":
    interface_admin()
