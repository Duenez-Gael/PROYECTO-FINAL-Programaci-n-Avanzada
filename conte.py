
"""
#Lista

class Temperatura:
    def __init__(self):
        self.temperaturas = []

    def agregar(self):
        temp = float(input("Ingrese la nueva temperatura a agregar: "))
        self.temperaturas.append(temp)

    def eliminar(self):
        temp = float(input("Ingrese la temperatura a eliminar: "))
        if temp in self.temperaturas:
            self.temperaturas.remove(temp)
            print(f"Temperatura {temp} eliminada.")
        else:
            print("La temperatura no se encuentra en la lista.")

    def menu(self):
        while True:
            print("\nMenú de opciones:")
            print("1. Agregar nueva temperatura")
            print("2. Eliminar una temperatura")
            print("3. Mostrar temperaturas registradas")
            print("0. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar()
            elif opcion == "2":
                self.eliminar()
            elif opcion == "3":
                print("Temperaturas registradas:", self.temperaturas)
            elif opcion == "0":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida, intente nuevamente.")

temperatura = Temperatura()
temperatura.menu()
"""


"""
#Tupla

class TemperaturaTupla:
    def __init__(self):
        self.temperaturas = ()

    def crear(self):
        n = int(input("¿Cuántas temperaturas quieres ingresar?: "))
        valores = []
        for i in range(n):
            temp = float(input(f"Ingrese la temperatura #{i+1}: "))
            valores.append(temp)
        self.temperaturas = tuple(valores)
        print("Tupla creada correctamente.")

    def mostrar(self):
        if self.temperaturas:
            print("Tupla de temperaturas:", self.temperaturas)
        else:
            print("No has creado una tupla aún.")

    def menu(self):
        while True:
            print("\nMenú de opciones:")
            print("1. Crear tupla de temperaturas")
            print("2. Mostrar tupla")
            print("0. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.crear()
            elif opcion == "2":
                self.mostrar()
            elif opcion == "0":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida, intente nuevamente.")

temperatura = TemperaturaTupla()
temperatura.menu()
"""


"""
#Conjuntos

class Alumnos:
    def __init__(self):
        self.curso1 = set()
        self.curso2 = set()

    def almacenar(self):
        print("Ingresa los alumnos para el curso 1 (separados por comas):")
        alumnos_curso1 = input().split(",")
        self.curso1 = set(alumnos_curso1)

        print("Ingresa los alumnos para el curso 2 (separados por comas):")
        alumnos_curso2 = input().split(",")
        self.curso2 = set(alumnos_curso2)

    def encontrarDuplicado(self):
        duplicados = self.curso1 & self.curso2
        return duplicados

    def encontrarExclusivos(self):
        exclusivos_curso1 = self.curso1 - self.curso2
        exclusivos_curso2 = self.curso2 - self.curso1
        return exclusivos_curso1, exclusivos_curso2

    def alumnosDuplicados(self):
        return self.encontrarDuplicado()

    def alumnosNoDuplicados(self):
        exclusivos_curso1, exclusivos_curso2 = self.encontrarExclusivos()
        return exclusivos_curso1.union(exclusivos_curso2)

    def menu(self):
        while True:
            print("\n--- Menú ---")
            print("1. Almacenar alumnos")
            print("2. Encontrar alumnos duplicados")
            print("3. Encontrar alumnos exclusivos de cada curso")
            print("4. Mostrar alumnos no duplicados")
            print("5. Salir")

            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.almacenar()
            elif opcion == "2":
                duplicados = self.alumnosDuplicados()
                print("Alumnos duplicados en ambos cursos:", duplicados)
            elif opcion == "3":
                exclusivos_curso1, exclusivos_curso2 = self.encontrarExclusivos()
                print("Alumnos exclusivos del curso 1:", exclusivos_curso1)
                print("Alumnos exclusivos del curso 2:", exclusivos_curso2)
            elif opcion == "4":
                no_duplicados = self.alumnosNoDuplicados()
                print("Alumnos no duplicados:", no_duplicados)
            elif opcion == "5":
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")

alumnos = Alumnos()
alumnos.menu()
"""


#Diccionaio

class RegistroEmpleados:
    def __init__(self):
        self.empleados = {
            "E001": {"nombre": "Carlos", "puesto": "Analista", "salario": 35000},
            "E002": {"nombre": "María", "puesto": "Desarrollador", "salario": 40000},
            "E003": {"nombre": "Elena", "puesto": "Gerente", "salario": 60000}
        }

    def agregar_empleado(self):
        id_empleado = input("Ingresa el ID del empleado: ")
        nombre = input("Ingresa el nombre: ")
        puesto = input("Ingresa el puesto: ")
        salario = float(input("Ingresa el salario: "))
        self.empleados[id_empleado] = {"nombre": nombre, "puesto": puesto, "salario": salario}
        print(f"Empleado {id_empleado} agregado.")

    def actualizar_salario(self):
        id_empleado = input("Ingresa el ID del empleado: ")
        if id_empleado in self.empleados:
            nuevo_salario = float(input("Ingresa el nuevo salario: "))
            self.empleados[id_empleado]["salario"] = nuevo_salario
            print(f"Salario de {id_empleado} actualizado.")
        else:
            print("Empleado no encontrado.")

    def eliminar_empleado(self):
        id_empleado = input("Ingresa el ID del empleado a eliminar: ")
        if id_empleado in self.empleados:
            del self.empleados[id_empleado]
            print(f"Empleado {id_empleado} eliminado.")
        else:
            print("Empleado no encontrado.")

    def listar_empleados(self):
        if not self.empleados:
            print("No hay empleados registrados.")
        else:
            print("\n--- Lista de Empleados ---")
            for id_empleado, datos in self.empleados.items():
                print(f"ID: {id_empleado}, Nombre: {datos['nombre']}, Puesto: {datos['puesto']}, Salario: {datos['salario']}")

    def menu(self):
        while True:
            print("\n--- Menú de Registro de Empleados ---")
            print("1. Agregar empleado")
            print("2. Actualizar salario")
            print("3. Eliminar empleado")
            print("4. Listar empleados")
            print("5. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.agregar_empleado()
            elif opcion == "2":
                self.actualizar_salario()
            elif opcion == "3":
                self.eliminar_empleado()
            elif opcion == "4":
                self.listar_empleados()
            elif opcion == "5":
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")

registro = RegistroEmpleados()
registro.menu()


"""
#POSTORDEN

import graphviz
from IPython.display import display

class Nodo:
  def __init__(self, dato):
    self.valor = dato
    self.izq = None
    self.der = None


class ABB:
  def __init__(self):
    self.raiz = None

  def insertar(self, valor):
    if self.raiz is None:
      self.raiz = Nodo(valor)
    else:
      self._insertar_recursividad(self.raiz, valor)

  def _insertar_recursividad(self, nodo, valor):
    if valor < nodo.valor:
      if nodo.izq is None:
        nodo.izq = Nodo(valor)
      else:
        self._insertar_recursividad(nodo.izq, valor)
    elif valor > nodo.valor:
      if nodo.der is None:
        nodo.der = Nodo(valor)
      else:
        self._insertar_recursividad(nodo.der, valor)

  def imprimir(self):
    self._imprimir_recursividad(self.raiz, 0)

  def _imprimir_recursividad(self, nodo, nivel):
    if nodo is not None:
      self._imprimir_recursividad(nodo.der, nivel + 1)
      print('    ' * nivel + f' → {nodo.valor}')
      self._imprimir_recursividad(nodo.izq, nivel + 1)

  def visualizar(self):
    punto = graphviz.Digraph()
    punto.attr('node', shape='circle')

    if self.raiz is not None:
      self._visualizar_recursividad(self.raiz, punto)
    return punto

  def _visualizar_recursividad(self, nodo, punto):
    punto.node(str(nodo.valor))

    if nodo.izq is not None:
      punto.edge(str(nodo.valor), str(nodo.izq.valor))
      self._visualizar_recursividad(nodo.izq, punto)

    if nodo.der is not None:
      punto.edge(str(nodo.valor), str(nodo.der.valor))
      self._visualizar_recursividad(nodo.der, punto)


  def inorden(self):
    print('Inorden:', end=" ")
    self._inorden_recursividad(self.raiz)
    print()

  def _inorden_recursividad(self, nodo):
    if nodo is not None:
      self._inorden_recursividad(nodo.izq)
      print(nodo.valor, end=" ")
      self._inorden_recursividad(nodo.der)

  def preorden(self):
    self._preorden_recursividad(self.raiz)
    print()

  def _preorden_recursividad(self, nodo):
    if nodo is not None:
      print(nodo.valor, end=" ")
      self._preorden_recursividad(nodo.izq)
      self._preorden_recursividad(nodo.der)

  def postorden(self):
    print("Postorden:", end=" ")
    self._postorden_recursividad(self.raiz)
    print()

  def _postorden_recursividad(self,nodo):
    if nodo is not None:
      self._postorden_recursividad(nodo.izq)
      self._postorden_recursividad(nodo.der)
      print(nodo.valor, end=" ")



if __name__ == "__main__":
  abb = ABB()
  for valor in [501, 302, 705, 203, 404, 705, 606, 807]:
    abb.insertar(valor)

  display(abb.visualizar())
  print("")
  print("Recorrido Inorden:")
  abb.inorden()
  print("")
  print("Recorrido Preorden:")
  abb.preorden()
  print("")
  print("Recorrido Postorden:")
  abb.postorden()
"""

"""
import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Grafo:
    def __init__(self):
        self.adyacencias = {}

    def agregarArista(self, origen, destino):
        self.adyacencias.setdefault(origen, []).append(destino)
        self.adyacencias.setdefault(destino, []).append(origen)

    def bfs(self, inicio):
        visitados = set()
        cola = deque([inicio])
        recorrido = []

        while cola:
            nodo = cola.popleft()
            if nodo not in visitados:
                visitados.add(nodo)
                recorrido.append(nodo)
                cola.extend([vecino for vecino in self.adyacencias[nodo] if vecino not in visitados])
        return recorrido

    def graficar(self, recorrido):
        G = nx.Graph()
        for nodo, vecinos in self.adyacencias.items():
            for vecino in vecinos:
                G.add_edge(nodo, vecino)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightgray', edge_color='gray', node_size=800, font_weight='bold')

        colores = ['red', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']
        for i, nodo in enumerate(recorrido):
            nx.draw_networkx_nodes(G, pos, nodelist=[nodo], node_color=colores[i % len(colores)], node_size=800)

        plt.title(f"Recorrido BFS desde '{recorrido[0]}'")
        fig = plt.gcf()
        return fig


class Menu:
    def __init__(self):
        pass

    def menuGama(self):
        pass

    def menuCarac(self):
        pass

    def opc(self, opcion, gama):
        grafo = Grafo()
        inicio = None

        if opcion == 1: # Camara
            if gama == 1: # Gama Alta
                grafo.agregarArista('Camara Pro', 'Apple\niPhone 16 Pro Max')
                grafo.agregarArista('Camara Pro', 'Samsung\nGalaxy S25 Ultra')
                grafo.agregarArista('Apple\niPhone 16 Pro Max', 'Google\nPixel 9 Pro')
                grafo.agregarArista('Samsung\nGalaxy S25 Ultra', 'Xiaomi\nXiaomi 15 Ultra')
                inicio = 'Camara Pro'
            elif gama == 2: # Gama Baja
                grafo.agregarArista('Buena Camara', 'Motorola\nMoto E13')
                grafo.agregarArista('Buena Camara', 'Xiaomi\nRedmi A2')
                grafo.agregarArista('Motorola\nMoto E13', 'Samsung\nGalaxy A03')
                grafo.agregarArista('Xiaomi\nRedmi A2', 'Infinix\nInfinix Smart 7')
                inicio = 'Buena Camara'
            elif gama == 3: # Gama Media
                grafo.agregarArista('Camara Equilibrada', 'Samsung\nGalaxy A24')
                grafo.agregarArista('Camara Equilibrada', 'Xiaomi\nRedmi Note 12')
                grafo.agregarArista('Samsung\nGalaxy A24', 'Realme\nRealme C55')
                grafo.agregarArista('Xiaomi\nRedmi Note 12', 'Motorola\nMoto G32')
                inicio = 'Camara Intermedia'


        elif opcion == 2: # Bateria
            if gama == 1: # Gama Alta
                grafo.agregarArista('Bateria Premium', 'Apple\niPhone 15 Plus')
                grafo.agregarArista('Bateria Premium', 'Samsung\nGalaxy S24 Ultra')
                grafo.agregarArista('Apple\niPhone 15 Plus', 'OnePlus\nOneplus 12R')
                grafo.agregarArista('Xiaomi\nXiaomi 13 Ultra', 'Samsung\nGalaxy S23 Ultra')
                inicio = 'Bateria Premium'
            elif gama == 2: # Gama Baja
                grafo.agregarArista('Buena Bateria', 'Xiaomi\nRedmi 10C')
                grafo.agregarArista('Buena Bateria', 'Motorola\nMoto G13')
                grafo.agregarArista('Motorola\nMoto G13', 'Itel\nIntel P40')
                inicio = 'Buena Bateria'
            elif gama == 3: # Gama Media
                grafo.agregarArista('Bateria Equilibrada', 'Samsung\nSamsung M14')
                grafo.agregarArista('Bateria Equilibrada', 'Realme\nRealme Narzo 50A')
                grafo.agregarArista('Realme\nRealme Narzo 50A', 'Xiaomi\nXiaomi Redmi Note 11')
                inicio = 'Bateria Equilibrada'

        elif opcion == 3: # Almacenamiento
            if gama == 1: # Gama Alta
                grafo.agregarArista('Almacenamiento Alto', 'Samsung\nGalaxy S24 Ultra')
                grafo.agregarArista('Almacenamiento Alto', 'Apple\niPhone 15 Pro Max')
                inicio = 'Almacenamiento Alto'
            elif gama == 2: # Gama Baja
                grafo.agregarArista('Almacenamiento Básico', 'Infinix\nInfinix Smart 6')
                grafo.agregarArista('Almacenamiento Básico', 'Tecno\nTecno Spark 10')
                inicio = 'Almacenamiento Básico'
            elif gama == 3: # Gama Media
                grafo.agregarArista('Almacenamiento Medio', 'Xiaomi\nRedmi Note 11')
                grafo.agregarArista('Almacenamiento Medio', 'Motorola\nMoto G22')
                inicio = 'Almacenamiento Medio'

        elif opcion == 4: # Memoria RAM
            if gama == 1: # Gama Alta
                grafo.agregarArista('RAM Premium', 'Apple\niPhone 15 Pro')
                grafo.agregarArista('RAM Premium', 'Samsung\nGalaxy S23 Ultra')
                inicio = 'RAM Premium'
            elif gama == 2: # Gama Baja
                grafo.agregarArista('RAM Básica', 'Xiaomi\nRedmi A1')
                grafo.agregarArista('RAM Básica', 'Motorola\nMoto E20')
                inicio = 'RAM Básica'
            elif gama == 3: # Gama Media
                grafo.agregarArista('RAM Intermedia', 'Realme\nRealme C25Y')
                grafo.agregarArista('RAM Intermedia', 'Xiaomi\nXiaomi Redmi 10')
                inicio = 'RAM Intermedia'

        elif opcion == 5: # Procesador
            if gama == 1: # Gama Alta
                grafo.agregarArista('Procesador Premium', 'Oneplus\nOneplus 12R')
                grafo.agregarArista('Procesador Premium',  'Apple\niPhone 15 Pro Max')
                inicio = 'Procesador Premium'
            elif gama == 2: # Gama Baja
                grafo.agregarArista('Procesador Básico', 'Infinix\nInfinix Hot 11')
                grafo.agregarArista('Procesador Básico', 'Xiaomi\nRedmi 10A')
                inicio = 'Procesador Básico'
            elif gama == 3: # Gama Media
                grafo.agregarArista('Procesador Medio', 'Motorola\nMoto esge 50 neo')
                grafo.agregarArista('Procesador Medio', 'Xiaomi\nRedmi note 13 pro')
                inicio = 'Procesador Medio'

        if inicio:
            recorrido = grafo.bfs(inicio)
            fig = grafo.graficar(recorrido)
            return recorrido, fig
        else:
            return None, None

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Recomendador de Celulares")

        self.menu = Menu()

        self.gama_label = tk.Label(root, text="Selecciona la Gama:")
        self.gama_label.pack()
        self.gama_var = tk.StringVar(root)
        self.gama_var.set("Gama Alta")
        self.gama_options = ["Gama Alta", "Gama Baja", "Gama Media"]
        self.gama_menu = tk.OptionMenu(root, self.gama_var, *self.gama_options)
        self.gama_menu.pack()

        self.carac_label = tk.Label(root, text="Selecciona la Característica Principal:")
        self.carac_label.pack()
        self.carac_var = tk.StringVar(root)
        self.carac_var.set("Camara")
        self.carac_options = ["Camara", "Bateria", "Almacenamiento", "Memoria RAM", "Procesador"]
        self.carac_menu = tk.OptionMenu(root, self.carac_var, *self.carac_options)
        self.carac_menu.pack()

        self.search_button = tk.Button(root, text="Buscar Recomendación", command=self.buscar_recomendacion)
        self.search_button.pack()

        self.graph_frame = tk.Frame(root)
        self.graph_frame.pack()
        self.canvas = None

    def buscar_recomendacion(self):
        selected_gama_text = self.gama_var.get()
        selected_carac_text = self.carac_var.get()

        gama_map = {"Gama Alta": 1, "Gama Baja": 2, "Gama Media": 3}
        carac_map = {"Camara": 1, "Bateria": 2, "Almacenamiento": 3, "Memoria RAM": 4, "Procesador": 5}

        gama_value = gama_map.get(selected_gama_text)
        carac_value = carac_map.get(selected_carac_text)

        if gama_value is not None and carac_value is not None:
            recorrido, fig = self.menu.opc(carac_value, gama_value)
            if recorrido:
                messagebox.showinfo("Recorrido BFS", f"Recorrido BFS: {recorrido}")
                if fig:
                    if self.canvas:
                        self.canvas.get_tk_widget().destroy()
                        plt.close(self.canvas.figure)

                    self.canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
                    self.canvas.draw()
                    self.canvas.get_tk_widget().pack()
            else:
                messagebox.showwarning("Advertencia", "No se encontraron recomendaciones para esta combinación.")
        else:
            messagebox.showerror("Error", "Selecciones inválidas. Por favor, contacte al desarrollador.")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    
"""