#!/usr/bin/python3
"""JSON faylından obyekti yükləyən modul."""
import json


def load_from_json_file(filename):
    """JSON faylını oxuyur və Python obyekti qaytarır."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
