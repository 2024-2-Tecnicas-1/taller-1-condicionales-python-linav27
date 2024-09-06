def evaluar(anno):
    if anno % 4 == 0 and anno % 100 != 0:
        print(f"{anno} es bisiesto")
        else:
         print(f"{anno} no es bisiesto")   
        return

if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(anno)
    print(respuesta)
