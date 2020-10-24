
with open("Customer/AP.csv", 'r') as s, open("Customer/AccessPointList.csv", 'r') as t, open("Customer/Output.csv", 'w') as o:

    # Read in IT list and MedNet export file
    lines = s.readlines()
    records = t.readlines()

    # Write heading record for output file
    heading = "AccessPointId" + "," + "Description"
    o.write(heading)
    o.write("\n")

    for i in range(0, len(lines)):  # Loop through IT list
        line = lines[i]
        key = line[0:16]  # First 11 characters of MAC
        desc = line[18:]  # Description to be used in output file

        for j in range(0, len(records)):        # Loop through MedNet export
            record = records[j]
            lock = record[0:16]
            locker = record[0:17]
            if key == lock:                     # If first 11 characters of IT list match first 11 of export record, it's the same AP

                # Generate record using MAC from MedNet export and description from IT list
                newline = locker + "," + desc
                # Write a record to the new import file
                o.write(newline)
