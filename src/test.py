import unittest
from orders import Order, LinkedList

def make_order(n):
    return Order(f"{n}", f"Customer{n}", f"Item{n}", f"Time{n}")

class TestCases(unittest.TestCase):
    def test_single(self):
        ll = LinkedList()
        ll.append(make_order(1))
        self.assertEqual(ll.toString(), "1")
    def test_multiple(self):
        ll = LinkedList()
        for i in range(1, 6):
            ll.append(make_order(i))
        self.assertEqual(ll.toString(), "12345")
    def test_reverse(self):
        ll = LinkedList()
        for i in range(1, 6):
            ll.append(make_order(i))
        ll.reverse()
        self.assertEqual(ll.toString(), "54321")
    

if __name__ == '__main__':
    unittest.main()