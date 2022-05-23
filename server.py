from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def myHome():
    return render_template('index.html')

@app.route('/<string:page_name>')
def htmlPage(page_name):
    return render_template(page_name, pageName=page_name)

def writeToFile(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

def writeToCSV(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csvWriter = csv.writer(database2, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csvWriter.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submitForm():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            writeToCSV(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'

# @app.route('/works.html')
# def work():
#     return render_template('works.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')