from flask import Flask, request, Response
import os, time, requests, json, signal, ssl

app = Flask(__name__)

# Sample username and password (in production, use a more secure method to store and validate credentials)
USERNAME = 'admin'
PASSWORD = 'password'

# Call an API and return the response
def request_get_response(api, params):
    print(f"Calling API: {api}")
    url = f"{han_host}/" + f"{api}"
    response = requests.get(url, json=params)
    return response

@app.route('/electricity')
def electricity():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authenticate()
    params = {"meter_type": "elec"}
    rsp = request_get_response("get_meter_consumption", params)
    if  rsp.ok:
        meter_consump = json.loads(json.loads(rsp.text)['meter_consump'])
        output = json.dumps(meter_consump)
        return jsonify(output)
    
@app.route('/electricityStatus')
def electricity():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authenticate()
    params = {"meter_type": "elec"}
    rsp = request_get_response("get_meter_status", params)
    if  rsp.ok:
        meter_consump = json.loads(json.loads(rsp.text)['meter_consump'])
        output = json.dumps(meter_consump)
        return jsonify(output)
    
@app.route('/electricityStatus')
def electricity():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authenticate()
    params = {"meter_type": "elec"}
    rsp = request_get_response("get_meter_status", params)
    if  rsp.ok:
        meter_consump = json.loads(json.loads(rsp.text)['meter_consump'])
        output = json.dumps(meter_consump)
        return jsonify(output)

def check_auth(username, password):
    """Check if a username and password are valid."""
    return username == USERNAME and password == PASSWORD

def authenticate():
    """Send a 401 response to request authentication."""
    return Response(
        'Unauthorized. Please provide valid credentials.',
        401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )

if __name__ == '__main__':
    # Use SSL context to configure SSL certificate and key
    ssl_context = ('cert.pem', 'key.pem')
    app.run(debug=True, ssl_context=ssl_context)
