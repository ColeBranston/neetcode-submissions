class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        Preorder tells us WHICH node is the root; inorder tells us WHERE to split.

        We walk preorder left to right with a single shared pointer (self.pre_idx),
        so each call just takes the next value as its subtree's root. Looking that
        value up in inorder gives index `mid`, which splits the current inorder
        range [l, r] into everything left of the root (its left subtree) and
        everything right of it (its right subtree). We recurse on those two ranges,
        and `l > r` means an empty range, i.e. no child.

        Crucially we must build the LEFT side before the right: preorder lists a
        node's entire left subtree before its right subtree, so consuming the left
        range first is what keeps the shared pointer aligned with the range we're
        currently filling in. The `indices` dict precomputes value -> inorder
        position so each lookup is O(1) instead of scanning the array.

        Assumes values are unique (guaranteed by the problem), since the dict and
        the split both depend on a value mapping to exactly one position.

        Time: O(n) - each node is created once, each lookup is O(1).
        Space: O(n) for the dict, plus O(h) recursion stack (O(n) if skewed).
        '''
        indices = {val: idx for idx, val in enumerate(inorder)}

        self.pre_idx = 0
        def dfs(l, r):
            if l > r:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = indices[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root

        return dfs(0, len(inorder) - 1)