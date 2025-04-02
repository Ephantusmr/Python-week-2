def file_read_write():
    try:
        # Ask the user for the input filename
        input_filename = input("Enter the name of the file to read: ")

        # Open the input file in read mode
        file = open(input_filename, "r")
        content = file.read()

        # Modify the content (for example, converting to uppercase)
        modified_content = content.upper()

        # Ask the user for the output filename
        output_filename = input("Enter the name of the new file to save: ")

        # Open the output file in write mode and save modified content
        new_file = open(output_filename, "w")
        new_file.write(modified_content)

        print(f"Modified content has been saved to {output_filename}!")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")

    except IOError:
        print("Error: Unable to read or write to the file. Please check your file permissions.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        # Ensure files are closed regardless of what happens
        try:
            file.close()
        except NameError:
            pass  # File wasn't opened, ignore

        try:
            new_file.close()
        except NameError:
            pass  # New file wasn't opened, ignore

        # Add a print statement to make the finally block visible
        print("Finally block executed: Resources have been cleaned up!")

# Run the program
file_read_write()
