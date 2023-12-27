# Test Case Evaluator


This is a project for evaluating students in programming questions.

## Description

The project comprises an automated assessment system for C++ programming questions (so far). Users send the source codes of the proposed questions and the system runs automated tests to verify the accuracy of the solutions.

## Features

- Automated compilation of user-submitted codes.
- Execution of automated test cases.
- Evaluation and generation of grades based on test results.

## Project Structure

The project is organized as follows:

- `student_path.txt`: file containing the student's directory.
- `example_test_cases_input_vertical/` and `example_test_cases_input_horizontal/`: directories containing input test cases.
- `example_test_cases_output/` : directories containing expected output test cases.
- `grades.csv`: CSV file containing student grades.

## Requirements

- Python 3.x
- g++ Compiler (for compiling C++ codes)
- Input and output files for test cases

## How to Use


Hello, to use the evaluation script, follow the steps below:

1. Copy the folder with your codes into the /script-pp1 folder.
For example: for the duo José and Ana, the /script-pp1 folder will look like this:</br>
`student_path.txt`</br>
`/PP1-Jose-Ana`</br>
`/example_test_cases_input_horizontal`</br>
`/example_test_cases_input_vertical`</br>
`/example_test_cases_output`</br>

2. Now, open the file `student_path.txt` and type the relative path to your code folder. Pay attention to the folder hierarchy. The path must be exactly the same as the folder!
e.g., PP1-Jose-Ana
E.g. 2: If within the folder PP1-Jose-Ana there is another folder:
/PP1-Jose-Ana
-/AnotherFolder
-/PP1-Jose-Ana # This one really containing the scripts, the path should be: PP1-Jose-Ana/PP1-Jose-Ana

3. Open the CMD (terminal in Windows) and navigate to the folder where the script is along with the other files.

4. Now, being in the folder, at the same level as the script, type: python evaluate.py (or python3 evaluate.py, depending on your Python installation)

5. The grade count will be in the grades.csv file that will be generated after execution.



## Contribution

Contributions are welcome! Feel free to submit suggestions, corrections, or enhancements via pull requests.

## Authors

- Danilo Bruno da Silva  ([GitHub](https://github.com/danilobsilv)) - ([Linkedin](https://www.linkedin.com/in/danilo-bruno-da-silva-30b917225/)): Programmed and designed the script.


## License

This project is licensed under the [XYZ License](license link).
