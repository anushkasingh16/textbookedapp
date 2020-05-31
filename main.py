from flask import Flask, render_template
from flask import request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('/your.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['POST','GET'])
def recieve():
    if(request.method=="POST"):
        booksell = request.form.get("booknameadd", False)
        return render_template('addBookpage.html')
@app.route('/searchbook.html')
def buy():
    return render_template('searchbook.html')

@app.route('/addBookpage/',methods=['POST','GET'])
def addbook():
    bookname = request.form.get("bookadd", False)
    bookprice = request.form.get("priceadd", False)
    bookcontact = request.form.get("contactadd", False)
    doc_ref = db.collection(u'bookinventory').zdocument(bookname)
    doc_ref.set({
        u'price': bookprice,
        u'contact': bookcontact
    })
    return render_template('hasbeenlisted.html')
@app.route('/hasbeenlisted.html')
def listed():
    return render_template('hasbeenlisted.html')
if __name__ == '__main__':
    app.run(debug= True)
