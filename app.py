from flask import Flask, render_template

app = Flask("Diagnos")

@app.route("/")
def home():
	return render_template("index.html")

@app.route('/contact')
def contact():
	return render_template('contact.html')

if __name__ == "__main__":
	app.run("0.0.0.0", debug=True)