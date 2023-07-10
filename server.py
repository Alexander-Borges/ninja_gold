from flask import Flask, render_template, request, redirect, session 
import random
import datetime

app = Flask(__name__)
app.secret_key = 'mykey'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []
    activity_log = session['activities']
    return render_template('index.html', gold=session['gold'], activity_log=activity_log)

@app.route('/process_money', methods = ["POST"])
def process_money():
    building = request.form['building']
    earned_gold = 0
    activity = {'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

    if building == 'farm':
        earned_gold = random.randint(10,20)
    elif building == 'cave':
        earned_gold = random.randint(5,10)
    elif building == 'house':
        earned_gold = random.randint(2,5)
    elif building == 'casino':
        earned_gold = random.randint(-50,50)

    session['gold'] += earned_gold
    activity['earned_gold'] = earned_gold
    activity['building'] = building
    session['activities'].append(activity)

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)


