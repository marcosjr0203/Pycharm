import random

states_of_brazil = ["Amapá", "Rio Grande do Norte", "Rondônia", "Roraima", "Amazonas", "Ceará", "Acre", "Piauí",
                    "Bahia", "Sergipe", "Alagoas", "Maranhão", "Mato Grosso", "Mato Grosso do Sul", "São Paulo",
                    "Rio de Janeiro", "Espírito Santo", "Minas Gerais", "Pará", "Paraná", "Paraíba", "Tocantins",
                    "Rio Grande do Sul", "Santa Catarina", "Pernambuco", "Brasília", "Goiás"]
other_names = ["Tuiuiú", "Capivara", "Onça Pintada"]
# append = add an item to the end of the list. e.g.: listname.append(value)
states_of_brazil.append("Guanabara")
print(states_of_brazil)
# extend = Extend the list by appending all the items from an iterable. e.g.: listname.extend(anotherlist)
states_of_brazil.extend(other_names)
print(states_of_brazil)
# insert = insert an item at a given position. e.g.: listname.insert(index, value)
states_of_brazil.insert(5, "Tatu Bolinha")
print(states_of_brazil)
# remove = remove the first item equal to the informed value. e.g.: listname.remove(value)
states_of_brazil.remove("Capivara")
print(states_of_brazil)
# pop = remove the item at the given position. e.g.: listname.pop(index)
states_of_brazil.pop(29)
print(states_of_brazil)
# index = return index in the list of the 1st item whose value is equal to the informed. e.g.: listname.index(value)
print(states_of_brazil.index("Pernambuco"))
# count = return the number of times the value appears in the list. e.g.: listname.count(value)
print(states_of_brazil.count("Acre"))
# sort = sort the items of the list in place (arguments can be customizated). e.g.:listname.sort()
states_of_brazil.sort()
print(states_of_brazil)
# sorted = sort the items of the list alphabetically. e.g.: listname.sorted()
sorted(states_of_brazil)
# reverse = reverse the elements of the list in place. e.g.: listname.reverse()
states_of_brazil.reverse()
print(states_of_brazil)
# copy = returns a shallow copy of the list. e.g.: listname.copy()
newlist = states_of_brazil.copy()
print(newlist)

