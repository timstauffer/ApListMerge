import os
os.chdir('c:\\AP_Mapping')

with open("IT_List.csv","r") as s, open("MedNet_List.csv", 'r') as t, open("Output.csv", 'w') as o:

    # Read in IT list and MedNet export file
    lines = s.readlines()
    records = t.readlines()

    # Write heading record for output file
    newline = "AccessPointId" + "," + "Description"
    o.write(newline + "\n")
   
    for i in range(0, len(lines)):  # Loop through IT list
        line = lines[i]
        key = line[:16]            # First 11 characters of MAC

        if len(line) < 60:
            desc = line[18:-1]            # Description to be used in output file.
        else:                             # 40 char max. Strip off CR/LF.
            desc = line[18:58]
        
        for j in range(0, len(records)):        # Loop through MedNet export
            record = records[j]
            lock = record[:16]
            locker = record[:17]
        
            if key.lower() == lock.lower():     # both to lower case and compare first 11 char
                newline = locker + "," + desc   # Generate record using MAC from MedNet export and description from IT list
                o.write(newline + "\n")              # Write a record to the new import file
