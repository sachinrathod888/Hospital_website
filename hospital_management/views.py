from django.shortcuts import render, redirect
from .models import Myuser, PatientInfoNew
from django.http import HttpResponse, FileResponse
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.db.models import Q




def home(request):
    return render(request,'home.html',{'title':"Home Page"})


def render_pdf_view(request,id):
    patient = PatientInfoNew.objects.get(id=id)
    template_path = 'pdf_invoice.html'
    context = {'patient':patient}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="patientreport.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



def newinvoice(request,id):
    email = request.session['email']
    if email is not None:
        viewlist = PatientInfoNew.objects.get(id=id)
        return render(request,'index.html',{'title':'patient view','patient':viewlist})
    else:
        return render(request,'patientrecord.html',{'title':'patient list'})

    


def AddPatient(request):
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        address = request.POST.get('address')
        complaint = request.POST.get('complaint')
        pulse = request.POST.get('pulse')
        bp = request.POST.get('bp')
        temprature = request.POST.get('temprature')
        bsl = request.POST.get('bsl')
        general_exam = request.POST.get('general_exam')
        medicin_type = request.POST.get('medicin_type')
        medicin_name = request.POST.get('medicin_name')
        medicin = request.POST.get('medicine')
        unit = request.POST.get('unit')
        medicin_type2 = request.POST.get('medicin_type2')
        medicin_name2 = request.POST.get('medicin_name2')
        medicin2 = request.POST.get('medicine_detail2')
        unit2 = request.POST.get('unit2')
        medicin_type3 = request.POST.get('medicin_type3')
        medicin_name3 = request.POST.get('medicin_name3')
        medicin3 = request.POST.get('medicine_detail3')
        unit3 = request.POST.get('unit3')
        medicin_type4 = request.POST.get('medicin_type4')
        medicin_name4 = request.POST.get('medicin_name4')
        medicin4 = request.POST.get('medicine_detail4')
        unit4 = request.POST.get('unit4')
        medicin_type5 = request.POST.get('medicin_type5')
        medicin_name5 = request.POST.get('medicin_name5')
        medicin5 = request.POST.get('medicine_detail5')
        unit5 = request.POST.get('unit5')
        other_info = request.POST.get('other_info')
        total_bill = request.POST.get('total_amount')


        
        patient = PatientInfoNew(Patient_name=patient_name,email=email,mobile=mobile,gender=gender,age=age,address=address,complaint=complaint,pulse=pulse,bp=bp,temprature=temprature,bsl=bsl,general_exam=general_exam,medicine_type1=medicin_type,medicine_name1=medicin_name,medicine_detail1=medicin,medicine_units1=unit,medicine_type2=medicin_type2,medicine_name2=medicin_name2,medicine_detail2=medicin2,medicine_units2=unit2,medicine_type3=medicin_type3,medicine_name3=medicin_name3,medicin_detail3=medicin3,medicine_units3=unit3,medicine_type4=medicin_type4,medicine_name4=medicin_name4,medicine_detail4=medicin4,medicine_units4=unit4,medicine_type5=medicin_type5,medicine_name5=medicin_name5,medicine_detail5=medicin5,medicine_units5=unit5,other_information=other_info,total_bill=total_bill)

        patient.save()
        
        return render(request,'home.html',{'title':'Add Patient','result':'Patient Added Successfully'})
    else:
    
        return render(request,'NewPatient.html',{'title':"Add Patient"})
    

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if len(email)==0:
            return render(request,'login.html',{'title':"Login failed",'error':'email required'})
        elif len(password)==0:
            return render(request,'login.html',{'title':"Login failed",'error':'password required'})
        else:
            try:
                
                result = Myuser.objects.filter(email=email,password=password)
                
                if result is not None:
                    request.session['email']=email
                    return render(request,'home.html',{'title':'Home Page'})

            except Myuser.DoesNotExist:
                return render(request,'login.html',{'title':"Login failed",'error':'email or password is incorrect'})
    else:
        return render(request,'login.html',{'title':"Login Page"})

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')


        user = Myuser(name=name,email=email,password=password,mobile=mobile)
        user.save()

        return render(request,'home.html',{'title':'home page','result':'success'})
    else:
        return render(request,'signup.html',{'title':"Signup page"})

def PatientRecord(request):
    try:
        email = request.session['email']
        if email is not None:
            if 'q' in request.GET:
                q = request.GET['q']
                data = PatientInfoNew.objects.filter(Q(Patient_name__icontains=q)|Q(mobile__icontains=q))
                return render(request,'patientrecord.html',{'title':'patient list','patientdata':data})
            allPatient = PatientInfoNew.objects.all()
            return render(request,'patientrecord.html',{'title':'patient list','patientdata':allPatient})
        else:
            return render(request,'login.html',{'title':'Login Page'})
    except:
        return render(request,'login.html',{'title':'Login Page'})


def update_data(request, id):
    allPatient = PatientInfoNew.objects.get(pk=id)
    
    if request.method == 'POST':
            
        patient_name = request.POST.get('patient_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        address = request.POST.get('address')
        complaint = request.POST.get('complaint')
        pulse = request.POST.get('pulse')
        bp = request.POST.get('bp')
        temprature = request.POST.get('temprature')
        bsl = request.POST.get('bsl')
        general_exam = request.POST.get('general_exam')
        medicin_type = request.POST.get('medicin_type')
        medicin_name = request.POST.get('medicin_name')
        medicin = request.POST.get('medicine')
        unit = request.POST.get('unit')
        medicin_type2 = request.POST.get('medicin_type2')
        medicin_name2 = request.POST.get('medicin_name2')
        medicin2 = request.POST.get('medicine_detail2')
        unit2 = request.POST.get('unit2')
        medicin_type3 = request.POST.get('medicin_type3')
        medicin_name3 = request.POST.get('medicin_name3')
        medicin3 = request.POST.get('medicine_detail3')
        unit3 = request.POST.get('unit3')
        medicin_type4 = request.POST.get('medicin_type4')
        medicin_name4 = request.POST.get('medicin_name4')
        medicin4 = request.POST.get('medicine_detail4')
        unit4 = request.POST.get('unit4')
        medicin_type5 = request.POST.get('medicin_type5')
        medicin_name5 = request.POST.get('medicin_name5')
        medicin5 = request.POST.get('medicine_detail5')
        unit5 = request.POST.get('unit5')
        other_info = request.POST.get('other_info')
        total_bill = request.POST.get('total_amount')


        patient = PatientInfoNew(id=id,Patient_name=patient_name,email=email,mobile=mobile,gender=gender,age=age,address=address,complaint=complaint,pulse=pulse,bp=bp,temprature=temprature,bsl=bsl,general_exam=general_exam,medicine_type1=medicin_type,medicine_name1=medicin_name,medicine_detail1=medicin,medicine_units1=unit,medicine_type2=medicin_type2,medicine_name2=medicin_name2,medicine_detail2=medicin2,medicine_units2=unit2,medicine_type3=medicin_type3,medicine_name3=medicin_name3,medicin_detail3=medicin3,medicine_units3=unit3,medicine_type4=medicin_type4,medicine_name4=medicin_name4,medicine_detail4=medicin4,medicine_units4=unit4,medicine_type5=medicin_type5,medicine_name5=medicin_name5,medicine_detail5=medicin5,medicine_units5=unit5,other_information=other_info,total_bill=total_bill)


        

        patient.save()
        patient = PatientInfoNew.objects.all()
        return render(request,'patientrecord.html',{'title':'Patient Record','msg':'Data Updated Successfully!!!','patientdata': patient})
    else:
        return render(request,'Update_data.html',{"title":'Update data','patient':allPatient})
    

def delete_data(request,id):
    
    stu = PatientInfoNew.objects.get(id=id)
    stu.delete()
    allPatient = PatientInfoNew.objects.all()

    return render(request,'patientrecord.html',{'title':'patient record','patient':allPatient})

        
def view(request,id):
    email = request.session['email']
    if email is not None:
        viewlist = PatientInfoNew.objects.get(id=id)
        return render(request,'pdf_invoice.html',{'title':'patient view','patient':viewlist})
    else:
        return render(request,'patientrecord.html',{'title':'patient list'})



def logout(request):
    try:
        del request.session['email']
        return render(request,'home.html',{'title':'home page'})
    except:
        return render(request,'home.html',{'title':'home page'})
