#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Əgər indeks mənfidirsə və ya siyahının uzunluğundan böyükdürsə, orijinal siyahını qaytar
    if idx < 0 or idx >= len(my_list):
        return my_list
    
    # Siyahının nüsxəsini yarat (orijinalı dəyişməmək üçün)
    new_list = my_list[:]
    
    # Elementi dəyiş
    new_list[idx] = element
    return new_list
