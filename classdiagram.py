from graphviz import Digraph

# Create the class diagram
diagram = Digraph(comment='Class Diagram')

# Define classes (nodes)
diagram.node('A', 'DisneylandReviewAnalyser')
diagram.node('B', 'DataProcessor')
diagram.node('C', 'Visualizer')
diagram.node('D', 'DataExporter')
diagram.node('E', 'UserInterface')

# Define relationships (edges)
diagram.edge('A', 'B', label='uses')
diagram.edge('A', 'C', label='uses')
diagram.edge('A', 'D', label='uses')
diagram.edge('A', 'E', label='uses')

# Render the diagram to a file
diagram.render('class_diagram', format='png', cleanup=True)