class Graph:
    def __init__(self):
        self.graph = {}

    def addNode(self, node):
        if node not in self.graph:
            self.graph[node] = {}

    def addEdge(self, origen, fin, peso):
        if origen not in self.graph:
            self.graph[origen] = {}
        if fin not in self.graph:
            self.graph[fin] = {}
        self.graph[origen][fin] = peso

    def stable_marriage(self, men_list, women_list, men_pref, women_pref):
        n = len(men_list)
        unmarried_men = men_list.copy()
        man_spouse = [None] * n
        woman_spouse = [None] * n
        next_man_choice = [0] * n

        while unmarried_men:
            for i, man in enumerate(unmarried_men):
                # Hombre propone a la siguiente mujer en su lista
                woman = men_pref[man][next_man_choice[i]]
                her_spouse = woman_spouse[women_list.index(woman)]

                if her_spouse is None:
                    # Ella está libre, acepta la propuesta
                    man_spouse[men_list.index(man)] = woman
                    woman_spouse[women_list.index(woman)] = man
                    unmarried_men.remove(man)
                elif women_pref[woman].index(man) < women_pref[woman].index(her_spouse):
                    # Ella prefiere a este hombre a su actual esposo
                    man_spouse[men_list.index(man)] = woman
                    woman_spouse[women_list.index(woman)] = man
                    unmarried_men.remove(man)
                    unmarried_men.append(her_spouse)
                else:
                    # Ella rechaza la propuesta, el hombre pasa a la siguiente mujer en su lista
                    next_man_choice[i] += 1

        return man_spouse

    def findMariage(self):
        hombres = []
        mujeres = []
        for i in self.graph:
            if i[0] == "M":
                hombres.append(i)
            else:
                mujeres.append(i)

        hombres.sort()
        mujeres.sort()

        hombres_pref = {}
        mujeres_pref = {}

        for i in hombres:
            hombres_pref[i] = [
                j[0] for j in sorted(self.graph[i].items(), key=lambda x: x[1])
            ]

        for i in mujeres:
            mujeres_pref[i] = [
                j[0] for j in sorted(self.graph[i].items(), key=lambda x: x[1])
            ]

        return self.stable_marriage(hombres, mujeres, hombres_pref, mujeres_pref)


def main():
    grafo = Graph()
    grafo.addNode("W1")
    grafo.addNode("W2")
    grafo.addNode("W3")
    grafo.addNode("W4")
    grafo.addNode("M1")
    grafo.addNode("M2")
    grafo.addNode("M3")
    grafo.addNode("M4")

    grafo.addEdge("W1", "M4", 1)
    grafo.addEdge("W1", "M3", 2)
    grafo.addEdge("W1", "M1", 3)
    grafo.addEdge("W1", "M2", 4)

    grafo.addEdge("W2", "M2", 1)
    grafo.addEdge("W2", "M1", 2)
    grafo.addEdge("W2", "M3", 3)
    grafo.addEdge("W2", "M4", 4)

    grafo.addEdge("W3", "M1", 1)
    grafo.addEdge("W3", "M3", 2)
    grafo.addEdge("W3", "M4", 3)
    grafo.addEdge("W3", "M2", 4)

    grafo.addEdge("W4", "M4", 1)
    grafo.addEdge("W4", "M3", 2)
    grafo.addEdge("W4", "M1", 3)
    grafo.addEdge("W4", "M2", 4)

    """ hombres """

    grafo.addEdge("M1", "W3", 2)
    grafo.addEdge("M1", "W2", 1)
    grafo.addEdge("M1", "W4", 3)
    grafo.addEdge("M1", "W1", 4)

    grafo.addEdge("M2", "W2", 1)
    grafo.addEdge("M2", "W3", 2)
    grafo.addEdge("M2", "W1", 3)
    grafo.addEdge("M2", "W4", 4)

    grafo.addEdge("M3", "W3", 1)
    grafo.addEdge("M3", "W1", 2)
    grafo.addEdge("M3", "W2", 3)
    grafo.addEdge("M3", "W4", 4)

    grafo.addEdge("M4", "W3", 1)
    grafo.addEdge("M4", "W2", 2)
    grafo.addEdge("M4", "W4", 3)
    grafo.addEdge("M4", "W1", 4)

    mariages = grafo.findMariage()

    for i in range(len(mariages)):
        print(f"M{i+1} se casa con {mariages[i]}")


if __name__ == "__main__":
    main()
