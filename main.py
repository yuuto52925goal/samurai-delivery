import os
import random
from flask_cors import CORS
from flask import Flask, abort, render_template, redirect, url_for, flash, jsonify, send_file
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)
CORS(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/image/random")
def random_image():
    try:
        files = os.listdir("./samurai_hero_image")
        image_files = [file for file in files if file.lower().endswith(('png', 'jpg', 'jpeg', 'gif'))]
        if not image_files:
            return jsonify({'error': 'No image files found'}), 404
        random_samurai_image = random.choice(image_files)
        image_path = os.path.join("./samurai_hero_image", random_samurai_image)
        return send_file(image_path, mimetype='image/jpeg')
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == "__main__":
    app.run(debug=True, port=5002)
