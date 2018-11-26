def golos():
    print("Hello Hello")
    return 123

zdoroviy_chelovek = {"name":"Anton", "age":18, "ves":'45',"dengi":[10000], "golos": golos}
print(zdoroviy_chelovek)

ves = zdoroviy_chelovek["ves"]
print(ves)

age = zdoroviy_chelovek.get("age")
print(age)

email = zdoroviy_chelovek.get("email", "email@email.com")
print(email)

print(zdoroviy_chelovek['golos']())

import json
dump
dumps
load
loads


import json
# dump -> to file
# dumps -> to string
# load -> from file
# loads -> from string

ds = json.dumps(d) # convert dict to string
print(type(ds))

# try:

#     f = open("example.txt", "w") # this is THE FILE
#     json.dump(d, f) # Save data from dictionary "d" into file "f" AS TEXT STRING
# except Exception as ex:
#     print("got an exception: {}".format(ex)) # if some shit happens
# finally:
#     f.close() # CLOSE it anyway

# try:
#     f = open("example.txt", "r")
#     content = f.read()
# except Exception as ex:
#     print("got an exception: {}".format(ex))
# finally:
#     f.close()

ds = json.dumps(d) # convert dict "d" to string "ds"
print(type(ds))
ssd = json.loads(ds)
print(type(ssd)) # convert stringify dictionary "ds" to real dictionary "ssd"

with open("example.txt", 'w') as fp:
    json.dump(d, fp) # write (dump) dictionary "d" into file example.txt, opened for "write" with file descriptor as "fp"

with open("example.txt", "r") as fp:
    content = json.load(fp) # load (read) dictionary "content" from file example.txt, opened for "read" with file descriptor as "fp"

if content:
    print("from file:")
    print(content)



