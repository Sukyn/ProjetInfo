from modules.utils import *

class node:

    '''
    identity: int; its unique id in the graph
    label: string;
    parents: int list; a sorted list containing the ids of its parents
    children: int list; a sorted list containing the ids of its children
    '''
    def __init__(self, identity, label, parents, children):
        self.id = identity
        self.label = label
        self.parents = parents
        self.children = children

    '''
    **Example**
    id : 0
    label : d
    parents : [2, 3, 4]
    children : [5, 6]
    => (0, d, [2, 3, 4], [5, 6])
    '''
    def __str__(self):
        return ("("+str(self.id)+", "+self.label+", "
              +str(self.parents)+", "+str(self.children)+")")

    '''
    **Example**
    id : 0
    label : d
    parents : [2, 3, 4]
    children : [5, 6]
    => node(0, d, [2, 3, 4], [5, 6])
    '''
    def __repr__(self):
        return "node"+str(self)

    '''
    function that returns a copy of the object
    '''
    def copy(self):
        return node(self.id, self.label, self.parents, self.children)

    '''
    GETTERS
    functions to get the attributes of the object
    (encapsulation)
    '''
    def get_id(self):
        return self.id
    def get_label(self):
        return self.label
    def get_parent_ids(self):
        return self.parents
    def get_children_ids(self):
        return self.children

    '''
    SETTERS
    functions to modify the attributes of the object
    (encapsulation)
    '''
    def set_id(self, new_id):
        self.id = new_id
    def set_label(self, new_label):
        self.label = new_label
    def set_parent_ids(self, new_ids):
        self.parents = new_ids
    def set_children_ids(self, new_ids):
        self.children = new_ids
    def add_child_id(self, new_id):
        self.children.append(new_id)
    def add_parent_id(self, new_id):
        self.parents.append(new_id)

    '''
    functions to manage parents and children
    '''
    def remove_parent_id(self, id):
        try:
            self.parents.remove(id)
        except ValueError:
            pass
    def remove_child_id(self, id):
        try:
            self.children.remove(id)
        except ValueError:
            pass
    def remove_parent_id_all(self, id):
        remove_all(self.parents, id)
    def remove_child_id_all(self, id):
        remove_all(self.children, id)








class open_digraph: # for open directed graph


    '''
    inputs: int list; the ids of the input nodes
    outputs: int list; the ids of the output nodes
    nodes: node list;
    '''
    def __init__(self, inputs, outputs, nodes):
        self.inputs = inputs
        self.outputs = outputs
        self.nodes = {node.id:node for node in nodes} # self.nodes: <int,node> dict
        self.ids = [node.id for node in nodes]



    '''
    **EXAMPLE**
        ([0, 1], [2], 4)
    '''
    def __str__(self):
        return ("("+str(self.inputs)+", "+str(self.nodes)
                    +", "+str(self.outputs)+")")

    '''
    **EXAMPLE**
    open_digraph([0,1], [2], [node(4, 'i', [0, 2], [3])])
    '''
    def __repr__(self):
        return "open_digraph"+str(self)

    '''
    constructor of an empty graph
    no inputs, no outputs, no nodes
    '''
    def empty():
        return open_digraph([],[],[])

    '''
    function that returns a copy of the object
    '''
    def copy(self):
        return open_digraph(self.inputs, self.outputs, self.nodes.values())

    '''
    GETTERS
    functions to get the attributes of the object
    (encapsulation)
    '''
    def get_input_ids(self):
        return self.inputs
    def get_output_ids(self):
        return self.outputs
    def get_id_node_map(self):
        return self.nodes
    def get_nodes(self):
        return list(self.nodes.values())
    def get_node_ids(self):
        return [i for i in self.nodes]
    def get_node_by_id(self, id):
        return self.nodes[id]
    def get_nodes_by_ids(self, idlist):
        return [self.nodes[i] for i in idlist]
    def get_length(self):
        return len(self.ids)
    '''
    SETTERS
    functions to modify the attributes of the object
    (encapsulation)
    '''
    def set_input_ids(self, new_idlist):
        self.inputs = new_idlist
    def set_output_ids(self, new_idlist):
        self.outputs = new_idlist
    def add_input_id(self, new_id):
        self.inputs.append(new_id)
    def add_output_id(self, new_id):
        self.outputs.append(new_id)

    def new_id(self):
        '''
        function that returns an used id for an edge
        '''
        id = 0
        while(self.ids.count(id) > 0):
            id += 1
        return id

    '''
    functions to add edges
    '''
    def add_edge(self, src, tgt):
        self.get_node_by_id(src).children.append(tgt)
        self.get_node_by_id(tgt).parents.append(src)

    def add_edges(self, src_list, tgt_list):
        for src,tgt in zip(src_list,tgt_list):
            self.add_edge(src, tgt)

    def add_node(self, label = '', parents = [], children = []):
        id = self.new_id()
        thisnode = node(id, label, parents, children)
        self.nodes[thisnode.id] = thisnode
        for parent in parents:
            self.add_edge(parent, id)
        for child in children:
            self.add_edge(id, child)
        return id

    '''
    functions to remove edges
    '''
    def remove_edge(self, src, tgt):
        self.get_node_by_id(src).children.remove(tgt)
        self.get_node_by_id(tgt).parents.remove(src)

    def remove_node_by_id(self, id):
        del self.nodes[id]


    def remove_edges(self, src_list, tgt_list):
        for src, tgt in zip(src_list, tgt_list):
            try:
                while(True): #si jamais on a des arrêtes multiples
                    self.remove_edge(src,tgt)
            except ValueError:
                pass
    def remove_nodes_by_id(self, id_list):
        for id in id_list:
            try:
                self.remove_node_by_id(id)
            except KeyError:
                pass

    '''
    functions that verify if the graph is well formed
    '''
    def is_well_formed(self):

        nodes_ids = self.get_id_node_map() # Getting every id of nodes in the graph
        for node_id in nodes_ids:
            if nodes_ids[node_id].get_id() != node_id: # Checking that keys and nodes are linked
                return False

            sons = nodes_ids[node_id].get_children_ids()
            for child in sons: # Checking that parents and sons are coherent
                n = count_occurence(sons, child)
                if (count_occurence(nodes_ids[child].get_parent_ids(), nodes_ids[node_id].get_id()) != n):
                    return False

        for inp in self.get_input_ids(): # Checking inputs are in nodes
            if inp not in nodes_ids:
                return False
        for outp in self.get_output_ids(): # Checking outputs are in nodes
            if outp not in nodes_ids:
                return False
        return True

    def change_id(self, new_id, node_id):
        if(new_id in self.get_node_ids()):
            print("The node id already exists")
            #raise
        elif(node_id == new_id):
            pass
        else:
            self.get_id_node_map()[new_id] = self.get_id_node_map().pop(node_id)
            for node in self.get_nodes():
                if node_id in node.get_parent_ids():
                    node.remove_parent_id(node_id)
                    node.add_parent_id(new_id)
                if node_id in node.get_children_ids():
                    node.remove_child_id(node_id)
                    node.add_child_id(new_id)


    def change_ids(self, new_ids, node_ids):
        list = sorted(zip(new_ids, node_ids), key = lambda x: x[0])
        print(list)
        for new_id, node_id in list:
            self.change_id(new_id, node_id)

    def normalize_ids(self):
        normalized_list = [i for i in range(self.get_length())]
        old_ids = self.get_node_ids()
        self.change_ids(normalized_list, old_ids)

    def adjacency_matrix(self):
        n = self.get_length()
        self.normalize_ids()
        return [[count_occurence(self.get_node_by_id(i).get_parent_ids(), j) for i in range(n)] for j in range(n)]
