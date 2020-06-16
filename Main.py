# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# Laura Truong, 6.12.2020 Edited attributes in the DataClasses file to collect employee_ID in Employee(person)class
# Laura Truong 6.13.2020, Modified print_current_list_items from the IOClasses file for the rows to display. The format Professor Root used got changed becausse it did not work.
#Laura Truong, 6.13.2020, Modified the rows in the ProcessingClasses file in the read_data_from_file method to read the employee data formatted by rows.
#Laura Truong, 6.14.2020, Copied over data from TestHarness. Added Data Code to the main body in a while loop.
# ------------------------------------------------------------------------ #
# TODO: Import Modules(Done)
if __name__ == "__main__":
    from DataClasses import Employee as Emp # Imports Employee and names it Emp
    from ProcessingClasses import FileProcessor as Fp # Imports FileProcessor and names it Fp
    from IOClasses import EmployeeIO as Eio # Imports EmployeeIO and names it Eio
else:
    raise Exception("This file was not created to be imported")

# Test data module
lstOfEmployeeObjects = [] # A list of object rows
strFileName = "EmployeeData.txt" # The target file for reading/writing
strMenuChoice = "" # Captures user input for menu choice
objFile = None  # Object for opening/closing target file
objEmployee = None  # Object collecting user input data, 3 attributes

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body (Done)
# Load data from file into a list of employee objects when script starts
lstOfEmployeeObjects = Fp.read_data_from_file(strFileName)
print(lstOfEmployeeObjects) #Prints statement to user

# Show user a menu of options
while True: # While loop to let user choose their menu option
    Eio.print_menu_items() #Calls print_menu_items

# Get user's menu option choice
    strChoice = Eio.input_menu_options() #Assigns the input of the menu option to strChoice

# Show user current data in the list of employee objects
    if strChoice.strip() == "1":
        Eio.print_current_list_items(lstOfEmployeeObjects) #Prints list of employee objects
        continue # Takes us back to the main menu

# Let user add data to the list of employee objects
    if strChoice.strip() == "2":
        while True: # While loop to let user add names
            try:
                objEmployee = Eio.input_employee_data() #Creates objEmployee
                lstOfEmployeeObjects.append(objEmployee) #Appends
                print(objEmployee.first_name + " " + #Prints statement to user
                      objEmployee.last_name +
                      " has been added." + #Let's user know the name has been added
                      str(objEmployee.employee_id) + "\n",
                      type(objEmployee))
            except Exception as e:
                print("\n", e, "\n")
                print("\t** Error - Cannot Create Employee **\n") #Prints statement to user
            finally:
                break # Exits the loop
        continue # Takes us back to the main menu

# let user save current data to file
    if strChoice.strip() == "3":
        Fp.save_data_to_file(strFileName, lstOfEmployeeObjects)
        continue # Takes us back to the main menu

    # Let user exit program
    if strChoice.strip() == "4":
        print("Exiting Program!") #Prints statement to user
        break #Exits program

    else:
        print("ERROR- Please enter a value 1-4. ") #Prints statement to user
# Main Body of Script  ---------------------------------------------------- #

