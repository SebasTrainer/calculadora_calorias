def calcular_calorias(sexo, peso, altura, edad, nivel_actividad, objetivo):
    """
    Calcula las calorías diarias necesarias según el objetivo del individuo.
    :param sexo: 'hombre' o 'mujer'
    :param peso: en kg
    :param altura: en cm
    :param edad: en años
    :param nivel_actividad: 'sedentario', 'ligero', 'moderado', 'activo', 'muy_activo'
    :param objetivo: 'perder grasa', 'mantener peso', 'ganar músculo'
    :return: calorías diarias recomendadas y macronutrientes
    """
    
    # Fórmula de Harris-Benedict para la TMB
    if sexo == 'hombre':
        tmb = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * edad)
    else:
        tmb = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * edad)
    
    # Factores de actividad
    factores_actividad = {
        'sedentario': 1.2,
        'ligero': 1.375,
        'moderado': 1.55,
        'activo': 1.725,
        'muy_activo': 1.9
    }
    
    tdee = tmb * factores_actividad[nivel_actividad]
    
    # Ajuste de calorías según objetivo
    if objetivo == 'perder grasa':
        calorias = tdee - 500  # Déficit de 500 kcal
    elif objetivo == 'mantener peso':
        calorias = tdee
    else:
        calorias = tdee + 500  # Superávit de 500 kcal
    
    # Distribución de macronutrientes
    proteinas = (calorias * 0.3) / 4  # 30% de calorías en proteínas (1g = 4 kcal)
    carbohidratos = (calorias * 0.5) / 4  # 50% de calorías en carbohidratos (1g = 4 kcal)
    grasas = (calorias * 0.2) / 9  # 20% de calorías en grasas (1g = 9 kcal)
    
    return {
        'Calorías recomendadas': round(calorias),
        'Proteínas (g)': round(proteinas),
        'Carbohidratos (g)': round(carbohidratos),
        'Grasas (g)': round(grasas)
    }

# Ejemplo de uso
resultado = calcular_calorias(sexo='hombre', peso=70, altura=175, edad=25, nivel_actividad='moderado', objetivo='ganar músculo')
print(resultado)

# Solicitar datos al usuario
sexo = input("Ingrese su sexo (hombre/mujer): ").strip().lower()
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en cm: "))
edad = int(input("Ingrese su edad: "))
nivel_actividad = input("Nivel de actividad (sedentario, ligero, moderado, activo, muy_activo): ").strip().lower()
objetivo = input("Objetivo (perder grasa, mantener peso, ganar músculo): ").strip().lower()

# Llamar a la función con los datos ingresados
resultado = calcular_calorias(sexo, peso, altura, edad, nivel_actividad, objetivo)

# Mostrar el resultado
print("\n📊 **Resultados**:")
for clave, valor in resultado.items():
    print(f"{clave}: {valor}")
