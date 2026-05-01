#!/usr/bin/python3
"""Bu modul fayl oxumaq üçün funksiyanı ehtiva edir."""


def read_file(filename=""):
    """Faylı UTF8 olaraq oxuyur və ekrana çap edir."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
