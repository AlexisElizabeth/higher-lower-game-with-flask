from flask import Flask
from random import randint
app = Flask(__name__)
secret_number = randint(0, 9)

@app.route('/')
def guess_a_number():
    print(secret_number)
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<int:number>')
def guess(number):
    if number > secret_number:
        return '<h1 style="color:purple">Too high!  Try again!</h1><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=200>'
    elif number < secret_number:
        return '<h1 style="color:red">Too low!  Try again!</h1><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=200>'
    else:
        return '<h1 style="color:green"">You found me!</h1><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=200>'


if __name__ == "__main__":
    app.run(debug=True)


