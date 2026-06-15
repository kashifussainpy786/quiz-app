import json
class Question:
	def __init__(self,question,options, correct_option):
		self.question = question 
		self.options = options 
		self.correct_option = correct_option 
	def __str__(self):
		return(f"question:{self.question}\n"
		f"options:{self.options}\n")
class Quiz:
		def __init__(self):
			self.questions = []
			self.score = 0
		def load_questions(self):
			try:
				with open("quiz.json","r")as file:
					data = json.load(file)
					for d in data:
						q = Question(**d)
						self.questions.append(q)
			except FileNotFoundError:
				print("NO FILE FOUND...")
		def save_results(self):
			results = {
			"score":self.score,
			"total":len(self.questions)
			}
			with open("results.json","w")as file:
				json.dump(results,file)
		def run(self):
			for i in self.questions:
				print(i)
				answer = input("Enter answer:")
				if answer == i.correct_option:
					self.score +=1
				else:
					print("Wrong answer ")
					break
			self.save_results()
			print(f"Your score: {self.score}/{len(self.questions)}")
quiz = Quiz()
quiz.load_questions()
quiz.run()