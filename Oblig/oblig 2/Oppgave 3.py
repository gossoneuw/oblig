books = ['The Hobbit', 'Farmer Giles of Ham', 'The Fellowship of the Ring', 'The Two Towers', 'The Return of the King',
         'The Adventures of Tom Bombadil', 'Tree and Lea']

two_last_books = books[5:7]
two_first_books = books[0:2]
two_last_and_first_books = two_first_books + two_last_books
print(two_last_and_first_books)

books.append('The Silmarillion')
books.append('Unfinished Tales')

books.remove('The Fellowship of the Ring')
books.remove('The Two Towers')
books.remove('The Return of the King')

books.append('lord of the Rings: The Fellowship of the Ring')
books.append('lord of the Rings: The Two Towers')
books.append('lord of the Rings: The Return of the King')
print()
books.sort()
print(books)