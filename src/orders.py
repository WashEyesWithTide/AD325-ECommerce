class Order:
    def __init__(self, order_id, customer, details, timestamp):
        self.order_id = order_id
        self.customer = customer
        self.details = details
        self.timestamp = timestamp

class Node:
    def __init__(self, order):
        self.order = order
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
 
    def append(self, order):
        node = Node(order)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def display(self):
        current = self.head
        while current:
            o = current.order
            print(f"  [{o.order_id}] {o.customer} | {o.details} | {o.timestamp}")
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def toString(self):
        result = []
        current = self.head
        while current:
            result.append(current.order.order_id)
            current = current.next
        return "".join(result)

