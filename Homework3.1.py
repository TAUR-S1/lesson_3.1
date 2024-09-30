calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    count_calls()
    leight = len(string)
    UP = string.upper()
    lo = string.lower()
    t = [leight, UP, lo]
    Tuple = tuple(t)
    return Tuple

def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        slovo = string.upper()
        sl_txt = i.upper()
        if slovo == sl_txt:
            c = True
        else:
            c = False
    return c



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)