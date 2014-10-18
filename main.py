#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import urllib2
from urlparse import urlparse

PORT_NUMBER = 8082
#FIXME this table is more then likely incomplete.
html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    ">": "&gt;",
    "<": "&lt;",
    }

#This class will handle browser requests and reply with the real html
class proxy(BaseHTTPRequestHandler):
	def get_url(self,server,page):
		#FIXME currently supports http only because urllib2 has no cert validation
		try:		
			response = urllib2.urlopen("http://"+server+page)
		except urllib2.HTTPError:
			return {'html':"",'header':{'contentType':''}}
		headerContentType = response.info().getheader('Content-Type');
		html = response.read()
		return {'html':html,'header':{'contentType':headerContentType}}
	#Handler for the GET requests
	def html_escape(self,text):
	    """Produce entities within text."""
    	    return "".join(html_escape_table.get(c,c) for c in text)

	def do_GET(self):
		server = self.headers.get('host');
		url = urlparse(self.path);
		page = url.path;
		returnData = self.get_url(server,page);
		self.send_response(200)
		#pass on the content type
		self.send_header('Content-type',returnData['header']['contentType'])
		#setup a no cache header to hopefully prevent cache revelations
		self.send_header('Cache-Control',"no-cache, no-store, must-revalidate");
		self.send_header('Pragma', "no-cache");
		self.send_header('Expires',0);
		self.end_headers()
		# Send the html message
		self.wfile.write("<iframe srcdoc='"+self.html_escape(returnData['html'].replace("https://","http://"))+"' sandbox='allow-forms' style='width:100%;height:100%;border:none;'></iframe>")
		return
try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), proxy)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()


