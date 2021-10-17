# leetcode 104, maximum depth of binary tree
# solution from https://walkccc.me/LeetCode/problems/0104/?h=maximum+depth+binary+tree
# time: O(n), space: O(1)

class Solution:
	def maxDepth(self, root: Optional([TreeNode]) -> int:
		if not root:
			return 0
		return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
