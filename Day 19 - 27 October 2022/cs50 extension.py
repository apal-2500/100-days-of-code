#request file input
file = input("Filename = ")

type = file.lower()

#print file type
if ".gif" in type:
    print("image/gif")
elif ".jpg" in type:
    print("image/jpeg")
elif ".jpeg" in type:
    print("image/jpeg")
elif ".png" in type:
    print("image/png")
elif ".pdf" in type:
    print("application/pdf")
elif ".txt" in type:
    print("text/plain")
elif ".zip" in type:
    print("application/zip")
else:
    print("application/octet-stream")
