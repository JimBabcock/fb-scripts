#!/usr/bin/env python

import facebook


oauth_code = ""
graph = facebook.GraphAPI(oauth_code)
friends = graph.get_connections("me", "friends")

#for friend in friends['data']:
#    print friend['name']

#Get id of acquaintances
friend_lists = graph.get_connections("me","friendlists")
ac_list = None
other_lists = []
for list in friend_lists['data']:
    if list['name'] == "Acquaintances":
        ac_list = list['id']
    else: other_lists.append(list['id'])
#Add all users to Acquaintances list
for friend in friends['data']:
    print "Adding %s to acquaintances" % friend["name"]
    if(graph.put_object(ac_list + "/members",friend["id"]  )):
        print "Success"
    else: print "Failed!"
    
#Remove them from the other lists
for list in other_lists:
    #Get a list of members
    members = graph.get_connections(list, "members")["data"]
    #Remove them from the list
    for member in members:
        print "Deleting %s from list %s" % (member["name"], list)
        print graph.delete_object(list+"/members/" + member["id"])