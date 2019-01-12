#Napisz program, który liczy za użytkownika. Umożliw użytkownikowi
#wprowadzenie liczby początkowej, liczby końcowej i wielkości odstępu między kolejnymi
#liczbami.

poczatek = int(input("Podaj swoja liczbe poczatkowa: "))
koniec = int(input("Podaj swoja liczbe koncowa: "))
skok = int(input("Podaj wielkosc odstepu miedzy kolejnymi liczbami: "))
 
for i in range(poczatek, koniec, skok):
	print(i, end=" ")
 
input("\n\nAby zakonczyc program, nacisnij klawisz Enter.")
