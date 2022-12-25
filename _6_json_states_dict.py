import json
import os

dict1 = {
			"Assam" : "Dispur",
		 	"Bihar" : "Patna",
			"Chhattisgarh" : "Raipur",
			"Goa": "Panji",
			"Himachal Pradesh" : "Shimla",
			"Jharkhand" : "Ranchi",
			"Karnataka" : "Bengaluru"
		}

file = open(os.getcwd() + "/Python/_0_Assignments/states_dict.json", "w")

json.dump(dict1,file, indent=1)