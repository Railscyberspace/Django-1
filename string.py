book = ['Python', 'development']
book.append(2008)
book.insert(1,'web')
print(book)


table = []
table.append('Ruby')
table.insert(0, 'My')
table.insert(1, 'favorite')
table.insert(2, 'Baby')
print(table)


data = [x + 1 for x in range(10)]
print(data)

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)



Books = ['python', 'web', 'development']
Books.extend(['with', 'Django'])
print(Books)


Data = ( x for x in range(10000) if x % 2 == 0)
print(Data)