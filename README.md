# Napredno programiranje

Repozitorijum za zadatke iz predmeta Napredno programiranje (FIST4NP).

## Zadatak: priprema radnog okruzenja

- Python 3.12+
- VS Code ili Google Colab
- Git i GitHub
- Ruff za provjeru i formatiranje koda
- Pytest za automatizovano testiranje

## Struktura projekta

```text
np-ime-prezime/
 cijene.py
 test_cijene.py
 requirements-dev.txt
 pyproject.toml
 README.md
 .gitignore
```

## Instalacija

Klonirati repozitorijum:

```bash
git clone https://github.com/korisnicko-ime/np-ime-prezime.git
cd np-ime-prezime
```

Napraviti i aktivirati virtuelno okruzenje:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\\Scripts\\Activate.ps1
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Instalirati alate:

```bash
python -m pip install -r requirements-dev.txt
```

## Funkcija prosjecna_cijena

Funkcija u fajlu `cijene.py` cita CSV datoteku koja sadrzi kolone `gost`, `noci` i `cijena_noci`. Racuna prosjecnu cijenu nocenja ponderisanu brojem nocenja:

```python
from pathlib import Path

from cijene import prosjecna_cijena

print(prosjecna_cijena(Path("rezervacije.csv")))
```

Ako nema ostvarenih nocenja, funkcija podize `ValueError`.

## Testiranje

Pokretanje testova:

```bash
python -m pytest -v
```

Provjera kvaliteta koda:

```bash
ruff check .
```

Formatiranje:

```bash
ruff format .
```

## Upit koriscen AI asistentu

> Kontekst: Python 3.12; podaci o rezervacijama nalaze se u CSV datoteci sa kolonama `gost`, `noci` i `cijena_noci`. Zadatak: napisi funkciju `prosjecna_cijena(putanja: Path) -> float` koja cita CSV datoteku i racuna prosjecnu cijenu nocenja ponderisanu brojem nocenja. Ogranicenja: koristi samo standardnu biblioteku, type hints, `csv.DictReader`, `Path` i `with` za rad sa datotekom. Ako nema ostvarenih nocenja, podigni `ValueError`. Napisi najmanje tri pytest testa koristeci `tmp_path`. Prikazi kod i kratko obrazlozenje.

## Uoceni nedostaci i provjere generisanog koda

- Osnovna verzija ne provjerava da li CSV datoteka sadrzi sve ocekivane kolone. Nedostajuca kolona izaziva `KeyError`.
- Neispravan broj nocenja ili cijena izaziva `ValueError` prilikom konverzije pomocu `int()` ili `float()`.
- Funkcija pretpostavlja da su sve cijene izrazene u istoj valuti.
- Za finansijske obracune sa zahtjevom za preciznim decimalnim vrijednostima moze biti pogodniji `Decimal` umjesto `float`.
- Testovima su provjereni normalan obracun, ponderisanje, slucaj bez ostvarenih nocenja i neispravan broj nocenja.

## Autor

Ime i prezime: **Upisati ime i prezime**
