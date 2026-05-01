#!/usr/bin/python3
"""Faylın sonuna mətn əlavə edən modul."""


def append_write(filename="", text=""):
    """Mətni faylın sonuna əlavə edir və əlavə olunan simvol sayını qaytarır."""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
