stdata={
        'id':1,
        'name':'Sanket',
        'sub':'Python'
        }
"""print(stdata)
print(stdata['name'])
print(stdata.get("sub"))
print(stdata.keys())
print(stdata.values())"""

"""if 'name' in stdata:
    print("Yes...")
else:
    print("No..")"""
    
"""if 'Sanket' in stdata.values():
    print("Yes...")
else:
    print("No..")"""
    
#print(len(stdata))

# ---------------------------- #
print(stdata)

"""for i in stdata:
    print(i)"""
    
"""for i in stdata.values():
    print(i)"""
    
"""for i in stdata.items():
    print(i)"""

"""for i,j in stdata.items():
    #print(i,j)
    print(f"Key={i} and Value={j}")"""


#stdata["id"]=2 #change value
#stdata["city"]='Rajkot'
#stdata.pop('name')
#stdata.clear()
#del stdata['sub']
print(stdata)