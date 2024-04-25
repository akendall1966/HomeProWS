# Import the necessary modules
from http.server import BaseHTTPRequestHandler, HTTPServer
import os, time, requests, json, signal, ssl

han_host = os.getenv('HAN_API_HOST')
print(han_host)

# Define the HTTP request handler class
class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    # Handle GET requests
    def do_GET(self):
        match self.path:

            case '/electricity':
                # Set response status code
                self.send_response(200)
                params = {"meter_type": "elec"}
                # Set headers
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                rsp = request_get_response("get_meter_consumption", params)
                if  rsp.ok:
                    meter_consump = json.loads(json.loads(rsp.text)['meter_consump'])
                    output = json.dumps(meter_consump)
                    self.wfile.write(output.encode('utf8'))
                    return
                
            case '/electricityStatus':
                # Set response status code
                self.send_response(200)
                params = {"meter_type": "elec"}
                # Set headers
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                rsp = request_get_response("get_meter_status", params)
                if  rsp.ok:
                    meter_consump = json.loads(json.loads(rsp.text)['meter_status'])
                    output = json.dumps(meter_consump)
                    self.wfile.write(output.encode('utf8'))
                    return

            case '/electricityInfo':
                # Set response status code
                self.send_response(200)
                params = {"meter_type": "elec"}
                # Set headers
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                rsp = request_get_response("get_meter_info", params)
                if  rsp.ok:
                    meter_consump = json.loads(json.loads(rsp.text)['meter_info'])
                    output = json.dumps(meter_consump)
                    self.wfile.write(output.encode('utf8'))
                    return

                
            case '/gas':
                # Set response status code
                self.send_response(200)
                params = {"meter_type": "gas"}
                # Set headers
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                rsp = request_get_response("get_meter_consumption", params)
                if  rsp.ok:
                    meter_consump = json.loads(json.loads(rsp.text)['meter_consump'])
                    output = json.dumps(meter_consump)
                    self.wfile.write(output.encode('utf8'))
                    return

            case '/gasStatus':
                # Set response status code
                self.send_response(200)
                params = {"meter_type": "gas"}
                # Set headers
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                rsp = request_get_response("get_meter_status", params)
                if  rsp.ok:
                    meter_consump = json.loads(json.loads(rsp.text)['meter_status'])
                    output = json.dumps(meter_consump)
                    self.wfile.write(output.encode('utf8'))
                    return

            case '/gasInfo':
                # Set response status code
                self.send_response(200)
                params = {"meter_type": "gas"}
                # Set headers
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                rsp = request_get_response("get_meter_info", params)
                if  rsp.ok:
                    meter_consump = json.loads(json.loads(rsp.text)['meter_info'])
                    output = json.dumps(meter_consump)
                    self.wfile.write(output.encode('utf8'))
                    return

            case _:
                self.send_response(404)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
    #           self.wfile.write(b'404 Not Found')

# Call an API and return the response
def request_get_response(api, params):
    print(f"Calling API: {api}")
    url = f"{han_host}/" + f"{api}"
    response = requests.get(url, json=params)
    return response

# Define the main function
def main():
    # Set server address and port
    server_address = ('', 443)
    certfile = '/root/certificate.crt'
    keyfile = '/root/private_key.key'
    # Create an HTTP server instance
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    httpd.socket = ssl.wrap_socket(httpd.socket, certfile=certfile, keyfile=keyfile, server_side=True)
    # Print a message indicating the server has started
    print('Secure server started on port 443...')
    httpd.serve_forever()

# If the script is executed directly, run the main function
if __name__ == '__main__':
    main()
