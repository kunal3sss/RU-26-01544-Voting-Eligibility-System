# Project No. 13: Voting Eligibility System
# Language: Python 3

def check_eligibility(name, age, citizen):
    """
    Checks whether a person is eligible to vote.
    Returns True if eligible, otherwise False.
    """
    if age >= 18 and citizen == "y":
        print(f"{name} is eligible to vote.")
        return True

    elif age < 18:
        print(f"{name} is not eligible to vote.")
        print("Reason: Below 18 years of age.")
        print(f"Years left to become eligible: {18 - age}")
        return False

    elif citizen == "n":
        print(f"{name} is not eligible to vote.")
        print("Reason: Not an Indian citizen.")
        return False

    return False


def get_valid_age():
    """Accepts an age until a valid whole number from 0 to 120 is entered."""
    while True:
        try:
            age = int(input("Age: "))

            if 0 <= age <= 120:
                return age
            else:
                print("Invalid age. Age must be between 0 and 120.")

        except ValueError:
            print("Invalid input. Enter a whole number.")


def get_valid_citizenship():
    """Accepts only y or n as the citizenship response."""
    while True:
        citizen = input("Indian citizen (y/n): ").strip().lower()

        if citizen == "y" or citizen == "n":
            return citizen
        else:
            print("Invalid input. Please enter y or n.")


def main():
    voters_checked = 0
    eligible_voters = 0
    not_eligible_voters = 0

    print("=" * 45)
    print("       VOTING ELIGIBILITY SYSTEM")
    print("=" * 45)

    while True:
        name = input("\nEnter person's name: ").strip()

        while name == "":
            print("Name cannot be empty.")
            name = input("Enter person's name: ").strip()

        age = get_valid_age()
        citizen = get_valid_citizenship()

        voters_checked += 1

        if check_eligibility(name, age, citizen):
            eligible_voters += 1
        else:
            not_eligible_voters += 1

        print("\n" + "-" * 45)

        another = input("Check another voter? (y/n): ").strip().lower()

        while another not in ("y", "n"):
            print("Invalid choice. Please enter y or n.")
            another = input("Check another voter? (y/n): ").strip().lower()

        if another == "n":
            break

    # Display final statistics
    print("\n" + "=" * 45)
    print("             FINAL SUMMARY")
    print("=" * 45)
    print(f"Voters checked: {voters_checked}")
    print(f"Eligible: {eligible_voters}")
    print(f"Not eligible: {not_eligible_voters}")
    print("=" * 45)


if __name__ == "__main__":
    main()
