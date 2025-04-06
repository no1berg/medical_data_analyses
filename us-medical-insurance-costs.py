# pylint: disable= pointless-string-statement
# |%%--%%| <9ThQ0hjEu2|tNwmeMZmG0>

r"""°°°
# U.S. Medical Insurance Costs
°°°"""

# |%%--%%| <tNwmeMZmG0|yxC2c98IWP>
r"""°°°
## Project Overview
For this project, you will be investigating a medical insurance costs dataset in a .csv file,  
using the Python skills that you have developed.  
This dataset and its parameters will seem familiar if you have,  
done any of the previous Python projects in the data science path

## Project Goals:
Work locally on your own computer  
Import a dataset into your program  
Analyze a dataset by building out functions or class methods  
Use libraries to assist in your analysis  
Optional: Document and organize your findings  
°°°"""
# |%%--%%| <yxC2c98IWP|SfhfwqE3OI>
r"""°°°
## Step 1. Look at the data in *insurance.csv*
°°°"""
# |%%--%%| <SfhfwqE3OI|c4Qq0VYK3F>

# Import csv library
import csv

# Read the insurance.csv file
# with open("insurance.csv", newline="") as insurance_obj:
#     insurance_reader = csv.DictReader(insurance_obj)
#     for row in insurance_reader:
#         print(row)


# |%%--%%| <c4Qq0VYK3F|MFR1uAzWtf>
r"""°°°
Data includes the age, sex, bmi, number of children, smoker status, region, and charges of patients.
Data is stored in a .csv file, using delim = ",".
°°°"""
# |%%--%%| <MFR1uAzWtf|1xE9Ys6jkY>
r"""°°°
## Step 2. Define the scope of the analysis  
Potential Questions:
* What is the average age of the patients?
* What is the average cost (charge) of the patients?
* What is the ratio between the sexes of the patients?
* How does the different variables affect the charge within the dataset?
    * Is there a difference in average charge when grouped by:
        * Sexes?
        * Smoker status?
        * Number of children?
        * NB. These variables are likely confounded!
    * Is there a difference in average BMI when grouped by:
        * Sexes?
        * Smoker status?
        * Number of children?
        * NB. These variables are likely confounded!
°°°"""
# |%%--%%| <1xE9Ys6jkY|UCw8xLwycq>
r"""°°°
## Step 3. Import the *insurance.csv* dataset
°°°"""
# |%%--%%| <UCw8xLwycq|aKwpxSKW3Y>

# Import libraries
import csv

# Read in the insurance.csv file as a file object
# and store {"number": details} in insurance_dict
with open("insurance.csv", newline="") as insurance_csv:
    insurance_reader = csv.DictReader(insurance_csv)
    # Create a dict to store the data in
    insurance_dict = {}
    key = 0
    for row in insurance_reader:
        insurance_dict.update(
            {
                key: {
                    "Age": row["age"],
                    "Sex": row["sex"],
                    "BMI": row["bmi"],
                    "Children": row["children"],
                    "Smoker": row["smoker"],
                    "Region": row["region"],
                    "Charges": row["charges"],
                }
            }
        )
        key += 1

# |%%--%%| <aKwpxSKW3Y|hXZ0UdRdRg>

r"""°°°
## Step 4. Data Analysis

### Step 4.0 Defining Functions

°°°"""
# |%%--%%| <hXZ0UdRdRg|lFz1itt0Ad>


# Create funtion to generate dictionary with key and details
def create_dictionary(data, key):
    """
    Function for reconstructing a dictionary grouped by specified key
    ---
    data = dict
    key = key to group by
    """
    temp_dictionary = {}
    for record in data.values():
        temp_keys = record.keys()
        if key in temp_keys:
            new_key_from_value = record.get(key)
            temp_dictionary.setdefault(new_key_from_value, []).append(record)
    print(f"Created dictionary with {list(temp_dictionary.keys())} as the keys.\n")
    return temp_dictionary


# |%%--%%| <lFz1itt0Ad|DfwlhTKlLN>


# Create function to calculate average charge per group
def calculate_average_charge(data):
    """
    Function for Calculating Average Charge per Group
    ---

    data = Dictionary

    """
    keys_list = list(data.keys())
    charge_by_group = {}
    counter = 0
    for record in data.values():
        total_charge = 0
        total_patients = len(record)
        for details in record:
            charge = float(details.get("Charges"))
            total_charge += charge
        average_charge = total_charge / float(total_patients)
        charge_by_group.setdefault(keys_list[counter], average_charge)
        counter += 1
    return charge_by_group


# |%%--%%| <DfwlhTKlLN|JSkIJcnpsm>


# Create function to calculate average BMI per group
def calculate_average_bmi(data):
    """
    Function for Calculating Average BMI per Group
    ---

    data = Dictionary

    """
    keys_list = list(data.keys())
    bmi_by_group = {}
    counter = 0
    for record in data.values():
        total_bmi = 0
        total_patients = len(record)
        for details in record:
            bmi = float(details.get("BMI"))
            total_bmi += bmi
        average_bmi = total_bmi / float(total_patients)
        bmi_by_group.setdefault(keys_list[counter], average_bmi)
        counter += 1
    return bmi_by_group


# |%%--%%| <JSkIJcnpsm|22ufR3GPdA>
r"""°°°
### Step 4.1 Sexes
Does average charge differ between 'male' and 'female' patients?
°°°"""

# |%%--%%| <22ufR3GPdA|c4RIgMqccp>

# Construct dict with 'Sex' values as keys
insurance_sex_dict = create_dictionary(insurance_dict, "Sex")

# Calculate the per group average of Sexes
PRECISION = 2
average_charges_sexes = calculate_average_charge(insurance_sex_dict)
charge_sexes_dif = abs(average_charges_sexes["female"] - average_charges_sexes["male"])
print(
    f"Female patients average charge: {round(average_charges_sexes['female'], PRECISION)}"
)
print(
    f"Male patients average charge: {round(average_charges_sexes['male'], PRECISION)}"
)
print(f"Difference between sexes: {round(charge_sexes_dif, PRECISION)}")
# |%%--%%| <c4RIgMqccp|t0sR9lhw9O>
r"""°°°
Does average BMI differ between 'male' and 'female' patients?
°°°"""
# |%%--%%| <t0sR9lhw9O|05H7qQsIec>
# Calculate the per group average BMI of Sexes
average_bmi_sexes = calculate_average_bmi(insurance_sex_dict)
bmi_sexes_dif = abs(average_bmi_sexes["female"] - average_bmi_sexes["male"])
print(f"Female patients average BMI: {round(average_bmi_sexes['female'], PRECISION)}")
print(f"Male patients average BMI: {round(average_bmi_sexes['male'], PRECISION)}")
print(f"Difference between sexes: {round(bmi_sexes_dif, PRECISION)}")

# |%%--%%| <05H7qQsIec|MO3Y7R8KcD>
r"""°°°
### Setp 4.2 Smoker Status
°°°"""
# |%%--%%| <MO3Y7R8KcD|6Ms6LGIMTx>

# Construct dict with 'Smoker Status' as keys ('yes', 'no')
insurance_smoker_dict = create_dictionary(insurance_dict, "Smoker")

# Calculate the per group average of Smoker status
average_charges_smokerstatus = calculate_average_charge(insurance_smoker_dict)
charge_smokerstatus_dif = abs(
    average_charges_smokerstatus["yes"] - average_charges_smokerstatus["no"]
)
print(
    f"Smokers average insurance charge: {round(average_charges_smokerstatus['yes'], PRECISION)}"
)
print(
    f"Non-smokers average insurance charge: {round(average_charges_smokerstatus['no'], PRECISION)}"
)
print(
    f"Difference between Smokers and Non-smokers: {round(charge_smokerstatus_dif, PRECISION)}"
)
# |%%--%%| <6Ms6LGIMTx|cX3j53J0mJ>
r"""°°°
Does average BMI differ between Smokers and Non-smokers?
°°°"""
# |%%--%%| <cX3j53J0mJ|qoFnhEhpOv>

# Calculate average BMI per group
average_bmi_smokerstatus = calculate_average_bmi(insurance_smoker_dict)
bmi_smokerstatus_dif = abs(
    average_bmi_smokerstatus["yes"] - average_bmi_smokerstatus["no"]
)
print(
    f"Smoking patients average BMI: {round(average_bmi_smokerstatus['yes'], PRECISION)}"
)
print(
    f"Non-smoking patients average BMI: {round(average_bmi_smokerstatus['no'], PRECISION)}"
)
print(
    f"Difference between smokers and non-smokers: {round(bmi_smokerstatus_dif, PRECISION)}"
)

# |%%--%%| <qoFnhEhpOv|7S76VxcnIP>
r"""°°°
### Step 4.3 Number of Children
Is there a difference in average charge when grouped by number of children?
°°°"""
# |%%--%%| <7S76VxcnIP|uutu6cdBqs>

# Create dict with number of children as the key
insurance_children_dict = create_dictionary(insurance_dict, "Children")

# Calculate average charge per group (number of children per patient)
average_charges_children = calculate_average_charge(insurance_children_dict)
for group in average_charges_children.items():
    print(
        f"Average charge for patients with {group[0]} children: {round(group[1], PRECISION)} "
    )
# |%%--%%| <uutu6cdBqs|Dojmy6JVuv>
r"""°°°
Is there a difference in average BMI when grouped by number of children?
°°°"""
# |%%--%%| <Dojmy6JVuv|jUXgBf7nuL>

# Calculate average BMI per group (number of children)
average_bmi_children = calculate_average_bmi(insurance_children_dict)
for group in average_bmi_children.items():
    print(
        f"Average BMI for patients with {group[0]} children: {round(group[1], PRECISION)}"
    )
