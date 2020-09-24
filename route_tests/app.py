from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/color_form')
def show_color_form():
    return """
    <form action="/color_results" method="GET">
        <label>
            What's your favorite color?
            <input type="text" name="color">
        </label>
        <input type="submit" name="Submit!">
    </form>
    """


@app.route('/color_results')
def process_color_results():
    users_favorite_color = str(request.args.get('color')).lower().strip()
    print(users_favorite_color)
    if(not users_favorite_color):
        return "You didn't enter a color"

    return f"Wow, {users_favorite_color} is my favorite color, too!"


@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return """
    <form action="/froyo_results" method="GET">
        What is your favorite Fro-Yo flavor? <br/>
        <input type="text" name="flavor"><br/><br/>
        What toppings do you want?
        <input type="text" name="toppings"><br/>
        <input type="submit" value="Submit!">
    </form>
    """


@app.route('/froyo_results')
def show_froyo_results():
    users_froyo_flavor = request.args.get('flavor')
    toppings = request.args.get('toppings')

    if(not users_froyo_flavor):
        return "You didn't enter a flavor of froyo"

    if(not toppings):
        toppings = "no toppings"

    return f'You ordered {users_froyo_flavor} flavored Fro-Yo with toppings {toppings}!'


@app.route('/reverse_message')
def reverse_message_form():
    return """
    <form action="/message_results" method="POST">
        What's your message?
        <input type="text" name="message">
        <input type="submit" value="Submit!">
    </form>
    """


@app.route('/message_results', methods=['POST'])
def message_results():
    message = request.form.get('message')
    reversed_message = reverse(message)

    if(not message):
        return "You didn't enter a message."

    return f'Here\'s your reversed message: {reversed_message}'


def reverse(str):
    """Reverses the characters in a string."""
    return str[::-1]


@app.route('/calculator')
def calculator():
    return """
    <form action="/calculator_results" method="GET">
        Please enter 2 numbers and select an operator.<br/><br/>
        <input type="number" name="operand1">
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input type="number" name="operand2">
        <input type="submit" value="Submit!">
    </form>
    """


@app.route('/calculator_results')
def calculator_results():

    input_operand1 = request.args.get('operand1')
    input_operand2 = request.args.get('operand2')

    if(not input_operand1 or not input_operand2):
        return "Please enter two operands."

    operand1 = int(input_operand1)
    operand2 = int(input_operand2)
    operation = request.args.get('operation')

    if(operand2 == 0 and operation == "divide"):
        return "You Cannot Divide By Zero."

    if operation == 'add':
        result = operand1 + operand2
    elif operation == 'subtract':
        result = operand1 - operand2
    elif operation == 'multiply':
        result = operand1 * operand2
    else:
        result = operand1 / operand2
    return f'You chose to {operation} {operand1} and {operand2}. Your result is: {result}'


if __name__ == '__main__':
    app.run(debug=True)
