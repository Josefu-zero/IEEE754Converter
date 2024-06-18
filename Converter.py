def ieee754_converter():
    num0 = float(input("Ingrese un número decimal: "))
    number=num0
    # Punto a) El número dado
    print("Número dado:", number)

    # Determinar el signo (bit de signo)
    sign_bit = 1 if number < 0 else 0
    print("Bit del signo:", sign_bit)

    # Convertir el número a positivo si es negativo
    number = abs(number)

    # Obtener el exponente en base 2
    exponent = 0
    if number != 0.0:
        while number >= 2.0:
            number /= 2.0
            exponent += 1
        while number < 1.0:
            number *= 2.0
            exponent -= 1
    print("Exponente:", exponent)
    print("Valor Mantisa:", number)

    # Exponente sesgado
    biased_exponent = exponent + 127
    print("Exponente sesgado:", biased_exponent)

    # Convertir el número a la mantisa (omitiendo el bit implícito)
    number -= 1.0  # Quitar el 1 implícito
    mantissa = []
    for _ in range(23):
        number *= 2
        if number >= 1.0:
            mantissa.append('1')
            number -= 1.0
        else:
            mantissa.append('0')
    mantissa = ''.join(mantissa)
    print("Mantisa:", mantissa)

    # Construir el formato IEEE 754 en binario
    ieee754_binary = f"{sign_bit:1b}{biased_exponent:08b}{mantissa:23}"
    print("Formato IEEE 754 (binario):", ieee754_binary)
    
    # Verifica que la longitud del binario IEEE 754 sea de 32 bits
    assert len(ieee754_binary) == 32, "La representación binaria IEEE 754 debe tener 32 bits."
    
    # Divide la cadena binaria en segmentos de 4 bits
    segments = [ieee754_binary[i:i+4] for i in range(0, len(ieee754_binary), 4)]
    
    # Convierte cada segmento de 4 bits a su valor hexadecimal
    hex_segments = [hex(int(segment, 2))[2:].upper() for segment in segments]
    
    # Une todos los segmentos hexadecimales en una sola cadena
    ieee754_hex = ''.join(hex_segments)
    print("Formato IEEE 754 (hexadecimal):", ieee754_hex)
    return ieee754_hex
    

if __name__ == "__main__":
    ieee754_converter()
