import csv
def write_into_csv(info_list):
    with open('student_info.csv','a',newline='')as csv_file:
        writer=csv.writer(csv_file)

        if csv_file.tell()==0:
            writer.writerow(["Name","age","contactnumber","Email ID"])

        writer.writerow(info_list)


if __name__=='__main__':
    condition = True
    student_num=1


while(condition):
    student_info=input("Enter student information for student #{} in the following format (name age contact_number Email_ID):".format(student_num))
    print("Entered information:"+ student_info)

    #split

    student_info_list=student_info.split(' ')
    print("\n entered information is - \n Name:{} \n age:{} \ncontact_number:{}\n Email_ID:{}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
    choice_check=input("is the entered information correct ?(yes/no:)")

    if choice_check=="yes":
        write_into_csv(student_info_list)

        condition_check=input(" enter (yes/no) if you want to enter information for another student: ")
        if condition_check == "yes":
           condition = True
           student_num=student_num+1
        elif condition_check== "no":
           condition = False

    elif choice_check=="no":
        print("\n please re-enter the values:")
