class Student():
    def __init__(self, name=None, last_name=None, email=None, age=None, telephone=None, interest_courses=None, student_id=None,
                 education=None, started_studying_to_ENEM=None, public_school=None, school_evaluation=None, times_exam_taken=None,
                 daily_time_of_dedication=None, gender=None, family_income=None, cep=None, city=None, state=None, source_of_online_study=None,
                 guardian_name=None, guardian_email=None, guardian_telephone=None, favorite_school_subject=None):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.telephone = telephone
        self.guardian_name = guardian_name
        self.guardian_email = guardian_email
        self.guardian_telephone = guardian_telephone
        self.age = age
        self.gender = gender
        self.cep = cep
        self.city = city
        self.state = state
        self.student_id = student_id
        self.interest_courses = interest_courses
        self.favorite_school_subject = favorite_school_subject
        self.education = education
        self.started_studying_to_ENEM = started_studying_to_ENEM
        self.public_school = public_school
        self.school_evaluation = school_evaluation
        self.times_exam_taken = times_exam_taken
        self.daily_time_of_dedication = daily_time_of_dedication
        self.family_income = family_income
        self.source_of_online_study = source_of_online_study

    def jsonify(obj):
        result = dict()
        if 'name' in obj.keys():
            result['name'] = obj['name']

        if 'last_name' in obj.keys():
            result['last_name'] = obj['last_name']

        if 'email' in obj.keys():
                result['email'] = obj['email']

        if 'telephone' in obj.keys():
            result['telephone'] = obj['telephone']

        if 'guardian_name' in obj.keys():
            result['guardian_name'] = obj['guardian_name']

        if 'guardian_email' in obj.keys():
                result['guardian_email'] = obj['guardian_email']

        if 'guardian_telephone' in obj.keys():
            result['guardian_telephone'] = obj['guardian_telephone']

        if 'age' in obj.keys():
            result['age'] = obj['age']

        if 'gender' in obj.keys():
            result['gender'] = obj['gender']

        if 'cep' in obj.keys():
            result['cep'] = obj['cep']

        if 'city' in obj.keys():
            result['city'] = obj['city']

        if 'student_id' in obj.keys():
            result['student_id'] = obj['student_id']

        if 'state' in obj.keys():
            result['state'] = obj['state']

        if 'favorite_school_subject' in obj.keys():
            result['favorite_school_subject'] = obj['favorite_school_subject']

        if 'interest_course' in obj.keys():
            result['interest_course'] = obj['interest_course']

        if 'education' in obj.keys():
            result['education'] = obj['education']

        if 'started_studying_to_ENEM' in obj.keys():
            result['started_studying_to_ENEM'] = obj['started_studying_to_ENEM']

        if 'public_school' in obj.keys():
            result['public_school'] = obj['public_school']

        if 'school_evaluation' in obj.keys():
            result['school_evaluation'] = obj['school_evaluation']

        if 'times_exam_taken' in obj.keys():
            result['times_exam_taken'] = obj['times_exam_taken']

        if 'daily_time_of_dedication' in obj.keys():
            result['daily_time_of_dedication'] = obj['daily_time_of_dedication']

        if 'family_income' in obj.keys():
            result['family_income'] = obj['family_income']

        if 'source_of_online_study' in obj.keys():
            result['source_of_online_study'] = obj['source_of_online_study']

        return result
