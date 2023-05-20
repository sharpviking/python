import flask from Falsk

app= Flask(__name__)

manager = ProductManager()

@app.route('/')
def hello():
    return "Hello jupiter"

@app.route('getproducts')
def getproducts():

@app.route('/products/<name>')

@app.route('product', method=['POST'])
def create_product():
    product= request.json
    product_id = mongoDB

if __name__ =='__main__':
    app.run()


# Create a product
products1 = manager.create_product('Product 1', 10.99)

# Get a product
product2 = manager.get_product('Product 1')
if product2:
    print(f"Product name: {product2.name}")
    print(f"Product price: {product2.price}")

# Update a product
if manager.update_product('Product 1', 15.99):
    print("Product updated successfully")

# Delete a product
if manager.delete_product('Product 1'):
    print("Product deleted successfully")
