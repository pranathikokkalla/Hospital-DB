# Hospital-DB

# Our project is based on a hospital database. In this coding phase we have implemented few functional requirements and retrievals.

- At the first stage we are performing 4 operations, insert, delete, update and miscellaneous operations i.e the retrievals part. To perform the insert function,we should type 1. 
In this we have 2 sub functions. Here we need to press 1 to perform the first sub function i.e, inserting a new patient. When we press 1, the command line interface asks for all 
the required inputs like patient id, name, address, issues they are having etc and stores them in the corresponding tables. The information of the patient is stored in a tables called as 
'Patient Info'. The issues that the patients are having are stored ina table named 'Issues'.
- The CLI then asks us whether the patient is getting admitted or not. If yes then we press 1 else 2.
- When we press 1, It asks for some more details like Date of admission and date od discharge and these details are stored in the table named 'Inpatient',bill details in the 'Billing' table,
Treatment details in the 'Hospital stay' table.
- we press 2 instead of 1, the CLI asks to enter the contact number, date of appointment, doctor cost, satff ids of the staff who treat the patient etc. 
All these details are stored in corresponding tables. Contact numbers are stored in 'Contact_number', patient details in 'Outpatient' table, Bill details in Billing table and the treatment details in the treatment table. 

- Now when we choose the second function at the first step, i.e Update function, the command line interface gives us two options. First option updates the salary of a particular employee whose
'Staff Id' will be given by us. For this function to execute, we have to press 1 at the second stage. We could see that the salary of that paticular staff is updated in the 'Staff' table.
The second option that the CLI gives us is, Updating the room cost of a particular room whose Room no and Floor no will be given by the user. Once, we run this function and if there exists a romm
with the given numbers then the cost of the room will be updated to the amount which we enter. We could observe the changes in the Room table.

- Now when we choose the third function at the first step, i.e Delete function, Delete operation will be executed. We have to press 1 at this stage to do so. Now the CLI will ask for the 'Staff Id'
of the staff who has resigned the job. Once we enter a valid Staff Id, that staff with the given Id will be removed from the data base. We could observe that the data related to this particular
staff will be removed from the Staff table and if he is a doctor then his data will be removed from Doctor table and all the patients associated to him will be assigned some other staff.
We should enter the Id of the staff whom we want to assign the patients to. Same thing happens when the staff who has resigned is a Nurse. His/Her data will be completely removed 
from the Staff and Nurse table and His patients will be assigned some other nurse according to the Id entered by the user.



# Retrievals (Misc Functions)
- We have 5 different types of operations in retrievals 
  - 1.Selection
   - 2. Projection
   -  3. Aggregate
   - 4. Search
   - 5. Analysis

#### On entering <b>1</b> we go to <b>Selection</b> operations
In selection operation user is asked the table which must be selected and the user can choose any of the following tables.(give any of thse names as input)

- Room
- Department
- Staff
- Doctor
- Nurse
- Billing
- Patient Info
- Hospital Stay
- Finance1
- Finance2
- Treatment
- Issues
- Inpatient 
- Outpatient
- Contact_number


#### On entering <b>2</b> we go to <b>Projection</b> operations

In projection operation 2 kinds of functions can be performed 
On entering 1 the following function is performed :
1. Inpatients with bill greater than the value entered
(Input the amount with repect to which this function must be performed eg: 30000 )

On entering 2 the following function will be performed:
2. Staff whose salary is greater than the value entered
(Input the amount wtr to which this function must be performed say eg:10000)

#### On entering 3 we go to Aggregate operations

On entering 1 the following function is performed
1. Find out the Department Id that has the maximum Staff 

#### On entering 4 we go to Search operations
On entering 1 the following function is performed:
1. Doctors name  whose name starts with the letter ‘A’ is outputed.
On entering 1 the following function is performed:
2. Bill numbers ending with 1 is outputed .
#### On entering 5 we go to Analysis operations

On entering 1 the following fuction is implemented
1. Inpatients name whose last name starts with the ‘K’ whose bill is greater than the average bill cost is outputed .
