import squares

def within_threshold(a, b, threshold):

    if abs(a - b) > threshold:
        return True
    elif threshold < 0:
        return None
    else :
        return False


    
