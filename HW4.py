temperature = input("The  temperature you like to convert? : ")
degree = int(temperature[:-1])
i_convention = temperature[-1]

if i_convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  o_convention = "Celsius"
else:
  print("proper convention.")
print("The temperature in", o_convention, "is", result, "degrees.")