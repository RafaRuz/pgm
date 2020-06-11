import networkx as nx
import pygraphviz
from matplotlib import pylab as plt

# Visualizar los modelos de pomegranate haciendo uso de la librería NetworkX  
def plot_pomegranate_bn_nx(pgm, layout=None, node_size=2000, node_color='pink'):
    G = nx.DiGraph()
    for parent, child in pgm.edges:
        G.add_edge(parent.name, child.name)

    if layout==None:
        pos = nx.drawing.nx_agraph.graphviz_layout(G, prog='dot')
    else:
        pos = layout(G)
    nx.draw(G, pos=pos, with_labels=True, node_size=node_size, node_color=node_color)
    plt.show()
    
    
# Visualizar los modelos de pomegranate haciendo uso de la librería GraphViz
def plot_pomegranate_bn_pgvz(pgm, filename=None, prog='dot', color='red'):
    if pygraphviz is not None:
        G = pygraphviz.AGraph(directed=True)

        for state in pgm.states:
            G.add_node(state.name, color=color)

        for parent, child in pgm.edges:
            G.add_edge(parent.name, child.name)
        
        if filename is None:
            tf = os.path.join(tempfile._get_default_tempdir(), next(tempfile._get_candidate_names())+'.png')
            G.draw(tf, format='png', prog=prog)
            img = matplotlib.image.imread(tf)
            plt.imshow(img)
            plt.axis('off')
            os.unlink(tf)
        else:
            G.draw(filename, format='png', prog=prog)

    else:
        raise ValueError("must have pygraphviz installed for visualization")
        

# Visualizar redes de PGM con NetworkX
def plot_pgmpy_bn(pgm, layout=None, node_size=2000, node_color='pink'):
    pos=None
    if layout=='graphviz':
        pos = nx.drawing.nx_agraph.graphviz_layout(pgm, prog='dot')
    elif layout!=None:
        pos = layout(G)
    nx.draw(pgm, pos=pos, with_labels=True, node_size=node_size, node_color=node_color)
    plt.show()