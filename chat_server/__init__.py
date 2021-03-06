#!/usr/bin/env python3
from flask import Flask,render_template, request, session, Response, redirect

from math import sqrt
from typing import List
from os import chdir
from os.path import dirname, realpath

import json
import time

if __package__ is None or __package__ == '':
    from database import connector
    from model import entities
else:
    from .database import connector
    from .model import entities


db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)


@app.route('/static/<content>')
def static_content(content):
    return render_template(content)


@app.route('/espar/<n>')
def espar(n: int) -> str:
    if ((int(n) % 2) == 0):
        return 'True'
    else:
        return 'False'


@app.route('/esprimo/<n>')
def esprimo(n: int) -> str:
    _n: int = int(n)
    if(_n == 2):
        return 'True'

    primeList: List[int] = [2]
    for i in range(3, int(sqrt(_n)+2), 2):
        isPrime: bool = True
        for j in primeList:
            if ((i % j) == 0):
                isPrime = False
                break

        if (isPrime):
            primeList.append(i)

    for i in primeList:
        if((_n % i) == 0):
            return 'False'

    return 'True'


@app.route('/palindrome/<palabra>')
def palindrome(palabra: str) -> str:
    for i in range(0, int(len(palabra)/2)):
        if(palabra[i] != palabra[len(palabra)-1-i]):
            return 'False'
    return 'True'


@app.route('/multiplo/<n1>/<n2>')
def multiplo(n1: str, n2: str) -> str:
    _n1: int = int(n1)
    _n2: int = int(n2)

    if((_n1 % _n2) == 0):
        return 'True'
    else:
        return 'False'


def main():
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))


if __name__ == '__main__':
    main()
