import unittest
from linked_list import *
from linkedlist_stack import * 


class TestLinkedListStack(unittest.TestCase):

    def test_pushing(self):
        l = stack(2)
        l.pushing(Node("annu"))
        l.pushing(Node("annu"))
        print(l.get_top())
        
        
    def test_popping(self):
        l = stack(1)
        l.pushing(Node("annu"))
        l.pushing(Node(2))
        l.popping()
        print(l.get_top())
        
    def test_get_top(self):
        l = stack(1)
        l.pushing(Node("annu"))
        l.pushing(Node(2))
        print(l.get_top())
        
    def test_head(self):
        l = stack(1)
        l.pushing(Node("annu"))
        l.pushing(Node(2))
        print(l.head())
        
        

        
    
if __name__ == '__main__':
    unittest.main()