weather = {}

def add_data():
    city = input("City name: ")
    date = input("Date: ")
    temp = input("Temperature: ")
    hum = input("Humidity: ")
    cond = input("Condition: ")

    if city not in weather:
        weather[city] = {}
    weather[city][date] = {
        "temp": temp,
        "hum": hum,
        "cond": cond
    }
    print("Add")

def show_data():
    city = input("Enter city to show data: ")
    if city in weather:
        for date, info in weather[city].items():
            print(f"Date: {date}")
            for key, value in info.items():
                print(f" {key.capitalize()}: {value}")
            print("\n")
    else:
        print("No data for this city")

def main():
    while True:
        print("\n1 Add weather data")
        print("2 Show city weather data")
        print("3 Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_data()
        elif choice == "2":
            show_data()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main()
