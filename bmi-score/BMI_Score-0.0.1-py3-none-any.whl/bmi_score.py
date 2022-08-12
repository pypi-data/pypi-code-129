def bmi (height, weight):
    global final_bmi_score

    #Exception handling
    ##TypeError
    if not ((isinstance(height, int)) and (isinstance(weight,int))):
        return "String not supported:\nAgument 1 = Height in centimeters\nAgument 2 = Weight in kilograms"
 
    user_height = height / 100
    bmi = weight/(user_height**2)

    #Converting bmi value to string then to list
    bmi = str(bmi) 
    bmi_list = list(bmi) 

    # Deleting every number after 3/4 index
    del bmi_list[4:] 

    #Converting list back to string 
    final_bmi_score = "".join(bmi_list)
    return final_bmi_score


def bmi_information (final_bmi_score):
    if final_bmi_score < "18.5" :
        return "You're in the underweight range"
    elif final_bmi_score >= "18.5" and final_bmi_score <= "24.9":
        return "You're in the healthy weight range"
    elif final_bmi_score >= "25" and final_bmi_score <= "29.9":
        return "You're in the overweight range"
    else:
        return "You're in the obese range"



