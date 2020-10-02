def personal():
    for i in range(1):
        prenom=input("saisir le prenom:")
        nom=input("saisir le nom:")
        classe= input("saisir sa classe:")
        date_naissance=input("saisir la date de naissance:")
        fichier=open("info.txt","a")
        fichier.writelines(f"{prenom}:{nom}:{classe}Année:{date_naissance}\n")
        fichier.close

def appel():
    fichier=open("info.txt","r")
    homme=fichier.readlines()
    for liste in homme:
        liste=liste.split(":")
        prenom= liste[0]
        nom= liste[1]
        age= liste[2]
        date_naissance= liste[3]
        date_naissance=date_naissance.split("/")
        print(f"Nom de l'eleve est: {nom}\nMois de naissance est: {date_naissance[1]} mois")
    fichier.close


personal()    
appel()

