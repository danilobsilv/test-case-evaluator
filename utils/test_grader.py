import os
import subprocess


class TestGrader:
    @staticmethod
    def read_input_file(input_file_path):
        with open(input_file_path, 'r') as input_file:
            input_content = input_file.read().strip()

            if '\n' in input_content:
                input_values = input_content.split('\n')
            else:
                input_values = input_content.split()

        return input_values

    @staticmethod
    def run_tests(question, student_dir, input_dir, writer):
        compile_success = False

        for orientation in ["vertical", "horizontal"]:
            compile_command = ["g++", "-std=c++17", os.path.join(student_dir, f"{question}.cpp"), "-o", "code"]
            compile_process = subprocess.run(compile_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if compile_process.returncode == 0:
                compile_success = True
                break

        if compile_success:
            for i in range(1, 4):
                input_file_path = os.path.join(input_dir, f"pp1-{question.lower()}-ct{i}.{orientation}.in")

                try:
                    input_values = TestGrader.read_input_file(input_file_path)

                    with subprocess.Popen(["./code"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                          stderr=subprocess.PIPE) as run_process:
                        actual_output, _ = run_process.communicate(input='\n'.join(input_values).encode())
                        actual_output = actual_output.decode().strip()

                    writer.writerow([student_dir, question, f"CT{i}", 0.4166, True])

                except Exception as e:
                    writer.writerow([student_dir, question, f"CT{i}", 0.0, False])
                    print(f"Erro ao executar o teste {question}, CT{i}: {e}")

        else:
            for i in range(1, 4):
                writer.writerow([student_dir, question, f"CT{i}", 0.0, False])
                print(f"Falha ao compilar e executar testes para {question} em ambas as orientações")