# External Sorting Algorithm

External sorting algorithm written in Python that can be used for sorting of big files that don't fit into RAM.
The algorithm makes use of the concept of k-way Merge sort; where k is the number of splits of the original file.

# Brief Overview

Step 1: The source file is split into sub-files with 1000000 lines each.
Step 2: These sub-files fit in the RAM so these can be sorted individually.
Step 3: Now all these sub-files are merged together to form one individual sorted file.

# Steps to run

Step 1: Must have Python installed.
Step 2: Change the filepath and filename variables to the source of the desired file.
Step 3: Execute the script. A new file with the name FINALSORTED.txt will be made in the source older.
