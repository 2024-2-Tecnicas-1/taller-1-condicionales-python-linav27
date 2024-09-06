def evaluar(num_victorias_a, num_victorias_b):
    if (num_victorias_a < 0 or num_victorias_b < 0) or (num_victorias_a > 7 or num_victorias_b > 7)or num_victorias_a== 7 and num_victorias_b != 6 or (num_victorias_b == 7 and num_victorias_b != 6):
     return "invalido" 
    elif num_victorias_a < 6 and num_victorias_b < 6:
        return "Aun no ha termninado"
    elif abs(num_victorias_a - num_victorias_b) >= 2:
        return "Gano A" if num_victorias_a > num_victorias_b else "Gano B"
    elif num_victorias_a == 6 or num_victorias_b == 6:
        return "Gano A " if num_victorias_a == 6 else "Gano B"
    else:
     return "invalido"

if __name__ == '__main__':
    print("Los juegos ganaddor por A:", end="")
    num_victorias_a = int(input())
    print("Los juegos ganaddor por B:", end="")
    num_victorias_b = int(input())

    respuesta = evaluar(num_victorias_a, num_victorias_b)
    print(respuesta)
