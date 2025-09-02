import os
#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open(r"C:\Users\beatriz.souza\Downloads\Mail+Merge+Project+Start\Mail Merge Project Start\Input\Letters\starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
with open(r"C:\Users\beatriz.souza\Downloads\Mail+Merge+Project+Start\Mail Merge Project Start\Input\Names\invited_names.txt") as names_file:
    names = names_file.readlines() 

for name in names:
    nomes_convidados = name.strip()
    personalized_letter = letter_contents.replace("[name]", nomes_convidados)
    with open(f"C:\\Users\\beatriz.souza\\Downloads\\Mail+Merge+Project+Start\\Mail Merge Project Start\\Output\\ReadyToSend\\letter_to_{nomes_convidados}.txt", "w") as output_file:
        output_file.write(personalized_letter) 
    
