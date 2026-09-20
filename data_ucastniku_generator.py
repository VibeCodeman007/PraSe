import random
from pathlib import Path

"""
________________________________________________________________________

--- PRIKLANDNE DATA UCASTNIKU-------------------------------------------
________________________________________________________________________

"""

# Seznam všech položek, které mají nenulový počet (z tvého skladiště)
polozky_s_nenulovym_pocetem = [
    "termoska", "deka",
    "svetlomodra_mikina_XS_Female", "svetlomodra_mikina_S_Female",
    "cervene_smolkovske_tricko_S_Male", "cervene_smolkovske_tricko_M_Male", "cervene_smolkovske_tricko_M_Female",
    "tmavomodre_vesmirne_tricko_S_Male", "tmavomodre_vesmirne_tricko_S_Female",
    "svetlomodre_superprase_tricko_S_Female",
    "cervene_mafianske_tricko_s_dlhym_rukavom_S_Male", "cervene_mafianske_tricko_s_dlhym_rukavom_S_Female",
    "cervene_mafianske_tricko_s_dlhym_rukavom_L_Male", "cervene_mafianske_tricko_s_dlhym_rukavom_XL_Male",
    "cervene_mafianske_tricko_s_kratkym_rukavom_S_Male", "cervene_mafianske_tricko_s_kratkym_rukavom_S_Female",
    "cervene_mafianske_tricko_s_kratkym_rukavom_M_Female", "cervene_mafianske_tricko_s_kratkym_rukavom_XL_Male",
    "cervene_prase_tricko_XXL_Male",
    "modre_prase_tricko_XL_Male", "modre_prase_tricko_XXL_Male",
    "cervene_tielko_S_Female", "cervene_tielko_M_Female", "cervene_tielko_L_Female", "cervene_tielko_XL_Female",
    "modre_tielko_M_Female", "modre_tielko_L_Female",
    "zelene_tielko_S_Female", "zelene_tielko_M_Female", "zelene_tielko_L_Female", "zelene_tielko_XL_Female",
    "cervene_tricko_s_golierom_S_Male", "cervene_tricko_s_golierom_L_Male",
    "modre_tricko_s_golierom_L_Male",
    "sede_tielko_S_Female",
    "cierne_tricko_s_golierom_M_Male", "cierne_tricko_s_golierom_L_Male",
    "zelene_tricko_s_golierom_M_Male",
    "knihy_titul1", "knihy_titul2",
    "zapisnik", "pero", "platenna_taska"
]

# Generování náhodných jmen účastníků
ucastnici = [f"ucastnik_{i+1}" for i in range(26)]

# Datová struktura pro účastníky a jejich preference
data_ucastniku = {}

for i, ucastnik in enumerate(ucastnici):
    poradi = i + 1
    preference = {polozka: random.randint(-2, 2) for polozka in polozky_s_nenulovym_pocetem}

    """ !!! -2 BUDE SLOUZIT TAKY JAKO INDIKÁTOR VELIKOSTI, REKNEME JIM POKUD JIM NESEDI VELIKOST TAK AT DAJÍ TO CO NAM VYHODI CISLO -2
    TYTO VĚCI NEMUZOU DOSTAT"""

    data_ucastniku[ucastnik] = {
        "poradi": poradi,
        "preference": preference
    }

# Cesta k souboru ve stejné složce jako tento skript
cesta_k_txt = Path(__file__).parent / "data_ucastniku.txt"

# Zápis dat do txt souboru
with cesta_k_txt.open("w", encoding="utf-8") as soubor:
    soubor.write(str(data_ucastniku))

print(f"Data byla uložena do souboru: {cesta_k_txt}")