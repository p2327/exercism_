class Matrix(object):
	def __init__(self, matrix_string):
		self.string = matrix_string
		self.aslist = self.__listify(matrix_string)
	
	def __listify(self, seq):
		matrix = []
		_ = []
		
		for index, s in enumerate(seq):
			try:
				isinstance(int(s), int)
				_ += [int(seq[index])]
			except:
				matrix += [_]
				_ = []
				pass
		
		matrix += [_]
		
		return matrix
		
	def row(self, index):
		return [row for row in self.aslist][index]
	
	def column(self, index):
		return [[row[i] for row in self.aslist] for i in range(len(self.aslist[0]))][index]
