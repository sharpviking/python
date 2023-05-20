from addition import addition
from multiplication import mult
result = addition(4, 3)
print(result)


def module(x, y):
    return x*y


result = module(3, 4)
print(result)

products = [{
    "name": "thumsup",
    "price": 30
},
    {
    "name": "Coke",
    "price": 40

}
]
print(products[0]["name"])

# products will be in a seperate file
# create product(name, price)
# getting all the products
# getting a single product(name)
# updating a product(name)
# app.py file where you
# are going to acll all theese functions and print them


from flask import Flask
#we used to create the server
#app=express()

app = Flask(__name__)
#app.get("/",(req,res)=>{})


@app.route('/')
def hello():
    return "Hello, World!"
@app.route('getaproducts')
def getproducts():
    #code for get producrs