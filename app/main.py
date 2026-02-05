from dataclasses import dataclass
from datetime import datetime
from typing import List
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


    @classmethod
    def write_groups_information(cls, groups) -> int:
        with open(f"groups.pickle", "wb") as f:
            pickle.dump(groups, f)

        return max(len(g.students) for g in groups) if groups else 0


    @classmethod
    def write_students_information(cls, students: List[Student]) -> int:
        with open("students.pickle", "wb") as f:
            pickle.dump(students, f)

        return len(students)


    @classmethod
    def read_groups_information(cls, groups) -> List[str]:
        with open(f"groups.pickle", "rb") as f:
            pickle.load(f)
            names = list({g.specialty.name for g in groups})
        return names


    @classmethod
    def read_students_information(cls, students: List[Student]) -> int:
        with open("students.pickle", "rb") as f:
            pickle.load(f)
        return students
