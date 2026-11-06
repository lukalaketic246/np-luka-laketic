import csv
from pathlib import Path


def prosjecna_cijena(putanja: Path) -> float:
    """Vraca prosjecnu cijenu nocenja ponderisanu brojem nocenja."""
    ukupno, noci = 0.0, 0

    with putanja.open(newline="", encoding="utf-8") as f:
        for red in csv.DictReader(f):
            broj_noci = int(red["noci"])
            cijena_noci = float(red["cijena_noci"])

            ukupno += broj_noci * cijena_noci
            noci += broj_noci

    if noci == 0:
        raise ValueError("Nema ostvarenih nocenja")

    return ukupno / noci
