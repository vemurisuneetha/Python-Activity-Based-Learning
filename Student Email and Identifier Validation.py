email=input("Email: ")
valid="@" in email and "." in email and email.index("@")<email.rindex(".")
print(f"Email {email} valid: {valid}")