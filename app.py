from flask import Flask, request, render_template
from dotenv import load_dotenv
import os
from randomm import randomgender, randomdog, randomcat
load_dotenv()

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api')
def main():
    params = request.args
    if params['name'].lower() == 'male' or params['name'].lower() == 'female':
        title = params['name'].capitalize()
        users = randomgender(gender=params['name'], number=int(params['number']))
        return render_template('index.html',
                               context={
                                   'title':title,
                                   'users': users
                               })
    elif params['name'].lower() == 'dog':
        title = params['name'].capitalize()
        users = randomdog(name=params['name'], number=int(params['number']))
        return render_template('index.html',
                               context={
                                   'title':title,
                                   'users':users
                               })
    elif params['name'].lower() == 'cat':
        title = params['name'].capitalize()
        users = randomcat(name=params['name'], number=int(params['number']))
        return render_template('index.html',
                               context={
                                   'title':title,
                                   'users': users
                               })

if __name__ == "__main__":
    app.run(debug=os.getenv('DEBUG'), port=os.getenv("PORT"))

