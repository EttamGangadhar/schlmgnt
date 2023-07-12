from student.models import *



def add_update_school(school_info):
    school = None
    try:
        school = School.objects.get(id=school_info["id"])# read 'id' and update entities.
        school.name = school_info["name"]
        school.address = school_info["address"]# if the school exists we 'update attributs' and save the data.
        school.phone_number = school_info["phone_number"]
        school.email = school_info["email"]
        school.principal_name = school_info["principal_name"]
        school.save()
    except Exception as e :
        print("School doesn't exist")

    if not school:
        try:
            school = School(id=school_info["id"],
                            name=school_info["name"], # if school does not exist, we "create new object" and save it.
                            address=school_info["address"], 
                            phone_number=school_info["phone_number"],
                            email=school_info["email"],
                            principal_name=school_info["principal_name"])
            school.save()
        except Exception as e:
            print("School save failed: %s" % str(e))

    return school

    
def add_update_class(class_info):
    class_obj = None
    try:
        class_obj = Class.objects.get(class_id=class_info["class_id"])#read class_id and update entities.
        class_obj.name = class_info["name"]
        class_obj.teacher_name = class_info["teacher_name"]
        class_obj.start_date = class_info["start_date"]
        class_obj.end_date = class_info["end_date"]
        class_obj.save()
    except Exception as e:
        print("class doesn't exist")

    if not class_obj:
        try:
            class_obj = Class(
                              name=class_info["name"],
                              teacher_name=class_info["teacher_name"],
                              start_date=class_info["start_date"],
                              end_date=class_info["end_date"])
            class_obj.save()
        except Exception as e:
                print("Class save failed: %s" % str(e))

    return class_obj

def add_update_student(student_info):
        student_obj = None
        try:
            student_obj = Student.objects.get(roll_number=student_info["roll_number"])#read "student_id" and update entities.
            student_obj.first_name = student_info["first_name"]
            student_obj.last_name = student_info["last_name"]
            student_obj.date_of_birth = student_info["date_of_birth"]
            student_obj.address = student_info["address"]
            student_obj.phone_number = student_info["phone_number"]
            student_obj.email = student_info["email"]
            student_obj.save()
        except Exception as e:
            print("student dosn't exist.")

        if not student_obj: #if not found, create new data.
            try:
                student_obj = Student(roll_number=student_info["roll_number"],
                                      first_name=student_info["first_name"],
                                      last_name=student_info["last_name"],
                                      date_of_birth=student_info["date_of_birth"],
                                      address=student_info["address"],
                                      phone_number=student_info["phone_number"],
                                      email=student_info["email"])
                student_obj.save()
            except Exception as e:
                 print("Student save failed: %s" % str(e))

        return student_obj


def add_update_teacher(teacher_info):
        teacher = None
        try:
            teacher = Teacher.objects.get(id=teacher_info["id"])#read the id and update attributes.
            teacher.name = teacher_info["name"]
            teacher.email = teacher_info["email"]
            teacher.phone_number = teacher_info["phone_number"]
            teacher.qualification = teacher_info["qualification"]
            teacher.save()
        except Exception as e:
            print("teacher doesn't exist.")

        if not teacher:
            try:
                teacher = Teacher(id=teacher_info["id"],
                                      name=teacher_info["name"],
                                      email=teacher_info["email"],
                                      phone_number=teacher_info["phone_number"],qualification=teacher_info["qualification"])
                teacher.save()
            except Exception as e:
                print("Teacher save failed: %s" % str(e))

        return teacher

def add_update_subject(subject_info):
    subject = None
    try:
        subject = Subject.objects.get(name=subject_info["name"])
        subject.teacher = subject_info["teacher"]
        subject.class_field = subject_info["class_field"]
        subject.save()
    except Exception as e:
        print("subject doesn't exist.")

    if not subject:
        try:
            subject = Subject(name=subject_info["name"],
                                  teacher=subject_info["teacher"],
                                  class_field=subject_info["class_field"])
            subject.save()
        except Exception as e:
            print("Subject save failed: %s" % str(e))
    
    return subject


def add_update_attendance(attendance_info):
    attendance = None
    try:
        attendance = Attendance.objects.get(student=attendance_info["student"], date=attendance_info["date"])
        attendance.is_present = attendance_info["is_present"]
        attendance.save()
    except Exception as e:
        print("attendance doesn't exist.")

    if not attendance:
        try:
            attendance = Attendance(student=attendance_info["student"],
                                        date=attendance_info["date"],
                                        is_present=attendance_info["is_present"])
            attendance.save()
        except Exception as e:
            print("Attendance save failed: %s" % str(e))

    return attendance

def add_update_exam(exam_info):
    exam = None
    try:
        exam = Exam.objects.get(class_field=exam_info["class_field"], subject=exam_info["subject"], date=exam_info["date"])
        exam.maximum_marks = exam_info["maximum_marks"]
        exam.save()
    except Exception as e:
        print("exam doesn't exist.")

    if not exam:
        try:
            exam = Exam(class_field=exam_info["class_field"],
                            subject=exam_info["subject"],
                            date=exam_info["date"],
                            maximum_marks=exam_info["maximum_marks"])
            exam.save()
        except Exception as e:
            print("Exam save failed: %s" % str(e))

    return exam


def add_update_exam_result(exam_result_info):
    exam_result = None
    try:
        exam_result = ExamResult.objects.get(exam=exam_result_info["exam"], student=exam_result_info["student"])
        exam_result.obtained_marks = exam_result_info["obtained_marks"]
        exam_result.save()
    except Exception as e:
        print("exam doesn't exist.")

    if not exam_result:
        try:
            exam_result = ExamResult(exam=exam_result_info["exam"],
                                         student=exam_result_info["student"],
                                         obtained_marks=exam_result_info["obtained_marks"])
            exam_result.save()
        except Exception as e:
            print("ExamResult save failed: %s" % str(e))

    return exam_result


def delete_student(student_info):
    student = None
    try:
        student = Student.objects.get(roll_number=student_info["roll_number"]) # get the roll_number from student and delete it.
        student.delete()
    except Exception as e:
        print("student not found.")