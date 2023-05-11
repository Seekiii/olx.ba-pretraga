import requests
import json

krategorije = {
	"vozila":1,
	"nekretnine":2,
	"mobiteli":3,
	"kompjuteri":5,
	"tehnika":14,
	"multimedija":15,
	"literatura":16,
	"motocikli":21,
	"bicikli":22,
	"stanovi":23,
	"kuce":24,
	"vikendice":26,
	"apartmani":27,
	"zemljista":29,
	"ostalo":37,
	"laptopi":39,
	"poslovi":2286
}

def spremi_podatke(ime, data):
    with open(f"{ime}.json", 'w') as file:
        json.dump(data, file,indent=4)

def req(url, headers, data):
    r = requests.get(url, headers=headers, json=data)
    return r

def kategorija(lokacija, kolicina=1,spremi=False):
    if lokacija not in krategorije:
        return f"[ERROR] Naziv '{lokacija}' nije moguće pronaći. Provjerite definisana imena za pronalazak pod sekcijom 'kategorije'."
    
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
    url = "https://olx.ba/api/search"
    data = {
        "category_id": krategorije[lokacija],
        "per_page": kolicina
    }
    zahtjev = req(url, headers, data)
    if spremi:
    	if zahtjev.status_code == 200:
    		spremi_podatke("kategorija",zahtjev.json())
    
    return zahtjev.json()

def pretraga(args, kolicina=1,spremi=False):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
    url = "https://olx.ba/api/search"
    data = {
        "q": args,
        "per_page": kolicina
    }
    zahtjev = req(url, headers, data)
    if spremi:
    	if zahtjev.status_code == 200:
    		spremi_podatke("pretraga",zahtjev.json())
    
    return zahtjev.json()

#===================================#
#	vozila
#	nekretnine
#	mobiteli
#	kompjuteri
#	tehnika
#	multimedija
#	literatura
#	motocikli
#	bicikli
#	stanovi
#	kuce
#	vikendice
#	apartmani
#	zemljista
#	ostalo
#	laptopi
#	poslovi
#===================================#
# Mozete koristiti samo ove kategorije koje se trenutno nalaze u ovoj sekciji.

# kolicina = (Koliko zelite artikala da vam posalje olx.ba)
# spremi = (Da li zelite da se podaci spreme kao .json file na vas komp?)

kategorija_data = kategorija("vozila", kolicina=1, spremi=True)
pretraga_data = pretraga('bmw f10 top stanje', kolicina = 1, spremi=True)

print(kategorija_data)
print("================================")
print(pretraga_data)
