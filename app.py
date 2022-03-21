from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('home.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

# @app.route('/gallary')
# def galary():
#     return render_template('gallary.html')

# @app.route('/cart')
# def cart():
#     return render_template('cart.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

@app.route('/predict',methods=['post'])
def predict():

    model = joblib.load('dibatic_81.pkl')

    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    # print(exp)
    # print(phone)
    # print(mail)
    print(preg , plas, pres, skin, test, mass, pedi, age)
    
    output = model.predict([[preg , plas, pres, skin, test, mass, pedi, age]])

    if output[0] == 0:
        data='person is not dibatic'
    else:
        data='person is dibatic'

    return render_template('predict.html', data=data)
if __name__  == "__main__":
    app.run(debug=True)