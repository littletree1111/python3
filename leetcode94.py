# leetcode 94, binary tree inorder traversal
# solution from https://walkccc.me/LeetCode/problems/0094/?h=binary+tree+inorder+traversal
# iterative solution, time O(n), space O(n)

class Solution:
	def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		ans = []
		stack = []

		while root or stack:
			while root:
				stack.append(root)
				root = root.left
			root = stack.pop()
			ans.append(root.val)
			root = root.right

		return ans
