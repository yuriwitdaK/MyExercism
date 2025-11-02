def is_isogram(string):
    string = string.replace('-', '') # no'-' whatsoever no disturbance
    string = string.replace(' ','')  # no empty spaces they disturb
    string = string.lower() #erases capital letters so they dont disturb
    
    return len(string) == len(set(string)) 
    #counts and checks if the string is still the same after erasing duplicates if so true if not false

