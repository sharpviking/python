from product import products 

def get_product(self, product_id):
        for product in products:
            if product.id == product_id:
                return product
        return None

    def update_product( product_id, new_data):
        if product:
            product.name = new_data.get('name', product.name)
            product.price = new_data.get('price', product.price)
            return True
        return False

    def create_product( name, price):
        new_product = Product(product_id, name, price)
        products.append(new_product)
        return new_product.id