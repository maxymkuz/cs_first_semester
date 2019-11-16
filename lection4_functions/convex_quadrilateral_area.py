from math import sqrt

def lines_intersection(k1, c1, k2, c2):
    """
    int/float, int/float, int/float, int/float -> tupple 
    Finds intersection of two functions
    """
    if k1 == k2:
        return None
    else:
        x = (c2 - c1)/(k1 - k2)
        y = round(k1 * x + c1, 2)
        return round(x, 2), y

def distance(x1, y1, x2, y2):
    """
    finds the distance between two givwn points: A(x1, y1) and B(x2, y2)
    int/float, int/float, int/float, int/float -> float
    """
    res = round(sqrt((x1 - x2)**2 + (y1 - y2)**2), 2)
    return res

def quadrangle_area(a, b, c, d, f1, f2):
    """
    Finds an area of a quadrangle
    int/float, int/float, int/float, int/float, int/float, int/float -> float
    """
    try:
        area = sqrt(4*(f1**2)*(f2**2) - (b**2 + d**2 - a**2 - c**2)**2)/4
        return round(area, 2)
    except:
        return None
    
def lines_distance(c1, c2):
    lines_len = abs(c1 - c2)
    return lines_len

def trapezoid_area(h,l1, l2):
    area = h * (l1 + l2)/2
    return area

def check_intersection(k1, c1, k2, c2, P_1, P_2, d):
    try:
        M = lines_intersection(k1, c1, k2, c2)
        print(M, P_1, P_2)
        am = distance(M[0], M[1], P_1[0], P_1[1])
        bm = distance(M[0], M[1], P_1[0], P_2[1])
        print (am, bm)
        if round(am + bm) == d:
            return True
        else:
            print(am + bm, d)
            return False
    except(TypeError):
        return False


def four_lines_area(k1, c1, k2, c2, k3, c3, k4, c4):
    #Finding all points and sides/diagnal
    A_1 = lines_intersection(k1, c1, k2, c2)
    A_2 = lines_intersection(k2, c2, k3, c3)
    A_3 = lines_intersection(k3, c3, k4, c4)
    A_4 = lines_intersection(k4, c4, k1, c1)
    a = distance(A_1[0], A_1[1], A_2[0], A_2[1])
    b = distance(A_2[0], A_2[1], A_3[0], A_3[1])
    c = distance(A_3[0], A_3[1], A_4[0], A_4[1])
    d = distance(A_4[0], A_4[1], A_1[0], A_1[1])
    f1 = distance(A_1[0], A_1[1], A_3[0], A_3[1])   
    f2 = distance(A_2[0], A_2[1], A_4[0], A_4[1])

    print("A_4", A_4)
    print(check_intersection(k1, c1, k3, c3, A_2, A_3, d))
    print(A_1, A_2, A_3, A_4)
    print(a, b, c, d)
    #Checking if our quadrangle is a trapezoid
    if k1 == k3:
        h = lines_distance(c1, c3)
        area = trapezoid_area(h, b, d)
        print(h, b, d)
    elif k2 == k4:
        h = lines_distance(c2, c4)
        area = trapezoid_area(h, a, c)
    else:
        area = quadrangle_area(a, b, c, d, f1, f2)

    return area


#print(four_lines_area(-3, 5, 0, -1, 3, 5, 0, 2))
print(four_lines_area(1,0,0,-2,-1,0,0,1))