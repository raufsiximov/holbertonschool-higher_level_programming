#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # Moduldakı bütün adları al
    names = dir(hidden_4)
    # Qoşa alt xətt ilə başlamayanları seç və sırala
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
