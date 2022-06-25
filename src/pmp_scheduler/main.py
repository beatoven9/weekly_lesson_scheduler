import argparse
from typing import Optional
from pmp_scheduler.Parser import parse_sch_students
import json


def main():
    student_file: Optional[str] = None
    teacher_file: Optional[str] = None
    output_dir: Optional[str] = None

    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--student_file",
        required=False,
        default=None,
        help="path to file containing list of students. OPTIONAL",
    )
    parser.add_argument(
        "-t",
        "--teacher_file",
        required=False,
        default=None,
        help="path to file containing list of teachers. OPTIONAL",
    )
    parser.add_argument(
        "-d",
        "--output_dir",
        required=False,
        default=None,
        help="path to directory where json files will be written. If not provided, user will be prompted for this.",
    )

    args: argparse.Namespace = parser.parse_args()
    student_file = args.student_file
    teacher_file = args.teacher_file
    output_dir = args.output_dir

    print("Student file is: ", student_file)
    print("Teacher file is: ", teacher_file)
    print("Output dir is: ", output_dir)

    if student_file is not None:
        students = parse_sch_students(student_file)
        with open("~/Development/PythonPrograms/pmp_scheduler/src/tests/test_data/students.json", "w") as f:
            json.dump(students, f)


if __name__ == "__main__":
    main()
