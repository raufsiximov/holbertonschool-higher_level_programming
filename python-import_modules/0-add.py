#!/usr/bin/python3
if __name__ == "__main__":
    # 0-add.py faylından add funksiyasını import edirik
    add = __import__('0-add').add
    
    a = 1
    b = 2
    print(f"{a} + {b} = {add(a, b)}")
