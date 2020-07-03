import tkinter as tk

def run():

    def run_ip():
        root.destroy()
        find_by_ip()

    def run_net():
        root.destroy()
        find_by_net()

    def run_net_host():
        root.destroy()
        find_by_nethost()

    def run_sub_met():
        root.destroy()
        find_by_metric()

    root = tk.Tk() 
    root.geometry("200x200") 
    root.resizable(False, False)
    root.title("Calc")

    ip_btn = tk.Button(root, text = 'Find By IP', command = run_ip) 
    net_btn = tk.Button(root, text = 'Find By Net(Subnet)' , command = run_net)
    net_host_btn = tk.Button(root, text = 'Find By Net(Host)' , command = run_net_host)
    sub_met_btn = tk.Button(root, text = 'Find By Metric(Subnet)' , command = run_sub_met)

    ip_btn.pack(expand = True)
    net_host_btn.pack(expand = True)
    net_btn.pack(expand = True)
    sub_met_btn.pack(expand = True)

    root.mainloop()
    return 0

def find_by_net():

    # Setup of the main window
    root = tk.Tk() 
    root.geometry("400x200") 
    root.resizable(False, False)
    root.title("Network ID by Subnet")
    #

    subs = [128, 192, 224, 240, 248, 252, 254, 255] # Constant subnetting calculations
    magic_number = [128, 64, 32, 16, 8, 4, 2, 1]

    # Entry variables
    net_id_var = tk.StringVar()
    sub_req_var = tk.StringVar()
    sec_sub_var = tk.StringVar() 
    next_last_var = tk.StringVar() 
    sub_mask_var = tk.StringVar()
    class_var= tk.StringVar()
    num_bit_var = tk.StringVar()
    #

    def return_clean():
        clear_entries()
        root.destroy()
        run()

    # Function to calculate the Network settings according to the information provided
    def calculate():
        bits_used = 0
        bit_counter = 0
        sub_mask = []
        sub_mask_temp = []
        sec_sub = []
        next_last = []
        temp = 0
        net_id = net_id_var.get().split(".")
        sub_req = sub_req_var.get()
        
        while int(sub_req) > temp:
            bit_counter += 1
            bits_used += 1
            temp = 2**bits_used
            if bit_counter == len(subs):
                bit_counter = 0

        bit_counter -= 1
        if int(net_id[0]) >= 0 and int(net_id[0]) <= 127:
            class_var.set("A")
            sub_mask_var.set("255.255." + str(subs[bit_counter]) + ".0")
            num_bit_var.set(str(bits_used))
        
        elif int(net_id[0]) >= 128 and int(net_id[0]) <= 191:
            class_var.set("B")
            sub_mask_var.set("255.255." + str(subs[bit_counter]) + ".0")
            num_bit_var.set(str(bits_used))

        elif int(net_id[0]) >= 192 and int(net_id[0]) <= 223:
            class_var.set("C")
            sub_mask_var.set("255.255.255." + str(subs[bit_counter]))
            num_bit_var.set(str(bits_used))

        else:
            class_var.set("D or E")

        sub_mask = sub_mask_var.get().split(".")
        for i in range(4):
            if int(sub_mask[i]) == 0 or int(sub_mask[i]) == 255:
                sec_sub.append(net_id[i])
                if int(net_id[i]) == 0 and int(sub_mask[i]) != 0:
                    next_last.append("255")
                else:
                    next_last.append(net_id[i])
            else:
                sec_sub.append(str(int(int(net_id[i]) + (256 - int(sub_mask[i])))))
                next_last.append(str(int(int(sub_mask[i]) - (256 - int(sub_mask[i])))))
        sub_mask_var.set(sub_mask[0] + "." + sub_mask[1] + "." + sub_mask[2] + "." + sub_mask[3])
        sec_sub_var.set(sec_sub[0] + "." + sec_sub[1] + "." + sec_sub[2] + "." + sec_sub[3])
        next_last_var.set(next_last[0] + "." + next_last[1] + "." + next_last[2] + "." + next_last[3])
    #

    # Deletes all the entry in preparation for a new run
    def clear_entries():
        sub_req_var.set("")
        sub_mask_var.set("")
        net_id_var.set("")
        sec_sub_var.set("")
        next_last_var.set("")
        class_var.set("")
        num_bit_var.set("")
    #

    # Network ID
    net_id_label = tk.Label(root, text = 'Network ID:', font = ('calibre', 10, 'bold')) 
    net_id_entry = tk.Entry(root, textvariable = net_id_var, font = ('calibre',10,'normal')) 
    #

    # Requested number of subnet
    sub_req_label = tk.Label(root, text = 'Requested # of Subnets:', font = ('calibre', 10, 'bold')) 
    sub_req_entry = tk.Entry(root, textvariable = sub_req_var, font = ('calibre',10,'normal')) 
    #

    # Subnet Mask
    sub_mask_label = tk.Label(root, text = 'Subnet Mask: ', font = ('calibre',10,'bold')) 
    sub_mask_val = tk.Label(root, textvariable = sub_mask_var, font = ('calibre',10,'bold')) 
    #

    # Second subnet ID
    sec_sub_label = tk.Label(root, text = 'Second Subnet ID:', font = ('calibre', 10, 'bold')) 
    sec_sub_val = tk.Label(root, textvariable = sec_sub_var, font = ('calibre',10,'bold')) 
    #

    # Next to Last Subnet ID
    next_last_label = tk.Label(root, text = 'Next to Last Subnet ID:', font = ('calibre', 10, 'bold')) 
    next_last_val = tk.Label(root, textvariable = next_last_var, font = ('calibre',10,'bold')) 
    #

    # Network Classful
    class_label = tk.Label(root, text = 'Class: ', font = ('calibre',10,'bold')) 
    class_val = tk.Label(root, textvariable = class_var, font = ('calibre',10,'bold')) 
    #

    # Number of bits taken for subnet
    num_bit_label = tk.Label(root, text = 'Number of bits taken: ', font = ('calibre',10,'bold')) 
    num_bit_val = tk.Label(root, textvariable = num_bit_var, font = ('calibre',10,'bold')) 
    #

    # Calculation, Clear, and Quit Buttons
    calc_btn = tk.Button(root, text = 'Calculate', command = calculate) 
    clear_btn = tk.Button(root, text = 'Clear' , command = clear_entries)
    quit_btn = tk.Button(root, text = 'Quit', command = return_clean)
    #

    # Putting everything on screen
    widget_counter = 0

    net_id_label.grid(row = widget_counter, column = 0) 
    net_id_entry.grid(row = widget_counter, column = 1) 
    widget_counter += 1

    sub_req_label.grid(row = widget_counter, column = 0) 
    sub_req_entry.grid(row = widget_counter, column = 1) 
    widget_counter += 1

    sub_mask_label.grid(row = widget_counter, column = 0) 
    sub_mask_val.grid(row = widget_counter, column = 1) 
    widget_counter += 1

    sec_sub_label.grid(row = widget_counter, column = 0) 
    sec_sub_val.grid(row = widget_counter, column = 1) 
    widget_counter += 1

    next_last_label.grid(row = widget_counter, column = 0) 
    next_last_val.grid(row = widget_counter, column = 1) 
    widget_counter += 1

    class_label.grid(row = widget_counter, column = 0)
    class_val.grid(row = widget_counter, column = 1)
    widget_counter += 1

    num_bit_label.grid(row = widget_counter, column = 0)
    num_bit_val.grid(row = widget_counter, column = 1)
    widget_counter += 1

    calc_btn.grid(row = widget_counter, column = 0)
    clear_btn.grid(row = widget_counter, column = 1)
    quit_btn.grid(row = widget_counter, column = 2)
    widget_counter += 1
    #

    # Infinite Loop of the main window
    root.mainloop()

def find_by_ip():
    # Setup of the main window
    root = tk.Tk() 
    root.geometry("400x200") 
    root.resizable(False, False)
    root.title("Network Calculator by IP")
    #

    subs = [128, 192, 224, 240, 248, 252, 254, 255] # Constant subnetting calculations
    magic_number = [128, 64, 32, 16, 8, 4, 2, 1] # Constant for the magic number. Not used in this case. Added for expansion

    # Entry variables to manipulate data in the window / frame
    ip_add_var = tk.StringVar() 
    sub_mask_var = tk.StringVar()
    class_var = tk.StringVar()
    num_bit_var = tk.StringVar()
    net_id_var = tk.StringVar()
    sub_id_var = tk.StringVar()
    #

    def return_clean():
        clear_entries()
        root.destroy()
        run()

    # Function to calculate the Network settings according to the information provided
    def calculate():
        cidr_met = 0 # Cider metric used determine the number of bits used for the subnet
        bit_counter = 0
        temp = []
        ip_add = ip_add_var.get().split(".")
        sub_mask = sub_mask_var.get().split(".")

        for i in range(4):
            temp.append(str(int(int(ip_add[i]) / (256 - int(sub_mask[i]))) * (256 - int(sub_mask[i])))) # Subnet ID calculation
            for j in range(len(subs)):
                bit_counter += 1
                if int(sub_mask[i]) == subs[j]:
                    cidr_met += bit_counter
                    bit_counter = 0

        sub_id_var.set(temp[0] + "." + temp[1] + "." + temp[2] + "." + temp[3])

        # Classful range for Class A
        if int(ip_add[0]) >= 0 and int(ip_add[0]) <= 127:
            class_var.set("A")
            num_bit_var.set(cidr_met - 8)
            net_id_var.set(ip_add[0] + ".0.0.0")

        # Classful range for Class B
        elif int(ip_add[0]) >= 128 and int(ip_add[0]) <= 191:
            class_var.set("B")
            num_bit_var.set(cidr_met - 16)
            net_id_var.set(ip_add[0] + "." + ip_add[1] + ".0.0")

        # Classful range for Class C
        elif int(ip_add[0]) >= 192 and int(ip_add[0]) <= 223:
            class_var.set("C")
            num_bit_var.set(cidr_met - 24)
            net_id_var.set(ip_add[0] + "." + ip_add[1] + "." + ip_add[2] + ".0")
        
        # Classful range for Class D and E. Not used in this program
        else:
            class_var.set("D or E")
    #

    # Deletes all the entry in preparation for a new run
    def clear_entries():
        ip_add_var.set("")
        sub_mask_var.set("")
        net_id_var.set("")
        sub_id_var.set("")
        class_var.set("")
        num_bit_var.set("")
    #

    # IP Address
    ip_add_label = tk.Label(root, text = 'IP Address:', font = ('calibre', 10, 'bold')) 
    ip_add_entry = tk.Entry(root, textvariable = ip_add_var, font = ('calibre',10,'normal')) 
    #

    # Subnet Mask
    sub_mask_label = tk.Label(root, text = 'Subnet Mask: ', font = ('calibre',10,'bold')) 
    sub_mask_entry = tk.Entry(root, textvariable = sub_mask_var, font = ('calibre',10,'normal')) 
    #

    # Network ID
    net_id_label = tk.Label(root, text = 'Network ID:', font = ('calibre', 10, 'bold')) 
    net_id_val = tk.Label(root, textvariable = net_id_var, font = ('calibre',10,'bold')) 
    #

    # Subnet ID
    sub_id_label = tk.Label(root, text = 'Subnet ID:', font = ('calibre', 10, 'bold')) 
    sub_id_val = tk.Label(root, textvariable = sub_id_var, font = ('calibre',10,'bold')) 
    #

    # Network Class
    class_label = tk.Label(root, text = 'Class: ', font = ('calibre',10,'bold')) 
    class_val = tk.Label(root, textvariable = class_var, font = ('calibre',10,'bold')) 
    #

    # Number of bits taken for subnet
    num_bit_label = tk.Label(root, text = 'Number of bits taken: ', font = ('calibre',10,'bold')) 
    num_bit_val = tk.Label(root, textvariable = num_bit_var, font = ('calibre',10,'bold')) 
    #

    # Calculation and Clear Buttons
    calc_btn = tk.Button(root, text = 'Calculate', command = calculate) 
    clear_btn = tk.Button(root, text = 'Clear' , command = clear_entries)
    quit_btn = tk.Button(root, text = 'Quit', command = return_clean)
    #

    # Putting everything on screen
    widget_counter = 0 # Easier to use this when expanding or copying the code for another window

    ip_add_label.grid(row = widget_counter, column = 0) 
    ip_add_entry.grid(row = widget_counter, column = 1) 
    widget_counter += 1

    sub_mask_label.grid(row = widget_counter, column = 0) 
    sub_mask_entry.grid(row = widget_counter, column = 1) 
    widget_counter += 1

    net_id_label.grid(row = widget_counter, column = 0) 
    net_id_val.grid(row = widget_counter, column = 1) 
    widget_counter += 1

    sub_id_label.grid(row = widget_counter, column = 0) 
    sub_id_val.grid(row = widget_counter, column = 1) 
    widget_counter += 1

    class_label.grid(row = widget_counter, column = 0)
    class_val.grid(row = widget_counter, column = 1)
    widget_counter += 1

    num_bit_label.grid(row = widget_counter, column = 0)
    num_bit_val.grid(row = widget_counter, column = 1)
    widget_counter += 1

    calc_btn.grid(row = widget_counter, column = 0)
    clear_btn.grid(row = widget_counter, column = 1)
    quit_btn.grid(row = widget_counter, column = 3)
    widget_counter += 1
    #

    # Infinite Loop of the main window
    root.mainloop()

def find_by_nethost():

    # Setup of the main window
    root = tk.Tk() 
    root.geometry("400x200") 
    root.resizable(False, False)
    root.title("Network ID by Host")
    #

    subs = [128, 192, 224, 240, 248, 252, 254, 255] # Constant subnetting calculations
    magic_number = [1, 2, 4, 8, 16, 32, 64, 128]

    # Entry variables
    net_id_var = tk.StringVar()
    host_req_var = tk.StringVar()
    first_host_var = tk.StringVar() 
    last_host_var = tk.StringVar() 
    sub_mask_var = tk.StringVar()
    class_var= tk.StringVar()
    num_bit_var = tk.StringVar()
    #

    def return_clean():
        clear_entries()
        root.destroy()
        run()

    # Function to calculate the Network settings according to the information provided
    def calculate():
        bits_used = 0
        bit_counter = 8
        sub_mask = []
        sub_mask_temp = []
        first_host = []
        sec_sub = []
        last_host = []
        temp = 0
        net_id = net_id_var.get().split(".")
        host_req = host_req_var.get()
        
        while int(host_req) >= temp:
            bit_counter -= 1
            bits_used += 1
            temp = 2**bits_used
            if bit_counter == len(subs):
                bit_counter = 8

        bit_counter -= 1
        if int(net_id[0]) >= 0 and int(net_id[0]) <= 127:
            class_var.set("A")
            sub_mask_var.set("255.255." + str(subs[bit_counter]) + ".0")
            num_bit_var.set(str(bits_used))
        
        elif int(net_id[0]) >= 128 and int(net_id[0]) <= 191:
            class_var.set("B")
            if bits_used < 8:
                sub_mask_var.set("255.255.255." + str(subs[bit_counter]))
            else:
                sub_mask_var.set("255.255." + str(subs[bit_counter]) + ".0")
            num_bit_var.set(str(bits_used))

        elif int(net_id[0]) >= 192 and int(net_id[0]) <= 223:
            class_var.set("C")
            sub_mask_var.set("255.255.255." + str(subs[bit_counter]))
            num_bit_var.set(str(bits_used))

        else:
            class_var.set("D or E")

        sub_mask = sub_mask_var.get().split(".")
        for i in range(4):

            if int(sub_mask[i]) == 0 or int(sub_mask[i]) == 255:
                first_host.append(str(int(int(net_id[i]) / (256 - int(sub_mask[i]))) * (256 - int(sub_mask[i]))))
                sec_sub.append(str(int(int(net_id[i]) / (256 - int(sub_mask[i]))) * (256 - int(sub_mask[i]))))
            else:
                first_host.append(str((256 - int(sub_mask[i]))))
                sec_sub.append(str((256 - int(sub_mask[i])) * 2))

        for i in range(4):
            last_host.append(sec_sub[i])

        if int(last_host[3]) == 0:
            last_host[2] = str(int(last_host[2]) - 1)
            last_host[3] = "254"
        else:
            last_host[3] = str(int(last_host[3]) - 2)

        sub_mask_var.set(sub_mask[0] + "." + sub_mask[1] + "." + sub_mask[2] + "." + sub_mask[3])
        first_host_var.set(first_host[0] + "." + first_host[1] + "." + first_host[2] + "." + str(int(first_host[3]) + 1))
        last_host_var.set(last_host[0] + "." + last_host[1] + "." + last_host[2] + "." + last_host[3])
    #

    # Deletes all the entry in preparation for a new run
    def clear_entries():
        host_req_var.set("")
        sub_mask_var.set("")
        net_id_var.set("")
        first_host_var.set("")
        last_host_var.set("")
        class_var.set("")
        num_bit_var.set("")
    #

    # Network ID
    net_id_label = tk.Label(root, text = 'Network ID:', font = ('calibre', 10, 'bold')) 
    net_id_entry = tk.Entry(root, textvariable = net_id_var, font = ('calibre',10,'normal')) 
    #

    # Requested number of subnet
    host_req_label = tk.Label(root, text = 'Requested # of Host:', font = ('calibre', 10, 'bold')) 
    host_req_entry = tk.Entry(root, textvariable = host_req_var, font = ('calibre',10,'normal')) 
    #

    # Subnet Mask
    sub_mask_label = tk.Label(root, text = 'Subnet Mask: ', font = ('calibre',10,'bold')) 
    sub_mask_val = tk.Label(root, textvariable = sub_mask_var, font = ('calibre',10,'bold')) 
    #

    # Second subnet ID
    first_host_label = tk.Label(root, text = 'First Host IP:', font = ('calibre', 10, 'bold')) 
    first_host_val = tk.Label(root, textvariable = first_host_var, font = ('calibre',10,'bold')) 
    #

    # Next to Last Subnet ID
    last_host_label = tk.Label(root, text = 'Last Host IP:', font = ('calibre', 10, 'bold')) 
    last_host_val = tk.Label(root, textvariable = last_host_var, font = ('calibre',10,'bold')) 
    #

    # Network Classful
    class_label = tk.Label(root, text = 'Class: ', font = ('calibre',10,'bold')) 
    class_val = tk.Label(root, textvariable = class_var, font = ('calibre',10,'bold')) 
    #

    # Number of bits taken for subnet
    num_bit_label = tk.Label(root, text = 'Number of bits taken: ', font = ('calibre',10,'bold')) 
    num_bit_val = tk.Label(root, textvariable = num_bit_var, font = ('calibre',10,'bold')) 
    #

    # Calculation, Clear, and Quit Buttons
    calc_btn = tk.Button(root, text = 'Calculate', command = calculate) 
    clear_btn = tk.Button(root, text = 'Clear' , command = clear_entries)
    quit_btn = tk.Button(root, text = 'Quit', command = return_clean)
    #

    # Putting everything on screen
    widget_counter = 0

    net_id_label.grid(row = widget_counter, column = 0) 
    net_id_entry.grid(row = widget_counter, column = 1) 
    widget_counter += 1

    host_req_label.grid(row = widget_counter, column = 0) 
    host_req_entry.grid(row = widget_counter, column = 1) 
    widget_counter += 1

    sub_mask_label.grid(row = widget_counter, column = 0) 
    sub_mask_val.grid(row = widget_counter, column = 1) 
    widget_counter += 1

    first_host_label.grid(row = widget_counter, column = 0) 
    first_host_val.grid(row = widget_counter, column = 1) 
    widget_counter += 1

    last_host_label.grid(row = widget_counter, column = 0) 
    last_host_val.grid(row = widget_counter, column = 1) 
    widget_counter += 1

    class_label.grid(row = widget_counter, column = 0)
    class_val.grid(row = widget_counter, column = 1)
    widget_counter += 1

    num_bit_label.grid(row = widget_counter, column = 0)
    num_bit_val.grid(row = widget_counter, column = 1)
    widget_counter += 1

    calc_btn.grid(row = widget_counter, column = 0)
    clear_btn.grid(row = widget_counter, column = 1)
    quit_btn.grid(row = widget_counter, column = 2)
    widget_counter += 1
    #

    # Infinite Loop of the main window
    root.mainloop()

def find_by_metric():

    # Setup of the main window
    root = tk.Tk() 
    root.geometry("400x200") 
    root.resizable(False, False)
    root.title("Network Calculator by Metric")
    #

    subs = [128, 192, 224, 240, 248, 252, 254, 255] # Constant subnetting calculations
    magic_number = [128, 64, 32, 16, 8, 4, 2, 1] # Constant for the magic number.

    # Entry variables to manipulate data in the window / frame
    last_ip_var = tk.StringVar() 
    broad_add_var = tk.StringVar()
    sub_mask_var = tk.StringVar()
    class_var = tk.StringVar()
    first_ip_var = tk.StringVar()
    cidr_met_var = tk.StringVar()
    sub_id_var = tk.StringVar()
    #

    def return_clean():
        clear_entries()
        root.destroy()
        run()

    # Function to calculate the Network settings according to the information provided
    def calculate():
        magic_num = 0
        cidr_met = int(cidr_met_var.get())
        bit_counter = 0
        sub_id = sub_id_var.get().split(".")

        # Classful range for Class A
        if int(sub_id[0]) >= 0 and int(sub_id[0]) <= 127:
            class_var.set("A")
            first_ip_var.set(sub_id[0] + "." +  sub_id[1] + "." + sub_id[2] + "." + str(int(sub_id[3]) + 1))
            magic_num = cidr_met - 8
            if magic_num >= 8 and magic_num <= 16:
                magic_num -= 8
            elif magic_num >= 17 and magic_num <= 24:
                magic_num -= 16

            if int(sub_id[3]) == 0 and int(sub_id[2]) == 0:
                broad_add_var.set(sub_id[0] + "." + str(int(sub_id[1]) + magic_number[magic_num - 1] - 1) + ".255.255")
                broad_add = broad_add_var.get().split(".")
                last_ip_var.set(broad_add[0] + "." +  broad_add[1] + "." + broad_add[2] + "." + str(int(broad_add[3]) - 1))
            elif int(sub_id[3]) == 0:
                if cidr_met >= 25:
                    broad_add_var.set(sub_id[0] + "." +  sub_id[1] + "." + sub_id[2] + "." + str(int(sub_id[3]) + magic_number[magic_num - 1] - 1))
                    broad_add = broad_add_var.get().split(".")
                    last_ip_var.set(broad_add[0] + "." +  broad_add[1] + "." + broad_add[2] + "." + str(int(broad_add[3]) - 1))
                else:
                    broad_add_var.set(sub_id[0] + "." +  sub_id[1] + "." + str(int(sub_id[2]) + magic_number[magic_num - 1] - 1) + ".255")
                    broad_add = broad_add_var.get().split(".")
                    last_ip_var.set(broad_add[0] + "." +  broad_add[1] + "." + broad_add[2] + "." + str(int(broad_add[3]) - 1))
            else:
                broad_add_var.set(sub_id[0] + "." +  sub_id[1] + "." + sub_id[2] + "." + str(int(sub_id[3]) + magic_number[magic_num - 1] - 1))
                broad_add = broad_add_var.get().split(".")
                last_ip_var.set(broad_add[0] + "." +  broad_add[1] + "." + broad_add[2] + "." + str(int(broad_add[3]) - 1))

        # Classful range for Class B
        elif int(sub_id[0]) >= 128 and int(sub_id[0]) <= 191:
            class_var.set("B")
            first_ip_var.set(sub_id[0] + "." +  sub_id[1] + "." + sub_id[2] + "." + str(int(sub_id[3]) + 1))
            magic_num = cidr_met - 16
            if magic_num >= 8 and magic_num <= 16:
                magic_num -= 8
            elif magic_num > 17 and magic_num < 24:
                magic_num -= 16
            if int(sub_id[3]) == 0:
                broad_add_var.set(sub_id[0] + "." +  sub_id[1] + "." + str(int(sub_id[2]) + magic_number[magic_num - 1] - 1) + ".255")
                broad_add = broad_add_var.get().split(".")
                last_ip_var.set(broad_add[0] + "." +  broad_add[1] + "." + broad_add[2] + "." + str(int(broad_add[3]) - 1))
            else:
                broad_add_var.set(sub_id[0] + "." +  sub_id[1] + "." + sub_id[2] + "." + str(int(sub_id[3]) + magic_number[magic_num - 1] - 1))
                last_ip_var.set(sub_id[0] + "." +  sub_id[1] + "." + sub_id[2] + "." + str(int(sub_id[3]) + magic_number[magic_num - 1] - 2))

        # Classful range for Class C
        elif int(sub_id[0]) >= 192 and int(sub_id[0]) <= 223:
            class_var.set("C")
            first_ip_var.set(sub_id[0] + "." +  sub_id[1] + "." + sub_id[2] + "." + str(int(sub_id[3]) + 1))
            magic_num = cidr_met - 24
            broad_add_var.set(sub_id[0] + "." +  sub_id[1] + "." + sub_id[2] + "." + str(int(sub_id[3]) + magic_number[magic_num - 1] - 1))
            broad_add = broad_add_var.get().split(".")
            last_ip_var.set(broad_add[0] + "." +  broad_add[1] + "." + broad_add[2] + "." + str(int(broad_add[3]) - 1))
        
        # Classful range for Class D and E. Not used in this program
        else:
            class_var.set("D or E")
    #

    # Deletes all the entry in preparation for a new run
    def clear_entries():
        last_ip_var.set("")
        broad_add_var.set("")
        sub_mask_var.set("")
        sub_id_var.set("")
        class_var.set("")
        first_ip_var.set("")
        cidr_met_var.set("")
    #

    # Subnet ID
    sub_id_label = tk.Label(root, text = 'Subnet ID:', font = ('calibre', 10, 'bold')) 
    sub_id_entry = tk.Entry(root, textvariable = sub_id_var, font = ('calibre',10,'normal')) 
    #

    # CIDR Metrics
    cidr_met_label = tk.Label(root, text = 'CIDR Metric: ', font = ('calibre',10,'bold')) 
    cidr_met_entry = tk.Entry(root, textvariable = cidr_met_var, font = ('calibre',10,'normal')) 
    #

    # First IP
    first_ip_label = tk.Label(root, text = 'First IP Address:', font = ('calibre', 10, 'bold')) 
    first_ip_val = tk.Label(root, textvariable = first_ip_var, font = ('calibre',10,'bold')) 
    #

    # Last IP
    last_ip_label = tk.Label(root, text = 'Last IP Address:', font = ('calibre', 10, 'bold')) 
    last_ip_val = tk.Label(root, textvariable = last_ip_var, font = ('calibre',10,'bold')) 
    #

    # Broadcast Address
    broad_add_label = tk.Label(root, text = 'Broadcast Address: ', font = ('calibre',10,'bold')) 
    broad_add_val = tk.Label(root, textvariable = broad_add_var, font = ('calibre',10,'bold')) 
    #

    # Number of bits taken for subnet
    class_label = tk.Label(root, text = 'Class: ', font = ('calibre',10,'bold')) 
    class_val = tk.Label(root, textvariable = class_var, font = ('calibre',10,'bold')) 
    #

    # Calculation and Clear Buttons
    calc_btn = tk.Button(root, text = 'Calculate', command = calculate) 
    clear_btn = tk.Button(root, text = 'Clear' , command = clear_entries)
    quit_btn = tk.Button(root, text = 'Quit', command = return_clean)
    #

    # Putting everything on screen
    widget_counter = 0 # Easier to use this when expanding or copying the code for another window

    sub_id_label.grid(row = widget_counter, column = 0) 
    sub_id_entry.grid(row = widget_counter, column = 1) 
    widget_counter += 1

    cidr_met_label.grid(row = widget_counter, column = 0) 
    cidr_met_entry.grid(row = widget_counter, column = 1) 
    widget_counter += 1

    first_ip_label.grid(row = widget_counter, column = 0) 
    first_ip_val.grid(row = widget_counter, column = 1) 
    widget_counter += 1

    last_ip_label.grid(row = widget_counter, column = 0) 
    last_ip_val.grid(row = widget_counter, column = 1) 
    widget_counter += 1

    broad_add_label.grid(row = widget_counter, column = 0)
    broad_add_val.grid(row = widget_counter, column = 1)
    widget_counter += 1

    class_label.grid(row = widget_counter, column = 0)
    class_val.grid(row = widget_counter, column = 1)
    widget_counter += 1

    calc_btn.grid(row = widget_counter, column = 0)
    clear_btn.grid(row = widget_counter, column = 1)
    quit_btn.grid(row = widget_counter, column = 2)
    widget_counter += 1
    #

    # Infinite Loop of the main window
    root.mainloop()

if __name__ == "__main__":
    run()
