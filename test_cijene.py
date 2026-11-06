from pathlib import Path

import pytest

from cijene import prosjecna_cijena


def test_prosjecna_cijena(tmp_path: Path) -> None:
    putanja = tmp_path / "rezervacije.csv"
    putanja.write_text(
        "gost,noci,cijena_noci\nAna,2,100\nMarko,2,50\n",
        encoding="utf-8",
    )

    assert prosjecna_cijena(putanja) == 75.0


def test_ponderisani_prosjek(tmp_path: Path) -> None:
    putanja = tmp_path / "rezervacije.csv"
    putanja.write_text(
        "gost,noci,cijena_noci\nAna,3,80\nMarko,1,100\n",
        encoding="utf-8",
    )

    assert prosjecna_cijena(putanja) == 85.0


def test_prazna_datoteka_bez_nocenja(tmp_path: Path) -> None:
    putanja = tmp_path / "rezervacije.csv"
    putanja.write_text("gost,noci,cijena_noci\n", encoding="utf-8")

    with pytest.raises(ValueError, match="Nema ostvarenih nocenja"):
        prosjecna_cijena(putanja)


def test_neispravan_broj_nocenja(tmp_path: Path) -> None:
    putanja = tmp_path / "rezervacije.csv"
    putanja.write_text(
        "gost,noci,cijena_noci\nAna,dva,100\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        prosjecna_cijena(putanja)
