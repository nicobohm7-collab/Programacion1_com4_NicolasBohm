fecha = input("Ingrese la fecha en formato 'día, DD/MM': ")

partes = fecha.split(",")
if len(partes) != 2:
    print("Error en el formato de la fecha.")
else:
    dia_semana = partes[0].strip().lower()
    dia_mes, mes = partes[1].strip().split("/")

    dia_mes = int(dia_mes)
    mes = int(mes)

    if dia_mes < 1 or dia_mes > 31 or mes < 1 or mes > 12:
        print("Error en la fecha ingresada.")
    else:
        if dia_semana == "lunes":
            print("Hoy corresponde nivel inicial.")
            examenes = input("¿Se tomaron exámenes? (si/no): ").lower()
            if examenes == "si":
                aprobados = int(input("Ingrese cantidad de alumnos aprobados: "))
                desaprobados = int(input("Ingrese cantidad de alumnos desaprobados: "))
                total = aprobados + desaprobados
                if total > 0:
                    porcentaje = (aprobados * 100) / total
                    print("Porcentaje de aprobados:", porcentaje, "%")
                else:
                    print("No hubo alumnos.")
        elif dia_semana == "martes":
            print("Hoy corresponde nivel intermedio.")
            examenes = input("¿Se tomaron exámenes? (si/no): ").lower()
            if examenes == "si":
                aprobados = int(input("Ingrese cantidad de alumnos aprobados: "))
                desaprobados = int(input("Ingrese cantidad de alumnos desaprobados: "))
                total = aprobados + desaprobados
                if total > 0:
                    porcentaje = (aprobados * 100) / total
                    print("Porcentaje de aprobados:", porcentaje, "%")
                else:
                    print("No hubo alumnos.")
        elif dia_semana == "miercoles" or dia_semana == "miércoles":
            print("Hoy corresponde nivel avanzado.")
            examenes = input("¿Se tomaron exámenes? (si/no): ").lower()
            if examenes == "si":
                aprobados = int(input("Ingrese cantidad de alumnos aprobados: "))
                desaprobados = int(input("Ingrese cantidad de alumnos desaprobados: "))
                total = aprobados + desaprobados
                if total > 0:
                    porcentaje = (aprobados * 100) / total
                    print("Porcentaje de aprobados:", porcentaje, "%")
                else:
                    print("No hubo alumnos.")
        elif dia_semana == "jueves":
            print("Hoy corresponde práctica hablada.")
            asistencia = int(input("Ingrese porcentaje de asistencia: "))
            if asistencia > 50:
                print("Asistió la mayoría.")
            else:
                print("No asistió la mayoría.")
        elif dia_semana == "viernes":
            print("Hoy corresponde inglés para viajeros.")
            if dia_mes == 1 and (mes == 1 or mes == 7):
                print("Comienzo de nuevo ciclo.")
                alumnos = int(input("Ingrese cantidad de alumnos: "))
                arancel = float(input("Ingrese arancel por alumno en $: "))
                ingreso = alumnos * arancel
                print("Ingreso total del ciclo: $", ingreso)
        else:
            print("Error: el día ingresado no corresponde a ningún nivel.")