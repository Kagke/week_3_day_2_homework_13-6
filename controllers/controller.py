from app import app
from flask import render_template
from models.order_list import *
from models.order import Order

@app.route('/')
def index():
    return "Welcome To The Shoe Shop"

@app.route('/orders')
def show_all():
    return render_template("index.html" ,  title = "Order Page" , orders = orders)

@app.route("/orders/<index>")
def show_seperate(index):
    order = orders[int(index)]
    return render_template("seperate_order.html" ,title = "What ever" ,  order = order)