# Inicio del programa Conjutos
# Autor: E.A.H.
# Fecha: 09/Abril/2019

def U(x,y):
    un = []
    for i in x:
        if i in y:
            continue
        else:
            un.append(i)
    return (un + y)

def Inter(x,y):
    inter = []
    for i in x:
        if i in y:
            inter.append(i)
        else:
            continue
    return (inter)

def Com(x,y):
    com_uni = []
    for i in y:
        if i in x:
            continue
        else:
            com_uni.append(i)
    return (com_uni)

def Res(x,y):
    rest = []
    for i in x:
        if i in y:
            continue
        else:
            rest.append(i)
    return (rest)

def main():
    # Tabla de datos
    u=[1,2,5,6,8,9,10]
    a=[1,2,5,9]
    b=[5,8,9,10]
    c=[1,2,4,6,8]

    # EJERCICIO 3.2 DEL CAPÍTULO 3 DEL LIBRO "ESTADÍSTICA I, FUNDAMENTOS DE PROBABILIDAD Y ESTADÍSTICA", BY MTRA. SILVIA SÁNCHEZ DÍAZ


    print("a)", U(a,b))                         # Union de A y B
    print("b)", Inter(a, b))                    # Intersección de A y B
    print("c)", U(a, c))
    print("d)", Inter(U(a,c),Com(b,u)))
    print("e)", Inter(a, c))
    print("f)", Com(a,u))                       # Complemento de A
    print("g)", Com(b, u))
    print("h)", Com(c, u))
    print("i)", Inter(U(b,c),a) )
    print("j)", Inter(U(b,c), b ))
    print("k)", U(U(Com(b,u),Com(c,u)), a) )
    print("l)", U(Com(b,u),Com(c,u) ))
    print("m)", Inter(Com(b,u),Com(c,u)) )
    print("n)", Res(a,c) )                      # Diferencia de A y C


main()

