
name = "carl"
location = "nashville"

def greet(name, location):
    print(f"hello {name}")
    print(f"are we in {location}")

greet(name, location)
greet(name="jack", location="philly")
greet(location="austin", name="steve")
greet("greg", "geneva")