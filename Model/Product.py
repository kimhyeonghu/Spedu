class Product:
    def __init__(self, productID, category, image, name, price, description, rating, reviews, tag, stock):
        self.productID = productID
        self.category = category
        self.image = image
        self.name = name
        self.price = price
        self.description = description
        self.rating = rating
        self.reviews = reviews
        self.tag = tag
        self.stock = stock

class Product_For_Search(Product):
    def __init__(self, productID, category, image, name, price, description, rating, reviews, tag, stock, search_points):
        Product.__init__(self, productID, category, image, name, price, description, rating, reviews, tag, stock)
        self.search_points = search_points
