from app import app

#home page
@app.route("/")
def home():
    return "<h1>My Blog<h1>"