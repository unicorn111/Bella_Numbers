def bella_number(n):
	'''
	This program generates the correct Bella number
	bella_number(-1)
	Please, type only positive numbers
	None
	bella_number(1.5)
	Please, type only integers
	None
	bella_number(10)
	115975
	bella_number('a')
	Please, type only numbers
	None
	print(bella_number(1))
	1
	'''
	try:
		if n < 0:
			print('Please, type only positive numbers')
		elif n != int(n):
			print('Please, type only integers')
		else:
			init_list = [1]
			while len(init_list) < n:
				res = []
				res.append(init_list[-1])
				for i in range(len(init_list)):
					if len(res) < n:
						res.append(res[i]+init_list[i])
				init_list = res
			return str(init_list[-1])
	except TypeError:
		print('Please, type only numbers')
