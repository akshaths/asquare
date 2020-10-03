# 'heredoc' is better for formatted text than the string literal
# Assigning my first two days of school calendar into mySchoolCalendar variable 
mySchoolCalendar = '''
Day         Time                    Subject
Monday      7:45am  -  8:50am       Pf
            9:10am  -  10:15am      Math
            10:35am -  11:40am      Science
            12:10pm -  1:15pm       Art
            
Tuesday     9:10am  -  10:15am      ELD
            10:35am -  11:40am      SS
            12:10pm -  1:15pm       ELA
           
           
'''
# printing my school calendar
print(mySchoolCalendar) 

# check if your schedule has Monday
def findMonday(calendar):
    if(calendar.find('Monday') == -1):
        print('Monday is not present')
    else:
        print('Monday is present')


findMonday(mySchoolCalendar)

# printing schedule in upper case ltters
print(mySchoolCalendar.upper())

