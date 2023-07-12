from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import School, Class, Student, Teacher, Subject, Attendance, Exam, ExamResult
from schoolmm.utils import convert_data
from student.helpers import add_update_school,add_update_class,add_update_student,delete_student,add_update_teacher,add_update_subject,add_update_attendance,add_update_exam,add_update_exam_result

@api_view(['POST'])
def creupschool(request):
    data = {} #created to store the response data.
    school = None
    if request.method == "POST":
        post_data = convert_data(request.body)#extracts the data from the request body.
        if post_data:
            id = post_data.get("id",None)  # it is not empty,  retrieve the below fields from post_data dictionary.
            name = post_data.get("name", None)
            address = post_data.get("address", None)
            phone_number = post_data.get("phone_number", None)
            email = post_data.get("email", None)
            principal_name = post_data.get("principal_name", None)

            school = add_update_school({
                "id":id,
                "name": name,          #add_update_school function with the extracted data to add or update a school record.
                "address": address,
                "phone_number": phone_number,
                "email": email,
                "principal_name": principal_name
            })

            if school: # if the school exists, 
                data["school"] = {
                    "id": school.id,
                    "name": school.name,
                    "address": school.address,
                    "phone_number": school.phone_number,
                    "email": school.email,
                    "principal_name": school.principal_name
                }
                data["success"] = True
            else:
                data["school"] = None
                data["success"] = False
        else:
            data["school"] = None
            data["success"] = False
            data["errors"] = "Invalid data format"

    return Response(data)


@api_view(['POST'])
def creupclass(request):
    data = {}
    if request.method == "POST":
        post_data = request.data
        if post_data:
            school_id = post_data.get("id", None)
            name = post_data.get("name", None)
            teacher_name = post_data.get("teacher_name", None)
            start_date = post_data.get("start_date", None)
            end_date = post_data.get("end_date", None)

            school = School.objects.get(id=school_id)
            class_obj = add_update_class({
                "school": school,
                "name": name,
                "teacher_name": teacher_name,
                "start_date": start_date,
                "end_date": end_date
            })

            if class_obj:
                data["class"] = {
                    "id": class_obj.id,
                    "school": class_obj.school.id,
                    "name": class_obj.name,
                    "teacher_name": class_obj.teacher_name,
                    "start_date": class_obj.start_date,
                    "end_date": class_obj.end_date
                }
                data["success"] = True
            else:
                data["class"] = None
                data["success"] = False
        else:
            data["class"] = None
            data["success"] = False
            data["errors"] = "Invalid data format"

    return Response(data)


@api_view(['POST'])
def adduptea(request):
    data = {}
    teacher = None
    if request.method == "POST":
        post_data =convert_data (request.body)
        if post_data:
            teacher_id = post_data.get("id", None)
            name = post_data.get("name", None)
            email = post_data.get("email", None)
            phone_number = post_data.get("phone_number", None)
            qualification = post_data.get("qualification", None)

            teacher = add_update_teacher({
                "id": teacher_id,
                "name": name,
                "email": email,
                "phone_number": phone_number,
                "qualification": qualification
            })

            if teacher:
                data["teacher"] = {
                    "id": teacher.id,
                    "name": teacher.name,
                    "email": teacher.email,
                    "phone_number": teacher.phone_number,
                    "qualification": teacher.qualification
                }
                data["success"] = True
            else:
                data["teacher"] = None
                data["success"] = False
        else:
            data["teacher"] = None
            data["success"] = False
            data["errors"] = "Invalid data format"

    return Response(data)


@api_view(['POST'])
def addupdstu(request):
    data = {}
    student = None
    if request.method == "POST":
        post_data =convert_data(request.body)
        if post_data:
            first_name = post_data.get("first_name", None)
            last_name = post_data.get("last_name", None)
            date_of_birth = post_data.get("date_of_birth", None)
            address = post_data.get("address", None)
            phone_number = post_data.get("phone_number", None)
            email = post_data.get("email", None)

            student = add_update_student({
                "first_name": first_name,
                "last_name": last_name,
                "date_of_birth": date_of_birth,
                "address": address,
                "phone_number": phone_number,
                "email": email
            })

            if student:
                data["student"] = {
                    "id": student.id,
                    "first_name": student.first_name,
                    "last_name": student.last_name,
                    "date_of_birth": student.date_of_birth,
                    "address": student.address,
                    "phone_number": student.phone_number,
                    "email": student.email
                }
                data["success"] = True
            else:
                data["student"] = None
                data["success"] = False
        else:
            data["student"] = None
            data["success"] = False
            data["errors"] = "Invalid data format"

    return Response(data)


@api_view(['POST'])
def addupsub(request):
    data = {}
    subject = None
    if request.method == "POST":
        post_data =convert_data(request.body)
        if post_data:
            subject_id = post_data.get("id", None)
            name = post_data.get("name", None)
            teacher_id = post_data.get("teacher_id", None)
            class_id = post_data.get("class_id", None)

            subject = add_update_subject({
                "id": subject_id,
                "name": name,
                "teacher_id": teacher_id,
                "class_id": class_id
            })

            if subject:
                data["subject"] = {
                    "id": subject.id,
                    "name": subject.name,
                    "teacher_id": subject.teacher_id,
                    "class_id": subject.class_id
                }
                data["success"] = True
            else:
                data["subject"] = None
                data["success"] = False
        else:
            data["subject"] = None
            data["success"] = False
            data["errors"] = "Invalid data format"

    return Response(data)

@api_view(['POST'])
def addupadnce(request):
    data = {}
    attendance = None
    if request.method == "POST":
        post_data = convert_data(request.body)
        if post_data:
            attendance_id = post_data.get("id", None)
            student_id = post_data.get("student_id", None)
            date = post_data.get("date", None)
            is_present = post_data.get("is_present", None)

            attendance = add_update_attendance({
                "id": attendance_id,
                "student_id": student_id,
                "date": date,
                "is_present": is_present
            })

            if attendance:
                data["attendance"] = {
                    "id": attendance.id,
                    "student_id": attendance.student_id,
                    "date": attendance.date,
                    "is_present": attendance.is_present
                }
                data["success"] = True
            else:
                data["attendance"] = None
                data["success"] = False
        else:
            data["attendance"] = None
            data["success"] = False
            data["errors"] = "Invalid data format"

    return Response(data)


@api_view(['POST'])
def addupexam(request):
    data = {}
    exam = None
    if request.method == "POST":
        post_data = convert_data(request.body)
        if post_data:
            exam_id = post_data.get("id", None)
            class_id = post_data.get("class_id", None)
            subject_id = post_data.get("subject_id", None)
            date = post_data.get("date", None)
            maximum_marks = post_data.get("maximum_marks", None)

            exam = add_update_exam({
                "id": exam_id,
                "class_id": class_id,
                "subject_id": subject_id,
                "date": date,
                "maximum_marks": maximum_marks
            })

            if exam:
                data["exam"] = {
                    "id": exam.id,
                    "class_id": exam.class_id,
                    "subject_id": exam.subject_id,
                    "date": exam.date,
                    "maximum_marks": exam.maximum_marks
                }
                data["success"] = True
            else:
                data["exam"] = None
                data["success"] = False
        else:
            data["exam"] = None
            data["success"] = False
            data["errors"] = "Invalid data format"

    return Response(data)


@api_view(['POST'])
def addupexamres(request):
    data = {}
    if request.method == "POST":
        post_data = request.data
        if post_data:
            exam_result_id = post_data.get("id", None)
            exam_id = post_data.get("exam_id", None)
            student_id = post_data.get("student_id", None)
            obtained_marks = post_data.get("obtained_marks", None)

            exam_result = add_update_exam_result({
                "id": exam_result_id,
                "exam_id": exam_id,
                "student_id": student_id,
                "obtained_marks": obtained_marks
            })

            if exam_result:
                data["exam_result"] = {
                    "id": exam_result.id,
                    "exam_id": exam_result.exam_id,
                    "student_id": exam_result.student_id,
                    "obtained_marks": exam_result.obtained_marks
                }
                data["success"] = True
            else:
                data["exam_result"] = None
                data["success"] = False
        else:
            data["exam_result"] = None
            data["success"] = False
            data["errors"] = "Invalid data format"

    return Response(data)


@api_view(['DELETE'])
def delstu(request):
    data = {}
    if request.method == "DELETE":
        post_data = convert_data(request.body)
        if post_data:
            roll_number = post_data.get("roll_number", None)

            success = delete_student({"roll_number": roll_number})

            data["success"] = success
        else:
            data["success"] = False
            data["errors"] = "Invalid data format"

    return Response(data)

@api_view(['GET'])
def getteach(request):
    data = {}
    if request.method == "GET":
        teacher = Teacher.objects.filter(id=True).values()
        data["teacher"]= teacher
        data["success"]= True

    return Response(data)

@api_view(['GET'])
def getschl(request):
    data={}
    if request.method == "GET":
        school = School.objects.filter(id=True).values()
        data["school"] = school
        data["success"]= True

    return Response(data)