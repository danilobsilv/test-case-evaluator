import csv
from utils.student import Student
from utils.test_grader import TestGrader

if __name__ == "__main__":
      class_grader = Student("")
      class_grader.read_student_dir()

      questions = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8"]
      input_dir_vertical = "test_cases_input_vertical"
      output_dir_vertical = "test_cases_output_vertical"
      input_dir_horizontal = "test_cases_input_horizontal"
      output_dir_horizontal = "test_cases_output_horizontal"

      with open('notas.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["-TEAM- ", " -QUESTION- ", " -CASE TEST- ", " -GRADE- ", " -COMPILED- "])

            for question in questions:
                  TestGrader.run_tests(question, class_grader.student_dir, input_dir_vertical, writer)

      class_grader.check_correct_test_case("notas.csv")
      class_grader.check_grade("notas.csv")

      input("Pressione ENTER para encerrar.")