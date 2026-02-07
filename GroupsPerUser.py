# the groups_per_user function receives a dictionary, which contains group names with the list of users.
# Uses can belong to multiple groups.
# Return a dictionary with the users as keys and a list of their groups as values.

def groups_per_user(group_dict):
    users_group = {}
    
    for group in group_dict:
        for user in group_dict[group]:
            if user not in users_group:
                users_group[user] = []
            users_group[user].append(group)
            
    return users_group
    
# main
user_dict = {"local": ["admin", "userA"],
             "public": ["admin", "userB"],
             "administrator": ["admin"]}

print(groups_per_user(user_dict))