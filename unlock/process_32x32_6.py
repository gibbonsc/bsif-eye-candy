frame_list = []  # initialize empty collection of bytearray encoded frames
path='./'

for file in ['unlock40','unlock41','unlock42','unlock43','unlock44','unlock45']:
    with open(path+file+'.xbm') as fh:
        fh.readline()
        fh.readline()
        fh.readline()
        bk=[]  # initialize empty byte list
        while True:
            line = fh.readline().strip().strip(",").strip("};")
            if not line:
                break
            octets = line.split(",")
            for octet in octets:
                bk.append(int(octet,0))
        frame_list.append(bytearray(bk))
print("def init_frames():")
print("    return "+str(frame_list))
