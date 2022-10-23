#receives input
def main():
    message = input("Smile or sad? ")
    emoji = convert(message)
    print(emoji)

#convert happy face and sad face text into emoticon
def convert(message):
    words = message.split(" ")
    emojis = {
        ":)" : "🙂",
        ":(" : "🙁"
    }
    outcome = " "
    for word in words:
        outcome += emojis.get(word,word) + " "
    return outcome

main()
