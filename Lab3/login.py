#!/usr/bin/env python3
import cgi, cgitb
from http.cookies import SimpleCookie

form = cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('password')


from templates import secret_page, after_login_incorrect
from secret import username as username_secret, password as password_secret

# Question 6
import os
cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
if cookie.get("username"):
    username = cookie.get("username").value
if cookie.get("password"):
    password = cookie.get("password").value

# Question 5
if(username.upper() == username_secret.upper() and password == password_secret):
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")
    print("Content-Type: text/html\r\n")
    print(secret_page(username, password))
else: # Question 6
    print("Content-Type: text/html\r\n")
    print(after_login_incorrect())