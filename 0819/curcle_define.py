r=float(input("半徑:"))
def circle_area(l):
    l=r*r*3.14
    return l
def circle_circum(l):
    l=r*2*3.14
    return l
print("圓周長為",circle_circum(r))
print("圓面積為",circle_area(r))