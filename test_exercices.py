import subprocess
from ex01.format_ft_time import format_time, scientific_notation

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


if __name__ == "__main__":
	test_ex00()
	test_ex01()
