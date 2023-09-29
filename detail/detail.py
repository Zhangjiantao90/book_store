from flask import Flask
import requests

app = Flask(__name__)

# The UI:
@app.route('/<identifier>')
def index(identifier):     
    """ Display productpage with normal user and test user buttons"""
    headers = {'Connection': 'close'}
    requests.adapters.DEFAULT_RETRIES = 5
    try:
    	response=requests.get('http://book-library/book/'+identifier,headers =headers, verify=False)
    except:
    	response=requests.get('http://book-library/book/'+identifier,headers =headers, verify=False)
    data=response.json()['data']
    return data

        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
