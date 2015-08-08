#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module: todoapp.py
Author: zlamberty
Created: 2015-08-07

Description:
    test app "todo list"

Usage:
    <usage>

"""

from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://test_webapp:test_webapp@localhost/todoapp'

from views import *


if __name__ == '__main__':

    app.run()
