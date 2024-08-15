gust = ['ALI','AHMED','TAHA','OSMAN','Baber']



# Notify guests that they are not invited and pop them from the list  
while len(gust) > 2:  
    removed_guest = gust.pop()  
    print(f"Sorry {removed_guest}, you can't be invited to dinner.")  

# Notify the remaining guests that they are still invited  
for guest in gust:  
    print(f"{guest}, you are still invited to dinner!")  

# Remove the last two guests from the list using del  
del gust[:]  

# Print the final guest list to confirm it is empty  
print("Final guest list:", gust)