import sys
sys.path.append('../')# allows us to fetch files from the project root
import unittest
from modules.open_digraph import *


class InitTest(unittest.TestCase):
    def test_init_node(self):
        n0 = node(0, 'i', [], [1])
        self.assertEqual(n0.id, 0)
        self.assertEqual(n0.label, 'i')
        self.assertEqual(n0.parents, [])
        self.assertEqual(n0.children, [1])
        self.assertIsInstance(n0, node)

    def test_init_open_digraph(self):
        n0list = [node(i, '{}'.format(i), [], [1]) for i in range(5)]
        g = open_digraph([1], [2], n0list)
        self.assertEqual(g.nodes[0], n0list[0])
        self.assertEqual(g.inputs, [1])
        self.assertEqual(g.outputs, [2])
        self.assertIsInstance(g, open_digraph)
        self.assertIsInstance(n0list[0], node)

class NodeTest(unittest.TestCase):

    def test_repr(self):
        n0 = node(0, 'i', [], [1])
        print("------ NODE STR ------")
        print(n0)
        print("------ NODE REPR ------")
        print(repr(n0))

    # Tests de copy
    def test_copy(self):
        n0 = node(0, 'i', [], [1])
        n0copy = n0.copy()
        self.assertEqual(n0copy.id, n0.id)
        self.assertEqual(n0copy.label, n0.label)
        self.assertEqual(n0copy.parents, n0.parents)
        self.assertEqual(n0copy.children, n0.children)

    # Tests des getters
    def test_getters(self):
        n0 = node(0, 'i', [], [1])
        self.assertEqual(n0.get_id(), 0)
        self.assertEqual(n0.get_label(), 'i')
        self.assertEqual(n0.get_parent_ids(), [])
        self.assertEqual(n0.get_children_ids(), [1])

    # Tests des setters
    def test_setters(self):
        n0 = node(0, 'i', [], [1])

        n0.set_id(3)
        self.assertEqual(n0.get_id(), 3)

        n0.set_label('j')
        self.assertEqual(n0.get_label(), 'j')

        n0.set_parent_ids([2, 3])
        self.assertEqual(n0.get_parent_ids(), [2, 3])

        n0.set_children_ids([])
        self.assertEqual(n0.get_children_ids(), [])

        n0.add_parent_id(7)
        self.assertEqual(n0.get_parent_ids(), [2, 3, 7])

        n0.add_child_id(8)
        self.assertEqual(n0.get_children_ids(), [8])

    def test_remove(self):
        n0 = node(0, 'i', [], [1])

        n0.add_parent_id(7)
        n0.remove_parent_id(7)
        self.assertEqual(n0.get_parent_ids(), [])

        n0.set_children_ids([7,8])
        n0.remove_child_id(7)
        self.assertEqual(n0.get_children_ids(), [8])

        n0.set_parent_ids([2, 2])
        n0.remove_parent_id_all(2)
        self.assertEqual(n0.get_parent_ids(), [])

        n0.set_children_ids([3,3,4])
        n0.remove_child_id_all(3)
        self.assertEqual(n0.get_children_ids(), [4])

    '''TEST TD6'''
    def exemples_de_node(self):
        '''
        on renvoie un couple de node exemples pour faire les tests
        '''
        node1 = odgraph.node(0, "Isabelle", [], [1,2,7,3,5,2,2])
        node2 = odgraph.node(1, "Adjani", [4,4], [7,5,5,8])
        return (node1,node2)

    def test_indegree(self):
        node1, node2 = self.exemples_de_node()
        self.assertEqual(node1.indegree(), 0)
        self.assertEqual(node2.indegree(), 2)

    def test_outdegree(self):
        node1, node2 = self.exemples_de_node()
        self.assertEqual(node1.outdegree(), 7)
        self.assertEqual(node2.outdegree(), 4)

    def test_degree(self):
        node1, node2 = self.exemples_de_node()
        self.assertEqual(node1.degree(), 7)
        self.assertEqual(node2.degree(), 6)


class GraphTest(unittest.TestCase):
    def test_repr(self):
        n0list = [node(i, '{}'.format(i), [], [1]) for i in range(5)]
        g = open_digraph([1], [2], n0list)
        print("------ GRAPHE STR ------")
        print(g)
        print("------ GRAPHE REPR ------")
        print(repr(g))

    # Tests de Empty
    def test_empty(self):
        g = open_digraph.empty()
        self.assertEqual(open_digraph.empty().inputs, [])
        self.assertEqual(open_digraph.empty().outputs, [])
        self.assertEqual(open_digraph.empty().nodes, {})

    # Tests de copy
    def test_copy(self):
        n0list = [node(i, '{}'.format(i), [], [1]) for i in range(5)]
        g = open_digraph([1], [2], n0list)
        gCopy = g.copy()
        self.assertEqual(gCopy.inputs, g.inputs)
        self.assertEqual(gCopy.outputs, g.outputs)
        self.assertEqual(gCopy.nodes, g.nodes)

    # Tests des getters
    def test_getters(self):
        n0list = [node(i, '{}'.format(i), [], [1]) for i in range(5)]
        g = open_digraph([1], [2], n0list)
        self.assertEqual(g.get_input_ids(), [1])
        self.assertEqual(g.get_output_ids(), [2])
        self.assertEqual(g.get_nodes(), n0list)
        self.assertEqual(g.get_node_ids(), [0, 1, 2, 3, 4])
        self.assertEqual(g.get_id_node_map(), {0:n0list[0],
                                               1:n0list[1],
                                               2:n0list[2],
                                               3:n0list[3],
                                               4:n0list[4]})
        self.assertEqual(g.get_node_by_id(3), n0list[3])
        self.assertEqual(g.get_nodes_by_ids([3, 4]), [n0list[3], n0list[4]])

    # Tests des setters
    def test_setters(self):
        n0list = [node(i, '{}'.format(i), [], [1]) for i in range(5)]
        g = open_digraph([1], [2], n0list)
        g.set_input_ids([3, 4])
        self.assertEqual(g.get_input_ids(), [3, 4])
        g.set_output_ids([])
        self.assertEqual(g.get_output_ids(), [])
        g.add_input_id(5)
        self.assertEqual(g.get_input_ids(), [3, 4, 5])
        g.add_output_id(2)
        self.assertEqual(g.get_output_ids(), [2])

    def test_new_id(self):
        n0list = [node(i, '{}'.format(i), [], [1]) for i in range(5)]
        g = open_digraph([1], [2], n0list)
        id = g.new_id()
        self.assertEqual(g.new_id(), 5)

    def test_edges_management(self):
        n0list = [node(i, '{}'.format(i), [], []) for i in range(5)]
        g = open_digraph([1], [2], n0list)

        g.add_edge(2, 3)
        self.assertEqual(g.get_node_by_id(3).get_parent_ids(), [2])
        self.assertEqual(g.get_node_by_id(2).get_children_ids(), [3])
        g.remove_edge(2, 3)
        self.assertEqual(g.get_node_by_id(3).get_parent_ids(), [])
        self.assertEqual(g.get_node_by_id(2).get_children_ids(), [])

        g.add_edges([2, 3], [1, 4])
        self.assertEqual(g.get_node_by_id(1).get_parent_ids(), [2])
        self.assertEqual(g.get_node_by_id(3).get_children_ids(), [4])

        g.add_edge(2, 1)
        g.remove_edges([2, 3], [1, 4])
        self.assertEqual(g.get_node_by_id(1).get_parent_ids(), [])

        g.add_node()
        self.assertEqual(g.get_node_ids(), [0, 1, 2, 3, 4, 5])

        g.remove_node_by_id(4)
        self.assertEqual(g.get_node_ids(), [0, 1, 2, 3, 5])
        g.remove_nodes_by_id([2,3,4, 5])
        self.assertEqual(g.get_node_ids(), [0, 1])

    def test_well_formed(self):
        n0list = [node(i, '{}'.format(i), [], []) for i in range(5)]
        g = open_digraph([1], [2], n0list)
        self.assertEqual(g.is_well_formed(), True)

        good_list = [node(1, '1', [2, 3], [3]), node(2, '2', [], [1]), node(3, '3', [1], [1])]
        g_good = open_digraph([1], [2], good_list)
        self.assertEqual(g_good.is_well_formed(), True)

        wrong_list = [node(1, '1', [2, 3], [3]), node(2, '2', [], [1, 2]), node(3, '3', [1], [1])]
        g_wrong = open_digraph([1], [2], wrong_list)
        self.assertEqual(g_wrong.is_well_formed(), False)

        wrong_list2 = [node(1, '1', [2, 3], [3]), node(2, '2', [], [1]), node(3, '3', [1], [1])]
        g_wrong2 = open_digraph([1], [2, 4], wrong_list2)
        self.assertEqual(g_wrong2.is_well_formed(), False)

    def test_normalize(self):
        good_list = [node(1, '1', [2, 3], [3]), node(2, '2', [], [1]), node(3, '3', [1], [1])]
        g_good = open_digraph([1], [2], good_list)
        matrix = g_good.adjacency_matrix()
        for lin in matrix:
            print(lin)

    '''TEST TD6'''

    def exemples_de_graphe(self):
        '''
        on crée deux graph exemples qu'on réutilisera pour les tests
        return le couple (g,h)
        avec g un graph logique cohérant
        et h cyclique et incohérant
        '''
        node1 = odgraph.node(0,'',[],[1, 3])
        node2 = odgraph.node(1,'&',[0,2],[])
        node3 = odgraph.node(2,'',[],[1, 3])
        node4 = odgraph.node(3,'|',[0,2],[4])
        node5 = odgraph.node(4,'~',[3],[])
        nodelist = [node1,node2,node3,node4,node5]
        g = odgraph.open_digraph([0,2], [1,4], nodelist)

        node6 = odgraph.node(5,'&',[6, 8],[6])
        node7 = odgraph.node(6,'~',[5],[5,7])
        node8 = odgraph.node(7,'&',[6],[])
        node9 = odgraph.node(8,'',[],[5])
        nodelist2 = [node6,node7,node8,node9]
        h = odgraph.open_digraph([5,5,6],[5,7], nodelist2)

        return (g,h)

    def test_max_indegree(self):
        g,h = self.exemples_de_graphe()
        self.assertEqual(g.max_indegree(), 2)
        print(h)
        self.assertEqual(h.max_indegree(), 4)

    def test_min_indegree(self):
        g,h = self.exemples_de_graphe()
        self.assertEqual(g.min_indegree(), 1)
        self.assertEqual(h.min_indegree(), 0)

    def test_max_outdegree(self):
        g,h = self.exemples_de_graphe()
        self.assertEqual(g.max_outdegree(), 2)
        self.assertEqual(h.max_outdegree(), 2)

    def test_min_outdegree(self):
        g,h = self.exemples_de_graphe()
        self.assertEqual(g.min_outdegree(), 1)
        self.assertEqual(h.min_outdegree(), 1)

    def test_is_cyclic(self):
        g,h = self.exemples_de_graphe()
        self.assertEqual(g.is_cyclic(), False)
        self.assertEqual(h.is_cyclic(), True)

class BoolCircTest(unittest.TestCase):
    '''TEST TD6'''

    '''
    def test_init(self):
        #ct = bool_circ()
        pass

    def test_to_graph(self):
        self.assertIsInstance(self, open_digraph)
        pass

    def test_is_well_formed(self):
        pass
    '''

if __name__ == '__main__':  # the following code is called only when
    unittest.main()         # precisely this file is run