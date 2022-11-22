#SPLIT
my_str = ' this is a test'
string_elements = my_str.split()
print(string_elements)

#REVERSED
reversed_elements = []
for element in string_elements:
	reversed_elements.append(element[::-1])
print(reversed_elements)

#JOIN THE REVERSED
new_str= ' '.join(reversed_elements)
print(new_str)
