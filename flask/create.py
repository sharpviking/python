from product import products


def create_product(self, name, price):
    product_id = len(self.products) + 1
    new_product = Product(product_id, name, price)
    self.products.append(new_product)
    return new_product.id
