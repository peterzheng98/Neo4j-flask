from flask import Flask,render_template
from flask import request,redirect,url_for
from my_neo import get_drug

app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def homepage():
    if request.method == 'POST':
        symp_name = request.form.get('symptom_name')

        drug1_name =request.form.get('drug1')
        drug2_name=request.form.get('drug2')
        return redirect(url_for('getdrug',symp_name=symp_name))

    return render_template('home.html')

@app.route('/drugs/?<string:symp_name>')
def getdrug(symp_name):
    print('here')
    print(symp_name)
    drug_result = get_drug(symp_name)
    print('*****************')
    print(drug_result)
    return render_template('suitable_drugs.html', drug_result=drug_result)

if __name__  ==  '__main__':
    app.run()
