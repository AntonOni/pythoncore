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
# dump -> трансформирует словарь в строку и загружает ее в файл
# dumps -> трансформирует словарь в строку (для передачи по сети например)
# load -> берет строку из файла и трансформирует в словарь
# loads -> трансформирует строку в словарь

# ds = json.dumps(d) # convert dict to string
# print(type(ds))

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




import json

s = {}

with open("result.txt", "r") as fp:
    # load s as DICT from string file
    s = json.load(fp)
    print(type(s))
    print(s)

with open("result_2.txt", "w") as fp:
    # write DICT s as STRING into file via fp
    json.dump(s, fp)

ds = json.dumps(s) # s is a dict -> to string
print("type ds: {}".format(type(ds))) # ds is a string

dss = json.loads(ds) # ds us a string -> dict
print("type dss: {}".format(type(dss))) # dss is a dict


