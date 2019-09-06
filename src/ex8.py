def wczytaj_dane():
	date = []
	with open("dane.txt") as file:
		plik = file.readline()
		for i in range(0,len(plik)):
			date.append(plik[i])
	return date

print(sum(wczytaj_dane()))
