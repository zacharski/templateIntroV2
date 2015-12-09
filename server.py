from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def mainIndex():
	return render_template('index.html')

@app.route('/officers')
def showOfficers():
	return render_template('clubOfficers.html')


# start the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8080, debug=True)
