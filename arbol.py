titulo = 'SERVICIO DE INTERNET'
print (titulo.center(100,('*')))
print ('una empresa del departamento de Solola desea adquirir servicio de internet cuenta con dos opciones que le pueden distribuir el servicio, dichas alternativas son la empresa CLARO, TIGO.')

# preguntas
print ('opcion TIGO\n')

pago = float(input("si elige tigo cual seria la probabilidad de que page la instalacion: \n"))
disgusto = float(input("indique el desacuerdo del pago de la instalacion: \n"))
no_pago = float(input("si elige tigo cual seria la probabilidad de que no page la instalacion: \n"))
paquete = float(input("si no pagara la instalacion que posibilidad hay que contrate un paquete adicional: \n"))
disgusto_1 = float(input("indique el nivel de disgusto: \n"))
velocidad = float(input("si no pagara la instalacion cual seria la prosividad de adquirir un paquete > 20MB: \n"))
disgusto_2 = float(input("indique el nivel de disgusto: \n"))

print ('opcion CLARO\n')

contrato = float(input("si elige CLARO  cual seria la probabilidad de contratar un paquete < 10MB: \n"))
disgusto_3 = float(input("indique el nivel de disgusto: \n"))
contrato_1 = float(input("si elige CLARO cual seria la probabilidad de contratar un paquete > 20MB: \n"))
disgusto_4 = float(input("indique el nivel de disgusto: \n"))

# operaciones 

# opcion TIGO

# pagar instalacion 

respueta_1 = pago*disgusto

#contratar paquete adicional 

respueta_2 = no_pago*paquete*disgusto_1

# o	Aumentar velocidad > 20 MB
respueta_3 = no_pago*velocidad*disgusto_2

# opcion claro 
#Contratar paquete < 10MB 

respuesta_4 = contrato*disgusto_3

#Contratar Paquete  > 20 MB

respuesta_5 = contrato_1*disgusto_4

# condiciones 

if respueta_1 >= respueta_2 and respueta_1 >= respueta_3 and respueta_1 >= respuesta_4 and respueta_1 >= respuesta_5: 
    total = respueta_1
    mensaje = "contratar tigo y pagar instalacion" 
elif respueta_2 >= respueta_1 and respueta_2 >= respueta_3 and respueta_2 >= respuesta_4 and respueta_2 >= respuesta_5: 
    total = respueta_2
    mensaje = "contratar tigo y paquete adicional"
elif respueta_3 >= respueta_1 and respueta_3 >= respueta_2 and respueta_3 >= respuesta_4 and respueta_3 >= respuesta_5:
    total = respueta_3
    mensaje = "contratar tigo y no pagar instalacion, contratar paquete adicional > 20MB" 
elif respuesta_4 >= respueta_1 and respuesta_4 >= respueta_2 and respuesta_4 >= respueta_3 and respuesta_4 >= respuesta_5:
    total = respuesta_4
    mensaje = "contratar claro y contratar paquete < 10MB" 
elif respuesta_5 >= respueta_1 and respuesta_5 >= respueta_2 and respuesta_5 >= respueta_3 and respuesta_5 >= respuesta_4:
    total = respuesta_5
    mensaje = "contratar claro y  contratar paquete  > 20MB" 

print ('\n datos \n')
print ('decuerdo con los datos introducidos la mejor opcion es: ',mensaje)
print ('con un grado de adaptacion a tu persona de un: '"{0:.4f}".format(total*100),"%")
print ('fin de la simulacion')














