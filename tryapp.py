from flask import Flask,render_template
from flask import request,redirect,url_for
from flask_wtf import FlaskForm
from my_neo import get_drug
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "12345678"


@app.route('/a11')
def getdrug():
    drug_result,product_result = ['d1', 'd2'], {'d1': ['da1', 'da2', 'da3'], 'd2': ['db1', 'db2']}
    print('*****************')
    return render_template('try.html', drug_result=drug_result,product_result=product_result)

if __name__  ==  '__main__':
    app.run(debug=True)
