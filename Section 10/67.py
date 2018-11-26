## Writing Binary Files Manually ##

# with open("binary", 'bw') as bin_file:
#     for i in range(17):
#         # bin_file.write(i)             throws error
#         bin_file.write(bytes([i]))      # Must use this form ([i])

# with open("binary", 'bw') as bin_file:      # better, shorter
#     bin_file.write(bytes(range(17)))
#
# with open("binary", 'br') as binFile:
#     for b in binFile:
#         print(b)

a = 65534       # FF FE
b = 65535       # FF FF
c = 65536       # 00 01 00 00
x = 2998302     # 02 2D C0 1E

with open("binary2", 'bw') as bin_file:         # when writing binary it is usual to use an even number of bytes
    bin_file.write(a.to_bytes(2, 'big'))
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(c.to_bytes(4, 'big'))        #   ^^^^^^^^^^^^^^
    bin_file.write(x.to_bytes(4, 'big'))        # big - most significant byte stored first and the rest follow
    bin_file.write(x.to_bytes(4, 'little'))     # little - least significant byte stored first and the rest follow

with open("binary2", 'br') as bin_file:
    e = int.from_bytes(bin_file.read(2), 'big')
    print(e)
    f = int.from_bytes(bin_file.read(2), 'big')
    print(f)
    g = int.from_bytes(bin_file.read(4), 'big')
    print(g)
    h = int.from_bytes(bin_file.read(4), 'big')
    print(h)
    i = int.from_bytes(bin_file.read(4), 'big') # read backwards because was saved as little
    print(i)