#!/usr/bin/python3
"""Obyekti JSON lüğətinə çevirən modul."""


def class_to_json(obj):
    """Obyektin lüğət strukturunu qaytarır."""
    return obj.__dict__
