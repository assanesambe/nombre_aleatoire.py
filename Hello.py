import random 


i = random.randint(1,100)
y= 3
x=int(input("Je pense à un nombre compris entre 1 et 100. Pouvez-vous deviner de quoi il s'agit ?"))

while x!=i:

    if x>i:
        print("Votre supposition est trop élevée. Devinez à nouveau")
        y-=1

    if x<i:
        print("Votre estimation est trop faible. Devinez à nouveau.")
        y-=1

    x=int(input("Veuillez reesayer: "))
  

    if x==i:
        print("Félicitations ! Vous avez deviné le nombre correctement !")
    if y==0:
        print("GAME OVER" )
        break





