class MathDojo(object):
	def __init__(self):
		self.result = 0

	def add(self, *nums):
		for num in nums:
			if type(num) is list:
				for x in num:
					self.result += x
			else:
				self.result += num
		return self

	def subtract(self, *nums):
		for num in nums:
			if type(num) is list:
				for x in num:
					self.result -= x
			else:
				self.result -= num
		return self

md = MathDojo()
print md.add(2,[1,4,5],[6,7,8],5,6,[1.1],[4.3,2.5]).result
print md.subtract(2,[1,3,4],6,2.3,[1.1,4.4,6.6]).result