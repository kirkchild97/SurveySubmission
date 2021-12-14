from flask import Flask, redirect, session, request, render_template
from datetime import date
app = Flask(__name__)
app.secret_key = '1456465468464'

@app.route('/')
def surveyPage():
    print('Wut')
    return render_template('survey.html')

@app.route('/submitSurvey', methods=['POST'])
def submitSurvey():
    if 'submissions' not in session:
        session['submissions'] = []
    session['submissions'].append({
    'first_name' : request.form['first_name'],
    'last_name' : request.form['last_name'],
    'dojo_program' : request.form['dojoProgram'],
    'favorite_language' : request.form['favorite_language'],
    'comment' : request.form['comment'],
    'date_submitted' : date.today().strftime("%m/%d/%Y")
    })
    session['count'] = len(session['submissions']) - 1
    print(session)
    return redirect('/submissions')

@app.route('/submissions')
def show_submissions():
    return render_template('submitted.html')

if __name__ == "__main__":
    app.run(debug= True)