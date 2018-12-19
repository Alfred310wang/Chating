from pygraphviz import *
g=AGraph(
        rankdir='LR',
        directed=True
        )
g.add_node('user',shape='doublecircle')
g.add_edge('user','state1',label='advance[is_going_to_state1]')
g.add_edge('user','state2',label='advance[is_going_to_state2]')
g.add_edge('user','state3',label='advance[is_going_to_state3]')
g.add_edge('state3','state3_1',label='advance[is_going_to_state3_1]')
g.add_edge('state3_1','user',label='go_back')
g.add_edge('state2','user',label='go_back')
g.add_edge('state1','user',label='go_back')
g.graph_attr['label']='State Machine'
g.node_attr['shape']='circle'
g.layout(prog='dot')
g.draw('fsm_graph.png')

