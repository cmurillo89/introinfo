# Los programas inteligentes usan booleanos para tomar decisiones sobre si ejecutar lineas de codigo u omitirlas

activo = True

if activo == True:
    print("El usuario está activo")
    activo = False


cargado = True
if cargado:
    print("EL celular está cargado")
else:
    print("Conecte el cargador")

pagado = True
if cargado:
    print("El artículo está pagado")
else:
    print("Moroso, por favor pague")

nota = 80
if nota <= 80:
    print("Penales, mamei")
else:
    print("Pasaste, bien soldado")

porcentaje = 45

if porcentaje < 60:
    print("REPROBADO, HASTA LA VISTA BABY")
elif porcentaje < 70:
    print("PENALES")
else:
    print("FELICIDADES, APROBASTE")


