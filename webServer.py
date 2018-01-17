import http.server
from urllib.parse import urlparse

PARAMS = '127.0.0.1', 8080

class WebHandler(http.server.BaseHTTPRequestHandler) :
    def do_GET(self):
        infos = []
        parse = str(urlparse(self.path))
        infos = [
            infos.append('client_address: %s' % str(self.client_address)),
            infos.append('address_string: %s' % str(self.address_string)),
            infos.append('command: %s' % str(self.command)),
            infos.append('unparsed path: %s' % str(self.path)),
            infos.append('parsed path: %s' % parse), 
            infos.append('request version: %s' % str(self.request_version)),
            infos.append('server version: %s' % str(self.server_version)),
            infos.append('sys version: %s' % str(self.sys_version)),   
            infos.append('protocol version: %s' % str(self.protocol_version))
        ]
        for k, v in self.headers.items(): infos.append('HEADER %s: %s' % (k, v.strip()))
        self.send_response(200)
        self.send_header(b'Content-type',b'text-html')
        self.end_headers()
        infos = b'<ul><li>' + b'</li><li>'.join([bytes(str(i), "utf-8") for i in infos]) + b'</li></ul>'  
        self.wfile.write(b"""<html><head><title>Hello World</title></head><body><p>hello world</p>""" + infos + b"""</body></html>""")
        return
 

def run():
  print('starting server...')
 
  server = http.server.HTTPServer(PARAMS, WebHandler)
  print('running server...')
  server.serve_forever()
 
run()
        

