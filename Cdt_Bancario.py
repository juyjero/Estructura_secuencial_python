cantidad = float(input("Ingrese la cantidad de dinero: "))
periodo = int(input("Ingrese el periodo en días: "))
porcentaje_interes = float(input("Ingrese el porcentaje de interés: "))
valor_interes = (cantidad * porcentaje_interes / 100 * periodo) / 360
valor_impuesto = valor_interes * 0.07
neto_pagar = cantidad + valor_interes - valor_impuesto
print("Intereses ganados:", valor_interes)
print("Valor del impuesto:", valor_impuesto)
print("Total a pagar al cliente:", neto_pagar)