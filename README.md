## Upotrijebljeni upit

> Kontekst: Python 3.12; podaci o rezervacijama nalaze se u CSV datoteci sa kolonama `gost`, `noci` i `cijena_noci`. Zadatak: napisi funkciju `prosjecna_cijena(putanja: Path) -> float` koja cita CSV datoteku i racuna prosjecnu cijenu nocenja ponderisanu brojem nocenja. Koristi standardnu biblioteku, type hints, `csv.DictReader`, `Path` i `with`. Ako nema ostvarenih nocenja, podigni `ValueError`. Napisi pytest testove koristeci `tmp_path`.

## Uoceni nedostaci generisanog koda

- Kod ne provjerava da li CSV datoteka sadrzi sve potrebne kolone.
- Neispravan broj nocenja ili cijena moze izazvati gresku.
- Pretpostavlja da su sve cijene izrazene u istoj valuti.
- Za preciznije finansijske obracune moze se koristiti `Decimal` umjesto `float`.

## Luka Laketic
