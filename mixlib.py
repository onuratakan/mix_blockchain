def starting_text_centered():
	print(" ")
	print(" STARTING \n")


def ended_text_centered():
	print(" ")
	print(" ENDED \n")

def printcentertext(text):
	print(" ")
	print(text)
	print(" ")

def banner_maker(sc_name,description,author,email):
	return("""Script Name    : """+sc_name+"""\n"""+"""Description    : """+description+"""\n"""+"""Author         : """+author+"""\n"""+"""Email          : """+email)

def question_maker(question_text=None,mode=None):
	
	if question_text == None:
		if mode == "main":
			question_text = "Please enter main option: "
		elif mode == "sub":
			question_text = "Please enter sub option: "
		elif mode == "anykeytocontinue":
			question_text = "Press any key to continue..."
	
	return(input(question_text))


def menu_maker(menu_number,menu_text):
	return(str(menu_number)+") "+menu_text+"\n")
	

def quit_menu_maker(mode):
	if mode == "main":
		quit_menu_maker_result = "\n0) Quit \n"
	elif mode == "sub":
		quit_menu_maker_result = "\n0) Quit sub menu \n"
	return(quit_menu_maker_result)


def menu_space():
	return("\n")

def menu_seperator():
	return("\n"+"*** \n"+"\n")

def menu_title(menu_title_text):
	return("\n"+"*** "+menu_title_text+" ***"+" \n"+"\n")


def decode(string):
	return string.encode('utf-8')




def clear():
	os.system("clear")
