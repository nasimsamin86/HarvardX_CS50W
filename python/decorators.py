def announce(f):
    def wrapper():
        print("About the run the function...")
        f()
        print("Done with the function...")
    return wrapper

# Adding the Decorator to the above function, with the @ sign.
# the "Hello" function being wrapped inside the "Announce" function, as the "f" function.
@announce
def hello():
    print("Hello, world!")

hello() 