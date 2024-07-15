from flask import Flask , render_template
app = Flask(__name__)

@app.route('/gallery')
def f1():
    return render_template('gallery.html')

@app.route('/cart')
def g2():
    return render_template('cart.html')



app.run()
