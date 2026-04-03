from django.shortcuts import render, redirect
from .models import Questions, Student_info, Result


# ---------------- LOGIN ----------------
def Login(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        try:
            user = Student_info.objects.get(username=username, password=password)

            request.session['user'] = username

            return redirect('/subject/')

        except:
            return render(request,'Student/login.html',{'msg':'Invalid Username or Password'})

    return render(request,'Student/login.html')


# ---------------- LOGOUT ----------------
def Logout(request):
    request.session.flush()
    return redirect('/login/')


# ---------------- SUBJECT ----------------
def Selectsubject(request):

    if 'user' not in request.session:
        return redirect('/login/')

    return render(request,'Question/subject.html')


def Starttest(request, subject):

    if 'user' not in request.session:
        return redirect('/login/')

    questions = list(Questions.objects.filter(subject__iexact=subject))

    if len(questions) == 0:
        return redirect('/subject/')

    if 'index' not in request.session:
        request.session['index'] = 0
        request.session['score'] = 0
        request.session['answers'] = []

    index = request.session['index']


    if index >= len(questions):

        score = request.session.get('score', 0)
        answers = request.session.get('answers', [])
        username = request.session.get('user')

        # SAVE RESULT with foreign 
        if username:
            try: 
                user_obj = Student_info.objects.get(username=username)

                Result.objects.create(
                    user=user_obj,
                    subject=subject,
                    score=score
                )
            except:
                pass

        # clear session
        request.session.pop('index', None)
        request.session.pop('score', None)
        request.session.pop('answers', None)

        return render(request,'Result/score.html',{'score':score, 'answers':answers})

    # ---------------- NEXT QUESTION ----------------
    q = questions[index]

    if request.method == "POST":

        selected = request.POST.get('answer')

        if not selected:
            return render(request,'Question/starttest.html',{'q':q, 'msg':'Please select an option'})

        answers = request.session['answers']

        answers.append({
            'question': q.qtext,
            'selected': selected,
            'correct': q.correct_ans
        })

        request.session['answers'] = answers

        if selected == q.correct_ans:
            request.session['score'] += 1

        request.session['index'] += 1

        return redirect(f'/starttest/{subject}/')

    return render(request,'Question/starttest.html',{'q':q})


# ---------------- QUESTIONS ----------------
def Addquestion(request):
    return render(request,'Question/addquestion.html')


def Addquestioncurd(request):

    if request.method == "POST":

        Questions.objects.create(
            qtext=request.POST['qtext'],
            op1=request.POST['op1'],
            op2=request.POST['op2'],
            op3=request.POST['op3'],
            op4=request.POST['op4'],
            correct_ans=request.POST['correct_ans'],
            subject=request.POST['subject']
        )

    return render(request,'Question/questioncurd.html')


def Showallquestions(request):

    data = Questions.objects.all()

    return render(request,'Question/showallquestions.html',{'data':data})


def Viewquestion(request, id):

    q = Questions.objects.get(qid=id)

    return render(request,'Question/viewquestion.html',{'q':q})


def Deletequestion(request, id):

    q = Questions.objects.get(qid=id)
    q.delete()

    return redirect('/showquestions/')


# ---------------- UPDATE QUESTION ----------------
def Viewupdatepage(request, id):

    q = Questions.objects.get(qid=id)

    return render(request,'Question/updatequestion.html',{'q':q})


def Updatequestioncurd(request, id):

    q = Questions.objects.get(qid=id)

    if request.method == "POST":

        q.qtext = request.POST['qtext']
        q.op1 = request.POST['op1']
        q.op2 = request.POST['op2']
        q.op3 = request.POST['op3']
        q.op4 = request.POST['op4']
        q.correct_ans = request.POST['correct_ans']
        q.subject = request.POST['subject']

        q.save()

    return redirect('/showquestions/')


# ---------------- STUDENT ----------------
def Addstudent(request):
    return render(request,'Student/addstudent.html')


def Addstudentcurd(request):

    if request.method == "POST":

        Student_info.objects.create(
            username=request.POST['username'],
            password=request.POST['password'],
            mobno=request.POST['mobno']
        )

    return render(request,'Student/studentcurd.html')


def Viewstudent(request, id):

    s = Student_info.objects.get(id=id)

    return render(request,'Student/viewstudent.html',{'s':s})


# ---------------- VIEW RESULTS ----------------
def Viewresults(request):

    if 'user' not in request.session:
        return redirect('/login/')

    username = request.session['user']

    try:
        user_obj = Student_info.objects.get(username=username)
        data = Result.objects.filter(user=user_obj)
    except:
        data = []

    return render(request,'Result/viewresults.html',{'data':data})


# ---------------- END TEST ----------------
def Endtest(request):
    return render(request,'Result/score.html')