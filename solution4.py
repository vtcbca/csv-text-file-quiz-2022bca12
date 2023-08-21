#Create salary.csv file which contain sid,sname,salary.
#Display the employee record whose name begins from "S" also show no. of employee with first letter "S‟ out of total record.
import csv
with open("salary.csv",'r',newline='')as f:
     data=csv.writer(f)
     header=['sid','sname','salary']
     record=[[1,'om',4000],
            [2,'sai',4500],
            [3,'ram',4200],
            [4,'parthvi',3000],
            [5,'krishna',2500]]
     data.writerow(header)
     data.writerows(record)
     data=csv.reader(f)
     for i in data :
         print(i)




               

    
    
    
    


    
    

    
    
               
          
