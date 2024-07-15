from flask import Flask,render_template,request
import pickle
app = Flask(__name__)
@app.route('/')
def base():
    return render_template("cloud_deployment.html")
@app.route('/predict',methods = ['post'])
def predict():
    exp = request.form.get("Experience")
    mail = request.form.get("mail")
    phone = request.form.get("mob_no")
    print(exp)
    return render_template('predict.html')

if __name__ == '__main__':
    app.run()


