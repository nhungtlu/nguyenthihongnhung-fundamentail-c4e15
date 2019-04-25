  
from flask import Flask, render_template, request
from db import add_bike, get_bike
app = Flask(__name__)

@app.route('/')
def get_newbike():
    return render_template('new_bike.html')

@app.route('/', methods=['POST'])
def post_newbike():

    Model = request.form.get('Model')
    Daily_fee = request.form.get('Daily_fee')
    Image = request.form.get('Image')
    Year = request.form.get('Year')
    add_bike(Model,Daily_fee,Image,Year)

    print(get_bike())

    return render_template('new_bike.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)