#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import requests
from urlparse import urlparse

PORT_NUMBER = 8082
#FIXME Not everything listed here 
potental_html = {
	'text/html'
}
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
		#FIXME hardcoded to https for the future still no cert validation 
		#SETUP FF useragent:
		headers = {
		    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0',
		}

		try:
			response = requests.get("https://"+server+page, headers=headers, verify='./cacert.pem')
		except requests.exceptions.SSLError as detail:
			return {'html':"<B>SSL ERROR</b><br><pre>"+str(detail)+"</pre>",'header':{'contentType':''}}					
		#FIXME deal with http status other then 200	
		if response.status_code	!= 200:
			return {'html':"",'header':{'contentType':''}}
		
		headerContentType = response.headers['content-type'];
		html = response.content;
		return {'html':html,'header':{'contentType':headerContentType}}
	#Handler for the GET requests
	def html_escape(self,text):
	    """Produce entities within text."""
    	    return "".join(html_escape_table.get(c,c) for c in text)

	def do_GET(self):
		server = self.headers.get('host');
		url = urlparse(self.path);
		if url.query == "":
			page = url.path;
		else:
			page = url.path+"?"+url.query

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
		if returnData['header']['contentType'].split(';')[0] in potental_html:
			#fixing Links because we are striping https to http
			returnData['html'] = returnData['html'].replace("https://", "http://");
			#fixing Links because the site is loaded in a iframe
			returnData['html'] = returnData['html'].replace("<a", "<a target=\"_top\"");
			self.wfile.write("<html><body><iframe srcdoc='"+self.html_escape(returnData['html'])+"' sandbox='allow-forms allow-top-navigation' style='width:100%;height:100%;border:none;' seamless></iframe></body></html>")
		else:
			self.wfile.write(returnData['html']);					
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


