# DATA 533 Assignment 2: Health Manager documentation

## Subpackage doctor

### Module adddoc

**Class doctor**  
- Creates an instance of a doctor, with parameters name, number of current patients, and maximum number of patients.

**Class specialist**
- Creates an instance of a specialist, utilizing parent class doctor to create all parameters with the exception of specialty.
- Method **newp** evaluates if a specialist is accepting new patients.  If they are, the number of current patients is increased by one and the patient is accepted.  Otherwise, an option is presented to join a waitlist.
- Method **waitlist** adds a patient to the wait list and returns their current position in the waitlist and the anticipated waiting time, assuming 4 new patients join per month.

### Module doctordb

**Function db_entry**
- Accepts both a pandas dataframe and an instance of specialist, and returns the updated dataframe.
- The dataframe serves as a database that can later be queried.

**Function doc_search**
- Accepts a dataframe and a specialization and queries the dataframe to see if any physicians match the desired specialist.
- If there are no doctors matching the specialization, a message is returned.
- If there is a match, a list of doctors matching the specialization is returned.

## Subpackage medmgr

### Module medls

**Class Medication**  
- Creates an instance of Medication, with parameters name, dose, and frequency.
- Method **medCount** displays the number of instances of Medication that have been created.
- Method **display** displays the instance of Medication being queried in a simple ASCII table format.
- Method **displayAll** displays the full list of medications in a simple ASCII table format.  
- Class attribute **count** keeps track of the number of instances of Medication created.
- Class attribute **medList** keeps track of the attributes associated with each instance (ie. name, dose and frequency).

**Class Antibiotic**
- Creates an instance of Antibiotic, with parent class Medication.
- A parameter duration is added, in addition to the parameters belonging to Medication.
- Method **abxCount** displays the number of instances of Medication that have been created.
- Method **display** displays the Antibiotic instance being queried in an ASCII table format including antibiotic duration.

### Module insdose
Performs basic insulin dose calculations.

**Function bbdosing**
- Estimates the total daily insulin dose and the basal insulin dose based on weight in kg.

**Function carbratio**
- Uses the "Rule of 500" to estimate the insulin to carbohydrate ratio using the total daily insulin dose.

**Function cfact**
- Uses the "100 Rule for Rapid Acting Insulin" to estimate the correction factor/dose of insulin.

**Function carbcorr**
- Estimates the carbohydrate correction dose based on the number of carbohydrates to be consumed in grams and the known insulin to carbohydrate ratio.
