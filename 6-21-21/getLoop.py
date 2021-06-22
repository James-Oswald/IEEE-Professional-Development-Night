
#https://www.codewars.com/kata/52a89c2ea8ddc5547a000863/train/python

def loop_size(node):
    nodes = []
    while node.next not in nodes:
        nodes.append(node.next)
        node = node.next
    return len(nodes) - nodes.index(node.next)