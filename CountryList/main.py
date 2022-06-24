# Country List
# Ask the user a list of country separate by commas and print the list alphabetically sorted

user_input = input('Write a country list separate by commas: ')
country_list = [country for country in user_input.split(",")]
sort_list = sorted(set(country_list))
print(sort_list)
print(",".join(sorted(list(set(country_list)))))

