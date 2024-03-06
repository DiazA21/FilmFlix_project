import readRecord, addRecord, updateRecord, deleteRecord, reports

def read_file(file_path): # Reads a file and returns its content as string
    try:
        with open(file_path) as readFile: # Open the file in read mode
            rf = readFile.read() # Save the content of the file to variable 'rf'
            return rf
    except FileNotFoundError as nf: # If the file is not found, raise an exception
        print(f"File not found because: {nf}")

def films_menu():
    option = 0 # initialise/assign the option variable with an integer value 0
     # create a list of string values/elements/items corresponding to optionsMenu.txt
    optionsList = ["1", "2", "3", "4", "5", "6"]
    # call the read file funcion to assign it to a variable called menuChoices
    menuChoices = read_file("optionsMenu.txt")

    # repeat the menu options until the option to exit the menu is entered
    while option not in optionsList:
         # print the optionsMenu by calling the variable that holds the read_file function in the print statement
        print(menuChoices)

        # re-assign the value of the option variable so it can be re-used
        option = input(f"\nEnter an option from the menu above:  ") # 1 = "1" or 2 = "2"

        # Check if the input value entered in the option variable above is not outside of 1,2,3,4,5,6
        if option not in optionsList:
            print(f"\n{option} Invalid Option!\nPlease enter again.")
    return option

mainProgram = True # Toggle to False to exit the while loop below

while mainProgram: # same as while True
    # call the films_menu() function and assign it to a variable

    mainMenu = films_menu()

    # Match case is the equivalent to switch statement in JS
    match mainMenu: # call the py files imported in line one and the functions inside them
        case "1": 
            addRecord.add_film()
        case "2":
            deleteRecord.del_film()
        case "3":
            updateRecord.update_record()
        case "4":
            readRecord.read_films()
        case "5":
            reports.search_record()
        case _: # anything else that isn't tied in, not in the import
            mainProgram = False # set main program to false to exit the menu
input("Press Enter To Exit The Program...")