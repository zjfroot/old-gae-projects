#!/usr/bin/env python
#
# Copyright Jifeng Zhang.
#
#
from google.appengine.ext import db
class Word(db.Model):
    word = db.StringProperty();
    translation = db.StringProperty();
    created = db.DateTimeProperty(auto_now_add=True);
    
class Counter(db.Model):
    name = db.StringProperty();
    count = db.IntegerProperty();