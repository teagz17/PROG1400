import simple_calculator

#using functions from the module
x = int(input('enter the number: '))
y = int(input('enter the number: '))

print(f'addition: {simple_calculator.add(x,y)}')
print ('subtraction: ', simple_calculator.subtract(x,y))
print ('multiplication: ', simple_calculator.multiply(x,y))
print ('division: ', simple_calculator.divide(x,y))

calc = simple_calculator.AdvancedCalculator()
print('exponentiation: ', calc.exponentiate(x,y))