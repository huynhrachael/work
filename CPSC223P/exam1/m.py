from test1 import *

#scores dictionary
scores={
    343:{"firstname":"John",
         "lastname":"Stockton",
         "HW_scores":[87,69,96,90]
         },
    12: {"firstname":"Martina",
         "lastname":"Navratilova",
         "HW_scores":[78,89,86,92]
         }, 
    500: {"firstname":"Julio",
         "lastname":"Chavez",
         "HW_scores":[88,89,100,100]
         }, 
    211: {"firstname":"Mary",
         "lastname":"Pham",
         "HW_scores":[80,99,77,100]
         }
    }

#use below for testing... do not limit your testing to only these

print(list_of_names(scores)) #should print [['Chavez','Julio'],['Navratilov','Martina'],['Pham','Mary'],['Stockton','John']]

print(student_hw_avg(scores, id=12))    #should print 86.25 

print(class_hw_avg(scores, hw_index=0))    #should print 83.25 '''



