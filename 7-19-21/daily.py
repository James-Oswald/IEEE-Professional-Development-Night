#https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/610/week-3-july-15th-july-21st/3819/

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class BetterTreeNode:
    def __init__(self, x, p, b):
        self.val = x
        self.parent = p
        self.treeNode = b

def makeBetterTree(root: 'TreeNode', parent: 'TreeNode' = None):
    newRoot = BetterTreeNode(root.val, parent, root)
    nodeConverter = {}
    nodeConverter[root.val] = newRoot
    if root.left != None:
        nodeConverter.update(makeBetterTree(root.left, newRoot))
    if root.right != None:
        nodeConverter.update(makeBetterTree(root.right, newRoot))
    return nodeConverter
    
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        nodeConverter = makeBetterTree(root)
        plist = []
        curp = nodeConverter[p.val]
        while curp is not None:
            plist.append(curp.val)
            curp = curp.parent
        curq = nodeConverter[q.val]
        while curq is not None:
            if curq.val in plist:
                return curq.treeNode
            curq = curq.parent
        return None