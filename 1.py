"""
Varias ciudades están conectadas por una red de carreteras. Cada carretera es bidireccional
y conecta dos ciudades, con un tiempo de viaje determinado. ¿Cuál es el tiempo más corto
para llegar de una ciudad dada a otra ciudad dada?
• Cree un algoritmo que tomando los valores del INPUT genere el resultado que se
visualice en el OUTPUT (ver ejemplo)
• Señale que algoritmo o técnica ha utilizado para resolver el problema
INPUT
La primera línea de entrada contiene el número de casos de prueba.
Cada caso de prueba comienza con una línea que contiene el número de ciudades n (2 ≤ n ≤
100000), el número de carreteras m (1 ≤ m ≤ 100000), la ciudad inicial y la ciudad final. Las
ciudades están numeradas del 1 al n.
Luego siguen m líneas, cada una describiendo una carretera. La descripción consiste en los
dos números de ciudad distintos y el tiempo en minutos para viajar a lo largo de la
carretera. El tiempo será entre 1 y 1000.
OUTPUT
Para cada caso de prueba, genere una sola línea que contenga el tiempo mínimo que se
tarda en llegar desde el inicio hasta el destino. Si no existe ninguna conexión,
salida NINGUNO.
Ejemplo:
Input:
2
4 2 1 4
1 2 5
3 4 5
4 4 1 4
1 2 5
2 3 5
3 4 5
4 2 6
Output:
NINGUNO
11
"""


# grofo no dirigido con pesos
class Graph:
    """
    The Graph class represents a graph data structure and provides methods for adding edges between nodes
    and finding the shortest path between two nodes using Dijkstra's algorithm.
    """

    def __init__(self):
        """
        Initializes an empty graph.
        """
        self.graph = {}

    def addNode(self, node):
        """
        Adds a node to the graph.
        :param node: The node to be added.
        """
        if node not in self.graph:
            self.graph[node] = {}

    def addEdge(self, origen, fin, peso):
        """
        Adds an edge between two nodes with a given weight.
        :param origen: The starting node.
        :param fin: The ending node.
        :param peso: The weight of the edge.
        """
        if origen not in self.graph:
            self.graph[origen] = {}
        if fin not in self.graph:
            self.graph[fin] = {}
        self.graph[origen][fin] = peso
        self.graph[fin][origen] = peso

    def dijkstra(self, origen, destino):
        """
        Encuentra la ruta más corta desde el nodo de origen al nodo de destino usando el algoritmo de Dijkstra.
        :param origen: El nodo de inicio.
        :param destino: El nodo de destino.
        :return: Una lista que contiene la ruta más corta desde el nodo de origen al nodo de destino, o None si no hay ruta.
        :return: El peso de la ruta más corta desde el nodo de origen al nodo de destino, o None si no hay ruta.
        """
        distancias = {node: float("infinity") for node in self.graph}
        distancias[origen] = 0

        nodos_no_visitados = list(self.graph.keys())
        camino_anterior = {}

        while nodos_no_visitados:
            nodo_actual = min(nodos_no_visitados, key=lambda node: distancias[node])
            nodos_no_visitados.remove(nodo_actual)

            if distancias[nodo_actual] == float("infinity"):
                break

            for vecino, peso in self.graph[nodo_actual].items():
                ruta_alternativa = distancias[nodo_actual] + peso
                if ruta_alternativa < distancias[vecino]:
                    distancias[vecino] = ruta_alternativa
                    camino_anterior[vecino] = nodo_actual

        camino = []
        peso = 0
        nodo_actual = destino
        while nodo_actual != origen:
            try:
                camino.insert(0, nodo_actual)
                nodo_actual = camino_anterior[nodo_actual]
                # agrega el peso
                peso += self.graph[nodo_actual][camino[0]]
            except KeyError:
                return None
        camino.insert(0, origen)

        return camino, peso


def main():
    grafo = Graph()
    grafo.addNode(1)
    grafo.addNode(2)
    grafo.addNode(3)
    grafo.addNode(4)
    grafo.addEdge(1, 2, 5)
    grafo.addEdge(2, 3, 5)
    grafo.addEdge(3, 4, 5)
    grafo.addEdge(4, 2, 6)
    path, peso = grafo.dijkstra(1, 4)
    print(path)
    print(peso)


if __name__ == "__main__":
    main()
