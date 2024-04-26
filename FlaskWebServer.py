from flask import Flask, request, Response, jsonify
import os, time, requests, json, signal, ssl

han_host = os.getenv('HAN_API_HOST')
print(han_host)

# Sample username and password (in production, use a more secure method to store and validate credentials)
USERNAME = 'admin'
PASSWORD = '46GF6OKQIMYX7BJ6N2M0GLWNCBHFWG29'

app = Flask(__name__)

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
        return jsonify(meter_consump), 200
    else return 'Resource Unavailiable', 500
    
@app.route('/electricityStatus')
def electricityStatus():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authenticate()
    params = {"meter_type": "elec"}
    rsp = request_get_response("get_meter_status", params)
    if  rsp.ok:
        meter_consump = json.loads(json.loads(rsp.text)['meter_consump'])
        return jsonify(meter_consump), 200
    else return 'Resource Unavailiable', 500
    
@app.route('/electricityInfo')
def electricityInfo():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authenticate()
    params = {"meter_type": "elec"}
    rsp = request_get_response("get_meter_info", params)
    if  rsp.ok:
        meter_consump = json.loads(json.loads(rsp.text)['meter_consump'])
        return jsonify(meter_consump), 200
     else return 'Resource Unavailiable', 500
    
@app.route('/gas')
def gas():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authenticate()
    params = {"meter_type": "gas"}
    rsp = request_get_response("get_meter_consumption", params)
    if  rsp.ok:
        meter_consump = json.loads(json.loads(rsp.text)['meter_consump'])
        return jsonify(meter_consump), 200
    else return 'Resource Unavailiable', 500
    
@app.route('/gasStatus')
def gasStatus():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authenticate()
    params = {"meter_type": "gas"}
    rsp = request_get_response("get_meter_status", params)
    if  rsp.ok:
        meter_consump = json.loads(json.loads(rsp.text)['meter_consump'])
        return jsonify(meter_consump), 200
    else return 'Resource Unavailiable', 500
    
@app.route('/gasInfo')
def gasInfo():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authenticate()
    params = {"meter_type": "gas"}
    rsp = request_get_response("get_meter_info", params)
    if  rsp.ok:
        meter_consump = json.loads(json.loads(rsp.text)['meter_consump'])
        return jsonify(meter_consump), 200
    else return 'Resource Unavailiable', 500

@app.route('/not_found')
def not_found():
    # Returning a 404 Not Found status code
    return jsonify({'error': 'Resource not found'}), 404

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
    app.run(debug=True, ssl_context=ssl_context, host='0.0.0.0', port=8080)
