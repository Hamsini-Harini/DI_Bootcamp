# Challenge 1
# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.
# Examples

# "dodo" ➞ { "d": [0, 2], "o": [1, 3] }

# "froggy" ➞ { "f":  [0], "r": [1], "o": [2], "g": [3, 4], "y": [5] }

# "grapes" ➞ { "g": [0], "r": [1], "a": [2], "p": [3]}


user_word = input("Enter a word: ")
def create_index_dictionary(word):
    index_dict = {}
    for index, letter in enumerate(word):  # Using enumerate to get both the index and the letter
        # If the letter is already a key in the dictionary, add the index to its list
        if letter in index_dict:
            index_dict[letter].append(index)
        # If the letter is not a key in the dictionary, create a new list with the index
        else:
            index_dict[letter] = [index]
    return index_dict

# Create the dictionary using the function
result = create_index_dictionary(user_word)
print(result)



# Challenge 2
# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.
# Hint : make sure to convert the amount from dollars to numbers. Create a program that deletes the $ sign, and the comma (for thousands)

# Examples

# The key is the product, the value is the price

# items_purchase = {
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }

# wallet = "$300"

# ➞ ["Bread", "Fertilizer", "Water"]

# items_purchase = {
#   "Apple": "$4",
#   "Honey": "$3",
#   "Fan": "$14",
#   "Bananas": "$4",
#   "Pan": "$100",
#   "Spoon": "$2"
# }

# wallet = "$100" 

# ➞ ["Apple", "Bananas", "Fan", "Honey", "Spoon"]

# # In fact the prices of Apple + Honey + Fan + Bananas + Pan is more that $100, so you cannot by the Pan, 
# # instead you can by the Spoon that is $2

# items_purchase = {
#   "Phone": "$999",
#   "Speakers": "$300",
#   "Laptop": "$5,000",
#   "PC": "$1200"
# }

# wallet = "$1" 

# ➞ "Nothing"



items_purchase_1 = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}
wallet_1 = "$300"
def affordable_items(items_purchase, wallet): #we need 2 parameters for the function, what is buyable and your budget
    wallet_amount = int(wallet.replace('$', '').replace(',', '')) # remove string elements and once it's clean of non numbers, convert to integer
    affordable = [] # list of things we can afford to buy
    
    for item, price in items_purchase.items(): #loop over keys and values
        price_amount = int(price.replace('$', '').replace(',', '')) #same thing we did for wallet
        
        # Check if the item can be afforded
        if price_amount <= wallet_amount:
            affordable.append(item) #add it to the list of affordables
    
    affordable.sort()
    
    # Return the sorted list or "Nothing" if no items can be afforded
    return affordable if affordable else "Nothing"

print(affordable_items(items_purchase_1, wallet_1))  # ➞ ["Bread", "Fertilizer", "Water"]