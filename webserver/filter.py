html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    ">": "&gt;",
    "<": "&lt;",
    }
def htmlEscape(text):
	    """Produce entities within text."""
    	    return "".join(html_escape_table.get(c,c) for c in text)
def html(html):
	#fixing Links because we are striping https to http
	html = html.replace("https://", "http://");
	#fixing Links because the site is loaded in a iframe
	html = html.replace("<a", "<a target=\"_top\"");
	html = "<html><body><iframe srcdoc='"+htmlEscape(html)+"' sandbox='allow-forms allow-top-navigation' style='width:100%;height:100%;border:none;' seamless></iframe></body></html>";
	return html
def css(css):
	return css;
def jpeg(jpeg):
	return jpeg;
