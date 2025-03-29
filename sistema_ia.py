import heapq  # Importamos heapq para usar una cola de prioridad en el algoritmo de Dijkstra.

class SistemaTransporte:
    def __init__(self):
        """
        Constructor de la clase que define el grafo del sistema de transporte.
        Cada nodo representa una estación y las aristas indican la conexión con su costo (tiempo en minutos).
        """
        self.grafo = {
            'A': {'B': 5, 'C': 10},  # Desde A a B cuesta 5 minutos, desde A a C cuesta 10 minutos.
            'B': {'A': 5, 'D': 7, 'E': 3},  # B se conecta con A, D y E con sus respectivos costos.
            'C': {'A': 10, 'F': 8},  # C se conecta con A y F.
            'D': {'B': 7, 'E': 2, 'G': 6},  # D se conecta con B, E y G.
            'E': {'B': 3, 'D': 2, 'H': 4},  # E se conecta con B, D y H.
            'F': {'C': 8, 'I': 12},  # F se conecta con C e I.
            'G': {'D': 6, 'H': 5},  # G se conecta con D y H.
            'H': {'E': 4, 'G': 5, 'I': 7},  # H se conecta con E, G e I.
            'I': {'F': 12, 'H': 7}  # I se conecta con F y H.
        }

    def encontrar_mejor_ruta(self, inicio, destino):
        """
        Implementa el algoritmo de Dijkstra para encontrar la ruta más corta entre dos estaciones.

        Parámetros:
        - inicio: La estación de origen.
        - destino: La estación de destino.

        Retorna:
        - Una tupla con la mejor ruta (lista de estaciones) y el costo total del viaje.
        """
        heap = [(0, inicio)]  # Cola de prioridad inicializada con el nodo de inicio y costo 0.
        costos = {nodo: float('inf') for nodo in self.grafo}  # Inicializamos costos como infinito.
        costos[inicio] = 0  # El costo de la estación de inicio es 0.
        ruta = {nodo: None for nodo in self.grafo}  # Diccionario para rastrear el camino más corto.

        while heap:  # Mientras haya nodos por explorar
            costo_actual, nodo_actual = heapq.heappop(heap)  # Extraemos el nodo con menor costo acumulado.

            if nodo_actual == destino:  # Si hemos llegado al destino, terminamos la búsqueda.
                break  

            for vecino, costo in self.grafo[nodo_actual].items():  # Exploramos las conexiones del nodo actual.
                nuevo_costo = costo_actual + costo  # Calculamos el costo total para llegar al vecino.

                if nuevo_costo < costos[vecino]:  # Si encontramos un camino más corto al vecino
                    costos[vecino] = nuevo_costo  # Actualizamos el costo mínimo.
                    ruta[vecino] = nodo_actual  # Registramos de dónde venimos.
                    heapq.heappush(heap, (nuevo_costo, vecino))  # Añadimos el vecino a la cola de prioridad.

        # Reconstrucción de la ruta óptima desde el destino hasta el origen
        camino = []
        nodo = destino
        while nodo:  # Recorremos hacia atrás usando el diccionario de rutas.
            camino.append(nodo)
            nodo = ruta[nodo]
        camino.reverse()  # Invertimos la lista para que vaya de inicio a destino.

        return camino, costos[destino]  # Retornamos la mejor ruta y el costo total.

# Ejemplo de uso del sistema:
sistema = SistemaTransporte()
punto_A = 'A'  # Estación de inicio.
punto_B = 'I'  # Estación de destino.

# Llamamos a la función para obtener la mejor ruta y su costo.
ruta_optima, costo_total = sistema.encontrar_mejor_ruta(punto_A, punto_B)

# Mostramos el resultado en la consola.
print(f"Mejor ruta de {punto_A} a {punto_B}: {' → '.join(ruta_optima)}")
print(f"Costo total del viaje: {costo_total} minutos")
