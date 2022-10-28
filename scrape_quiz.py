import re
import os
import sys
from bs4 import BeautifulSoup as bs
from question import Question


def scrape(html_file_path):

	output_file = html_file_path.split(".")[0] + ".txt"

	questions_obj = []

	try:
		with open(html_file_path,'r') as html:
			html_file_content = html.read()


			soup = bs(html_file_content,'html.parser')


			questions_container = soup.find(id="questions")

			list_of_questions_containers = questions_container.find_all("div",{'class':'quiz_sortable question_holder'})

			
			for container in list_of_questions_containers:

				q = Question()

				question_text = container.find(class_="question_text user_content").get_text()

				q.question = question_text.strip()


				question_number = container.find('div',{'class':'header'}).find('span',{'class':'name question_name'}).get_text()

				q.question_number = question_number

				answer_wrapper = container.find(class_="answers_wrapper")

				answers_containers = answer_wrapper.find_all("div",{'id':re.compile("answer_")})

				answers = []
				for ans in answers_containers:
					answers.append(ans['title'])

				q.answers = answers


				questions_obj.append(q)

	except FileNotFoundError:
		print("ERROR: File can't be found")
		return

	print(f"Questions Found: {len(questions_obj)}")


	with open(output_file,'w') as qfile:
		for q in questions_obj:
			qfile.write(q.to_string())
	print(f"Question saved:  {output_file}")



if len(sys.argv) <= 1 or sys.argv[1].lower() == "-h":
	print("USAGE: python3 scrape_quiz.py <path to html file>")
	print("\t-The output will be saved to the same location as the html file")

elif len(sys.argv) == 2:
	scrape(sys.argv[1])

