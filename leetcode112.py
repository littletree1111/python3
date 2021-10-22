# leetcode 112, path sum
# solution from https://walkccc.me/LeetCode/problems/0112/?h=path+sum
# time: O(n), space: O(h)

class Solution:
	def hasPathSum(self, root: TreeNode, sum: int) -> bool:
		if not root:
			return False
		if root.val == sum and not root.left and not root.right:
			return True


		return self.hasPathSum(root.left, sum - root.val) or \
			self.hasPathSum(root.right, sum - root.val)
		