#Naomi Williams
#4/30/2025
#Course Information Program
#Main funcion to ask the user to input a course number to display the information for that course
#Parameter - None
#Return - None
def main():
    CourseNum_RoomNum, CourseNum_InstructorName, CourseNum_MeetingTime = RoomNum_Dict()
    print("Please enter a course number: ")
    #Goes through the dictionary CourseNum_RoomNum and prints the key
    for key in CourseNum_RoomNum:
        print(key)
    #Ask the user to input the couse number
    #Put the .upper function at the end so that if the user inputs the course name in lowercase format it would be seen as
    #The right format by the program and won't cause an error to pop up
    CourseNum = input("Enter a course number: ").upper()
    bFlag = True
    while bFlag: 
        #If the Course Number inputed by the user is in the CourseNum_RoomNum dictionary as a key then print this information
        if CourseNum in CourseNum_RoomNum:
            #Print the course number inputed by the user
            print(f"\nCourse Number: {CourseNum} ")
            #Display the room number based on the CourseNum_RoomNum dictionary and the key is the course number inputed by the user
            print(f"Room Number: {CourseNum_RoomNum[CourseNum]}")
            #Display the Instructors name based on the CourseNum_InstructorName dictionary and the key is the course number inputed by the user
            print(f"Instructor Name: {CourseNum_InstructorName[CourseNum]}")
            #Display the Meeting time based on the CourseNum_MeetingTime dictionary and the key is the course number inputed by the user
            print(f"Meeting Time: {CourseNum_MeetingTime[CourseNum]}")
            bFlag = False
        else:
            #If the course number inputed by the user is not in the dictionary display and error and allow them to reenter
            print("Error - Invalid input. This course does not exist. Please reenter!")
            CourseNum = input("Enter a course numer: ").upper()
                   
def RoomNum_Dict():
    #Dictionary for the course number and the room number
    CourseNum_RoomNum = { #Give the Dictionary a name
        "CS101" : "3004",
        "CS102" : "4501",
        "CS103" : "6755",
        "NT110" : "1244",
        "CM241" : "1411"
    } #Close the dictionary
    #Dictionary for the course number and the instructor name
    CourseNum_InstructorName = { #Give the Dictionary a name
        "CS101" : "Haynes",
        "CS102" : "Alvarado",
        "CS103" : "Rich",
        "NT110" : "Burke",
        "CM241" : "Lee"
    } #Close the dictionary
    #Dictionary for the course number and the meeting time
    CourseNum_MeetingTime = { #Give the Dictionary a name
        "CS101" : "8:00 AM",
        "CS102" : "9:00 AM",
        "CS103" : "10:00 AM",
        "NT110" : "11:00 AM",
        "CM241" : "1:00 PM"
    } #Close the dictionary
    return CourseNum_RoomNum, CourseNum_InstructorName, CourseNum_MeetingTime
      
#Calling the main function back to display the program  
main()