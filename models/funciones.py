def sano(calorias:int, es_vegetariano:bool) -> bool: #dice si un producto es sano
    if calorias < 1000:
        return True
    if es_vegetariano is True:
        return True
    return False


#print(sano(80, False))  # True, porque tiene menos de 100 calorías

def conteo_calorias (cal_ingredientes:list) -> int : #hace el conteo de calorias por producto
    total_calorias = sum(cal_ingredientes)
    return round(total_calorias * 0.95,2)

#ingredientes = [150,250,300,250]
#print(conteo_calorias(ingredientes))

def Costo_produccion(precio_Ing1:dict, precio_Ing2:dict, precio_Ing3:dict) -> int: #determina el valor de producir un producto de la heladeria
    return precio_Ing1["precio"] + precio_Ing2["precio"] + precio_Ing3["precio"] 


#print(precio_ingredientes(ingrediente1,ingrediente2,ingrediente3))

def rentabilidad (Precio_p:int,Ingre1:dict,Ingre2:dict,Ingre3:dict) -> int: #proporciona la rentabilidad de cada producto vendido
    return Precio_p - Ingre1["precio"]- Ingre2["precio"] - Ingre3["precio"]

#ingrediente1 = {"nombre": "Helado de Fresa", "precio": 1200}
#ingrediente2 = {"nombre": "Chispas de chocolate", "precio": 500}
#ingrediente3 = {"nombre": "Mani Japonés", "precio": 900}
#precio_producto = 7500

#print(rentabilidad(precio_producto,ingrediente1,ingrediente2,ingrediente3))

def best_productv(*productos) -> str: #hace calculo para saber con que producto se gana mas
    rentabilidad_maxima = productos[0]["rentabilidad"]
    producto_rentable = productos[0]["nombre"]
    
    for producto in productos:
        if producto["rentabilidad"] > rentabilidad_maxima:
            producto_rentable = producto["nombre"]
    return producto_rentable


#producto1 = {"nombre": "Helado de Fresa", "rentabilidad": 4900}
#producto2 = {"nombre": "Chispas de Chocolate", "rentabilidad": 2000}
#producto3 = {"nombre": "Maní Japonés", "rentabilidad": 3000}
#producto4 = {"nombre": "Torta de Limón", "rentabilidad": 6000}

#print(best_productv(producto1,producto2,producto3,producto4))
