def numbertoordinal(number):
    if number < 0 or number > 10001:
        return None
      
    if number < 20:
        if number < 10:
            if number == 0:
                suffix =''
            elif number == 1: 
                suffix = 'st'
            elif number == 2:
                suffix = 'nd'
            elif number == 3:
                suffix = 'rd'
            else:
                suffix = 'th' 
        else:
            suffix = 'th' 

    else:
        tens = str(number)
        tens = tens[-2]
        unit = str(number)
        unit = unit[-1]
        if tens == "1":
           suffix = "th"
        else:
            if unit == "1": 
                suffix = 'st'
            elif unit == "2":
                suffix = 'nd'
            elif unit == "3":
                suffix = 'rd'
            else:
                suffix = 'th'
    return str(number)+ suffix
print(numbertoordinal(20))
