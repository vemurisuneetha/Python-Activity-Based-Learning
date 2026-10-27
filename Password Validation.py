pwd=input("Enter password: ")
has_upper=any(c.isupper() for c in pwd)
has_lower=any(c.islower() for c in pwd)
has_digits=any(c.isdigit() for c in pwd)
has_special=any(c in '@$!%*?&' for c in pwd)
valid=len(pwd)>=8 and has_upper and has_lower and has_digits and has_special
print(f"Valid : {valid}")
