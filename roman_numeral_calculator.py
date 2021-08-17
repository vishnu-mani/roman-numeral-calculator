import re
def roman_to_decimal(roman) :
	validRomanNumeral = bool(re.search(r"^M*(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$",roman))
	if not validRomanNumeral:
		raise ValueError("Invalid roman numeral : " + roman)

	previous = 0
	decimalValue = 0
	romanNumerals = {
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000
	}
	length = len(roman)
	for i in range(length-1, -1, -1):
		if romanNumerals[roman[i]] >= previous:
			decimalValue += romanNumerals[roman[i]]
		else:
			decimalValue -= romanNumerals[roman[i]]

		previous = romanNumerals[roman[i]]
	return decimalValue

def decimal_to_roman(decimal):
	if decimal < 1:
		return 0

	romanNumerals = {
		1000 : 'M',
		900 : 'CM',
		500 : 'D',
		400 : 'CD',
		100 : 'C',
		90 : 'XC',
		50 : 'L',
		40 : 'XL',
		10 : 'X',
		9 : 'IX',
		5 : 'V',
		4 : 'IV',
		1 : 'I'
	}
	result = ''
	for key, value in sorted(romanNumerals.items(), reverse=True):
		times = int(decimal / key)
		result += romanNumerals[key]*times
		decimal = decimal % key

		if decimal == 0:
			return result

def roman_numeral_calculator(number1, number2, operator):
	try:
		num1 = roman_to_decimal(number1.upper())
		num2 = roman_to_decimal(number2.upper())
		
	except ValueError as err:
		print(err)
		raise ValueError

	if operator == '+':
		result = num1 + num2
	elif operator == '-':
		result = num1 - num2
	elif operator == '*':
		result = num1 * num2
	elif operator == '/':
		result = num1 / num2
	else:
		print("Invalid operator [" + operator + "], Supported operators are + - * /")
		raise TypeError

	return decimal_to_roman(result)
	

if __name__ == '__main__':
	try:
		number1 = input()
		number2 = input()
		operator = input()
		result = roman_numeral_calculator(number1, number2, operator)

		print(result)
	except:
		pass