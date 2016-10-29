# coding=utf-8


class StackWithMin:
	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def push(self, value):
		self.stack1.append(value)

		if not self.min() or self.min()>value:
			self.stack2.append(value)
		else:
			self.stack2.append(self.min())

	def min(self):
		if self.stack2:
			return self.stack2[-1]

	def pop(self):
		self.stack2.pop()
		return self.stack1.pop()

ms = StackWithMin()
ms.push(3)
ms.push(4)
ms.push(2)
ms.push(1)
ms.pop()
ms.pop()
ms.push(0)
