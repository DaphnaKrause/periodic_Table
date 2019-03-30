from flask import Flask, render_template
from modules import convert_to_dict
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

elements_list = convert_to_dict("Periodic_Table.csv")

@app.route('/')
def index():
    ids_list = []
    name_list = []
    for element in elements_list:
        ids_list.append(element['atomic_number'])
        name_list.append(element['name'])
    pairs_list = zip(ids_list, name_list)

    return render_template('index.html', pairs=pairs_list, the_title="List of Elements")

@app.route('/element/<num>')
def detail(num):
    for element in elements_list:
        if element['atomic_number'] == num:
            elem_dict = element
            break
    return render_template('element.html', elem=elem_dict, the_title=elem_dict['name'])

if __name__ == '__main__':
    app.run(debug=True)
