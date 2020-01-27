from flask import Flask,render_template
from flask import request,redirect,url_for
from my_neo import get_drug

app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def homepage():
    if request.method == 'POST':
        symp_name = request.form.get('symptom_name')
        print(symp_name)
        drug_result = get_drug(symp_name)
        print('*****************')
        print(drug_result)
        return render_template('suitable_drugs.html', drug_result=drug_result)

    return render_template('home.html')


if __name__  ==  '__main__':
    app.run()
