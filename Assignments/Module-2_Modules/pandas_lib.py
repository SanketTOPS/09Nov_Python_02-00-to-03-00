import pandas

stdata={
    "id":[1,2,3,4,5],
    "name":["sanket","nirav","hitesh","ashok","darshan"],
    "city":["rajkot","ahmedabad","surat","baroda","navsari"]
}

pd=pandas.DataFrame(stdata)
print(pd)