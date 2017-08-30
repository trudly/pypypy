from flask import Flask
from flask import request
from flask import Response
import subprocess
import string
import array
import binascii
import hashlib
import json
from ctypes import *

lib = cdll.LoadLibrary('./libpure.so')
lib.py_result.restype = c_char_p
py_result = lib.py_result
py_result.restype = c_char_p

app = Flask(__name__)


@app.route('/test')
def qqruqu():
    out = py_result("0505f49384cb054b16f69fc108640a8f627e268f51d897b4f7c74eafe9777fefd9b04abed9eec500000000e321bd84e6b2008879a16497bf6ee58644a36146b63de7c217e7f467b05d67fa01", 164, 166)
    return out


@app.route('/')
def hello_world():
    return 'Hello from Flask!?'
