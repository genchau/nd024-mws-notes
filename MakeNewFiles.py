listOfFiles = [

]

def main():
	for file in listOfFiles:
		f= open(file,"w+")
		f.close()
		
main()