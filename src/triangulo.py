def evaluar(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "El triangulo es equiláletero"
        elif a == b or b == c or a == c:
            return "El triangulo es isósceles"
        else:
            return "El triangulo es escaleno"
    else:
     return "No es triángulo válido"

if __name__ == '__main__':
    print("a:", end="")
    a = float(input())
    print("b:", end="")
    b = float(input())
    print("c:", end="")
    c = float(input())
        
    respuesta = evaluar(a, b, c)
    print(respuesta)
