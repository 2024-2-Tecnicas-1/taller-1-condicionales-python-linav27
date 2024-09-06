from time import localtime
def evaluar(dia, mes, anno):
    t = localtime()
    diaA = t.tm_mday
    mesA = t.tm_mon
    annoA = t.tm_year
    edad =annoA - anno - 1
    if(mes > mesA) or (mes == mesA and dia > diaA)
    else : 
     annoA - anno 
    return ""

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
