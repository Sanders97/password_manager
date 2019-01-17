
import string
from random import *
min_char = 8
max_char = 12
allchar = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
print "This is your password : ",password
# upload code to db
# check to make sure password hasnt been used in 6 months
	def __new__(dbUpload):
	if password == dbPassword:
		print "already uploaded"
	else: print "new password added"
	upload password tp db 
	

