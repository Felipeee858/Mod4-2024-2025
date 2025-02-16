def VerificarJoaquim(array):
    if "Joaquim" in array:
        return True
    return False

def VerificarJoaquimV2(array):
    for nome in array:
        if "Joaquim"==nome:
            return True
    return False 
