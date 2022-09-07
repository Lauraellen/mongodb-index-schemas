from bson import ObjectId

from db.database import Database

class Pessoa:
    def __init__(self):
        self.db = Database(database="dblibrary", collection="Livros")
        # self.db.resetDatabase()
        self.collection = self.db.collection

    def getAllBooks(self):
        res = self.collection.find()
        return res

    def updatePrice(self, id: str, price: float):
        res = self.collection.update_one({"_id": ObjectId(id)}, {"$set": {"preco": price}})
        return res.modified_count

    def addBook(self, title: str, author: str, ano: int, preco: float):
        res = self.collection.insert_one({"titulo": title, "autor": author, "ano": ano, "preco": preco})
        return res.inserted_id

    def deleteBook(self, id):
        res = self.collection.delete_one({"_id": ObjectId(id)})
        return res.deleted_count