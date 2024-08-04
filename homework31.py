calls = 0

def count_calls():
    global calls
    calls +=1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    is_con = False
    for i in range(0,len(list_to_search)):
        if string.upper() == list_to_search[i].upper():
            is_con = True
            break
    return is_con

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)