import shelve

# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

with shelve.open('recipes', writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["beans_on_toast"] = beans_on_toast
    # recipes["scrambled_eggs"] = scrambled_eggs
    # recipes["pasta"] = pasta
    # recipes["soup"] = soup

    # recipes["blt"].append("butter")               <--- DOES NOT WORK
    # recipes["pasta"].append("tomato")

    # temp_list = recipes["blt"]            # FIRST METHOD FOR UPDATING
    # temp_list.append("butter")
    # recipes["blt"] = temp_list
    #
    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list            # SECOND METHOD
    # recipes["soup"].append("croutons")      # works with writeback=True, HEAVIER MEMORY USAGE using this method!

    recipes["soup"] = soup                    # soup stored on cache
    recipes.sync()                            # causes cache to be cleared
    soup.append("cream")

    for snack in recipes:
        print(snack, recipes[snack])