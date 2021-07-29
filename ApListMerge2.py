import os
os.chdir('c:\\Users\\TS00017847\\desktop\\python')

with open("AP.csv","r") as s, open("AccessPointList.csv", 'r') as t, open("Output.csv", 'w') as o:

    # Read in IT list and MedNet export file
    lines = s.readlines()
    records = t.readlines()

    # Write heading record for output file
    newline = "AccessPointId" + "," + "Description"
    o.write(newline + "\n")
   
    for i in range(0, len(lines)):  # Loop through IT list
        line = lines[i]
        key = line[:16]            # First 11 characters of MAC
        desc = line[18:]            # Description to be used in output file

        for j in range(0, len(records)):        # Loop through MedNet export
            record = records[j]
            lock = record[:16]
            locker = record[:17]
          
            if key.lower() == lock.lower():     # both to lower case and compare first 11 char
                newline = locker + "," + desc   # Generate record using MAC from MedNet export and description from IT list
                o.write(newline)                # Write a record to the new import file
