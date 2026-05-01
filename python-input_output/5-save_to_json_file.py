#!/usr/bin/python3
"""Obyekti JSON faylına yazan modul."""
import json


def save_to_json_file(my_obj, filename):
    """Obyektin JSON təmsilini fayla yazır."""
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
