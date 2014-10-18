Anonymous_Proxy
===============

A proxy Designed to strip away as much of the information from the Browser as Possible

TODO:
1. Currently NO SSL support is implemented this needs to be enforced
2. Currently Everything in in once file this needs to be fix 
3. HTML stripper is more then likely missing characters making a XSS against the rendered page possible
4. PORT Number needs to be dynamic loaded from a config file. 
5. Detection of browsers not supporting sandboxing in iframes. 
6. Cookie's are currently not handled at all those need to be handled locally on the Proxy Side to prevent user mistaking leaking his identity by using the machine outside of Tor. 
7. POST requests are not handled at all. 
8. SSL Support on the request side needs to be implemented. 
9. https to http replace needs to be removed ( dirty hack to keep the browser from going to ssl pages ). 
10. Some other stuff i more then like forgot about. 

What works:
1. Cache is set to 0 for all requests AND urllib2 ignore's cache completely 
2. Cookie's are stripped from the client
3. Javascript is disabled ( via html5 sandbox frames ). 
4. Content-type is forwarded in the header 
5. All requests headers look the same regardless of OS or browser. 
