class Question:
	def _init_(self):

		self.question_number = ""

		self.question        = ""

		self.answers         = []

		self.explaination    = ""

	def to_string(self):
		border = "============================================================================================"
		title  = f"#{' '*39}{self.question_number}{' '*40}#"
		header = border + "\n" + title +"\n"+border + "\n"

		string = header

		string += (self.question + "\n" + border +"\n")


		for answer in self.answers:
			string += f"[] {answer}\n"

		string += (border + ("\n"*3))
		return string
