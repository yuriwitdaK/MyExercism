def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):              #checks if length is equal
        raise ValueError("Strands must be of equal length.")#asked error message    
    if len(strand_a) == 0:
        return 0 #checks if lenght is above 0

    differences = 0
    

    for i in range(len(strand_a)): #loop comparing strands
        if strand_a[i] != strand_b[i]:
            differences += 1
            

    return differences 