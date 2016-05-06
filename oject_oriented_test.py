class Graph(object):
    def __init__(self,graph_dict={}):
        self.graph_dict = graph_dict
    
    def nodes(self):
        return list(self.graph_dict.keys())

    def edges(self):

g ={'a': {'c':2}, 'b': {'c':3,'f':7}, 'c': {'d':1, 'e':4}, 'd': {}, 'e': {'b':5,'f':8}, 'f': {}}
