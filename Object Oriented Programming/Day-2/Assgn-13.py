#OOPR-Assgn-13
#Start writing your code here
class Classroom:
    classroom_list = ['G015', 'G066', 'L123', 'L135', 'L143', 'L13']
    
    @staticmethod
    def search_classroom(class_room):
        #print(class_room.upper())
        if class_room.upper() in Classroom.classroom_list:
            return "Found"
        return -1

print(Classroom.search_classroom('L135'))
