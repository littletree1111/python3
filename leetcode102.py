# leetcode 102, binary tree level order traversal
# solution from https://walkccc.me/LeetCode/problems/0102/?h=binary+tree+level+order+traversal
# time: O(n), space: O(n)

class Solution:
	def levelOrder(self, root: Optional[TreeNode]) -> List [List[int]]:
		if not root:
			return []

		ans = []
		q = deque([root])

		while q:
			currLevel = []
			for _ in range(len(q)):
				node = q.popleft()
				currLevel.append(node.val)
				if node.left:
					q.append(node.left)
				if node.right:
					q.append(node.right)
			ans.append(currLevel)

		return ans




		# solution from https://www.youtube.com/watch?v=MBZ-gBkjdMc

		# queue = [root]
		# next_queue = []
		# level = []
		# result = []

		# while queue != []:
		# 	for root in queue:
		# 		level.append(root.val)
		# 		if root.left:
		# 			next_queue.append(root.left)
		# 		if root.right:
		# 			next_queue.append(root.right)
		# 	result.append(level)
		# 	level = []
		# 	queue = next_queue
		# 	next_queue = []
		# return result