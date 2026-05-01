#!/usr/bin/python3
"""Faylı oxuyan və ekrana çap edən funksiya."""


def read_file(filename=""):
    """UTF8 formatında olan mətni oxuyur və stdout-a çıxarır."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
