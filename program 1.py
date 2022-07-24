d = {}
records = open("records.txt" , "w")

for i in range(3):
    print("------------------------------------------------")
    roll = input("Enter the Roll Number : ")
    d[roll] = {}
    name = input("Enter the Name : ")
    
    Maths =  int(input("Enter the Maths Marks : "))
    Physics = int(input("Enter the Physics Marks : "))
    Chemistry = int(input("Enter the Chemistry Marks : "))
    print("------------------------------------------------")
    
    d[roll]["Name"] = name
    d[roll]["Maths"] = Maths
    d[roll]["Physics"] = Physics
    d[roll]["Chemistry"] = Chemistry
    
    
    
for i in d:
    records.write("------------------------------------------------\n")
    records.write("Roll Number : " + str(i) + "\n")
    records.write("Name : "+ d[i]["Name"] + "\n")
    records.write("Maths : " + str(d[i]["Maths"]) + "\n")
    records.write("Physics : " + str(d[i]["Physics"]) + "\n")
    records.write("Chemistry : " + str(d[i]["Chemistry"]) + "\n")
    
    total = d[i]["Maths"] + d[i]["Physics"] + d[i]["Chemistry"]
    records.write("Total : " + str(total) + "\n")
    
    average = d[i]["Maths"] + d[i]["Physics"] + d[i]["Chemistry"] / 300
    records.write("Average : " + str(average) + "\n")
    
    percentage  = (d[i]["Maths"] + d[i]["Physics"] + d[i]["Chemistry"])/300*100
    records.write("Percentage : " + str(percentage) + "\n")
    
    records.write("------------------------------------------------\n")


records.close()

records = open("records.txt" , "r")

print(records.read())

records.close()