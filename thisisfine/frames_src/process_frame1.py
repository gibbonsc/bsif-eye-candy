frame_list = []  # initialize empty collections of bytearray encoded frames
path='./'

for file in ['thisisfine']:
    with open(path+file+'.xbm') as fh:
        fh.readline()
        fh.readline()
        fh.readline()
        bl=[]  # initialize empty byte list
        while True:
            line = fh.readline().strip().strip(",").strip("};")
            if not line:
                break
            octets = line.split(", ")
            for octet in octets:
                bl.append(int(octet,0))  # put bitmap pattern into byte list
        # convert byte list into bytearray encoded frame object
        frame_list.append(bytearray(bl))
print("def init_frames():")
print("    return "+str(frame_list))
