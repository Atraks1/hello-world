import re

game_on = True

password = "metin to najlepsza gierka komputerowa"

# deklaruje różne zestawy liter
standard = f"rstlne"
standard_list = ["r", "s", "t", "l", "n", "e"]
litery_do_wyboru_str = f"[qwyuiopkjhgfdazxcvbmęóąśłżźćń]"
samogloski = "ęyuóoiąa"

print("Witam w finale koła Fortuny! ")
print("Oto standardowy zestaw liter: ",standard_list)

# litery nie z standardowego zestawu liter zastepuje pustym miejscem "[]"
tablica = re.sub(litery_do_wyboru_str.lower(), "[_]", password.lower())
print("Oto tablica po przypisaniu standardowego zestawu liter : \n",tablica)

wybrane_litery = []
# gracz wybiera 3 społgłoski
for ch in range(3):
    wybor = input("Wybierz 3 spolgloski: ").lower()
    if wybor in samogloski:
        print("Ty dzbanie, wybierz SPÓŁGŁOSKĘ")
    elif wybor not in samogloski:
        wybrane_litery.append(wybor)

#gracz wybiera samogłoskę
wybor2=input("\n Teraz wybierz 1 samogłoskę: ").lower()
if wybor2 not in samogloski:
    print("Powinieneś podać samogłoskę, inną niż E")
else:
    wybrane_litery.append(wybor2)

# "czyszcze" ekran
print("\n" * 100)

# sandardowe litery i wybrane przez gracza tworzą liste "wybrane_plus_standard_list"
wybrane_plus_standard_list = standard_list + wybrane_litery
print("Litery wybrane przez Ciebie i standardowe litery to: : ", wybrane_plus_standard_list)

# konwertuje liste 10 liter na string
wybrane_standard = ''.join(wybrane_litery) + standard

# od wszystkich liter dostepnych do wyboru odejmujemy 4 wybrane litery
final = (litery_do_wyboru_str.translate({ord(i): None for i in wybrane_standard}))

# odejmuje dostepne litery od wybranych liter
tablica_final = re.sub(final.lower(), "[]", password.lower())
print("Tablica wygląda tak:\n\n","[-]    ", tablica_final,"    [-]")
print("\nMasz 3 próby na odgadnięcie hasła","\n Wpisuj hasło z małych liter!")
# print(tablica_final)

game_on = True

# gra się zaczyna
while game_on:
    # n to liczba prób na zgadnięcie hasła
    n = 3
    for i in range(n):
        print("Pozostałe próby na odgadnięcie to :",n)
        n -= 1
        i = input('\n')
        if i == password.lower():
            print("Brawo! To poprawna odpowiedź!")
            game_on = False
            break

        elif n == 0:
            print("Koniec szans! Porażka!!!")
            game_on = False
            break
