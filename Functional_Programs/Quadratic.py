
def roots(a,b,c):
    '''
    Quadratic Equation:
    a*(x**2) + b*x + c = 0
    :param a:
    :param b:
    :param c:
    :return:Roots of Quadratic Equation
    '''
    delta = b**2 - 4*a*c
    root1 = (-b + delta**(1/2))/2*a
    root2 = (-b - delta**(1/2))/2*a
    return root1,root2


root1,root2 = roots(1, -7, 10)
print(f"Root 1: {root1}\nRoot 2: {root2}")