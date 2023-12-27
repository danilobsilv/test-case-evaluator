import csv

class Student:
      
      def __init__(self, student_dir:str) -> None:
            self.student_path_file = "student_path.txt"
            self.student_dir = student_dir

      def read_student_dir(self):
            with open(self.student_path_file, "r") as student_file_path:
                  self.student_dir = student_file_path.readline().strip()

      def check_grade(self, file_path) -> None:
            total_grade = 0.0

            with open(file_path, newline='') as csvfile:
                  reader = csv.DictReader(csvfile)
                  for row in reader:
                        grade = float(row[' -GRADE- ']) if row[' -GRADE- '].strip() else 0.0
                        total_grade += grade
    
            total_grade =  "{:.3f}".format(total_grade) # arredonda a nota pra cima
            if total_grade == "9.998": # arredonda pra 10
                  total_grade = 10
            print(f"Sua nota: {total_grade}")


      def check_correct_test_case(self, file_path) -> None:
            with open(file_path, newline='') as csvfile:
                  reader = csv.DictReader(csvfile)
                  for row in reader:
                        if float(row[' -GRADE- ']) == 0.4166:
                              print(f"O(a) aluno(a) {row['-TEAM- ']} acertou o caso de teste {row[' -CASE TEST- ']} da questão {row[' -QUESTION- ']}.")