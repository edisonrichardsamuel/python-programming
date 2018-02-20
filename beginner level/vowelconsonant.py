vb=['a','e','i','o','u']
bb=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
xb=raw_input()
if(xb in vb):
	print("Vowel")
elif(xb in bb):
	print("Consonants")
else:
	print("InvalidInput")
