''' Problem 1 '''
# Define the main function
def main():
    technician_guide()  # Call the technician_guide function

# Define the technician_guide function
def technician_guide():
    # Get the initial temperature with input validation
    while True:
        try:
            temperature = float(input("Enter the current temperature(Celsius): "))
            break  # Exit loop if input is valid
        except ValueError:
            print("Please enter a valid numerical temperature.")

    # Repeat checking until temperature is at or below 102.5
    while temperature > 102.5:
        print(f"\nThe temperature is {temperature:.1f} degrees celsius.")
        print("You must turn down the vat’s thermostat.")
        print("Wait 5 minutes and check again.\n")

        # Get the updated temperature with input validation
        while True:
            try:
                temperature = float(input("Enter the current temperature(Celsius): "))
                break  # Exit loop if input is valid
            except ValueError:
                print("Please enter a valid numerical temperature.")

    # Announce that the temperature is stable
    print(f"\nThe temperature is {temperature:.1f} degrees celsius.")
    print("You don't need to do anything.")

# Execute the main function
main()
