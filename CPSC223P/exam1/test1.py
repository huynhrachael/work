def list_of_names(scores,/):
	if dict == {}:     #if dict is empty
		print("Invalid")
		return None
	else:
		listName = []
		for k,v in scores.items():
			listName.append([v["lastname"],v["firstname"]])
		list(listName)
		listName.sort()
	return listName
	
			
			

def student_hw_avg(scores,/,*, id):
	if not scores:lis
		print("Invalid")
		return None
	else:
		student_grade = sum(scores[id]["HW_scores"])
		return student_grade / 4
		
		

def class_hw_avg(scores,/,*, hw_index):
	for k,v in scores.item():
		if((hw_index < 0 or (hw_index >= len(v['HW_scores']))):
			print("Index out of range")
			return None
	templist =[]
	for k in scores:
		templist.append(scores[k]["HW_scores"][hw_index])
	sum = 0
	for x in templist:
		sum = sum + int(x)
	return (sum/len(templist))
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
