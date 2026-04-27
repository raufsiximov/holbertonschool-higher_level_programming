#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # hidden_4 modulundakı bütün adları alırıq
    names = dir(hidden_4)
    
    # Adları sıralayırıq və "__" ilə başlamayanları çap edirik
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
