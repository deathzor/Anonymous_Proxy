Rubbergloves
===============

A proxy Designed to strip away as much of the information from the Browser as Possible<br>
<br>
TODO:<br>
1. Currently Everything in in once file this needs to be fix <br>
2. HTML stripper is more then likely missing characters making a XSS against the rendered page possible<br>
3. PORT Number needs to be dynamic loaded from a config file. <br>
4. Detection of browsers not supporting sandboxing in iframes. <br>
5. Cookie's are currently not handled at all those need to be handled locally on the Proxy Side to prevent user mistaking leaking his identity by using the machine outside of Tor. <br>
6. POST requests are not handled at all. <br>
7. SSL Support on the request side needs to be implemented. <br>
8. https to http replace needs to be removed ( dirty hack to keep the browser from going to ssl pages ). <br>
9. Some other stuff i more then like forgot about. <br>
<br>
What works:<br>
1. Cache is set to 0 for all requests AND urllib2 ignore's cache completely <br>
2. Cookie's are stripped from the client<br>
3. Javascript is disabled ( via html5 sandbox frames ). <br>
4. Content-type is forwarded in the header <br>
5. All requests headers look the same regardless of OS or browser. <br>
