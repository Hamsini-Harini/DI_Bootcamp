# user's word : "ttiiitllleeee" ➞ "title"

#             SET - {"ppoeemm"} -> "oemp", "oepm"... sets are not ordered
#             LIST - [] -> loop through chars in word and check if character is inside
#                           the list - if it is DONT add it to the list
#                           otherwise add it to the list
#                           -> ["p","o","e","m"] ... wont work since the characters can
#                           repeat themselves like it title (2 t's)


#               "ttiii" 
#                  i      
#                i = 0
#               ["t", "i"] 
#               current_char = word[i] # "t"
#               while i < len("ttiii"):
#
#                   if string[i] != current_char:
#                      ["t",].append("i")
#                      current_char = string[i] # "i"
#                   i += 1
#              
#               


#class notes - solving challenge 1
string = "dodo"

#get the word (string)
#look each letter of a string
# create dictionary   
# insert the letter as key of dictionary 
# insert the letter index as value of dictionary
# check if letter is in dictionary