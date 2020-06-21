strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set

print(1,2,3,4,sep='*')
# Output: 1*2*3*4
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('\n--- Positional Order ---')
print(positional_order)

# order using keyword argument
keyword_order = "Id name salary \n {s}  {b} {j}".format(j='360',b='Bill',s='1')
print('\n--- Keyword Order ---')
print(keyword_order,end='\t')


def print_inventory(dct):
    print("\nItems held:")
    for item, amount in dct.items():  # dct.iteritems() in Python 2
        print("{} ({})".format(item, amount))

inventory = {
    "shovels": 3,
    "sticks": 2,
    "dogs": 1,
}

print_inventory(inventory)