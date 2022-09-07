from db.pessoa import Pessoa
from helper.WriteAJson import writeAJson

pessoa = Pessoa();

addBook1 = pessoa.addBook('O Essencialismo', 'Greg MeKeown', 2014, 36.99)
addBook2 = pessoa.addBook('O Poder do Hábito', 'Charles Duhigg', 2012, 34.9)
addBook3 = pessoa.addBook('As coisas que você só vê quando desacelera', 'Haemin Sunim', 2017, 49.9)


updatePrice = pessoa.updatePrice('6318f167d33645a8abc49024', 45.7)
deleteBook = pessoa.deleteBook('6318f167d33645a8abc49026')
getAllBooks = pessoa.getAllBooks()

writeAJson(getAllBooks, "Livros")