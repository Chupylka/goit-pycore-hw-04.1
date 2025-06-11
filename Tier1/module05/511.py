# import colorama

# async
# await



original_dict = {
    "The Lagend of Zalda: Ocarina of Time": 1998,
    "Grand Theft Auto IV": 2008,
    "Red Dead Redemption": 2018,
    "Perfect Dark": 2000,
    "The Orange Box": 2007,
}

gemes_after_2000 = {game: year 
                    for game, year in original_dict.items() 
                    if year > 2000}
print(gemes_after_2000) 