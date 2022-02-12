class Course():
    
    def __init__(self):
        ## we will keep a dictionary of dictionary of courses for a easy access
        self.timetable = {}
        #self.coursedetails=
        self.totalUnitsTaken = 0

    
    def addCourses(self, name, units):
        ## find out if the course already exists or not
        if str(name) in self.timetable:
            print("This course already exists")
        else:
            self.timetable[name] = {"name" : str(name), "units": units}
            print("The course is added", name)
            self.totalUnitsTaken += int(units)
            

    def addLinks(self, name, link, optionNumber):
        if not name in self.timetable:
            print("Register the course first")
        else:
            if optionNumber == 1:
                # add the google meet link
                self.timetable[str(name)]["Google_Meet"] = link
            elif optionNumber == 2:
                # add the Notes/PPT link:
                self.timetable[str(name)]["Notes"] = link
            elif optionNumber == 3:
                # add any miscellanous links:
                self.timetable[str(name)]["Misc"] = link
            else:
                print("Not a valid option Number")
    
    def changeLinks(self, name, optionNumber, link):
        if not name in self.timetable:
            print("The course is not registered")
        else:

            if optionNumber == 1:
                # check if there's a google meet link already or not
                if not "Google_Meet" in self.timetable[name]:
                    print("The google meet link for this course was not added in the first place")
                self.timetable[name]["Google_Meet"] = link
            elif optionNumber == 2:
                # check if there's a Notes link already or not
                if not "Notes" in self.timetable[name]:
                    print("The Notes link for this course was not added in the first place")
                self.timetable[name]["Notes"] = link
            elif optionNumber == 3:
                # check if there's a Misc link already or not
                if not "Misc" in self.timetable[name]:
                    print("The misc link for this course was not added in the first place")
                self.timetable[name]["Misc"] = link
            else:
                print("Enter a valid optionNumber")

    def remove_link(self,name):
        if not name in self.timetable:
            print("The course with this name does not exist", name)
        else:
            print("1.Google Meet link")
            print("2.Notes for the course")
            print("3.Misc materials")
            user1=int(input("enter the number: \n"))
            if user1 == 1:
                # check if there's a google meet link already or not
                if not "Google_Meet" in self.timetable[name]:
                    print("The google meet link for this course was not added in the first place")
                else:
                    self.timetable[name].pop("Google_Meet")
            elif user1 == 2:
                # check if there's a Notes link already or not
                if not "Notes" in self.timetable[name]:
                    print("The Notes link for this course was not added in the first place")
                else:
                    self.timetable[name].pop("Notes")
            elif user1 == 3:
                # check if there's a Misc link already or not
                if not "Misc" in self.timetable[name]:
                    print("The misc link for this course was not added in the first place")
                else:
                    self.timetable[name].pop("Misc")
            else:
                print("Not a valid optionNumber")

                

    def access_course(self, name):
        if not name in self.timetable:
            print("The course with this name does not exist", name)
        else:
            print(self.timetable[name])
    
    def remove_course(self, name):
        if not name in self.timetable:
            print("The course with this name does not exists", name)
        else:
            self.totalUnitsTaken -= int(self.timetable[name]["units"])
            self.timetable.pop(name)

    def check_timetable(self):
        print("The courses in your timetable are as follows - ")
        for courses in self.timetable:
            print(self.timetable[courses])
    
    def check_total_units_taken(self):
        print("The total units taken by you uptil now is - ",self.totalUnitsTaken)

if __name__ == "__main__":
    sub_object =Course()
    while True:
       print("Welcome to courses")
       print("1. Add courses")
       print("2. Access courses")
       print("3. View all the courses taken till now")
       print("4. Check total units taken till now")     
       userC=int(input("Make Decisions : "))
       #print(userC)
        #if sub_object.coursedetails==True:           
       if userC==2:
            print("1.Add Links")                  
            print("2.Change Links")
            print("3.Access course material") 
            print("4.Remove Courses")
            print("5.Remove links")  
            print("6.Logout")
            user_choice=int(input("Make a choice:"))
            if user_choice==1:
                name=input("Enter the name of the course : \n")
                print("1.Google meet link")
                print("2.Notes link")
                print("3.Misc link")
                optionNumber=int(input("Enter your option for which the link has to be added \n"))
                link=input("enter your link: \n")
                sub_object.addLinks(name,link,optionNumber)
                print("\n1.back menu")
                print("2.log out")
                choose = int(input())
                if choose == 1:
                    continue
                elif choose == 2:
                    break
            elif user_choice==2:
                name=input("Enter the name of the course : \n")
                print("1.Google meet link")
                print("2.Notes link")
                print("3.Misc link")
                optionNumber=int(input("Enter your option for which the link has to be changed \n"))
                link=input("enter your link: \n")
                sub_object.changeLinks(name,link,optionNumber)
                print("\n1.back menu")
                print("2.log out")
                choose = int(input())
                if choose == 1:
                    continue
                elif choose == 2:
                    break
            elif user_choice==3:
                name=input("Enter the name of the course : \n")
                sub_object.access_course(name)
                print("\n1.back menu")
                print("2.log out")
                choose = int(input())
                if choose == 1:
                    continue
                elif choose == 2:
                    break
            elif user_choice==4:
                name=input("Enter the name of the course to be deleted: \n") 
                sub_object.remove_course(name)
                print("\n1.back menu")
                print("2.log out")
                choose = int(input())
                if choose == 1:
                    continue
                elif choose == 2:
                    break
            elif user_choice==5:
                name=input("enter the name of the course : \n")
                sub_object.remove_link(name) 
                print("\n1.back menu")
                print("2.log out")
                choose = int(input())
                if choose == 1:
                    continue
                elif choose == 2:
                    break   
            elif user_choice==6:
                break
       elif userC==1:
            name=input("Enter the name of the course to be added: \n")
            units=input("enter the units corresponding to the course: \n")
            sub_object.addCourses(name,units)
       elif userC==3:
            sub_object.check_timetable()
       elif userC==4:
            sub_object.check_total_units_taken()
       else:
            print("Enter a valid option Number")
