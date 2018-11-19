path=r"C:\Users\sandra.mathew\djangoWorkspace\fresh\media\Doc\/"
        finalarray = []
        with open (path+name) as f:
            print("hhhhh...........")
            text = f.read()
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
                    
                    if m[0].find("Student First Name") != -1 or m[0].find("Student Middle Initial") != -1 or m[0].find("Student Last Name") != -1 or m[0].find("Student Street Address 1") != -1 or m[0].find("Student City") != -1 or m[0].find("Student State Code") != -1 or m[0].find("Student Zip Code") != -1 or m[0].find("Student Home Phone Country Code") != -1 or  m[0].find("Student Work Phone Country Code") != -1 or m[0].find("Student Cell Phone Country Code") != -1 or m[0].find("Student Home Phone Number") != -1 or m[0].find("Student Work Phone Number") != -1 or m[0].find("Student Cell Phone Number") != -1:
                        m[0]=m[0].replace(" ","")
                        
                        m[1]=m[1].strip()
                        if m[1] == '':
                            returnobj[m[0]]='Null'
                        else:
                            returnobj[m[0]]=m[1]

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
                    final["studentDetails"] = json.dumps(returnobj)
                    returnobj.clear()
                
                else:
                    finalarray.extend([returnobj])
                    q=q+1
                    # returnobj.clear()

                i=i+1
    
        final["Loans"] = json.dumps(finalarray)
            
        finalresult = json.dumps(final)
        print(finalresult)