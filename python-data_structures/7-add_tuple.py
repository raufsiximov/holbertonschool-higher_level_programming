#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Hər bir tuple üçün boşluqları doldururuq (əgər element azdırsa 0 əlavə edirik)
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    
    # Yalnız ilk iki elementi götürüb toplayırıq
    return (a[0] + b[0], a[1] + b[1])
