import getpass
import mysql.connector

def menu():
    print("\nSelect an option:")
    print("1. FR1: Rooms and Rates")
    print("2. FR2: Reservations")
    print("3. FR3: Reservation Cancellation")
    print("4. FR4: Detailed Reservation Information")
    print("5. FR5: Revenue")
    print("6. QUIT")

def FR1(cursor):
    print("FR1: Rooms and Rates\n")
    query = """
        SELECT * FROM lab7_rooms
    """

    cursor.execute(query)
    results = cursor.fetchall()
    print(results)

def FR2(cursor):
    print("FR2: Reservations\n")

def FR3(cursor):
    print("FR3: Reservation Cancellation\n")

def FR4(cursor):
    print("FR4: Detailed Reservation Information\n")

def FR5(cursor):
    print("FR5: Revenue\n")




if __name__ == "__main__":
    db_password = getpass.getpass()
    conn = mysql.connector.connect(user='calpoly_user', password=db_password,
                            host='mysql.labthreesixfive.com',
                            database='calpoly_user')

    while True:
        menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            try:
                cursor = conn.cursor()
                FR1(cursor)
            finally:
                cursor.close()
        elif choice == "2":
            try:
                cursor = conn.cursor()
                FR2(cursor)
            finally:
                cursor.close()
        elif choice == "3":
            try:
                cursor = conn.cursor()
                FR3(cursor)
            finally:
                cursor.close()
        elif choice == "4":
            try:
                cursor = conn.cursor()
                FR4(cursor)
            finally:
                cursor.close()
        elif choice == "5":
            try:
                cursor = conn.cursor()
                FR5(cursor)
            finally:
                cursor.close()
        elif choice == "6":
            print("Exiting the program.")
            conn.close()
            break
        else:
            print("Invalid choice. Please try again.")