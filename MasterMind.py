import string
import secrets

digits = string.digits


def jeu():
    global pwd
    global longeur
    global nbr_test
    print("Dans cette version du jeu vous avez tours illimité")
    print("Les règles sont celle du mastermind")
    print("1-Facile (6561 possibilitées)")
    print("2-Medium (531441 possibilitées)")
    print("3-Pro (43046721 possibilitées)")
    print("4-Impossible (31381059609 possibilitées)")

    choix_difficulté = int(input("Saisir la difficulté: "))
    pwd = ''

    if choix_difficulté==1:
        for _ in range(4):
            pwd += ''.join(secrets.choice(digits))
        longeur= 4
        nbr_test = 7

    elif choix_difficulté==2:
        for _ in range(6):
            pwd += ''.join(secrets.choice(digits))
        longeur = 6
        nbr_test = 12

    elif choix_difficulté==3:
        for _ in range(8):
            pwd += ''.join(secrets.choice(digits))
        longeur = 8
        nbr_test = 17

    elif choix_difficulté==4:
        for _ in range(11):
            pwd += ''.join(secrets.choice(digits))
        longeur = 11
        nbr_test = 30
   
    else:
        print("Il faut soit 1, 2, 3, 4")
        print("\n \n \n \n")
        return jeu()

    
def prop(nbr_test):

    print(pwd)
    proposition = input("Proposez votre solution: ")
    proposition = list(proposition)
    compteur_egalité=0
    compteur_sim = 0
    print("------------------------------")

    if  nbr_test == 0:
        print("Vous n'avez plus de tentative le code était", pwd)
    
    else:
        for _ in range(nbr_test):
            print("Il vous reste", nbr_test , "tentative(s)")
            if len(proposition) == longeur :
                #parcourir si == et similitudes
                rang=0
                for _ in range(len(proposition)):
                    if proposition[rang]==pwd[rang]:
                        compteur_egalité += 1
                    rang += 1
                print("Vous avez deviné",compteur_egalité, "de bonne(s) position(s) et bonne(s) valeur(s)" )

                for _ in range(len(proposition)):
                    rang_pwd = 0
                    rang_propo = 0
                    for _ in range(len(pwd)):  
                        if proposition[rang_propo]==pwd[rang_pwd]:
                            compteur_sim+=1
                        rang_propo+=1
                    rang_pwd+=1
                    rang_propo=0
                compteur_sim= compteur_sim - compteur_egalité
                print("Vous avez" ,compteur_sim, "similitude(s) entre le mots de passe et votre proposition")

                if compteur_egalité==longeur:
                    print("Vous avez gagné")
                    return True

                elif compteur_egalité!=longeur:
                    print("------------------------------")
                    return prop(nbr_test - 1)
            else:
                print("Il faut ", longeur, "chiffres")
                return prop(nbr_test)
        


while True:
    print("--------------NEW---------------")
    input("Appuyer pour commencer le jeu...")
    jeu()
    prop(nbr_test)
