def sort_file(contents):
    arr = contents.split("/n")
    arr = sorted(arr)
    return ','.join(arr)
contents = "2,3,d\n1,4,d\n8,2,z\n2,4,x\n2,4,a"
print(sort_file(contents))