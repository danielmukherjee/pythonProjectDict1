
dictionary = {"off" : "on",
"night" : "day",
"entrance" : "exit",
"exterior" : "interior",
"true" : "false",
"dead" : "alive",
"push" : "pull",
"pass" : "fail",
"above" : "below,",
"servant" : "master",
"borrow" : "lend",
"give" : "receive",
"buy" : "sell",
"instructor" : "pupil"
}


a= input("Enter the Word - ")
for i in dictionary:
    if i == a:
        print(dictionary[a])
        break
else :
    print ("Sorry, No match found")