from pathlib import Path

def parse_sch_students(students_path_str: str):
    students_path: Path = Path(students_path_str) 
    with open(students_path, "r") as f:
        new_student = {}
        students = []
        for line in f.readlines():
            if line[0] == "#":
                continue
            else:
                key_value = line.lstrip().split(" ")
                if key_value[0] == "name:":
                    students.append(new_student)
                    new_student = {}
                    new_student["name"] = key_value[1].strip()
                elif key_value[0] == "lessons:":
                    new_student["lessons"] = {}
                    for lesson in key_value[1:]:
                        teacher_num = lesson.split(":")
                        new_student["lessons"][teacher_num[0]] = teacher_num[1].strip()
                else:
                    new_student[key_value[0].strip(":")] = key_value[1].strip()

                
    return students


