def personal():
    for i in range(1):
        prenom=input("saisir le prenom:")
        nom=input("saisir le nom:")
        age= input("saisir age:")
        classe=input("classe:")
        fichier=open("info.txt","a")
        fichier.writelines(f"{prenom}:{nom}:{age}ans:{classe}Année\n")
        fichier.close

def appel():
    fichier=open("info.txt","r")
    homme=fichier.readlines()
    for liste in homme:
        liste=liste.split(":")
        print(f"Nom et Prenom de l'eleve est:{liste [0]}\n{liste [1]}\nSon age est: {liste [2]}\nclasse:{liste[3]}")
        #print(f"{liste}" )

    fichier.close


personal()    
appel()

