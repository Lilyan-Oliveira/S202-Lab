from database import Database

class ProductAnalyzer:
    def __init__(self, db_name, collection_name):
        self.db = Database(database=db_name, collection=collection_name)

    def total_sales_per_day(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data_compra", "total_vendas": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"_id": 1}}
        ]
        result = self.db.collection.aggregate(pipeline)
        return list(result)

    def most_sold_product(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total_vendido": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total_vendido": -1}},
            {"$limit": 1}
        ]
        result = self.db.collection.aggregate(pipeline)
        return list(result)

    def customer_with_highest_spending(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total_gasto": -1}},
            {"$limit": 1}
        ]
        result = self.db.collection.aggregate(pipeline)
        return list(result)

    def products_sold_more_than_one(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "quantidade_vendida": {"$sum": "$produtos.quantidade"}}},
            {"$match": {"quantidade_vendida": {"$gt": 1}}},
            {"$sort": {"quantidade_vendida": -1}}
        ]
        result = self.db.collection.aggregate(pipeline)
        return list(result)
