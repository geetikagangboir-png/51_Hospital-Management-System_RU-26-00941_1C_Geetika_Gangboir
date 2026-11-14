patients = {}
next_patient_number = 101


def generate_patient_id():
    global next_patient_number

    patient_id = "P" + str(next_patient_number)
    next_patient_number += 1

    return patient_id


def add_patient():
    print("\n--- Add Patient ---")


    name = input("Name: ").strip()

    if name == "":
        print("Invalid name. Name cannot be empty.")
        print("Patient not added.")
        return


    age_input = input("Age: ").strip()

    try:
        age = int(age_input)
    except ValueError:
        print("Invalid age. Enter a number between 0 and 120.")
        print("Patient not added.")
        return

    if age < 0 or age > 120:
        print("Invalid age. Enter a number between 0 and 120.")
        print("Patient not added.")
        return

    disease = input("Disease: ").strip()
    doctor = input("Doctor: ").strip()

    patient_id = generate_patient_id()

    patients[patient_id] = {
        "Name": name,
        "Age": age,
        "Disease": disease,
        "Doctor": doctor
    }

    print(
        f"Patient added. ID: {patient_id} | "
        f"{name} | {age} | {disease} | {doctor}"
    )


def view_all_patients():
    print("\n--- All Patients ---")

    if len(patients) == 0:
        print("No patient records found.")
        return

    for patient_id, patient in patients.items():
        print(
            f"ID: {patient_id} | "
            f"Name: {patient['Name']} | "
            f"Age: {patient['Age']} | "
            f"Disease: {patient['Disease']} | "
            f"Doctor: {patient['Doctor']}"
        )


def search_patient():
    print("\n--- Search Patient ---")

    patient_id = input("Enter Patient ID: ").strip().upper()

    if patient_id in patients:
        patient = patients[patient_id]

        print(
            f"ID: {patient_id} | "
            f"Name: {patient['Name']} | "
            f"Age: {patient['Age']} | "
            f"Disease: {patient['Disease']} | "
            f"Doctor: {patient['Doctor']}"
        )
    else:
        print("No patient records found.")


def update_patient():
    print("\n--- Update Patient ---")

    patient_id = input("Enter Patient ID: ").strip().upper()

    if patient_id not in patients:
        print("No patient records found.")
        return

    patient = patients[patient_id]

    print("Enter new details:")


    name = input("Name: ").strip()

    if name == "":
        print("Invalid name. Name cannot be empty.")
        print("Patient not updated.")
        return


    age_input = input("Age: ").strip()

    try:
        age = int(age_input)
    except ValueError:
        print("Invalid age. Enter a number between 0 and 120.")
        print("Patient not updated.")
        return

    if age < 0 or age > 120:
        print("Invalid age. Enter a number between 0 and 120.")
        print("Patient not updated.")
        return

    disease = input("Disease: ").strip()
    doctor = input("Doctor: ").strip()

    patient["Name"] = name
    patient["Age"] = age
    patient["Disease"] = disease
    patient["Doctor"] = doctor

    print(f"Patient {patient_id} updated.")


def delete_patient():
    print("\n--- Delete Patient ---")

    patient_id = input("Enter Patient ID: ").strip().upper()

    if patient_id in patients:
        del patients[patient_id]
        print(f"Patient {patient_id} deleted.")
        print(f"Total patients: {len(patients)}")
    else:
        print("No patient records found.")


def display_menu():
    print("\n=================================")
    print("     HOSPITAL MANAGEMENT SYSTEM")
    print("=================================")
    print("1. Add Patient")
    print("2. View All Patients")
    print("3. Search Patient")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Exit")
    print("=================================")


def main():
    while True:
        display_menu()

        choice = input("Enter menu option: ").strip()

        if choice == "1":
            add_patient()

        elif choice == "2":
            view_all_patients()

        elif choice == "3":
            search_patient()

        elif choice == "4":
            update_patient()

        elif choice == "5":
            delete_patient()

        elif choice == "6":
            print("Thank you for using Hospital Management System.")
            break

        else:
            print("Invalid menu option. Please try again.")
if __name__ == "__main__":
    main()