from app import app

@app.route('/')
def indes():
    return render_template('index.html')

@app.route('/login/', methods=['POST'])
def login():
    return render_template('login.html')

@app.route('/search/', methods=['POST'])
def search():
    return render_template('search.html')