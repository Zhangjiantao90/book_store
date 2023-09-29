from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# The UI:
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('addbook.html')
        
        
@app.route('/submit',methods=['POST'])
def submit():
    identifier=request.form['identifier']
    name=request.form['name']
    author=request.form['author']
    data={"identifier":identifier,"name":name,"author":author}
    response = requests.post('http://book-library/books',data=data)
    return response.json()['message']
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
