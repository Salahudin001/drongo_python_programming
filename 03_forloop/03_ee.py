student_arrival_time=[9,25,39,9,75,84,2,18,13]

number = len(student_arrival_time)
print(number)

for student_counter in range(len(student_arrival_time)):
    if student_arrival_time[student_counter]==9:
        print("On time")
        student_counter+=1

    elif student_arrival_time[student_counter]>9 and student_arrival_time [student_counter]<=19: 
        print("10 min late")
        student_counter+=1


    elif student_arrival_time[student_counter]>19 and   student_arrival_time[student_counter]<= 39:
        print("30 minutes late")
        student_counter+=1



    else:
         print("zero marks")

