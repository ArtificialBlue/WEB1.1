from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template('froyo_form.html')

@app.route('/froyo_results', methods=['GET'])
def show_froyo_results():
    context = {
        'flavor': request.args.get('flavor'),
        'toppings': request.args.get('toppings')
    }
    return render_template('froyo_results.html', **context)

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorite_results" method="GET">
        What is your favorite Color? <br/>
        <input type="text" name="color"><br/>
       What is your favorite Animal? <br/>
        <input type="text" name="animal"><br/>
       What is your favorite City? <br/>
        <input type="text" name="city"><br/>       
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/favorite_results')
def favorites_results():
    users_color = request.args.get('color')
    users_animal = request.args.get('animal')
    users_city = request.args.get('city')
    return f'Wow, I didn\'t know {users_color} {users_animal} lived in {users_city}!'

@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
        Enter a Secret Message:<br/>
        <input type="text" name="message"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    users_message = request.form.get('message')
    scrambled_message = sort_letters(users_message)
    return scrambled_message

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('calculator_form.html')

@app.route('/calculator_results', methods=['GET'])
def calculator_results():
    """Shows the user the result of their calculation."""
    context = {
        'first_number': int(request.args.get('operand1')),
        'second_number': int(request.args.get('operand2')),
        'operation': request.args.get('operation')
    }
    if context['operation'] == "add":
        result = context['first_number'] + context['second_number']
    elif context['operation'] == "subtract":
        result = context['first_number'] - context['second_number']
    elif context['operation'] == "multiply":
        result = context['first_number'] * context['second_number']
    else:
        result = context['first_number'] / context['second_number']

    context['result'] = result

    return render_template('calculator_results.html', **context)
 



HOROSCOPE_PERSONALITIES = {
    'aries': 'Adventurous and energetic',
    'taurus': 'Patient and reliable',
    'gemini': 'Adaptable and versatile',
    'cancer': 'Emotional and loving',
    'leo': 'Generous and warmhearted',
    'virgo': 'Modest and shy',
    'libra': 'Easygoing and sociable',
    'scorpio': 'Determined and forceful',
    'sagittarius': 'Intellectual and philosophical',
    'capricorn': 'Practical and prudent',
    'aquarius': 'Friendly and humanitarian',
    'pisces': 'Imaginative and sensitive'
}

@app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')

@app.route('/horoscope_results', methods=['GET'])
def horoscope_results():
    """Shows the user the result for their chosen horoscope."""

    name = request.args.get('users_name')

    horoscope_sign = request.args.get('horoscope_sign')

    users_personality = HOROSCOPE_PERSONALITIES[horoscope_sign]

    lucky_number = random.randint(1, 99)

    context = {
        'horoscope_sign': horoscope_sign,
        'personality': users_personality, 
        'lucky_number': lucky_number,
        'users_name': name
    }

    return render_template('horoscope_results.html', **context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
