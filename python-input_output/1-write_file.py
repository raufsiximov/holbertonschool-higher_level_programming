#!/usr/bin/python3
"""Fayla mətn yazan modul."""


def write_file(filename="", text=""):
    """UTF8 formatında fayla yazır və simvol sayını qaytarır."""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
