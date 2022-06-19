import pandas as pd

#Convert type name to numerical index in Types table of the attacker
def type_to_index(pokemonsType):
    match pokemonsType:
        case 'Bug':
            return 0
        case 'Dark':
            return 1
        case 'Dragon':
            return 2
        case 'Electric':
            return 3
        case 'Fairy':
            return 4
        case 'Fighting':
            return 5
        case 'Fire':
            return 6
        case 'Flying':
            return 7
        case 'Ghost':
            return 8
        case 'Grass':
            return 9
        case 'Ground':
            return 10
        case 'Ice':
            return 11
        case 'Normal':
            return 12
        case 'Poison':
            return 13
        case 'Psychic':
            return 14
        case 'Rock':
            return 15
        case 'Steel':
            return 16
        case 'Water':
            return 17
        case 'None':
            return 18
        case default:
            return "Error Not A MATCH!"

#Convert type name to numerical index in Types table of the defender
def type_to_index_II(pokemonsType):
    return type_to_index(pokemonsType)+1

def get_pokemons_type1(pokemon, i):
    return pokemon.loc[[i], ['Type 1']].values[0][0]

def get_pokemons_type2(pokemon, i):
    return pokemon.loc[[i], ['Type 2']].values[0][0]


# read the main sheet csv file
pokemon = pd.read_excel('greatLeague.xlsx') #, index_col="Pokemon"
# read the types sheet of the csv file
Types = pd.read_excel('greatLeague.xlsx', sheet_name='Types') #, index_col="Types"

print('asd', Types.iloc[    [type_to_index(get_pokemons_type1(pokemon, 1))], [type_to_index_II(get_pokemons_type2(pokemon, 1))] ].values[0])