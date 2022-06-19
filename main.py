import pandas as pd

# read the main sheet csv file
pokemon = pd.read_excel('greatLeague.xlsx') #, index_col="Pokemon"
# read the types sheet of the csv file
Types = pd.read_excel('greatLeague.xlsx', sheet_name='Types') #, index_col="Types"
