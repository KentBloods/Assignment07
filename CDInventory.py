#------------------------------------------#
# Title: Assignment07_Starter.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# KBloodsworth, 2022-Mar-06, Completed TODO's
# KBloodsworth, 2022-Mar-13, Modified to include error handling
# KBloodsworth, 2022-Mar-13, Modified to use binary data
#------------------------------------------#

#Module need to pickle and unpickle data
import pickle

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.dat'  # data storage file
objFile = None  # file object


# -- PROCESSING -- #
class DataProcessor:
    # TODone add functions for processing here
    @staticmethod 
    def add_item(strID, strTitle, strArtist):
        """Function to add item to table
    
        Args:
            strID(string): CD ID, input from user to add to table
            strTitle(string): CD title, input from user to add to table
            strArtist(string): artist name, input from user to add to table
            
        Returns:
            None. 
        """
        #Tell user the value must be an integer
        try:
            intID = int(strID)
            dicRow = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}
            print('ID must be an integer')
            lstTbl.append(dicRow)
            IO.show_inventory(lstTbl)
        except ValueError:
            print('\nMust be an integer!\n')
    @staticmethod 
    def del_CD(ntIDDel):
        """Function to delete CD entry from 2D list of dictionary table
        
        Allows the user to choose to delete a CD entry from the table
        
        Args:
            None
            
        Returns:
            None
            
        """
        intRowNr = -1
        blnCDRemoved = False
        for row in lstTbl:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del lstTbl[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
          


class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        #Lets the user know that the file is missing
        try:
            table.clear()  # this clears existing data and allows to load data from file
            objFile = open(strFileName, 'rb')
            data = pickle.load(objFile)
            for row in data:
                table.append(row)
            objFile.close()
        except FileNotFoundError:
            print('\nFile not found!\n')
        except EOFError:
            print('\nFile is empty!\n')
            
    @staticmethod
    def write_file(file_name, table):
        """Function to write the table to file. 
        
        Writes the 2D data structure table consisting of list of dicts to file 
        
        Args:
            file_name (string): name of file used to write the 2D data structure to, from table: list of dicts
            written to file
            
        Returns:
            None
        """
        # TODone Add code here
        #Lets the user know that the file is missing
        try:
            objFile = open(strFileName, 'wb')
            pickle.dump(lstTbl, objFile)
            objFile.close()
        except FileNotFoundError:
            print('\nFile not found!\n')
        


# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    # TODone add I/O functions as needed
    @staticmethod 
    def add_input():
        """Function asks user to input new ID, Title, and Artist
                
        Args:
            None.
            
        Returns:
            strID(string): CD ID, input from user
            strTitle(string): CD title, input from user 
            strArtist(string): artist name, input from user
        
        """
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        return strID, strTitle, strArtist
   
     

# 1. When program starts, read in the currently saved Inventory
FileProcessor.read_file(strFileName, lstTbl)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileProcessor.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        # TODone move IO code into function
        strID, strTitle, strArtist = IO.add_input()

        # 3.3.2 Add item to the table
        # TODone move processing code into function
        DataProcessor.add_item(strID, strTitle, strArtist)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        try:
            IO.show_inventory(lstTbl)
            # 3.5.1.2 ask user which ID to remove
            intIDDel = int(input('Which ID would you like to delete? ').strip())
            # 3.5.2 search thru table and delete CD
            # TODone move processing code into function
            DataProcessor.del_CD(intIDDel)
            IO.show_inventory(lstTbl)
            continue  # start loop back at top.
        except ValueError:
            print('\nMust be an integer!\n')
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            # TODone move processing code into function
            FileProcessor.write_file(strFileName, lstTbl)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')





