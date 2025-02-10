# Cailli Church #
# Records of Students 
# the app will be able to searcha students name and see there gpa
def main ():
    gpa = float(input("Please enter Student's GPA:  "))
    name = input("Enter your name or put ZZZ to close program:  ")
    if name == "ZZZ":
          exit()
    else:
          print("continue")
    if gpa > 3.5:
        print( name + "has made the Dean's List")
    else : 
        print( name + "had made the Honor Roll")  
main()
