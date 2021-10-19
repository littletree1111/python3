# leetcode 101, symmetric tree
# solution from https://walkccc.me/LeetCode/problems/0101/?h=symme
# recursive solution, time: O(n), space: O(h)

class Solution:
	def isSymmetric(self, root: Optional[TreeNode]) -> bool:
		def isSymmetric(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
			if not p or not q:
				return p == q

			return p.val == q.val and \
				isSymmetric(p.left, q.right) and \
				isSymmetric(p.right, q.left)

		return isSymmetric(root, root)


# # iterative DFS
# # source https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/536/discuss/1518385/Python-recursive-and-iterative-solution
# class Solution:
# 	def isSymmetric(self, root: Optional[TreeNode]) -> bool:
# 	"""
# 	DFS solution with stack
# 		Each time pop two elements from stack
# 		Notice the alternating appending of right and left nodes respectively
# 	"""
# 	if not root:
# 		return True
# 	stack = [root, root]
# 	while stack:
# 		r1 = stack.pop()
# 		r2 = stack.pop()
# 		if (not r1) and (not r2):
# 			continue
# 		if (not r1) or (not r2):
# 			return False
# 		if r1.val != r2.val:
# 			return False
# 		stack.append(r1.left)
# 		stack.append(r2.right)
# 		stack.append(r1.right)
# 		stack.append(r2.left)
# 	return True



# #iterative BFS
# # source https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/536/discuss/1518385/Python-recursive-and-iterative-solution
# class Solution:
# 	def isSymmetric(self, root: Optional[TreeNode]) -> bool:
# 		"""
# 		BFS solution with queue
# 		"""
# 		if not root:
# 			return True
# 		q = collections.deque([root, root])
# 		while q:
# 			r1 = q.popleft()
# 			r2 = q.pop()
# 			if (not r1) and (not r2):
# 				continue # could not return, as we need to finish examining the remaining pairs of nodes in q
# 			if (not r1) or (not r2):
# 				return False
# 			if r1.val != r2.val:
# 				return False

# 			q.appendleft(r1.left)
# 			q.append(r2.right)
# 			q.appendleft(r1.right)
# 			q.append(r2.left)

# 		return True