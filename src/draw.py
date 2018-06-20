import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
from bokeh.palettes import Spectral8

from graph import *

graph_data = Graph()
graph_data.debug_create_test_data()
print(graph_data.vertexes)

# Cannot just increase this to get more vertexes
# Bokeh works if you decrease the number though - it will render what it can in
# the case of incomplete data.
N = len(graph_data.vertexes) # makes N dynamic
node_indices = list(range(N))

color_list = []
for vertex in graph_data.vertexes:
    color_list.append(vertex.color)

# debug_pallete += [a, b, c] # Can use this format as well to combine into one line

plot = figure(title='Graph Layout Demonstration', x_range=(0, 500), y_range=(0,500),
              tools='', toolbar_location=None)

graph = GraphRenderer()

# Adds node indices (N of them)
graph.node_renderer.data_source.add(node_indices, 'index')
# Spectral8 is a list of colors
graph.node_renderer.data_source.add(color_list, 'color')
graph.node_renderer.glyph = Oval(height=10, width=10, fill_color='color')

graph.edge_renderer.data_source.data = dict(
    start=[0]*N,
    end=node_indices)

### start of layout code
# Looks like this is setting the positions of the vertexes
x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)

output_file('graph.html')
show(plot)