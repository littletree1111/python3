# leetcode 145, binary tree postorder traversal
# solution from https://walkccc.me/LeetCode/problems/0145/?h=binary+tree+postorder+traversal
# iterative solution, time: O(n), space: O(h)

class Solution:
	def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		if not root:
			return []


		ans = []
		stack = [root]

		while stack:
			node = stack.pop()
			ans.append(node.val)
			if node.left:
				stack.append(node.left)
			if node.right:
				stack.append(node.right)

		return ans[::-1]
		
