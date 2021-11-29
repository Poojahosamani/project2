from pymongo import MongoClient
from flask import Flask, jsonify, request
from bson.json_util import dumps

def allproducts():
    client = MongoClient('localhost',27017)
    db = client['Retail']
    store = db['store']
    products = store.find()
    return dumps(products)

def allsoap():
    client = MongoClient('localhost',27017)
    db = client['Retail']
    soap  = db['soap']
    products =  soap.find()
    return dumps(products)

def allshampoo():
    client = MongoClient('localhost',27017)
    db = client['Retail']
    shampoo  = db['shampoo']
    products = shampoo .find()
    return dumps(products)

def allchocolates():
    client = MongoClient('localhost',27017)
    db = client['Retail']
    chocolates= db['chocolates']
    products = chocolates.find()
    return dumps(products)