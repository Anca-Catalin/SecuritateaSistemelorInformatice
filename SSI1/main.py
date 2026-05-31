import rarfile
import os

rarfile.UNRAR_TOOL = r"C:\Program Files\WinRAR\UnRAR.exe"

RAR_PATH      = "arhiva.rar"
WORDLIST_PATH = "parole.txt"

rf = rarfile.RarFile(RAR_PATH)
print("Fisiere in arhiva:", rf.namelist())
print()

gasit = False

with open(WORDLIST_PATH, "r", encoding="utf-8", errors="ignore") as f:
    for linie in f:
        parola = linie.strip()
        if not parola:
            continue

        print(f"Incerc: {parola}")

        try:
            date = rf.read(rf.namelist()[0], pwd=parola)
            print(f"\n>>> PAROLA GASITA: {parola} <<<")
            os.makedirs("extras", exist_ok=True)
            rf.extractall(path="extras", pwd=parola)
            print("Fisierele au fost extrase in folderul 'extras'")
            gasit = True
            break
        except rarfile.RarWrongPassword:
            pass
        except rarfile.BadRarFile:
            pass
        except Exception:
            pass

if not gasit:
    print("\nParola nu a fost gasita in lista.")