phone_book = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}

# Ask the user to enter a phone number
number = input("Enter the phone number: ")


if len(number) != 10:
    print("Invalid number")

elif number in phone_book:
    print("The owner of the number is:", phone_book[number])


else:
    print("Sorry, the number was not found")
