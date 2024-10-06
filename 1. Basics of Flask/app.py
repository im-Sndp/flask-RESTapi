from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page"

@app.route("/about")
def about():
    return "This is the About Page"

@app.route("/user/<username>")
def show_user_profile(username):
    return f"User: {username}"

@app.route('/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        return "This is a POST request"
    else:
        return "This is a GET request"

@app.route('/search')
def search():
    query = request.args.get('query')  # Get the value of 'query'
    return f'Search Results for: {query}'

if __name__  == "__main__":
    app.run(debug=True)