def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide a valid input"
  first = f_name.title()  
  last = l_name.title()
  return f"{first} {last}"


print(
  format_name(
    input("what is your 1st name? "),
    input("what is your last name? ")
  )
)