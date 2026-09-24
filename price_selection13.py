import random
from pathlib import Path
import ast


# vsechny veci, ktere mame 
skladiste = {
    "drazsi": {
        "termoska": 5,
        "deka": 5,
        "svetlomodra_mikina_XS_Female": 1,
        "svetlomodra_mikina_S_Female": 2,
    },
    "stredni": {
        # Červené šmolkovské tričko
        "cervene_smolkovske_tricko_S_Male": 5,
        "cervene_smolkovske_tricko_M_Male": 1,
        "cervene_smolkovske_tricko_M_Female": 1,

        # Tmavomodré vesmírné tričko
        "tmavomodre_vesmirne_tricko_S_Male": 1,
        "tmavomodre_vesmirne_tricko_S_Female": 4,

        # Svetlomodré superPraSe tričko
        "svetlomodre_superprase_tricko_S_Female": 3,

        # Červené mafiánské tričko s dlouhým rukávem
        "cervene_mafianske_tricko_s_dlhym_rukavom_S_Male": 2,
        "cervene_mafianske_tricko_s_dlhym_rukavom_S_Female": 4,
        "cervene_mafianske_tricko_s_dlhym_rukavom_L_Male": 1,
        "cervene_mafianske_tricko_s_dlhym_rukavom_XL_Male": 3,

        # Červené mafiánské tričko s krátkým rukávem
        "cervene_mafianske_tricko_s_kratkym_rukavom_S_Male": 2,
        "cervene_mafianske_tricko_s_kratkym_rukavom_S_Female": 4,
        "cervene_mafianske_tricko_s_kratkym_rukavom_M_Female": 1,
        "cervene_mafianske_tricko_s_kratkym_rukavom_XL_Male": 3,

        # Červené PraSe tričko
        "cervene_prase_tricko_XXL_Male": 1,

        # Modré PraSe tričko
        "modre_prase_tricko_XL_Male": 1,
        "modre_prase_tricko_XXL_Male": 2,

        # Červené tielko
        "cervene_tielko_S_Female": 3,
        "cervene_tielko_M_Female": 2,
        "cervene_tielko_L_Female": 2,
        "cervene_tielko_XL_Female": 1,

        # Modré tielko
        "modre_tielko_M_Female": 1,
        "modre_tielko_L_Female": 2,

        # Zelené tielko
        "zelene_tielko_S_Female": 2,
        "zelene_tielko_M_Female": 3,
        "zelene_tielko_L_Female": 2,
        "zelene_tielko_XL_Female": 1,

        # Červené tričko s golierom
        "cervene_tricko_s_golierom_S_Male": 1,
        "cervene_tricko_s_golierom_L_Male": 2,

        # Modré tričko s golierom
        "modre_tricko_s_golierom_L_Male": 1,

        # Šedé tielko
        "sede_tielko_S_Female": 4,

        # Čierne tričko s golierom
        "cierne_tricko_s_golierom_M_Male": 2,
        "cierne_tricko_s_golierom_L_Male": 2,

        # Zelené tričko s golierom
        "zelene_tricko_s_golierom_M_Male": 3,

        # Knihy
        "knihy_titul1": 1,
        "knihy_titul2": 2,
    },
    "levne": {
        "zapisnik": 20,
        "pero": 30,
        "platenna_taska": 10
    }
}

# Funkce pro získání množství podle názvu, velikosti a pohlaví
def get_mnozstvi(nazev, velikost, pohlavi):
    for kategorie in skladiste:
        if nazev in skladiste[kategorie]:
            return skladiste[kategorie][nazev][velikost][pohlavi]
    return 0

# Příklad použití
#print(get_mnozstvi("cervene_smolkovske_tricko", "S", "Male"))  # Výpis: 5


# cesta ke složce, kde je tento .py soubor
base_dir = Path(__file__).parent

# txt soubor ve stejné složce
file_path = base_dir / "data_ucastniku.txt"

with file_path.open("r", encoding="utf-8") as f:
    data_ucastniku = ast.literal_eval(f.read())



def get_mnozstvi_veci(skladiste, nazev_veci):
    for kategorie in skladiste.values():
        if nazev_veci in kategorie:
            return kategorie[nazev_veci]
    return 0  # Pokud věc není nalezená, vrátí 0

    
def serad_ucastniky_podle_preference_a_poradi(vec, data_ucastniku , skladiste):
    # Inicializace slovníku pro výstup
    serazeni_ucastnici = {
        2: [],
        1: [],
        0: [],
        -1: [],
        -2: []        # -2 slouzi jako automaticke vyrazeni  pro obleceni pokud nemaji sparvnou velikost 
    } 

    # Procházení všech účastníků
    for ucastnik, info in data_ucastniku.items():
        preference = info["preference"].get(vec, None)
        poradi = info["poradi"]

        # Pokud má účastník preferenci pro danou věc, přidáme ho do příslušného seznamu
        if preference is not None:
            serazeni_ucastnici[preference].append((poradi, ucastnik))

    # Seřazení účastníků v každé podskupině podle pořadí (od nejmenšího po největší)
    for klic in serazeni_ucastnici:
        serazeni_ucastnici[klic].sort(key=lambda x: x[0])  # Seřazení podle pořadí
        serazeni_ucastnici[klic] = [ucastnik for (poradi, ucastnik) in serazeni_ucastnici[klic]]  # Extrahování jen jmen

    '''______________________________________________________________________________'''



    oriznuty_seznam_o_nejhorsi_preferenci = (
        serazeni_ucastnici.get(2, []) +
        serazeni_ucastnici.get(1, []) +
        serazeni_ucastnici.get(0, []) + 
        serazeni_ucastnici.get(-1, [])
    )

    # celkovy_pocet_zajemcu_o_vec = len(oriznuty_seznam_o_nejhorsi_preferenci)  # bez tech co dali -2

    mnozsvti_ve_sklade = get_mnozstvi_veci(skladiste, vec)

    oriznuty_seznam_o_nejhorsi_preferenci_usmerneny_na_mnozsvi_ve_skladu = oriznuty_seznam_o_nejhorsi_preferenci[:mnozsvti_ve_sklade ]

    # return serazeni_ucastnici

    return oriznuty_seznam_o_nejhorsi_preferenci_usmerneny_na_mnozsvi_ve_skladu

#______________________________________________________________________________

# Příklad použití
'''
vec = "termoska"
serazeni = serad_ucastniky_podle_preference_a_poradi(vec, data_ucastniku, skladiste)
print(serazeni)
print('____________________________________________________________')
vec2 = "tmavomodre_vesmirne_tricko_S_Male"
serazeni2 = serad_ucastniky_podle_preference_a_poradi(vec2, data_ucastniku , skladiste)
print(serazeni2)
'''

#__________________________________________________________________________________

#print('___________________________________________')

def delka_nejdelsiho_seznamu(skladiste, data_ucastniku):
    delka_nejdelsiho_seznamu = 0
    for kategorie in skladiste.values():
        for polozka in kategorie.keys():
            # Získání seřazeného a oříznutého seznamu účastníků pro danou položku
            serazeny_seznam = serad_ucastniky_podle_preference_a_poradi(polozka, data_ucastniku, skladiste)
            # Aktualizace délky, pokud je aktuální seznam delší
            if len(serazeny_seznam) > delka_nejdelsiho_seznamu:
                delka_nejdelsiho_seznamu = len(serazeny_seznam)

    return delka_nejdelsiho_seznamu

#delka_nej_seznamu =  delka_nejdelsiho_seznamu(skladiste, data_ucastniku)
#print(delka_nej_seznamu)


def vyber_ucastniky_s_nejvetsim_pravem(skladiste, data_ucastniku):    # Jenom prvni prvek co dela funkce vektory_dle_preference
    ucastnici_s_nejvetsim_pravem_na_cenu = []

    # Procházení všech položek ve skladišti
    for kategorie in skladiste.values():
        for polozka in kategorie.keys():
            # Získání seřazeného a oříznutého seznamu účastníků pro danou položku
            serazeny_seznam = serad_ucastniky_podle_preference_a_poradi(polozka, data_ucastniku, skladiste)

            # Pokud je seznam neprázdný, přidáme záznam {"polozka": ..., "ucastnik": ..., "poradi": ...}
            if serazeny_seznam:
                ucastnik = serazeny_seznam[0]
                poradi = data_ucastniku[ucastnik]["poradi"]
                ucastnici_s_nejvetsim_pravem_na_cenu.append(
                    {"polozka": polozka, "ucastnik": ucastnik, "poradi": poradi}
                )

    return ucastnici_s_nejvetsim_pravem_na_cenu

# Příklad použití
ucastnici_s_nejvetsim_pravem = vyber_ucastniky_s_nejvetsim_pravem(skladiste, data_ucastniku)
#print(ucastnici_s_nejvetsim_pravem)


def vektory_dle_preference(skladiste, data_ucastniku):

    # Vektory s vyberem - prvni vektor --> nejvetsi naroky, druhy vektor druhe nejvetsi naroky, 3 vektor ...

    # Získání maximální délky seznamu
    max_delka = delka_nejdelsiho_seznamu(skladiste, data_ucastniku)

    # Inicializace vektoru vektorů
    vektory = [[] for _ in range(max_delka)]

    # Procházení všech položek ve skladišti
    for kategorie in skladiste.values():
        for polozka in kategorie.keys():
            serazeny_seznam = serad_ucastniky_podle_preference_a_poradi(polozka, data_ucastniku, skladiste)

            # Pro každý index k v rozmezí délky aktuálního seznamu
            for k in range(len(serazeny_seznam)):
                if k < max_delka:
                    ucastnik = serazeny_seznam[k]
                    poradi = data_ucastniku[ucastnik]["poradi"]
                    vektory[k].append({"polozka": polozka, "ucastnik":  ucastnik, "poradi": poradi})   # Puvodni radek:  vektory[k].append({polozka: ucastnik, "poradi": poradi})

    return vektory
'''
# Použití: Získání prvního vektoru a výpis účastníků s pořadím 1–8
vektory_s_vektory_preferenci_ucastniku = vektory_dle_preference(skladiste, data_ucastniku)

# Získání prvního vektoru
prvni_vektor = vektory_s_vektory_preferenci_ucastniku[0]

# Filtrování účastníků s pořadím 1–8 a jejich cen
ucastnici_1_8 = {}
for dvojice in prvni_vektor:
    for vec, ucastnik in dvojice.items():
        if vec != "poradi":  # Vyhneme se klíči "poradi"
            poradi = dvojice["poradi"]
            if 1 <= poradi <= 8:
                if ucastnik not in ucastnici_1_8:
                    ucastnici_1_8[ucastnik] = {"poradi": poradi, "ceny": []}
                ucastnici_1_8[ucastnik]["ceny"].append(vec)

# Výpis účastníků s pořadím 1–8 a jejich cen
print("Účastníci s pořadím 1–8 a jejich ceny:")
for ucastnik, info in ucastnici_1_8.items():
    print(f"{ucastnik} (pořadí: {info['poradi']}): {', '.join(info['ceny'])}")
'''


def vytvor_slovnik_ucastniku_a_cen(ucastnici_s_cenami, data_ucastniku, skladiste):
    """ PUVODNI VERZE VE VERZI price_selection11"""
    slovnik_ucastniku = []

    # Seznamy věcí podle kategorií
    drazsi_veci = set(skladiste["drazsi"].keys())
    stredni_veci = set(skladiste["stredni"].keys())
    levne_veci = set(skladiste["levne"].keys())

    # Pomocný slovník pro rychlé nalezení záznamu účastníka
    zaznamy_podle_ucastnika = {}

    # Procházení všech záznamů {"polozka": ..., "ucastnik": ..., "poradi": ...}
    for zaznam in ucastnici_s_cenami:
        vec = zaznam["polozka"]
        ucastnik = zaznam["ucastnik"]
        poradi = data_ucastniku[ucastnik]["poradi"]

        # Inicializace záznamu pro účastníka, pokud ještě není
        if ucastnik not in zaznamy_podle_ucastnika:
            novy_zaznam = {
                "ucastnik": ucastnik,
                "poradi": poradi,
                "drazsi": [],
                "stredni": [],
                "levne": []
            }
            slovnik_ucastniku.append(novy_zaznam)
            zaznamy_podle_ucastnika[ucastnik] = novy_zaznam

        # Reference na záznam aktuálního účastníka
        zaznam_ucastnika = zaznamy_podle_ucastnika[ucastnik]

        # Roztřídění ceny do příslušné kategorie
        if vec in drazsi_veci:
            zaznam_ucastnika["drazsi"].append(vec)
        elif vec in stredni_veci:
            zaznam_ucastnika["stredni"].append(vec)
        elif vec in levne_veci:
            zaznam_ucastnika["levne"].append(vec)

    return slovnik_ucastniku

# Příklad použití
slovnik_ucastniku_prvni_vyber = vytvor_slovnik_ucastniku_a_cen(
    ucastnici_s_nejvetsim_pravem,
    data_ucastniku,
    skladiste
)

#print(ucastnici_s_nejvetsim_pravem)
#print(slovnik_ucastniku_prvni_vyber)   # !!!!! Tady  je ucasnik , a jeho preferovane ceny !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!§

vektory_s_vektory_preferenci_ucastniku =  vektory_dle_preference(skladiste, data_ucastniku)

""" 
Zde bude funkce, ktera konecne priradi ceny

for vyberova_kola_dle_preferenci in vektory_s_vektory_preferenci_ucastniku 
    ucastnici_v_kazdem_kole_a_jejich_preference = vytvor_slovnik_ucastniku_a_cen(vyberova_kola_dle_preferenci )

    for ucastnicic in ucastnici_v_kazdem_kole_a_jejich_preference

        apikuji podminky, kdyz nema nejaky ucastnik komplentni ceny
        dalsi krok for-cyklu

"""


""" UDELAT FUNKCI Z TETO CASTI 
_____________________________________________________________________________________________________________________________
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

"""

# Inicializace: každý účastník má svůj podseznam [ucastnik, None, None],
# seřazeno podle pořadí, přístupné přímo jménem účastníka
vektor_ucastniku = {
    ucastnik: [ None, None]     # ucastnik: [ucastnik, None, None]
    for ucastnik in sorted(data_ucastniku.keys(), key=lambda u: data_ucastniku[u]["poradi"])
}


for i in range(0 , len(vektory_s_vektory_preferenci_ucastniku)):   # iterujeme  podle vektoru se stejnym pravem vyberu - nejpeve nejvetsi pravo , pak druhe nejvetsi pravo,...

    i_te_kolo_vektor = vektory_s_vektory_preferenci_ucastniku[i]

    ucastnici_v_kazdem_kole_a_jejich_preference =  vytvor_slovnik_ucastniku_a_cen(i_te_kolo_vektor, data_ucastniku ,skladiste )  # i ty vyber

    for j in range(0 , len( ucastnici_v_kazdem_kole_a_jejich_preference)):

        seznam_ucastnika_v_j_tem_vyberu = ucastnici_v_kazdem_kole_a_jejich_preference[j]

        ucastnik_v_j_tem_vyberu = seznam_ucastnika_v_j_tem_vyberu['ucastnik'] 
        poradi_ucastnika_v_tem_vyberu = seznam_ucastnika_v_j_tem_vyberu['poradi'] 
        drahe_preference_j_teho_ucastnika = seznam_ucastnika_v_j_tem_vyberu['drazsi']
        stredni_preference_j_teho_ucasntika = seznam_ucastnika_v_j_tem_vyberu['stredni']
        levne_preferecnce_j_teho_ucastnika = seznam_ucastnika_v_j_tem_vyberu['levne'] 

        """MA UCASTNIK V DANEM KOLE NEPRAZDNE PREFERENCE ?"""
        if drahe_preference_j_teho_ucastnika:  # pokud není prázdná množina 
            draha_cena_j_ucastnika = random.choice(drahe_preference_j_teho_ucastnika)
        else:
            draha_cena_j_ucastnika = None

        if stredni_preference_j_teho_ucasntika:
            stredni_cena_j_teho_ucasntika = random.choice(stredni_preference_j_teho_ucasntika)
        else:
            stredni_cena_j_teho_ucasntika = None

        if levne_preferecnce_j_teho_ucastnika:
            levne_cena_j_teho_ucastnika = random.choice(levne_preferecnce_j_teho_ucastnika)
        else: 
            levne_cena_j_teho_ucastnika = None

        """ROZARENI CEN DLE PORADI"""

        if poradi_ucastnika_v_tem_vyberu <= 8:

            """POKUS O PRIDELENI PRVNIHO PRVKU (MA BYT IDEALNE DRAHY)"""

            if vektor_ucastniku[ucastnik_v_j_tem_vyberu ][0] is None:
                if draha_cena_j_ucastnika is not None:
                  vektor_ucastniku[ucastnik_v_j_tem_vyberu ][0] = draha_cena_j_ucastnika 
                elif stredni_cena_j_teho_ucasntika is not None:
                   vektor_ucastniku[ucastnik_v_j_tem_vyberu ][0] = stredni_cena_j_teho_ucasntika 
                elif levne_cena_j_teho_ucastnika is not None:
                    vektor_ucastniku[ucastnik_v_j_tem_vyberu ][0] = levne_cena_j_teho_ucastnika

                """POKUS O PRIDELENI PRVNIHO PRVKU (MA BYT IDEALNE STRDNI)"""

            if vektor_ucastniku[ucastnik_v_j_tem_vyberu ][1] is None:
                if stredni_cena_j_teho_ucasntika is not None:
                   vektor_ucastniku[ucastnik_v_j_tem_vyberu ][1] = stredni_cena_j_teho_ucasntika 
                elif levne_cena_j_teho_ucastnika is not None:
                    vektor_ucastniku[ucastnik_v_j_tem_vyberu ][1] = levne_cena_j_teho_ucastnika

        elif poradi_ucastnika_v_tem_vyberu >= 9 and poradi_ucastnika_v_tem_vyberu <= 17:

            """POKUS O PRIDELENI PRVNIHO PRVKU (MA BYT IDEALNE STREDNY)"""

            if vektor_ucastniku[ucastnik_v_j_tem_vyberu ][0] is None:
                if stredni_cena_j_teho_ucasntika is not None:
                    vektor_ucastniku[ucastnik_v_j_tem_vyberu ][0] = stredni_cena_j_teho_ucasntika 
                elif levne_cena_j_teho_ucastnika is not None:
                    vektor_ucastniku[ucastnik_v_j_tem_vyberu ][0] = levne_cena_j_teho_ucastnika

            """POKUS O PRIDELENI PRVNIHO PRVKU (MA BYT IDEALNE LEVNY)"""

            if vektor_ucastniku[ucastnik_v_j_tem_vyberu ][1] is None:
                if levne_cena_j_teho_ucastnika is not None:
                    vektor_ucastniku[ucastnik_v_j_tem_vyberu ][1] = levne_cena_j_teho_ucastnika

        elif poradi_ucastnika_v_tem_vyberu >= 18:
            """POKUS O PRIDELENI PRVNIHO PRVKU (MA BYT IDEALNE STREDNY)"""

            if vektor_ucastniku[ucastnik_v_j_tem_vyberu ][0] is None:
                if stredni_cena_j_teho_ucasntika is not None:
                    vektor_ucastniku[ucastnik_v_j_tem_vyberu ][0] = stredni_cena_j_teho_ucasntika 
                elif levne_cena_j_teho_ucastnika is not None:
                    vektor_ucastniku[ucastnik_v_j_tem_vyberu ][0] = levne_cena_j_teho_ucastnika

            """dostane jen jednu vec"""

            vektor_ucastniku[ucastnik_v_j_tem_vyberu ][1] = 'Nic'
            '''
            if vektor_ucastniku[ucastnik_v_j_tem_vyberu ][1] is None:
                if levne_cena_j_teho_ucastnika is not None:
                    vektor_ucastniku[ucastnik_v_j_tem_vyberu ][1] = levne_cena_j_teho_ucastnika
            '''

# print(vektor_ucastniku)

"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""


def vytiskni_tabulku(vektor_ucastniku, data_ucastniku):
    # Hlavička tabulky
    print(f"{'Pořadí':<8}{'Jméno účastníka':<20}{'První věc':<35}{'Druhá věc':<35}")
    print("-" * 98)

    # Řádky tabulky – vektor_ucastniku už je seřazený podle pořadí
    for ucastnik, veci in vektor_ucastniku.items():
        poradi = data_ucastniku[ucastnik]["poradi"]
        prvni_vec = veci[0] if veci[0] is not None else "-"
        druha_vec = veci[1] if veci[1] is not None else "-"
        print(f"{poradi:<8}{ucastnik:<20}{prvni_vec:<35}{druha_vec:<35}")

vytiskni_tabulku(vektor_ucastniku, data_ucastniku)
