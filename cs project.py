seatlist={}
custdetails={}
import os
import pickle
def password():
         str='csproject'
         i=3
         while i>=0:
                password=raw_input('Enter your password')
                if password==str:
                        break
                else:
                        print 'You have ',i,' more chance'
                        i=i-1
         if i<0:
             exit()
def admin():
        f=open('busdetails','w')
        f1=open('seats','w')
        f2=open('cust','w')
        d={}
        bno=raw_input('Enter bus number: ')
        fr=raw_input('Enter from: ')
        to=raw_input('Enter to: ')
        date=raw_input('Enter date: ')
        time=raw_input('Enter time:')
        amt=input('Enter the amount: ')
        li=[bno,fr,to,date,time,amt]
        pickle.dump(li,f)
        for j in range(0,40):
                seatlist[j]='*'
        pickle.dump(seatlist,f1)
        try:
           pickle.dump(d,f2) 
           
        except WindowsError:
            pass
        f.close()   
def cancel():
        print '\t\t\t\tCANCEL TICKET'
        f2=open('seats','r+')
        r={}
        t=[]
        try :
                
                f=open('cust','r+') 
                seatlist = pickle.load(f2)          
                i=0
                deta=[]
                f.seek(0)               
                r=pickle.load(f)
                idn=input('Enter the ID ')
                try:               
                        
                             if idn in sorted(r.keys()):
                                       deta=r[idn]
                                       print 'Your Details:'
                                       print 'ID :',idn
                                       print 'Name : ',deta[0]
                                       print 'No. of seats booked : ',deta[1]
                                       print 'Seats chosen are : '
                                       while i<deta[1]:
                                                 print deta[2][i],
                                                 i=i+1
                                          
                                       ch2=raw_input('\nAre You Sure You Want To Cancel Ticket(y/n)')
                                       if ch2=='y' or ch2=='Y':
                                                 t=deta[2]
                                                 i=0
                                                 while i<deta[1]:
                                                            seatlist[t[i]-1]='*'
                                                            i=i+1
                                                 del r[idn]
                                                 print '\t\t\tTICKET CANCELLED'
                                                 
                                       else:
                                                 print 'Ticket not cancelled'
                                                 
                             else:   
                                       print 'Invalid ID'
                                       
                except EOFError:
                        print 'Invalid Data'
                        pass
        
                
                f.seek(0)
                pickle.dump(r,f)
                f2.seek(0)
                pickle.dump(seatlist,f2)
                
                f.close() 
        except EOFError:
                print 'Sorry !!No Tickets Booked'
        
                
def bdetails():
        print'\n\n\t\t\t\tBUS AVAILABLE'
        try:
                f=open('busdetails','r')
                c=[]
                c=pickle.load(f)
                print '1.    Bus Number: ',c[0]
                print '\tFrom      : ',c[1]
                print '\tTo        : ',c[2]
                print '\tDate      : ',c[3]
                print '\tTime      : ',c[4]
                print '\tAmount    : Rs.',c[5]
        except EOFError:
                print '\n\t\t\tSorry!! No bus available'
                
        return c[5]
def seat():
        print '\n\n\t\t\tSEATS'
        print '\n\n* - Vacant Seats'
        print '# - Booked Seats'
        print '\nW - Window\n\n'
        f=open('seats','r')
        seatlist=pickle.load(f)
        s=0
        p=0
        for i in range(0,10):
                print 'W    ',
                for j in range(0,4):
                        if seatlist[s]=='*':
                                 p=p+1
                        if j==2:
                                print '\t\t',
                        print s+1,seatlist[s],'\t',
                        s=s+1
                print 'W'       
        
        f.close()
        return p
def book():
        ac=0
        det={}
        print '\n\n\t\t\t\tBOOK TICKET'
        try:
            
            amt=bdetails()
        except IndexError:
            pass
        
        try:
                
                f2=open('cust','r+')
                f3=open('seats','r+')
                seatlist=pickle.load(f3)
                l=[]
                det=pickle.load(f2)
                bname=raw_input('Enter your name') 
                p=seat()
                n=input('Enter the no of seats')
                if n<p:
                        print 'Choose ',n,' seats'
                        seatl=[]
                        k=0
                        while k<n:
                                s=input()
                                if seatlist[s-1]=='#':
                                        print 'Seat already booked'
                                else:
                                        ac=ac*10+s
                                        seatl.insert(k,s)
                                        seatlist[s-1]='#'
                                        k=k+1
                        l.append(bname)
                        l.append(n)                 
                        l.append(seatl)
                        det[ac]=l
                        f2.seek(0)
                        pickle.dump(det,f2)
                
                        print '\n\t\t\tTICKET BOOKED'
                        f3.seek(0)
                        pickle.dump(seatlist,f3)
                        print 'Your Details: '
                        print 'ID : ',ac
                        print 'Name : ',bname
                        print 'No. of seats booked : ',n
                        print 'Seats booked : ',
                        k=0
                        while k<n:
                                print seatl[k],',',
                                k=k+1
                        print '\nAmount : ',n*amt
                        
                else:
                        print 'Sorry ',n,' seats are nor available'
        except EOFError:
                pass
        
print '\n\n\n\n\t\t\t\tWELCOME TO\n\t\t\t  BUS RESERVATION SYSTEM'
while True:
        os.system('cls')
        print '\n\n  \t\t\t\t     MENU'
        print '\n\t\t\t\t1.BOOK TICKET\n\t\t\t\t2.CANCEL TICKET\n\t\t\t\t3.ADMIN\n\t\t\t\t4.EXIT'
        try:
            
            ch=input('\n\t\t\tEnter Your Choice(1/2/3/4)')
            if ch==1:
                    book()
            elif ch==2:
                    cancel()
            elif ch==3:
                    password()
                    admin()
                
                    print '\t\t\t\rCHANGES MADE'
            elif ch==4:
                    print '\n\n\t\t\t    THANKYOU'
                    exit()
            else:
                    print '\n\n\t\t\tEnter a valid choice'
        except NameError:
            print 'Enter a valid choice'
   

        
        



