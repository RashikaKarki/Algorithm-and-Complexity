import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx


def main(path, label):

    sel = ["fb-pages-government",
            "fb-pages-public-figure",
            "fb-pages-politician",
            "fb-pages-tvshow"]

    if label in sel:
        E = pd.read_csv(path, sep=",", header=None, names=["a", "b", "w"])
        G = nx.from_pandas_edgelist(E, "a", "b", ["w"])
    else:
        E = pd.read_csv(path, sep=" ", header=None, names=["a", "b", "w"])
        G = nx.from_pandas_edgelist(E, "a", "b", ["w"])
    
    return G

def node_count(G):
    return nx.number_of_nodes(G)

def edge_count(G):
    return nx.number_of_edges(G)

def density(G):
    e = edge_count(G)
    n = node_count(G)
    return (2*e)/(n*(n-1))

def vertex_degree(G, V):
    return len(G.adj[V])

def average_degree(G):
    i = 0
    for V in G.nodes:
        i += vertex_degree(G, V)
    return i/node_count(G)

def diameter(G):
    return nx.diameter(G)

def clustering_coefficient(G):
    coefficients = {}
    for V in G.nodes:
        k = len(G.adj[V])
        if(k <= 1):
            coefficients[V] = 0
            continue
        e = 0
        for v in G.adj[V]:
            for u in G.adj[V]:
                if(v == u):
                    continue
                if(G.has_edge(u, v)):
                    e += 1
        e = e/2
        coefficients[V] = (2*e)/(k*(k-1))
    return coefficients

def degree_distribution(G):
    degrees = {i: 0 for i in range(len(G.nodes))}
    for i in G.nodes:
        degrees[vertex_degree(G, i)] += 1
    for i in range(len(degrees)):
        degrees[i] /= len(G.nodes)
    return degrees

def plot(G, label):
    a = degree_distribution(G)
    keys = a.keys()
    values = a.values()
    plt.figure(num=label)
    plt.xlabel("$k$")
    plt.ylabel("$P(k)$")
    plt.title(label)
    plt.plot(keys, values)


def draw_graph(G):
    nx.draw(G)
    plt.show()


if __name__ == "__main__":
    
    labels = ["fb-pages-public-figure",
          "fb-pages-politician",
          "fb-pages-tvshow",
          "soc-wiki-elec"]

    for label in labels:
        G = main('data/'+ label + '/' + label+ '.edges', label)
        print()
        print()
        print(label)
        print()
        print("NODE COUNT")
        print(node_count(G))
        print("EDGE COUNT")
        print(edge_count(G))
        print("DENSITY")
        print(density(G))
        print("AVERAGE DEGREE")
        print(average_degree(G))
        print("DIAMETER")
        print(diameter(G))
        print("CLUSTERING COEFFICIENT")
        print(clustering_coefficient(G))
        print("DEGREE DISTRIBUTION")
        print(degree_distribution(G))
 
