#!/usr/bin/env python3
import os, json

print("Content-type:text/html\r\n\r\n")
print("<title>Test CGI</title>")
print("<p>Hello World</p>")

json_object = json.dumps(dict(os.environ))
print("Environmental Variables:")
print(json_object)
print("<br>")

for param in os.environ.keys():
    if(param == "QUERY_STRING"):
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))

for param in os.environ.keys():
    if(param == "HTTP_USER_AGENT"):
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))
