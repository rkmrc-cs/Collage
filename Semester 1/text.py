
data = [{"V" : "S001"},{"V" : "S002"},{"VI" : "S001"},{"VI" : "S005"},{"VII" : "S005"},{"V" : "S009"},{"VIII" : "S007"}]

dictionary = {}
for d in data:
    for key, value in d.items():
        if key in dictionary:
            dictionary[key].append(value)
        else:
            dictionary[key] = [value]

unique_values = set(value for values in dictionary.values() for value in values)

print(unique_values)
