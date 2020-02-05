def probarBool():
    num1=1
    num2=2
    num3=3
    num4=4
    if not(( not (num1==num2 or num2==num3) and not(num2!=num1)and num1>num2))and num4==5:
        print ("SI")
    elif(num4<num2):
        print ("No")
    else:
        print ("otro")


def ejercicioIfs(num1):
    num2=6
    if num1>=12 and num2>3:
        num1=num1+10
    else:
        num1=num1+3
    if num1 >5 or num2 > 0:
        num1=num1+10
    if num1 >20:
        num1=num1+5
    num1=num1+2
    print (num1)

def ejercicioIfs2(num1):
    num2=6 * num1
    if num1>=12 and not(num2>3 and num2==5):
        num1=num1+5
    elif num1 >5 or num2 > 0:
        num1=num1+10
    elif num1 >20:
        num1=num1+5
    else:
        num1=num1+3
    num1=num1+2
    print (num1)
def ejercicioIfs3(num1):
    num2=6 * num1
    if num1>=12 and num2>3:
        num1=num1+10
    if num1 >5 or num2 > 0:
        num1=num1+10
    if num1 >20:
        num1=num1+5
    else:
        num1=num1+3
    num1=num1+2
    print (num1)

def ejercicioIfs4(num1):
    num2=6 * num1 
    if num1>=12 or num2>3:
        num1=num1+10
        if num1 >5 or num2 > 0:
            num1=num1+10
            if num1 >20:
                num1=num1+5
        else:
            num1=num1+3
    else:
        num1=num1* -1
    num1=num1+2
    print (num1)


ejercicioIfs(10)
