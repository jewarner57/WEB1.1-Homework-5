import pytest

from .app import app

#######################
# Index Tests
# (there's only one here because there is only one possible scenario!)
#######################


def test_index():
    """Test that the index page shows "Hello, World!" """
    res = app.test_client().get('/')
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    expected_page_text = "Hello, World!"
    assert expected_page_text == result_page_text


#######################
# Color Tests
#######################

def test_color_results_blue():
    result = app.test_client().get('/color_results?color=blue')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = 'Wow, blue is my favorite color, too!'
    assert expected_page_text == result_page_text


def test_color_results_red():
    result = app.test_client().get('/color_results?color=RED')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = 'Wow, red is my favorite color, too!'
    assert expected_page_text == result_page_text


def test_color_results_edgecase1():
    result = app.test_client().get('/color_results?color=')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = 'You didn\'t enter a color'
    assert expected_page_text == result_page_text


#######################
# Froyo Tests
#######################

def test_froyo_results_vanilla():
    result = app.test_client().get('/froyo_results?flavor=vanilla&toppings=gummy+bears')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = 'You ordered vanilla flavored Fro-Yo with toppings gummy bears!'
    assert expected_page_text == result_page_text


def test_froyo_results_strawberry():
    result = app.test_client().get(
        '/froyo_results?flavor=strawberry&toppings=gummy+bears%2C+gummy+worms')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = 'You ordered strawberry flavored Fro-Yo with toppings gummy bears, gummy worms!'
    assert expected_page_text == result_page_text


def test_froyo_results_edgecase1():
    result = app.test_client().get(
        '/froyo_results?flavor=&toppings=gummy+bears')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = 'You didn\'t enter a flavor of froyo'
    assert expected_page_text == result_page_text


def test_froyo_results_edgecase2():
    result = app.test_client().get(
        '/froyo_results?flavor=vanilla&toppings=')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = 'You ordered vanilla flavored Fro-Yo with toppings no toppings!'
    assert expected_page_text == result_page_text


#######################
# Reverse Message Tests
#######################

def test_message_results_helloworld():
    form_data = {
        'message': 'Hello World'
    }
    res = app.test_client().post('/message_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert 'dlroW olleH' in result_page_text


def test_message_results_testing():
    form_data = {
        'message': 'testing'
    }
    res = app.test_client().post('/message_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert 'gnitset' in result_page_text


def test_message_results_edgecase1():
    form_data = {
        'message': ''
    }
    res = app.test_client().post('/message_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert 'You didn\'t enter a message.' == result_page_text


#######################
# Calculator Tests
#######################

def test_calculator_results_addition():
    result = app.test_client().get(
        '/calculator_results?operand1=1&operation=add&operand2=2001')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "2002"
    assert expected_page_text in result_page_text


def test_calculator_results_subtract():
    result = app.test_client().get(
        '/calculator_results?operand1=70&operation=subtract&operand2=105')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "-35"
    assert expected_page_text in result_page_text


def test_calculator_results_multiply():
    result = app.test_client().get(
        '/calculator_results?operand1=70&operation=multiply&operand2=105')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "7350"
    assert expected_page_text in result_page_text


def test_calculator_results_divide():
    result = app.test_client().get(
        '/calculator_results?operand1=50&operation=divide&operand2=25')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "2"
    assert expected_page_text in result_page_text


def test_calculator_results_edgecase1():
    result = app.test_client().get(
        '/calculator_results?operand1=50&operation=divide&operand2=0')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "You Cannot Divide By Zero."
    assert expected_page_text in result_page_text


def test_calculator_results_edgecase2():
    result = app.test_client().get(
        '/calculator_results?operand1=&operation=add&operand2=')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "Please enter two operands."
    assert expected_page_text in result_page_text
