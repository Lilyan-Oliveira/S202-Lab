from database import Database
from product_analyzer import ProductAnalyzer
from helper.writeAJson import writeAJson

db = Database(database="Relatório4-MongoDBpt3", collection="Compras")
#db.resetDatabase()

analyzer = ProductAnalyzer(db_name="Relatório4-MongoDBpt3", collection_name="Compras")

# 1- Total de vendas por dia:
total_sales = analyzer.total_sales_per_day()
writeAJson(total_sales, "Total de vendas por dia")

# 2- Produto mais vendido:
most_sold = analyzer.most_sold_product()
writeAJson(most_sold, "Produto mais vendido")

# 3- Cliente que mais gastou em uma única compra:
top_spender = analyzer.customer_with_highest_spending()
writeAJson(top_spender, "Cliente com maior gasto em uma única compra")

# 4- Produtos que tiveram uma quantidade vendida acima de 1 unidade:
products_more_than_one = analyzer.products_sold_more_than_one()
writeAJson(products_more_than_one, "Produtos vendidos mais de uma unidade")





# 1- Média de gasto total:
# result = db.collection.aggregate([
#    {"$unwind": "$produtos"},
#    {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
#    {"$group": {"_id": None, "media": {"$avg": "$total"}}}
# ])

# writeAJson(result, "Média de gasto total")

# # 2- Cliente que mais comprou em cada dia:
# result = db.collection.aggregate([
#     {"$unwind": "$produtos"},
#     {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
#     {"$sort": {"_id.data": 1, "total": -1}},
#     {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
# ])

# writeAJson(result, "Cliente que mais comprou em cada dia")

# 3- Produto mais vendido:
#result = db.collection.aggregate([
 #   {"$unwind": "$produtos"},
 #   {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
 #   {"$sort": {"total": -1}},
 #   {"$limit": 1}
#])

#writeAJson(result, "Produto mais vendido")


