#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    
    # İlk elementi ən böyük kimi götürürük
    result = my_list[0]
    
    # Siyahını dövr edərək daha böyük ədəd varmı yoxlayırıq
    for i in my_list:
        if i > result:
            result = i
            
    return result
