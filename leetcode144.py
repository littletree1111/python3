# leetcode 144, binary tree preorder traversal
# solution from https://walkccc.me/LeetCode/problems/0144/?h=binary+tree+pre
# iterative solution, time O(n), space O(h)

class Solution:
	def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		if not root:
			return []

		ans = []
		stack = [root]

		while stack:
			node = stack.pop()
			ans.append(node.val)
			if node.right:
				stack.append(node.right)
			if node.left:
				stack.append(node.left)

		return ans