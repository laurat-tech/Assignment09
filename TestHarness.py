# ---------------------------------------------------------- #
# Title: TestHarness (Listing 08)
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ---------------------------------------------------------- #
if __name__ == "__main__":
    import DataClasses as D  # data classes
    import ProcessingClasses as P  # processing classes
    import IOClasses as IO # IO classes
else:
    raise Exception("This file was not created to be imported")

# Test data module
objP1 = D.Person("Bob", "Smith")
objP2 = D.Person("Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test processing module
P.FileProcessor.save_data_to_file("PersonData.txt", lstTable)
lstFileData = P.FileProcessor.read_data_from_file("PersonData.txt")
for row in lstFileData:
    p = D.Person(row[0], row[1])
    print(p.to_string().strip(), type(p))
# Test IO classes
# TODO: create and test IO module
IO.EmployeeIO.print_menu_items()
IO.EmployeeIO.print_current_list_items(lstTable)
print(IO.EmployeeIO.input_employee_data())
print(IO.EmployeeIO.input_menu_options())
