# -*- coding: utf-8 -*-
"""ASTRID_COY_PGY1121_006_V.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VF4uX2n-Z5k8HepBtWXyPZZCKYbc3Qyc
"""

precio_hectarea = 500000
num_columna = 5
n_fila = 4

lotes_d = [
   [None, None, None, None, None],
   [None, None, None, None, None],
   [None, None, None, None, None],
   [None, None, None, None, None],
]

def mostrar_lotes_d():
    print("Lotes disponibles:")
    for fila in lotes_d:
        for lote in fila:
            print('[X]' if lote == 'X' else '[ ]', end=' ')
        print()

def mostrar_detalles_lote():
    if len(lotes_seleccionados) == 0:
        print("No ha seleccionado ningun lote.")
        return

    for i, lote in enumerate(lotes_seleccionados, start=1):
        fila, columna = lote
        n_lote = i
        t_terreno = 1
        precio = t_terreno * precio_hectarea

        print(f"Detalles del Lote:", n_lote)
        print(f"Número de lote: ", n_lote)
        print(f"Tamaño del terreno: ", t_terreno,"hectarea")
        print(f"Precio: $", precio)

lotes_seleccionados = []

clientes = []

def mostrar_clientes():
    if len(clientes) == 0:
        print("Aún no hay clientes registrados.")
        return

    print("Lista de Clientes:")
    print("------------------------------------")
    for cliente in clientes:
        rut, nombre, fono, correo = cliente
        print(f"RUT: ", rut)
        print(f"Nombre: ", nombre)
        print(f"Fono: ", fono)
        print(f"Correo: ", correo)
        print()
    print("-------------------------------------")

def seleccionar_lote():
    while True:
        try:
            fila = int(input("Ingrese la fila del lote: "))
            print("")
            columna = int(input("Ingrese la columna del lote: "))
            print("")
        except ValueError:
            print("Opcion invalida. Intente nuevamente.")
            continue
        if fila < 0 or fila >= n_fila or columna < 0 or columna >= num_columna:
            print("Coordenadas invalidas. Intente nuevamente.")
            continue
        if lotes_d[fila][columna] is None:
            break
        else:
            print("El lote seleccionado no se encuentra disponible. Seleccione otro.")

    print("")
    print("Ahora ingrese los datos de cliente:")
    print("")
    rut_c = input("Ingrese rut de cliente (sin puntos ni guión): ")
    nombre_c = input("Ingrese nombre completo de cliente: ")
    fono_c = input("Ingrese fono de cliente: ")
    correo_c = input("Ingrese correo electronico de cliente: ")

    lotes_seleccionados.append((fila, columna))
    lotes_d[fila][columna] = 'X'
    clientes.append((rut_c, nombre_c, fono_c, correo_c))

    print("")
    print("¡¡¡Felicidades!!!. Lote seleccionado correctamente.")
    print("")


while True:
  print("--------------------- BIENVENIDO AL MENÚ PRINCIPAL LOTEOS DUOC --------------------------")
  print("1 - VER DISPONIBILIDAD DE LOTES")
  print("2 - SELECCIONAR UN LOTE")
  print("3 - VER DETALLES DEL LOTE SELECCIONADO")
  print("4 - VER CLIENTES")
  print("5 - SALIR DEL SISTEMA. ")
  print("-----------------------------------------------------------------------------")
  try:
    menu1 = int(input("Ingrese la opción de su preferencia:"))
    print("")
    if menu1 == 1:
      print("Lotes disponibles:")
      print("")
      mostrar_lotes_d()

    elif menu1 == 2:
      print("Por favor seleccione un lote:")
      print("")
      seleccionar_lote()

    elif menu1 == 3:
      print("Datelles del lote que ha seleccionado:")
      print("")
      mostrar_detalles_lote()

    elif menu1 == 4:
      print("")
      print("Clientes:")
      print("")
      mostrar_clientes()

    else:
      print("****** SALIENDO DEL SISTEMA, HASTA LUEGO!!! *******")
      break
  except ValueError:
    print("Valor ingresado invalido. Intente nuevamente.")
  except TypeError:
    print("Error. Ingrese un valor válido.")