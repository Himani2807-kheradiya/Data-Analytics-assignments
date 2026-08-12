insta_filters = ('Clarendon', 'Juno', 'Lark', 'Valencia')

try:
    insta_filters[1] = 'Vintage'
except TypeError as e:
    print("Error:", e)

# This error occurs because tuples are immutable.
# We cannot change an element of a tuple after it is created.