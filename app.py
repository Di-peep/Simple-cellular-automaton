from flask import Flask, render_template

from game_of_life import GameOfLife

app = Flask(__name__)


@app.route('/')
def index():
    GameOfLife(20, 15)
    return render_template('index.html')


@app.route('/live')
def live():
    # if you pass arguments to the constructor, then each time a new object will be created
    # so the arguments are passed in the index function and here the singleton property is used
    obj_life = GameOfLife()
    obj_life.form_new_generation()
    return render_template('live.html', obj_life=obj_life)


if __name__ == "__main__":
    app.run(debug=True)
