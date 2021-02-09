from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def mad_lib(adjective,noun):
    return f'There once was a {adjective} {noun} who had a lot of {adjective} {noun} children.'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    try: 
        int(number1)
        int(number2)
        result = int(number1) * int(number2)
        return f'{number1} times {number2} is {result}.'
    except ValueError:
        return "Invalid inputs. Please try again by entering 2 numbers!"

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word,n):
    try: 
        int(n)
        return (word + ' ')  * int(n)
    except ValueError:
        return "Invalid input. Please try again by entering a word and a number!"


if __name__ == '__main__':
    app.run(debug=True)
