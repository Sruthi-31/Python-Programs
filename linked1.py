class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None

    def output(self):
        p=self.head
        while(p):
            print p.data,
            p = p.next


if __name__ == '__main__':
    newlist = List()
    newlist.head = Node(1)
    two = Node(2)
    three = Node(3)
    four  =Node(4)
    five = Node(5)

    newlist.head.next = two
    two.next = three
    three.next=four
    four.next=five

    newlist.output()