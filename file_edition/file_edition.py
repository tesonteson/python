import csv
import os
import pathlib
import glob
import shutil

with open("test.csv", "w") as csv_file:
    fieldnames = ["Name", "Count"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Name": "teson", "Count": "22"})

with open("test.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row["Name"], row["Count"])



print(os.path.exists("test.txt"))
print(os.path.isfile("test.txt"))
print(os.path.isdir("sample_package"))

# os.rename("test.txt", "text.txt")
# os.mk
# os.symlink("test.txt", "text.txt")


# pathlib.Path("empty.txt").touch()

print(glob.glob("sample_package/*"))



import zipfile

with zipfile.ZipFile("test.zip", "w") as z:
    #z.write("text.txt")
    for f in glob.glob("zzz/**", recursive=True):
        print(f)
        z.write(f)


# unzip test.zip -d <ジップファイル名>





import datetime
import time

now = datetime.datetime.now()

print(now)
d = datetime.timedelta(days=365)
time.sleep(5)
print(now - d)

print(time.time())


file_name = "test.txt"

if os.path.exists(file_name):
    shutil.copy(file_name, f"{now.strftime('%Y_%m')}")
