def ssfl_body_function(choice_list):
    for i,each in enumerate(choice_list):
        print("Option [%i]: %s" %(i+1,each))
    user_sel_str = input("\nPlease select one an option from the list above or press 'q' to quit\n--> ")
    try:
        user_sel = int(user_sel_str)-1
        if user_sel not in range(len(choice_list)):
            raise Exception('Value out of range') 
    except:
        print("\nYou have entered an invalid option, please try again or press 'q' to quit\n")
        if user_sel_str.lower().replace(" ","") == 'q':
            print("Exiting...\n")
            return None
        else:
            user_sel = ssfl_body_function(choice_list)
    return user_sel

def single_select_from_list(choice_list):
    user_sel = ssfl_body_function(choice_list)
    return choice_list[user_sel] if user_sel != None else None

def multi_select_from_list(choice_list):
    import re
    for i,each in enumerate(choice_list):
        print("Option [%i]: %s" %(i+1,each))
    user_sel_str = input("\nPlease select one an option from the list above or press 'q' to quit\n--> ")
    if user_sel_str.lower().replace(" ","") == 'q':
        print("Exiting...\n")
        return None
    remove_whitspaces = user_sel_str.replace(" ","")
    seperate_by_comma = remove_whitspaces.split(',')
    selection_array = [re.sub("\D", "", each) for each in seperate_by_comma]
    try:
        selection_array.remove('') #remove empty entries
    except:
        pass
    for each_selection in selection_array:
        user_sel = int(each_selection)-1
        if user_sel not in range(len(choice_list)):
            print("\nEntry [%s] is an invalid option, please try again or press 'q' to quit\n" %(int(user_sel)+1))
            multi_select_from_list(choice_dict);break
    else:
        return [choice_list[int(each_sel)-1] for each_sel in selection_array]

def single_select_from_dict(choice_dict):
    list_keys=list(choice_dict.keys())
    for i,each in enumerate(list_keys):
        print("Option [%i]: Key:[%s] Value:[%s]" %(i+1,each,choice_dict[each]))
    user_sel_str = input("\nPlease select one an option from the list above or press 'q' to quit\n--> ")
    if user_sel_str.lower().replace(" ","") == 'q':
        print("Exiting...\n")
        return None
    user_sel = int(user_sel_str)-1
    if user_sel not in range(len(list_keys)):
        print("\nYou have entered an invalid option, please try again or press 'q' to quit\n")
        single_select_from_dict(choice_dict)
    return {list_keys[user_sel]:choice_dict[list_keys[user_sel]]}

def multi_select_from_dict(choice_dict):
    import re
    list_keys=list(choice_dict.keys())
    for i,each in enumerate(list_keys):
        print("Option [%i]: %s %s" %(i+1,each,choice_dict[each]))
    user_sel_str = input("\nPlease select one an option from the list above or press 'q' to quit\n--> ")
    if user_sel_str.lower().replace(" ","") == 'q':
        print("Exiting...\n")
        return None
    remove_whitspaces = user_sel_str.replace(" ","")
    seperate_by_comma = remove_whitspaces.split(',')
    selection_array = [re.sub("\D", "", each) for each in seperate_by_comma]
    try:
        selection_array.remove('') #remove empty entries
    except:
        pass
    for each_selection in selection_array:
        user_sel = int(each_selection)-1
        if user_sel not in range(len(list_keys)):
            print("\nEntry [%s] is an invalid option, please try again or press 'q' to quit\n" %(int(user_sel)+1))
            multi_select_from_dict(choice_dict);break
    else:
        return {list_keys[int(each_sel)-1]:choice_dict[list_keys[int(each_sel)-1]] for each_sel in selection_array}