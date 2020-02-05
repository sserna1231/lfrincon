def ejercicioIfs(num1):
    if num1 >=5:
        num1=num1+10
    if num1 >12:
        num1+=10
    if num1 >20:
        num1+=5
    print (num1)

def ejercicioIfs4(num1):
    if num1 >=5:
        num1+=2
        if num1 >12:
            num1+=10
             if num1 >20:
                num1+=5
    print (num1)

def ejercicioIfs2(num1):
    if num1 >=5:
        num1+=10
    elif num1 >12:
        num1+=10
    elif num1 >20:
        num1+=5
    print (num1)

def ejercicioIfs3(num1):
    if num1 >=5:
        num1+=10
    if num1 >12:
        num1+=10
    else:
        num1+=5
    print (num1)


ejercicioIfs(10)
ejercicioIfs2(10)
ejercicioIfs3(10)


def calcBonificacion(cedula,parcial,taller):
    bonificacion=0
    if parcial >=4.5 and parcial <= 5:
        if taller >= 4.8 and taller <=5:
            bonificacion= bonificacion+0.5
        elif taller >=4.5 and  taller < 4.8:
            bonificacion= bonificacion+0.3
    elif parcial >=4 and parcial < 4.5:
        if taller >= 4.0 and taller <=5:
            bonificacion= bonificacion +0.2
    if cedula %2 == 0:
        bonificacion=bonificacion+0.1
    print("La bonificacion es", bonificacion)

#calcBonificacion(101222,5,5)
        


def tamNumero(numero1,numero2):
    if numero1==numero2:
        print ("Igual")
    if numero1< numero2:
        print ("Menor")
    else:
        print ("Mayor")

tamNumero(4,4)







def ejemplo(dia):
    if dia == "viernes":
        print(" :D")

def ejemplo2(dia):
    if dia == "viernes":
        print(" :D")
    else:
        print (":(")

def ejemplo3(dia):
    if dia == "lunes":
        print(" :(")
    elif dia == "Martes" or dia == "Miercoles":
        print (":|")
    elif dia =="Jueves":
        print (": p")
    elif dia == "Viernes" or dia == "Sabado":
        print (":D")
    elif dia =="Domingo":
        print("triste")

def ejemplo4(dia):
    if dia == "lunes":
        print(" :(")
    elif dia == "Martes" or dia == "Miercoles":
        print (":|")
    elif dia =="Jueves":
        print (": p")
    elif dia == "Viernes" or dia == "Sabado":
        print (":D")
    elif dia =="Domingo":
        print("triste")
    num1=5
    if(num1==5):
        if(num1>4):
            print("Es cinco")



            

#ejemplo2("viernes")

    
