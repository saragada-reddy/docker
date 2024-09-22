# The Docker image contains the following code
from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def showPinehead():
    html = "<div style='text-align:center;margin:20px;'><h1>Greetings from Edu!</h1><h2>This is Version 1</h2><img src='https://media.licdn.com/dms/image/C4D0BAQHIXUJjedkclA/company-logo_200_200/0/1645442188611/edureka_logo?e=2147483647&v=beta&t=eb0Kf9Sxmw9lxuK3_Msn37XJffpwyyYSn-A47YeR0oA' width='40%' alt='Pinehead @ Edureka'></div>"
    return html

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)