"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaarom7avj5o49i4ogg-a.oregon-postgres.render.com",
        database="todo_63vc",
        user="root",
        password="HkRgOSlmdSmGudIm4dKKJcSDV5p5xdK6")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
