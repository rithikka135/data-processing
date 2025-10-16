Step-by-Step: Run Data Preprocessing on Ubuntu
🪜 Step 1: Open your Linux terminal

You can use:

Ubuntu terminal, or

VS Code integrated terminal (Ctrl + ~)

🪜 Step 2: Go to your project folder

If your project is in Documents, for example:

cd ~/Documents/DataProcessingProject/Data_Preprocessing


Check your files:

ls


You should see:

dataset.csv  preprocessing.py

🪜 Step 3: Give permission to run the script

Make it executable (Linux requirement):

chmod +x preprocessing.py


This tells Linux the file can be executed directly.

🪜 Step 4: Run the script
Option 1: Direct execution (recommended for Linux)
./preprocessing.py

Option 2: Using Python 3
python3 preprocessing.py

🪜 Step 5: Output you will see

In your terminal, you’ll see something like this 👇

🔹 Reading dataset from: /home/rithikka/Documents/DataProcessingProject/Data_Preprocessing/dataset.csv
✅ Original Data:
             timestamp  value category
0  2025-10-15 08:00:00   10.0        A
1  2025-10-15 09:00:00   15.0        B
2  2025-10-15 10:00:00    NaN        A
3  2025-10-15 11:00:00   20.0        B
4  2025-10-15 11:00:00   20.0        B

✅ Cleaned and Processed Data:
   value  hour_of_day  value_diff
0  -1.16        -1.34     -1.12
1  -0.12        -0.45     -0.32
2   0.43         0.56      0.24
3   0.85         1.23      1.20

💾 Cleaned dataset saved to: /home/rithikka/Documents/DataProcessingProject/Data_Preprocessing/cleaned_dataset.csv

🪜 Step 6: Verify output file

After running successfully, check:

ls


You’ll see:

dataset.csv  preprocessing.py  cleaned_dataset.csv


Open and view the new file:

cat cleaned_dataset.csv


OR open it in VS Code:

code cleaned_dataset.csv
