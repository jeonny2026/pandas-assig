import  pandas as pd
# nigeria_state = ["Lasgos", "Kaduna", "Abuja", "Abia", "Ondo",]
# series_sample =  pd.Series(nigeria_state, index = {"a", "b", "c", "d", "e"})
# print(series_sample)

#print(series_sample["c"])


data = {
 "name":  ["Ada", "John", "Mary", "Peter", "Grace"],
 "age":  [21, 24, 19, 27, 23],
 "gender":  ["Female", "Male", "Female", "Male", "Female"],
 "city":  ["Lagos", "Abuja", "Kano", "Enugu", "Kaduna"]
}

df = pd.DataFrame(data)

#print(df)
#print(df["age"])
#print(df[df["age"] < 23]) 
#print(df[df["age"] > 23])

#df[df["city"] == "Kaduna"] 
#print(df[df["city"] == "Kaduna"])
#count = df[(df["city"] == "Kaduna") & (df["gender"] =="Female")] . shape[0]
#print(count)
#print(df["age"].mean())
#print(df["age"].max())
#print(df["age"].min())
#print(df.describe())

#save as class_data.csv
#df.to_csv("class_data.csv",
#convert city colum into python list
#city_list = df. data_read[" index=False)

#print("saved successfully!")
 
#index=false=
import pandas as pd

# new_student = {"Name": "Micheal", "age": 22, "gender": "Male", "city": "ibadan"}
# df = pd.concat([df, pd.DataFrame([new_student])], ignore_index=True)
# #save as update_class_data.csv.
# print(df)


#Read class_data.csv into new variable data_read
# data_read = pd.read_csv("class_data.csv")
# #first five rows
# print("\nFirst five rows:")
# print(data_read.head())
# #convert name colum into python list
# name_list = data_read["name"].tolist()
# print("\nName list:")
# print(name_list)
#redconvert age colum into python list
# age_list =  df. data_read["age"]. tolist()
# print("\nAge list:")
# print(int["age"])city"]. tolist()
# print("\nCity list:")
# print(city_list )
# print("\n" + "-"*30 + "\n")
#using data_read - Example: search for a student
# lets search for Ada, Micheal, and student in lagos
# print("\nSearch for student name 'Ada:")
# print(data_read[data_read["name"] == "Micheal:"])
# print("\nsearch for student living in lagos:")
# print(data_read[data_read['city'] == "lagos"])


# print("\n1. information for Grace:")
# print(data_read[data_read["name"] == Grace])
# print("\n information for John:")
# name = input("enter name")
# name = input("John")
# print(name)

print("\n3 students whose names started with letter'' M':")
PRINT(data_read[data_read["name"], str.startswith("M", na=False)])
print("\n" + "="*40 + "\n")

#Creat dataframe containing the information scores_data = {"Name": ["David"], "Esther",
#  "Samule, "James, "peter", "Ruth", "daniel", "favour",} "Age": [20, 22. 24, 21, 19, 25,22,23]
# , "Final Exam Score": [82, 91, 68, 76, 55, 88, 73, 95]
# score_df = pd.DataFarme(scores_data)
# print(Scores_df)
# #save as student_scores.csv (no extra index)
# scores_df.to_csv("student_scores.csv", index=False)
# print("\nsaved as student_scorese.csv")
# print(scores_df)
# print("\n" + "=*40 + "\n")

# #Read student_scores.csv into new DataFrame
# scores_read = pd.read_csv("student_scores.csv")
# #Display statistical summary using describe()
# print("\nstatistical summary:")
# print(scores_read.describe())
# #Find average final exam score
# print(f"\naverge final exam score: {scores_read['Final Exam Score'].mean()}")
# #Find highest final examscore
# print(highest final exan scores:  {scores_read['Final Exam score'].max()}"")
# #Findlowest  final exam score
# print(f"lowest final exam score: {scores_read['Final Exam Score']. min()}")
# print("\n " + "-" *30 + '\n')

# Filtering student
# print("Q11: filtering students")

# Display student younger than 23
# print("\nstudents younger than 23:")
# print(scores_read[scores_read["age"] < 23])

#display student with final exam scores of 75 or above
# print("\n2. students with final exam scores of 75 or above:")
# print(scores_read[Scores_read["Final Exam Scores"] <=75])

# #display students whoscored below 60
# print("\\n3. students who scored below 60:")
# print(scores_read[scores_read["Final Exam Scores"] < 60])

#display students who are 22 years old or older and scored at least 75
# print("\n4. students who are 22 or older and scored at least 75:")
# print("scores_read"[(scores_read["Age"] >= 22) & (scores_read['Final Exam Score']  >= 75)]
# )

# print("\n" + "="*40 + "\n")

#QUESTION 12Scholasrhip List ====
# print("Q12: Scholarship List")

# The school awards scholarships to students who score 75 or above
# Filter out all eligible students
# scholarship_eligible = scores_read[scores_read"["Final Exam Score"] >= 75]
# print("\nEligibe students for scholarship:")
# print(scholarship_eligible)

# #save the result as scholarship_students.csv (no index)
# scholarship_eligible. to_csv("scholarship_students.csv", index=False)
# print('\nSaved as scholarship_students.csv(without index)')

#Read the new CSV file back into Pandas and print its contents
# scholarship_check = pd. read_csv("scholarship_students,csv", index=False)
# print("\nReading back scholarship_students.csv:")
# print(scholarship_check)

# Name Base filtering
# # using student_scores.csv
 df = Read_Csv("student_scores.csv")

# display students whose names begin with 'D' 
# print("\n1. students whose names begin with'D' :")
#print(df[df["Name"] .str.startwith("D")])

# display student whose names begin with 'S'
#print("\n2. students whose names begin with 'S' :")
#print(df[df["Name"] .str.startwith('S')])

#Save student whose name begin wuth 'D' into students_starting_D.csv
#Students_D = df[df["Name"]. str.startswith("D")]
#Students_D.to_csv("students_starting_D.csv", index=False)
#print("\nsaved students staring with D as students_starting_D.csv")
#print(Students_D)
print("\n" + "="*40 + '\n')

print("Q14: Independent Practice - Create your own DataFrame")


my_data = {"name": ["Chinedu", "Amina", "Tolu", "Emeka", "Yusuf", "Chioma", "Femi", "Zainab", "Tbrahim", "Kemi", "Segun"]
           , "age": [20, 22, 19, 24, 21, 23, 20, 22, 19, 25, 21, 24],
           'gender': ["Male", "Female", "Female", 'Male'm "Female", "Male", "Female", "Male", 'Female', "Male", "Female", "Male",],
           "city": ["Lagos", "Abuja", "Ibadan", "Enugu", "Port Harrcourt", "Kano", "Owerri", "Lagos", "Kaduna", "Sokoto", "Abeokuta", "Lagos"],
           "score": [85, 92, 78, 66, 89,73,95, 81, 70,85,76, 84]}

my_df = pd.DataFrame(my_data)

# display complete DataFrame
print("\n1. Complete DataFrame:")
print(my_df)

# display startistical summary
print("\n2, Statisticl summary:")
print(my_df.describe())

# 3. filtering examples
print("\n3. Students with score >= 80:")
print(my_df[my_df["score"] >= 80])

print("\n4. Average score:")
print(my_df["score"].mean())

print("\n5. Students from Lagos:")
print(my_df[my_df["city"] == "Lagos"])

# save the data
my_df.to_csv("my_students.csv", index=False)
prinnt("\nsaved as my_students.csv")





