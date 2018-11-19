from django.shortcuts import render
from .forms import ContactForm
from uploader.models import UploadForm,Upload
from django.http import HttpResponseRedirect
from django.urls import reverse
import time, json
# Create your views here.

final = {}
result = {}

def home(request):
    name = 'san'
    # if request.method=="POST":
    doc = UploadForm(request.POST, request.FILES) 
    print(doc)
    doc_file = str(request.FILES)
    print(doc_file)
    if doc_file != "<MultiValueDict: {}>":
        spliting = doc_file.split(" ")
        print(spliting[3])
        name = str(spliting[3])
        print("before docs...........")
        print(name)
        if doc.is_valid():
            doc.save()  
            # return HttpResponseRedirect(reverse('imageupload'))
        path=r'.\media\Doc'
        v=str('\\')
        name=v+name
    
        finalarray = []
        LoanCount = 0
        LoanCountArray = []
      
        print(path)
        # with open ('.\media\Doc\hello.txt','r') as f:
        with open (path+name,'r') as f:
            print("hhhhh...........")
            text = f.read()
            # print(text)
            para = text.split("Loan Type")
            x=len(para)
            i=0
            q=0
            while(x>0):
            # while(q>0):
                returnobj = {}
                line = para[i].split("\n")
                l=0
                l=len(line)
                j=0
                f1=0
                f2=0
        
                while(l>0):
                    m = line[j].split(":")
                    
                    if m[0].find("Student First Name") != -1: 
                        m[0]=m[0].replace(" ","")
                        
                        m[1]=m[1].strip()
                        if m[1] == '':
                            returnobj[m[0]]='Null'
                            StudentFirstName = 'Null'
                        else:
                            returnobj[m[0]]=m[1]
                            StudentFirstName = m[1]

                    elif m[0].find("Student Middle Initial") != -1:
                        m[0]=m[0].replace(" ","")
                        
                        m[1]=m[1].strip()
                        if m[1] == '':
                            StudentMiddleInitial = 'Null'
                        else:
                            StudentMiddleInitial = m[1] 

                    elif m[0].find("Student Last Name") != -1:
                        m[0]=m[0].replace(" ","")
                        
                        m[1]=m[1].strip()
                        if m[1] == '':
                            StudentLastName = 'Null'
                        else:
                            StudentLastName = m[1]
                        
                        
                    elif m[0].find("Student Street Address 1") != -1:
                        m[0]=m[0].replace(" ","")
                        
                        m[1]=m[1].strip()
                        if m[1] == '':
                            StudentStreetAddress = 'Null'
                        else:
                            StudentStreetAddress = m[1]
                    
                    elif m[0].find("Student City") != -1:
                        m[0]=m[0].replace(" ","")
                        
                        m[1]=m[1].strip()
                        if m[1] == '':
                            StudentCity = 'Null'
                        else:
                            StudentCity = m[1]
                        
                    elif m[0].find("Student State Code") != -1:
                        m[0]=m[0].replace(" ","")
                        
                        m[1]=m[1].strip()
                        if m[1] == '':
                            StudentStateCode = 'Null'
                        else:
                            StudentStateCode = m[1]

                    elif m[0].find("Student Zip Code") != -1:
                        m[0]=m[0].replace(" ","")
                        
                        m[1]=m[1].strip()
                        if m[1] == '':
                            StudentZipCode = 'Null'
                        else:
                            StudentZipCode = m[1]

                    elif m[0].find("Student Home Phone Country Code") != -1:
                        m[0]=m[0].replace(" ","")
                        
                        m[1]=m[1].strip()
                        if m[1] == '':
                            StudentHomePhoneCountryCode = 'Null'
                        else:
                            StudentHomePhoneCountryCode = m[1]

                    elif m[0].find("Student Work Phone Country Code") != -1:
                        m[0]=m[0].replace(" ","")
                        
                        m[1]=m[1].strip()
                        if m[1] == '':
                            StudentWorkPhoneCountryCode = 'Null'
                        else:
                            StudentWorkPhoneCountryCode = m[1]

                    elif m[0].find("Student Cell Phone Country Code") != -1:
                        m[0]=m[0].replace(" ","")
                        
                        m[1]=m[1].strip()
                        if m[1] == '':
                            StudentCellPhoneCountryCode = 'Null'
                        else:
                            StudentCellPhoneCountryCode = m[1]

                    elif m[0].find("Student Home Phone Number") != -1:
                        m[0]=m[0].replace(" ","")
                        
                        m[1]=m[1].strip()
                        if m[1] == '':
                            StudentHomePhoneNumber = 'Null'
                        else:
                            StudentHomePhoneNumber = m[1]

                    elif m[0].find("Student Work Phone Number") != -1:
                        m[0]=m[0].replace(" ","")
                        
                        m[1]=m[1].strip()
                        if m[1] == '':
                            StudentWorkPhoneNumber = 'Null'
                        else:
                            StudentWorkPhoneNumber = m[1]

                    elif m[0].find("Student Cell Phone Number") != -1:
                        m[0]=m[0].replace(" ","")
                        
                        m[1]=m[1].strip()
                        if m[1] == '':
                            StudentCellPhoneNumber = 'Null'
                        else:
                            StudentCellPhoneNumber = m[1]
                            
                    elif m[0].find("Loan Outstanding Principal Balance") != -1 or m[0].find("Loan Outstanding Interest Balance") != -1 or m[0].find("Loan Interest Rate") != -1 or m[0].find("Loan Date") != -1 or m[0].find("Loan Canceled Date") != -1 or m[0].find("Loan Canceled Amount") != -1 or m[0].find("Loan Contact Name") != -1 or m[0].find("Student Cell Phone Country Code") != -1 or m[0].find("Loan Repayment Plan Type") != -1:
                        m[0]=m[0].replace(" ","")
                        m[1]=m[1].strip()
                        if m[1] == '':
                            returnobj[m[0]]='Null'
                        else:
                            returnobj[m[0]]=m[1]

                    elif m[0].find("Loan Status Description") != -1 and f1 == 0:
                        m[0]=m[0].replace(" ","")
                        m[1]=m[1].strip()
                        if m[1] == '':
                            returnobj[m[0]]='Null'
                        else:
                            returnobj[m[0]]=m[1]
                        f1=1

                    elif m[0].find("Loan Status Effective Date") != -1 and f2 == 0:
                        m[0]=m[0].replace(" ","")
                        m[1]=m[1].strip()
                        if m[1] == '':
                            returnobj[m[0]]='Null'
                        else:
                            returnobj[m[0]]=m[1]
                        f2=1

                    elif len(m[0]) == 0 and len(m) != 1:
            
                        m[1]=m[1].strip()
                        # if m[1] == '':
                        #     returnobj["Loan type"]='Null'
                        # else:
                        returnobj["LoanType"]=m[1]

                    j=j+1
                    l=l-1
                    
                x=x-1
        
                if i == 0:
                    # final["studentDetails"] = result
                    # final["studentDetails"] = json.dumps(returnobj)
                    # returnobj.clear()
                    pass
                
                else:
                    finalarray.extend([returnobj])
                    q=q+1
                    LoanCount = LoanCount + 1
                    LoanCountArray.extend([LoanCount])
                    # returnobj.clear()

                i=i+1
    
        final["Loans"] = json.dumps(finalarray)    
        finalresult = json.dumps(final)
        print(type(finalresult))
        return render(request,'home.html',{'Doc':StudentFirstName, 'StudentMiddleInitial':StudentMiddleInitial, 'StudentLastName':StudentLastName, 'StudentStreetAddress':StudentStreetAddress, 'StudentCity':StudentCity, 'StudentStateCode':StudentStateCode, 'StudentZipCode':StudentZipCode, 'StudentHomePhoneCountryCode':StudentHomePhoneCountryCode, 'StudentWorkPhoneCountryCode':StudentWorkPhoneCountryCode, 'StudentCellPhoneCountryCode':StudentCellPhoneCountryCode, 'StudentHomePhoneNumber':StudentHomePhoneNumber, 'StudentWorkPhoneNumber':StudentWorkPhoneNumber, 'StudentCellPhoneNumber':StudentCellPhoneNumber, 'final':finalarray, 'LoanCount':LoanCountArray})
    docs=Upload.objects.all().order_by('-upload_date')
    return render(request,'home.html',{'form':doc,'Doc':docs})
    

