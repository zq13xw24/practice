'''
house是按照树状连到一起的，直接相连的不能偷
'''

class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree():
    # 建立二叉树是以层序遍历方式输入，节点不存在时以None表示
    def creatTree(self, nodeList):
        if nodeList[0] == None:
            return None
        head = TreeNode(nodeList[0])
        Nodes = [head]
        j = 1
        for node in Nodes:
            if node != None:
                node.left = (TreeNode(nodeList[j]) if nodeList[j] != None else None)
                Nodes.append(node.left)
                j += 1
                if j == len(nodeList):
                    return head
                node.right = (TreeNode(nodeList[j]) if nodeList[j] != None else None)
                j += 1
                Nodes.append(node.right)
                if j == len(nodeList):
                    return head

class Solution():
    def rob(self, root):
        return max(self.tryRob(root))

    def tryRob(self, node):
        if node == None:
            return [0, 0]
        result = [0] * 2    # [0]是不偷现在这家，[1]是偷现在这家
        left_val = self.tryRob(node.left)
        right_val = self.tryRob(node.right)
        result[0] = max(left_val[0], left_val[1]) + max(right_val[0], right_val[1])
        result[1] = left_val[0] + right_val[0] + node.val
        return result

if __name__ == '__main__':
    element = [3,4,5,1,3,None,1]
    tree = Tree()
    head = tree.creatTree(element)
    solution = Solution()
    print('result: {}'.format(solution.rob(head)))
