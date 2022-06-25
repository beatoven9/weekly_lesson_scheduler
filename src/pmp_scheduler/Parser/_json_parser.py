from pathlib import Path
from typing import List
import json
from pmp_scheduler.Person import Student

def parse_json_students(students_path_str: str):
    students_path: Path = Path(students_path_str) 
    students: List[Student] = []
    with open(students_path, "r") as f:
        students_dict = json.load(f)
        for key in students_dict.keys():
            json_student = students_dict[key]
            new_student = Student(
                json_student[]
            )
