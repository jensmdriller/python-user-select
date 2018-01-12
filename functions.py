def single_select_from_dict(choice_dict):
    list_keys=list(choice_dict.keys())
    for i,each in enumerate(list_keys):
        print("Selection [%i]: %s %s" %(i+1,each,choice_dict[each]))
    user_sel_str = input("\nPlease select one an option from the list above or press 'q' to quit\n--> ")
    if user_sel_str.lower().replace(" ","") == 'q':
        print("Exiting...\n")
        return None
    user_sel = int(user_sel_str)-1
    if user_sel not in range(len(list_keys)):
        print("\nYou have entered an invalid option, please try again or press 'q' to quit\n")
        multi_select_dict(choice_dict)
    return {list_keys[user_sel]:choice_dict[list_keys[user_sel]]}

def multi_select_from_dict(choice_dict):
    import re
    list_keys=list(choice_dict.keys())
    for i,each in enumerate(list_keys):
        print("Selection [%i]: %s %s" %(i+1,each,choice_dict[each]))
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
            multi_select_dict(choice_dict);break
    else:
        return {list_keys[int(each_sel)-1]:choice_dict[list_keys[int(each_sel)-1]] for each_sel in selection_array}