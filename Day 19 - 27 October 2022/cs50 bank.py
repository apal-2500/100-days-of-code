#request greeting input
greet = input("greeting ... ")

lower_greet = greet.lower().strip()

#Hello is $0.00
if 'hello' in lower_greet:
    print("$0")

#if contains 'h' $20
elif 'h' == lower_greet[0]:
    print("$20")

#everything else $100
else:
    print("$100")
