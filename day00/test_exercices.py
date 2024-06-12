import subprocess
import sys
from ex01.format_ft_time import format_time, scientific_notation
from ex02.find_ft_type import all_thing_is_obj
from ex05.building import main, print_data, parser
from ex06.ft_filter import ft_filter


def test_ex00():
    result = subprocess.run(['python3', 'ex00/Hello.py'], capture_output=True, text=True)
    expected_output = (
        "['Hello', 'World!']\n"
        "('Hello', 'France!')\n"
        "{'Hello', 'Paris!'}\n"
        "{'Hello': '42Paris!'}\n"
    )
    assert result.stdout == expected_output


def test_ex01():
    assert format_time(1) == 'Invalid Value!'
    assert format_time(1.0) == '1.0'
    assert format_time(1234) == 'Invalid Value!'
    assert format_time(1234.0) == '1,234.0'
    assert format_time(-1.0) == 'Invalid Value!'
    assert format_time(0) == 'Invalid Value!'

    assert scientific_notation(1) == 'Invalid Value!'
    assert scientific_notation(1.0) == 'Invalid Value!'
    assert scientific_notation(1234) == '1.23e+03'
    assert scientific_notation(1234.0) == '1.23e+03'
    assert scientific_notation(-1.0) == 'Invalid Value!'
    assert scientific_notation(0) == 'Invalid Value!'


def test_ex02():
    result = subprocess.run(['python3', 'test_02.py'], capture_output=True, text=True)
    expected_output =  "List : <class 'list'>\n" + \
        "Tuple : <class 'tuple'>\n" + \
        "Set : <class 'set'>\n" + \
        "Dict : <class 'dict'>\n" + \
        "Brian is in the kitchen : <class 'str'>\n" + \
        "Toto is in the kitchen : <class 'str'>\n" + \
        "Type not found\n" + \
        "42\n"
    assert result.stdout == expected_output


def test_ex03():
    result = subprocess.run(['python3', 'test_03.py'], capture_output=True, text=True)
    expected_output = "Nothing: None <class 'NoneType'>\n" + \
        "Cheese: nan <class 'float'>\n" + \
        "Zero: 0 <class 'int'>\n" + \
        "Empty: <class 'str'>\n" + \
        "Fake: False <class 'bool'>\n" + \
        "Type not Found\n" + \
        "1\n"
    assert result.stdout == expected_output


def test_ex04():
    process = lambda arg: subprocess.run(['python3', 'ex04/whatis.py', arg], capture_output=True, text=True)
    assert process('+5').stdout == "I'm Odd.\n" 
    assert process('5').stdout == "I'm Odd.\n" 
    assert process('-5').stdout == "I'm Odd.\n" 
    assert process('+4').stdout == "I'm Even.\n" 
    assert process('4').stdout == "I'm Even.\n" 
    assert process('-4').stdout == "I'm Even.\n" 
    assert process('+0').stdout == "I'm Even.\n" 
    assert process('0').stdout == "I'm Even.\n" 
    assert process('-0').stdout == "I'm Even.\n"
    assert process('').stdout == ''
    assert "AssertionError: argument is not an integer\n" in process('Hi!').stderr
    assert "AssertionError: more than one argument is provided\n" in subprocess.run(['python3', 'ex04/whatis.py', '12', '0'], capture_output=True, text=True).stderr


def test_ex05():
    process = lambda arg: subprocess.run(['python3', 'ex05/building.py', arg], capture_output=True, text=True)
    assert process("Hi").stdout == "The text contains 2 characters:\n1 upper letters\n1 lower letters\n0 punctuation marks\n0 spaces\n0 digits\n"
    assert process("Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.").stdout == "The text contains 171 characters:\n2 upper letters\n121 lower letters\n8 punctuation marks\n25 spaces\n15 digits\n"
    result = subprocess.run(['python3', 'ex05/building.py'], input="Hi!\n", capture_output=True, text=True)
    assert result.stdout == "What is the text to count?\nThe text contains 4 characters:\n1 upper letters\n1 lower letters\n1 punctuation marks\n1 spaces\n0 digits\n"
    result = subprocess.run(['python3', 'ex05/building.py'], input="\n", capture_output=True, text=True)
    assert result.stdout == "What is the text to count?\nThe text contains 1 characters:\n0 upper letters\n0 lower letters\n0 punctuation marks\n1 spaces\n0 digits\n"
    result = subprocess.run(['python3', 'ex05/building.py', "Multiple", "Strings"], capture_output=True, text=True)
    assert "AssertionError: usage: python3 building.py <string>" in result.stderr



def test_06a():
    functions = [
        lambda n: n % 2,
        lambda string: 'T' in string,
        lambda boolean: True,
        None,
    ]
    lists = [
        [0, 1, 2, 3, 4, 5, 6],
        ["My name is Tom", "Hello How Are You?", "I like potatoes"],
        [1, True, 'HIIII', None, 0, 3.1415],
        ["It's", "a mystery", list, "that", 1, "have", True, 42.0],
    ]
    for i in range(len(functions)):
        assert list(filter(functions[i], lists[i])) == ft_filter(functions[i], lists[i])

def test_06b():
    process = lambda string, n: subprocess.run(['python3', 'ex06/filterstring.py', string, n], capture_output=True, text=True)
    assert process('Hello the World', '4').stdout == "['Hello', 'World']\n"
    assert process('Hello the World', '99').stdout == "[]\n"
    assert "AssertionError: the arguments are bad\n" in process('3', 'Hello the World').stderr
    assert "AssertionError: the arguments are bad\n" in process('', '').stderr
    assert process('Salut\tComment\nCa\vVa\fToi\rMoi Ca\tClaque\n', '5').stdout == "['Comment', 'Claque']\n"
    assert process('Salut\tComment\nCa\vVa\fToi\rMoi Ca\tClaque\n', '0').stdout == "['Salut', 'Comment', 'Ca', 'Va', 'Toi', 'Moi', 'Ca', 'Claque']\n"

def test_07():
    process = lambda string: subprocess.run(['python3', 'ex07/sos.py', string], capture_output=True, text=True)
    assert process('sos').stdout ==  "... --- ... \n"
    assert process('hello how are you').stdout ==  ".... . .-.. .-.. --- / .... --- .-- / .- .-. . / -.-- --- ..- \n"
    assert "AssertionError: the arguments are bad\n" in process('').stderr
    assert "AssertionError: the arguments are bad\n" in process('h$llo').stderr

if __name__ == "__main__":
    test_ex00()
    test_ex01()
    test_ex02()
    test_ex03()
    test_ex04()
    test_ex05()
    test_ex06a()
    test_ex06b()
    test_ex07()

