#!/usr/bin/python3
"""
Bu modul MyList sinfini təqdim edir.
"""


class MyList(list):
    """list sinfindən miras alan sinif."""

    def print_sorted(self):
        """Siyahını artan sıra ilə çap edir (orijinalı dəyişmədən)."""
        print(sorted(self))
