from flask import Flask, render_template, redirect
import requests

app = Flask(__name__)

# The UI:
@app.route('/')
@app.route('/index.html')
def index():
        
    """ Display productpage with normal user and test user buttons"""
    headers = {'Connection': 'close'}
    requests.adapters.DEFAULT_RETRIES = 5
    try:
    	response=requests.get('http://book-library/books',headers =headers, verify=False)
    except:
    	response=requests.get('http://book-library/books',headers =headers, verify=False)
    data=response.json()['data']
    print(data)
    return render_template('productpage.html', books=data, detail=detail)

@app.route('/detail/<iden>')
def detail(iden):
    #return f'hello,{iden}'
    headers = {'Connection': 'close'}
    requests.adapters.DEFAULT_RETRIES = 5
    try:
    	response=requests.get('http://detail/'+iden,headers =headers, verify=False)
    except:
    	response=requests.get('http://detail/'+iden,headers =headers, verify=False)
    return response.json()
        
@app.route('/addbook')
def addbook():
    return redirect('http://localhost:5003/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
