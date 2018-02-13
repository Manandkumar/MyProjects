firstname=str(input("Please enter your First Name"))
middlename=str(input("Please enter your Middle Name"))
lastname=str(input("Please enter your Last Name"))

firstname=firstname.capitalize()
middlename=middlename.capitalize()
lastname=lastname.capitalize()

name_format="{first}{middle:.1s}{last}"
print(name_format.format(first=firstname, middle=middlename, last =lastname))