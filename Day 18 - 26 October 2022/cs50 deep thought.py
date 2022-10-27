#request input
answer = input("The Great Question of Life, The Universe and Everything is ...  ")
#respond if answer is a version of 42
if answer.strip() == "42":
    print("Yes")
elif answer.lower().strip() ==  "forty-two":
    print("Yes")
elif answer.lower().strip() == "forty two":
    print ("Yes")
else:
    print ("No")
