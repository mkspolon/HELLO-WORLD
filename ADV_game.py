def answer_input(statement,input_q,a,b,output_string_a,output_string_b):

    print(statement)
    print()
    
    answer = input(input_q).lower()
    if answer == a:
        print(output_string_a)
        
    elif answer == b:
        print(output_string_b)
        
    else:
        print('invalid, you die!')
        answer_input()

answer_input('Hello',"Are you ready to start? [yes/no]",'yes','no','Lets play!','Goodbye')

def choosingadoor_input(statement,input_q,a,b,output_string_a,output_string_b):
    print(statement)
    print()
    
    answer = input(input_q).lower()
    if answer == a:
        print(output_string_a)
        
    elif answer == b:
        print(output_string_b)
        
    else:
        print('invalid, you die!')

choosingadoor_input('Choose a door', 'door on the left or on the righ? l/r: ','l','r','you got into the castel, the door behind you closed, there are some zumbi monsters sleeping in front of you \n would you silently open the door in your right or\n pass trough the zumbies monsters and open the door in front? [f/r] ', 'it is locked, Game over')

def choosingadoor1_input(statement,input_q,a,b,output_string_a,output_string_b):
        print(statement)
        print()
        answer = input(input_q).lower()
        if answer == a:
           print(output_string_a)
            
        elif answer == b:
           print(output_string_b)
            
        else:
           print('invalid, you die!')

choosingadoor1_input('Choose a door', 'door in front or on the righ? f/r: ','f','r','you got into the kichen, luckly there is a man to save you. ', 'it is locked, trigered the alarm, Game over')

#def choosing_a_door(statement,input_q,a,b,output_string_a,output_string_b):
#        print(statement)
 #       print()
  #      answer = input(input_q).lower()
   #     if answer == a:
    #        print(output_string_a)
     #       choosing_a_door()
      #  elif answer == b:
       #     print(output_string_b)
        #    answer_input()
        #else:
            #print('invalid, you die!')

#choosing_a_door('Choose a door', 'door on the left or on the righ? [l/r]: ','l','r','you got into the castel', 'it is locked, Game over')