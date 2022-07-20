from flask import Flask, render_template

from game_of_life import GameOfLife

app = Flask(__name__)
# GameOfLife(25, 25)


@app.route('/')
def index():
    GameOfLife()
    return render_template('index.html')


@app.route('/live')
def live():
    obj_life = GameOfLife(20, 15)
    obj_life.form_new_generation()
    return render_template('live.html', obj_life=obj_life)


if __name__ == "__main__":
    app.run(debug=True)
