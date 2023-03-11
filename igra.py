import random
import os

kamen = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papir = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

škare = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_over = """
                                                                                                                                
     _/_/_/         _/_/        _/      _/       _/_/_/_/                   _/_/      _/      _/       _/_/_/_/       _/_/_/    
  _/             _/    _/      _/_/  _/_/       _/                       _/    _/    _/      _/       _/             _/    _/   
 _/  _/_/       _/_/_/_/      _/  _/  _/       _/_/_/                   _/    _/    _/      _/       _/_/_/         _/_/_/      
_/    _/       _/    _/      _/      _/       _/                       _/    _/      _/  _/         _/             _/    _/     
 _/_/_/       _/    _/      _/      _/       _/_/_/_/                   _/_/          _/           _/_/_/_/       _/    _/      
                                                                                                                                
                                                                                                                                
"""

game_images = [kamen, papir, škare]




while True:
    korisnikov_izbor = int(input("Unesi 0 za kamen, 1 za papir ili 2 za škare\n"))
   
    if korisnikov_izbor >= 3 or korisnikov_izbor < 0: 
        os.system("cls")       
        print("Unijeli ste krivi broj! Molim Vas unesite slijedeće.")

    else:
        print(game_images[korisnikov_izbor])
        comPyuterov_izbor = random.randint(0, 2)
        print("ComPyuter je odigrao:")
        print(game_images[comPyuterov_izbor])

        if korisnikov_izbor == 0 and comPyuterov_izbor == 2:
            print("Pobjedio si!")
        elif comPyuterov_izbor == 0 and korisnikov_izbor == 2:
            print("Izgubio si...")
        elif comPyuterov_izbor > korisnikov_izbor:
            print("Izgubio si...")
        elif korisnikov_izbor > comPyuterov_izbor:
            print("Pobjedio si!")
        elif comPyuterov_izbor == korisnikov_izbor:
            print("Izjednačeno je.")


        ponoviti_igru = int(input("Želite li igrati ponovno?\n Unesite 0 za DA ili unesite 1 za NE\n"))
        print(ponoviti_igru)
        if ponoviti_igru == 0:
            os.system("cls")


        else:
            os.system("cls")
            print ("Vidimo se drugi put!\n")
            print (game_over)
            break
