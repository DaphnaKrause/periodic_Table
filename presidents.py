from flask import Flask, render_template
from modules import convert_to_dict
app = Flask(__name__)

presidents_list = convert_to_dict("presidents.csv")

@app.route('/')
def index():
    ids_list = []
    name_list = []
    # fill one list with the number of each presidency and
    # fill the other with the name of each president
    for president in presidents_list:
        ids_list.append(president['Presidency'])
        name_list.append(president['President'])

    # presidents_list[0]['President']
    # presidents_list[0]['Birthplace']
    pairs_list = zip(ids_list, name_list)

    return render_template('index.html', pairs=pairs_list, the_title="Presidents Index")
# your code here
@app.route('/president/<num>')
def detail(num):
    for president in presidents_list:
        if president['Presidency'] == num:
            pres_dict = president
            break

    return render_template('president.html', pres=pres_dict, the_title=pres_dict['President'])



# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
