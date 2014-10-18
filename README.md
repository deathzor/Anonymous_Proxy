Anonymous_Proxy
===============

A proxy Designed to strip away as much of the information from the Browser as Possible<br>
<br>
TODO:<br>
1. Currently NO SSL support is implemented this needs to be enforced<br>
2. Currently Everything in in once file this needs to be fix <br>
3. HTML stripper is more then likely missing characters making a XSS against the rendered page possible<br>
4. PORT Number needs to be dynamic loaded from a config file. <br>
5. Detection of browsers not supporting sandboxing in iframes. <br>
6. Cookie's are currently not handled at all those need to be handled locally on the Proxy Side to prevent user mistaking leaking his identity by using the machine outside of Tor. <br>
7. POST requests are not handled at all. <br>
8. SSL Support on the request side needs to be implemented. <br>
9. https to http replace needs to be removed ( dirty hack to keep the browser from going to ssl pages ). <br>
10. Some other stuff i more then like forgot about. <br>
<br>
What works:<br>
1. Cache is set to 0 for all requests AND urllib2 ignore's cache completely <br>
2. Cookie's are stripped from the client<br>
3. Javascript is disabled ( via html5 sandbox frames ). <br>
4. Content-type is forwarded in the header <br>
5. All requests headers look the same regardless of OS or browser. <br>
