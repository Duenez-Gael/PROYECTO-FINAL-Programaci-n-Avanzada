import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt


# Estructuras globales
cola = []
pila = []

class Cola:
    def __init__(self, padre):
        self.ventana = tk.Toplevel(padre)
        self.ventana.title("COLAS")
        self.ventana.geometry("400x300")
        self._crear_interfaz()

    def _crear_interfaz(self):
        self.etiquetac1 = tk.Label(self.ventana, text="Ingresa un valor:", font=("Arial", 10))
        self.etiquetac2 = tk.Label(self.ventana, text="Ingresa un valor:", font=("Arial", 10))
        self.entradac1 = tk.Entry(self.ventana, width=30)
        self.entradac2 = tk.Entry(self.ventana, width=30)
        self.etiqueta_mcola = tk.Label(self.ventana, text="", font=("Arial", 10))

        self.boton_encolar = tk.Button(self.ventana, text="Encolar", command=self.encolar)
        self.boton_desencolar = tk.Button(self.ventana, text="Desencolar", command=self.desencolar)
        self.boton_mostrar = tk.Button(self.ventana, text="Mostrar Cola", command=self.mostrar_cola)

        self.etiquetac1.pack(pady=5)
        self.entradac1.pack(pady=5)
        self.etiquetac2.pack(pady=5)
        self.entradac2.pack(pady=5)
        self.boton_encolar.pack(pady=5)
        self.boton_desencolar.pack(pady=5)
        self.boton_mostrar.pack(pady=5)
        self.etiqueta_mcola.pack(pady=5)

    def encolar(self):
        v1 = self.entradac1.get()
        v2 = self.entradac2.get()
        if v1 and v2:
            cola.append(v1)
            cola.append(v2)
            self.entradac1.delete(0, tk.END)
            self.entradac2.delete(0, tk.END)

    def desencolar(self):
        if cola:
            cola.pop(0)

    def mostrar_cola(self):
        self.etiqueta_mcola.config(text=f"Cola: {cola}")


class Pila:
    def __init__(self, padre):
        self.ventana = tk.Toplevel(padre)
        self.ventana.title("PILAS")
        self.ventana.geometry("400x300")
        self._crear_interfaz()

    def _crear_interfaz(self):
        self.etiquetap1 = tk.Label(self.ventana, text="Ingresa un valor:", font=("Arial", 10))
        self.etiquetap2 = tk.Label(self.ventana, text="Ingresa un valor:", font=("Arial", 10))
        self.entradap1 = tk.Entry(self.ventana, width=30)
        self.entradap2 = tk.Entry(self.ventana, width=30)
        self.etiqueta_mpila = tk.Label(self.ventana, text="", font=("Arial", 10))

        self.boton_apilar = tk.Button(self.ventana, text="Apilar", command=self.apilar)
        self.boton_desapilar = tk.Button(self.ventana, text="Desapilar", command=self.desapilar)
        self.boton_mostrar = tk.Button(self.ventana, text="Mostrar Pila", command=self.mostrar_pila)

        self.etiquetap1.pack(pady=5)
        self.entradap1.pack(pady=5)
        self.etiquetap2.pack(pady=5)
        self.entradap2.pack(pady=5)
        self.boton_apilar.pack(pady=5)
        self.boton_desapilar.pack(pady=5)
        self.boton_mostrar.pack(pady=5)
        self.etiqueta_mpila.pack(pady=5)

    def apilar(self):
        v1 = self.entradap1.get()
        v2 = self.entradap2.get()
        if v1 and v2:
            pila.append(v1)
            pila.append(v2)
            self.entradap1.delete(0, tk.END)
            self.entradap2.delete(0, tk.END)

    def desapilar(self):
        if pila:
            pila.pop()

    def mostrar_pila(self):
        self.etiqueta_mpila.config(text=f"Pila: {pila}")


class Contenedores:
    def __init__(self, padre, tipo):
        self.tipo = tipo
        self.ventana = tk.Toplevel(padre)
        self.ventana.title(tipo.upper())
        self.ventana.geometry("400x300")
        self._crear_interfaz()

    def _crear_interfaz(self):
        if self.tipo == "listas":
            self.lista = []
            self.entrada = tk.Entry(self.ventana, width=30)
            self.boton_agregar = tk.Button(self.ventana, text="Agregar", command=self.agregar_lista)
            self.boton_eliminar = tk.Button(self.ventana, text="Eliminar", command=self.eliminar_lista)
            self.boton_mostrar = tk.Button(self.ventana, text="Mostrar", command=self.mostrar_lista)
            self.etiqueta = tk.Label(self.ventana, text="", font=("Arial", 10))

            self.entrada.pack(pady=5)
            self.boton_agregar.pack(pady=5)
            self.boton_eliminar.pack(pady=5)
            self.boton_mostrar.pack(pady=5)
            self.etiqueta.pack(pady=5)

        elif self.tipo == "tuplas":
            self.tupla = ()
            self.entrada = tk.Entry(self.ventana, width=30)
            self.boton_crear = tk.Button(self.ventana, text="Crear tupla", command=self.crear_tupla)
            self.boton_mostrar = tk.Button(self.ventana, text="Mostrar", command=self.mostrar_tupla)
            self.etiqueta = tk.Label(self.ventana, text="", font=("Arial", 10))

            self.entrada.pack(pady=5)
            self.boton_crear.pack(pady=5)
            self.boton_mostrar.pack(pady=5)
            self.etiqueta.pack(pady=5)

        elif self.tipo == "conjuntos":
            self.curso1 = set()
            self.curso2 = set()
            self.entrada1 = tk.Entry(self.ventana, width=30)
            self.entrada2 = tk.Entry(self.ventana, width=30)
            self.boton_cargar = tk.Button(self.ventana, text="Cargar alumnos", command=self.cargar_conjuntos)
            self.boton_duplicados = tk.Button(self.ventana, text="Duplicados", command=self.mostrar_duplicados)
            self.boton_exclusivos = tk.Button(self.ventana, text="Exclusivos", command=self.mostrar_exclusivos)
            self.etiqueta = tk.Label(self.ventana, text="", font=("Arial", 10))

            self.entrada1.pack(pady=5)
            self.entrada2.pack(pady=5)
            self.boton_cargar.pack(pady=5)
            self.boton_duplicados.pack(pady=5)
            self.boton_exclusivos.pack(pady=5)
            self.etiqueta.pack(pady=5)

        elif self.tipo == "diccionarios":
            self.empleados = {}
            self.entrada_id = tk.Entry(self.ventana, width=30)
            self.entrada_nombre = tk.Entry(self.ventana, width=30)
            self.entrada_puesto = tk.Entry(self.ventana, width=30)
            self.entrada_salario = tk.Entry(self.ventana, width=30)
            self.boton_agregar = tk.Button(self.ventana, text="Agregar", command=self.agregar_empleado)
            self.boton_listar = tk.Button(self.ventana, text="Listar", command=self.listar_empleados)
            self.etiqueta = tk.Label(self.ventana, text="", font=("Arial", 10))

            self.entrada_id.pack(pady=2)
            self.entrada_nombre.pack(pady=2)
            self.entrada_puesto.pack(pady=2)
            self.entrada_salario.pack(pady=2)
            self.boton_agregar.pack(pady=5)
            self.boton_listar.pack(pady=5)
            self.etiqueta.pack(pady=5)

    def agregar_lista(self):
        valor = self.entrada.get()
        self.lista.append(valor)
        self.entrada.delete(0, tk.END)

    def eliminar_lista(self):
        valor = self.entrada.get()
        if valor in self.lista:
            self.lista.remove(valor)
        self.entrada.delete(0, tk.END)

    def mostrar_lista(self):
        self.etiqueta.config(text=f"Lista: {self.lista}")

    def crear_tupla(self):
        datos = self.entrada.get().split(',')
        self.tupla = tuple(map(str.strip, datos))

    def mostrar_tupla(self):
        self.etiqueta.config(text=f"Tupla: {self.tupla}")

    def cargar_conjuntos(self):
        self.curso1 = set(map(str.strip, self.entrada1.get().split(',')))
        self.curso2 = set(map(str.strip, self.entrada2.get().split(',')))

    def mostrar_duplicados(self):
        duplicados = self.curso1 & self.curso2
        self.etiqueta.config(text=f"Duplicados: {duplicados}")

    def mostrar_exclusivos(self):
        exclusivos = (self.curso1 - self.curso2) | (self.curso2 - self.curso1)
        self.etiqueta.config(text=f"Exclusivos: {exclusivos}")

    def agregar_empleado(self):
        try:
            id_emp = self.entrada_id.get()
            nombre = self.entrada_nombre.get()
            puesto = self.entrada_puesto.get()
            salario = float(self.entrada_salario.get())
            self.empleados[id_emp] = {"nombre": nombre, "puesto": puesto, "salario": salario}
        except ValueError:
            messagebox.showerror("Error", "Salario inválido")

    def listar_empleados(self):
        texto = "\n".join([f"{id}: {info['nombre']}, {info['puesto']}, ${info['salario']}" for id, info in self.empleados.items()])
        self.etiqueta.config(text=texto or "No hay empleados registrados")



class Grafo:
    def __init__(self, padre, tipo):
        self.ventana = tk.Toplevel(padre)
        self.ventana.title(f"Grafo {tipo}")
        self.ventana.geometry("400x150")
        self.tipo = tipo
        self._crear_interfaz()

    def _crear_interfaz(self):
        etiqueta = tk.Label(self.ventana, text=f"Grafo {self.tipo}", font=("Arial", 12, "bold"))
        etiqueta.pack(pady=10)

        boton_mostrar = tk.Button(self.ventana, text="Mostrar grafo", command=self.mostrar_grafo)
        boton_mostrar.pack(pady=10)

    def mostrar_grafo(self):
        if self.tipo == "No Dirigido":
            self.grafo_no_dirigido()
        elif self.tipo == "Dirigido":
            self.grafo_dirigido()
        elif self.tipo == "Ponderado":
            self.grafo_ponderado()
        elif self.tipo == "Matriz de Adyacencia":
            self.grafo_matriz_adyacencia()

    def grafo_no_dirigido(self):
        G = nx.Graph()
        G.add_nodes_from(["A", "B", "C", "D"])
        G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')])
        plt.figure()
        plt.gcf().canvas.manager.set_window_title("Grafo No Dirigido")
        nx.draw(G, with_labels=True)
        plt.show()

    def grafo_dirigido(self):
        g = nx.DiGraph()
        g.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F'])
        g.add_edges_from([
            ('A', 'B'), ('A', 'C'),
            ('B', 'D'), ('B', 'E'),
            ('B', 'F')
        ])
        plt.figure(figsize=(5, 5))
        plt.gcf().canvas.manager.set_window_title("Grafo Dirigido")
        nx.draw(g, with_labels=True, arrows=True,
                node_color='skyblue', edge_color='black',
                node_size=2000, font_size=12)
        plt.title("Grafo Dirigido \n Angel Gael")
        plt.show()

    def grafo_ponderado(self):
        g = nx.DiGraph()
        g.add_edge('A', 'B', weight=8)
        g.add_edge('A', 'C', weight=22)
        g.add_edge('B', 'C', weight=4)

        pos = nx.spring_layout(g)
        plt.figure()
        nx.draw(g, pos, with_labels=True, font_color='black',
                node_color='skyblue', node_size=2000,
                font_size=15, font_weight='bold', arrows=True)

        edge_labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)
        plt.gcf().canvas.manager.set_window_title("Grafo Ponderado")
        plt.title("Grafo Ponderado")
        plt.show()

    def grafo_matriz_adyacencia(self):
        class MatrizGrafo:
            def __init__(self, numVertices, dirigido=False):
                self.numVertices = numVertices
                self.dirigido = dirigido
                self.matriz = [[0] * numVertices for _ in range(numVertices)]

            def agregar_arista(self, origen, destino, peso=1):
                self.matriz[origen][destino] = peso
                if not self.dirigido:
                    self.matriz[destino][origen] = peso

            def visualizar(self):
                G = nx.DiGraph() if self.dirigido else nx.Graph()
                for i in range(self.numVertices):
                    G.add_node(i)
                for i in range(self.numVertices):
                    for j in range(self.numVertices):
                        if self.matriz[i][j] != 0:
                            G.add_edge(i, j, weight=self.matriz[i][j])
                pos = nx.spring_layout(G)
                plt.figure()
                nx.draw(G, pos, with_labels=True, node_color='skyblue',
                        edge_color='black', node_size=2000, font_size=12)
                edge_labels = nx.get_edge_attributes(G, 'weight')
                nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
                plt.title("Matriz y Grafo\nAGael")
                plt.gcf().canvas.manager.set_window_title("Matriz de Adyacencia")
                plt.show()

        grafo = MatrizGrafo(4, dirigido=False)
        grafo.agregar_arista(0, 1)
        grafo.agregar_arista(0, 2)
        grafo.agregar_arista(1, 3)
        grafo.visualizar()


class MenuPrincipal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Proyecto Final AG")
        self.ventana.geometry("600x400")
        self.crear_menu()

    def crear_menu(self):
        barra_menu = tk.Menu(self.ventana)

        estructura_menus = {
            "Principal": {
                "Salir": self._salir
            },
            "Programación Avanzada": {
                "Contenedores": {
                    "Listas": lambda: Contenedores(self.ventana, "listas"),
                    "Tuplas": lambda: Contenedores(self.ventana, "tuplas"),
                    "Conjuntos": lambda: Contenedores(self.ventana, "conjuntos"),
                    "Diccionarios": lambda: Contenedores(self.ventana, "diccionarios")
                },
                "Pilas y Colas": {
                    "Pilas": lambda: Pila(self.ventana),
                    "Colas": lambda: Cola(self.ventana)
                },
                "Grafos": {
                    "No Dirigidos": lambda: Grafo(self.ventana, "No Dirigido"),
                    "Dirigidos": lambda: Grafo(self.ventana, "Dirigido"),
                    "Ponderado": lambda: Grafo(self.ventana, "Ponderado"),
                    "Matriz de Adyacencia": lambda: Grafo(self.ventana, "Matriz de Adyacencia")
                },
                "Arbol Binario":{
                    
                },
                "Concurrencia":{
                    
                }
            },
            "Proyecto":{
                
                
            },
            
            "Ayuda": {
                "Acerca de": self._acerca
            }
        }

        def crear_submenu(padre, estructura):
            for etiqueta, accion in estructura.items():
                if callable(accion):
                    padre.add_command(label=etiqueta, command=accion)
                elif isinstance(accion, dict):
                    submenu = tk.Menu(padre, tearoff=0)
                    crear_submenu(submenu, accion)
                    padre.add_cascade(label=etiqueta, menu=submenu)

        crear_submenu(barra_menu, estructura_menus)
        self.ventana.config(menu=barra_menu)

    def _salir(self):
        self.ventana.quit()
        self.ventana.destroy()

    def _acerca(self):
        messagebox.showinfo("Acerca de", "Programa de Programación Avanzada\npor Angel Gael Dueñez Mejia\nGrupo 2CV13")


if __name__ == "__main__":
    menu = MenuPrincipal()
    menu.ventana.mainloop()