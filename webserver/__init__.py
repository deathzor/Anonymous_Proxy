from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import requests
from webserver import filter
from urlparse import urlparse
#FIXME Not everything listed here 
htmlType = {
	'text/html'
}
imageType = {
	'image/jpeg',
	'image/png'
}
cssType = {
	'text/css'
}
#FIXME this table is more then likely incomplete.

class proxy(BaseHTTPRequestHandler):
	def get_url(self,server,page):
		#FIXME hardcoded to https. 
		#SETUP FF useragent:
		headers = {
		    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0',
		}

		try:
			response = requests.get("https://"+server+page, headers=headers, verify='./cacert.pem')
		except requests.exceptions.SSLError as detail:
			return {'html':"<B>SSL ERROR</b><br><pre>"+str(detail)+"</pre>",'header':{'contentType':''}}					
		#FIXME deal with http status other then 200	
		if response.status_code	== 301:
			#FIXME not exactly the same thing as a 301
			return {'security':0,'html':"<META http-equiv=\"refresh\" content=\"0; URL="+filter.htmlEscape(str(response.headers['location']))+"\">",'header':{'contentType':'text/html'}}
		if response.status_code == 200:
			return {'security':1,'html':response.content,'header':{'contentType':response.headers['content-type']}}
		return {'security':1,'html':"<b>Unknown Status</b>"+str(response.status_code),'header':{'contentType':'text/html'}} 

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
		if returnData['header']['contentType'].split(';')[0] in htmlType and returnData['security'] == 1:
			self.wfile.write(filter.html(returnData['html']));
		if returnData['header']['contentType'].split(':')[0] in imageType:
			self.wfile.write(returnData['html']);
		if returnData['header']['contentType'].split(':')[0] in cssType:
			self.wfile.write(filter.css(returnData['html']));
		return
