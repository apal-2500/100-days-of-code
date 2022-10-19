# request input and print with "..." in between each word
request = input("Say something please: ")

#replace spaces with "..."
dots = "...".join(request.split())

print(dots)
