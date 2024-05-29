# lib/cli.py

from helpers import (
    exit_program,
    helper_1,
    list_patients,
    find_patient_by_name,
    find_patient_by_id,
    create_patient,
    update_patient,
    delete_patient,
    list_doctors,
    find_doctor_by_name,
    find_doctor_by_id,
    create_doctor,
    update_doctor,
    delete_doctor,
    list_patient_doctors
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
