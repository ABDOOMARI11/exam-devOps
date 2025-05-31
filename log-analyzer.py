from collections import Counter

def analyser_log(fichier_log, fichier_rapport):
    compteur = Counter({"ERROR": 0, "WARNING": 0, "INFO": 0})
    
    with open(fichier_log, 'r') as f:
        lignes = f.readlines()
        for ligne in lignes:
            if "ERROR" in ligne:
                compteur["ERROR"] += 1
            elif "WARNING" in ligne:
                compteur["WARNING"] += 1
            elif "INFO" in ligne:
                compteur["INFO"] += 1

    with open(fichier_rapport, 'w') as f:
        for niveau, nb in compteur.items():
            f.write(f"{niveau}: {nb}\n")

    print("Analyse terminée. Rapport généré.")

if __name__ == "__main__":
    analyser_log("log.txt", "rapport.txt")
