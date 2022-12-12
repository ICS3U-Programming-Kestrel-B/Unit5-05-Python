#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Dec. 7, 2022
# This program asks for the user's
# residency information and
# then formats it into a valid
# canadian mailing address


def main():
    # introductory paragraph
    print("This program asks for the user's")
    print("residency information and")
    print("then formats it into a valid")
    print("canadian mailing address")
    print("")

    # user input
    # initializing user_f_name
    user_f_name = input("Enter your first name: ")
    # initializing user_l_name
    user_l_name = input("Enter your last name: ")
    # initializing user_apartment
    user_apartment = input("Enter your apartment number (n/a if no apartment): ")
    # initializing user_street_name
    user_street_name = input("Enter your street name (e.x: sesame st): ")
    # initializing user_street_number
    user_street_number = input("Enter your street number: ")
    # initializing user_city
    user_city = input("Enter your city: ")
    # initializing user_province
    user_province = input("Enter your province (e.x: AB, ON): ")
    # initializing user_postal
    user_postal = input("Enter your postal code (e.x: K1S 5P4): ")

    # making calculate function
    def format_address(
        user_f_name,
        user_l_name,
        user_apartment,
        user_street_number,
        user_street_name,
        user_city,
        user_province,
        user_postal,
    ):
        # making user_full_name
        user_full_name = user_f_name.upper() + " " + user_l_name.upper()
        if user_apartment != "n/a":
            user_address = (
                user_full_name
                + "\n"
                + user_apartment
                + "-"
                + user_street_number
                + " "
                + user_street_name.upper()
                + " "
                + user_city.upper()
                + " "
                + user_province.upper()
                + " "
                + user_postal
            )
        else:
            user_address = (
                user_full_name
                + "\n"
                + user_street_number
                + " "
                + user_street_name.upper()
                + " "
                + user_city.upper()
                + " "
                + user_province.upper()
                + " "
                + user_postal
            )
        # return user_address
        return user_address

    # calling function
    complete_address = format_address(
        user_f_name,
        user_l_name,
        user_apartment,
        user_street_number,
        user_street_name,
        user_city,
        user_province,
        user_postal,
    )

    # printing function
    print(complete_address)


if __name__ == "__main__":
    main()
