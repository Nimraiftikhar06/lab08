from flask import Flask, render_template # type: ignore

app = Flask(__name__)

# Route for Home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for About Us page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for Membership page
@app.route('/membership')
def membership():
    return render_template('membership.html')

if __name__ == '__main__':
    app.run(debug=True)
