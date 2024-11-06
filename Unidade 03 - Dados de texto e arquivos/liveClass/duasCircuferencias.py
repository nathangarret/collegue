import math

def colidem(c1, r1, c2, r2):
    # Verificar se as cincurferenecias se cruzam
    d = math.sqrt((c1[0] - c2[0])**2)+((c1[1]-c2[1])**2)
    if d <= (r1,r2):
        return True
    else:
        return False

c1 = [0,0]
r1 = 3
c2 = [0, 5]
r2 = 3