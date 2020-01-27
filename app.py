from flask import Flask,render_template
from flask import request,redirect,url_for
from flask_wtf import FlaskForm
from my_neo import get_drug
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "12345678"

class symptomForm(FlaskForm):
    sympt_name=StringField('Symptom:',validators=[DataRequired()])
    submit1=SubmitField('SUBMIT SYMPTOM')

class scriptForm(FlaskForm):
    sympt_name2=StringField('Symptom:',validators=[DataRequired()])
    drug1_name=StringField('Drug1:',validators=[DataRequired()])
    drug2_name=StringField('Drug2:',validators=[DataRequired()])
    submit2=SubmitField('SUBMIT SCRIPT')

@app.route('/',methods=['POST','GET'])
def homepage():
    symptom_form = symptomForm()
    script_form = scriptForm()
    print('ok')
    if request.method == 'POST':
        print('post')
        if symptom_form.submit1.data and symptom_form.validate():
            print('symptom')
            symp_name = symptom_form.sympt_name.data
            return redirect(url_for('getdrug',symp_name=symp_name))
        elif script_form.submit2.data and script_form.validate():
            print('script')
            symp2_name=script_form.sympt_name2.data
            drug1_name =script_form.drug1_name.data
            drug2_name=script_form.drug2_name.data
            return'hello'

    return render_template('home.html',symp_form=symptom_form,scri_form=script_form)

@app.route('/drugs/?<string:symp_name>')
def getdrug(symp_name):
    drug_result = get_drug(symp_name)
    print('*****************')
    print(drug_result)
    return render_template('suitable_drugs.html', drug_result=drug_result)

#@app.route('/result/?<string:')

if __name__  ==  '__main__':
    app.run()
