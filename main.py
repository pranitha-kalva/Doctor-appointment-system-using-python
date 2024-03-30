import os

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def book_appointment():
    clear_screen()

    print("\n ----- Book Your Appointment ---- \n")
    print("\n ----- Available slots ---- \n")

    try:
        with open("appointment.dat", "r") as read:
            appointments = read.readlines()
    except FileNotFoundError:
        appointments = []

    arr = ["0"] * 13
    record_found = 0

    if appointments:
        for line in appointments:
            temp = line[0]
            index = ord(temp) - 65
            arr[index] = line[2:].strip()
            record_found = 1

        print("\n Appointment Summary by hours:")
        key = 'A'
        hours = 9
        for i in range(13):
            if i == 0:
                if arr[i] == "0":
                    print(f"\n {key}-> 0{hours} - Available")
                else:
                    print(f"\n {key}-> 0{hours} - Booked by {arr[i]}")
            else:
                if arr[i] == "0":
                    print(f"\n {key}->{hours} - Available")
                else:
                    print(f"\n {key}->{hours} - Booked by {arr[i]}")
            hours += 1
            key = chr(ord(key) + 1)

    if record_found == 0:
        print("\n Appointment Available for following hours :")
        key = 'A'
        for i in range(9, 22):
            if i == 9:
                print(f"\n {key} -> 0{i} - Available")
            else:
                print(f"\n {key} -> {i} - Available")
            key = chr(ord(key) + 1)

    choice = input("\n\n Input your choice : ").upper()

    if not ('A' <= choice <= 'Z'):
        print("\n Error : Invalid Selection")
        print("\n Please select a correct value from menu A-Z")
        input("\n Press any key to continue")
        clear_screen()
        book_appointment()

    index = ord(choice) - 65
    is_booked = 1 if arr[index] != "0" else 0

    if is_booked == 1:
        print("\n Error : Appointment is already booked for this Hour")
        print("\n Please select a different time !!")
        input("\n Press any key to continue!!")
        clear_screen()
        book_appointment()

    name = input("\n Enter your first name:")
    with open("appointment.dat", "a") as out:
        out.write(f"{choice}:{name}\n")
        print(f"\n Appointment booked for Hours : {(ord(choice) - 65) + 9} successfully !!")

    input("\n Please any key to continue..")


def existing_appointment():
    clear_screen()
    print("\n ----- Appointments Summary ---- \n")
    try:
        with open("appointment.dat", "r") as read:
            appointments = read.readlines()
    except FileNotFoundError:
        appointments = []

    arr = ["0"] * 13
    record_found = 0

    if appointments:
        for line in appointments:
            temp = line[0]
            index = ord(temp) - 65
            arr[index] = line[2:].strip()
            record_found = 1

        print("\n Appointment Summary by hours:")
        key = 'A'
        hours = 9
        for i in range(13):
            if arr[i] == "0":
                print(f"\n {key}->{hours} - Available")
            else:
                print(f"\n {key}-> 0{hours} - Booked by {arr[i]}")
            hours += 1
            key = chr(ord(key) + 1)
    else:
        print("\n Appointment Available for following hours :")
        key = 'A'
        for i in range(9, 22):
            if i == 9:
                print(f"\n {key} -> 0{i} - Available")
            else:
                print(f"\n {key} -> {i} - Available")
            key = chr(ord(key) + 1)

    input("\n Please any key to continue..")


def main():
    while True:
        clear_screen()
        print("\tDoctor Appointment System\n")
        print("----------------------------------------\n\n")
        print("1. Book Appointment")
        print("2. Check Existing Appointment")
        print("0. Exit\n")
        choice = input("\n Enter your choice: ")

        if choice == '1':
            book_appointment()
        elif choice == '2':
            existing_appointment()
        elif choice == '0':
            while True:
                clear_screen()
                ex = input("\n Are you sure you want to exit? (y/n): ")
                if ex.lower() == 'y':
                    exit(0)
                elif ex.lower() == 'n':
                    break
                else:
                    print("\n Invalid choice !!!")
                    input("\n Press any key to continue")


if __name__ == "__main__":
    main()
