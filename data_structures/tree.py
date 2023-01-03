class TreeNode:
    def __init__(self, val=0):
        self.data = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)
