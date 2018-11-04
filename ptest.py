passwordfile = open('password.txt')
secret = passwordfile.read()
tsecret= str(secret)
print("The stored pwd is %s"% tsecret)
print(" Enter your password")
typedpassword = raw_input()
stypedpassword = str(typedpassword)
print("The typed pwd is %s"% stypedpassword)
if stypedpassword == tsecret:
	print(" Access granted")
else:
	print(" Denied")