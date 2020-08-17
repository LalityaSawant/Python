with open('binary','bw') as bin_file:
    bin_file.write(bytes(range(20)))

with open('binary','br') as binFile:
    for b in binFile:
        print(b)

a = 65534
b = 65535
c = 65536
x = 2998302

with open('binary2','bw') as bin_file_2:
    bin_file_2.write(a.to_bytes(2,'big'))
    bin_file_2.write(b.to_bytes(2,'big'))
    bin_file_2.write(c.to_bytes(4,'big'))
    bin_file_2.write(x.to_bytes(4,'big'))
    bin_file_2.write(x.to_bytes(4,'little'))

with open('binary2','br') as bin_file_2:
    e = int.from_bytes(bin_file_2.read(2),'big')
    f = int.from_bytes(bin_file_2.read(2),'big')
    g = int.from_bytes(bin_file_2.read(4),'big')
    h = int.from_bytes(bin_file_2.read(4),'big')
    i = int.from_bytes(bin_file_2.read(4),'big')  # number changes if wrong indent is provided
    j = int.from_bytes(bin_file_2.read(4),'big')
    k = int.from_bytes(bin_file_2.read(4),'big')

    print(e)
    print(f)
    print(g)
    print(h)
    print(i)
    print(j)
    print(k)

