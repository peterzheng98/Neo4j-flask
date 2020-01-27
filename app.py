from flask import Flask,render_template
from flask import request,redirect,url_for
from flask_wtf import FlaskForm
from my_neo import get_drug
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "12345678"

class symptomForm(FlaskForm):
    sympt_name=StringField('Symptom:')
    submit=SubmitField('Submit')

class scriptForm(FlaskForm):
    sympt_name=StringField('Symptom:')
    drug1_name=StringField('Drug1:')
    drug2_name=StringField('Drug2:')
    submit=SubmitField('Submit')

@app.route('/',methods=['POST','GET'])
def homepage():
    if request.method == 'POST':
        symp_name = request.form.get('sympt_name')
        drug1_name =request.form.get('drug1')
        drug2_name=request.form.get('drug2')

        return redirect(url_for('getdrug',symp_name=symp_name))

    symptom_form=symptomForm()
    script_form=scriptForm()
    return render_template('home.html',symp_form=symptom_form,scri_form=script_form)

@app.route('/drugs/?<string:symp_name>')
def getdrug(symp_name):
    drug_result = get_drug(symp_name)
    print('*****************')
    print(drug_result)
    return render_template('suitable_drugs.html', drug_result=drug_result)

if __name__  ==  '__main__':
    app.run()
