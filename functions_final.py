#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import string
import random


# In[12]:


# These are functions from Assignment3
def is_question(input_string):
    if '?' in input_string:
        output = True
    else:
        output = False
    return output

def remove_punctuation(input_string):
    
    out_string = ''
    
    
    for character in input_string:
        
        
        if character not in string.punctuation:
            out_string = out_string + character
            
    return out_string

def prepare_text(input_string):
    
    temp_string = ''
    out_list = []
    
    for characters in input_string.lower():
        temp_string = temp_string + characters
    
    temp_string = remove_punctuation(temp_string)
    
    for characters in temp_string.split():
        out_list.append(characters)
        
    return out_list

def respond_echo(input_string, number_of_echoes, spacer):
    echo_output = []

    if input_string is not None:
         
        echo_output = (input_string + spacer) * number_of_echoes
    
    else:
        echo_output = None
    return echo_output

def selector(input_list, check_list, return_list):
    
    output = None
    
    for element in input_list:
        if element in check_list:
            
            output = random.choice(return_list)
            
            break
            
    return output

def string_concatenator(string1, string2, separator):
    
    output = string1 + separator + string2
    
    return output

def list_to_string(input_list, separator):
    
    
    output = input_list[0]
    
    for characters in input_list[1:]:
        
        output = string_concatenator(output, characters, separator)
        
    return output

def end_chat(input_list):
    if 'quit' in input_list:
        return True
    else:
        return False
    
def is_in_list(list_one, list_two):
    """Check if any element of list_one is in list_two."""
    
    for element in list_one:
        if element in list_two:
            return True
    return False

def find_in_list(list_one, list_two):
    """Find and return an element from list_one that is in list_two, or None otherwise."""
    
    for element in list_one:
        if element in list_two:
            return element
    return None


# In[13]:


# This is my first function to calculate Body Mass Index(BMI)
def bmi_calculator():
    
    greeting = 'I will help you calculate some body statistics. But I need more information.\n'
    print(greeting)
    
    # Get body information from user
    global height, weight
    height = float(input('Enter your height in meters. '))
    weight = float(input('Enter your weight in kilograms. '))
    
    # the formula of BMI 
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        body_comments = '\nOh no! You are underweight.'
    elif 18.5 <= bmi < 24:
        body_comments = '\nCongrats! You are healthy. Keep it! :)'
    elif 24 <= bmi < 28:
        body_comments = '\nYou are overweight a little bit...'
    else:
        body_comments = "\nThere are some obesity issues :( It's time to lose weight"
        
    print('\nYour body BMI is {0}.'.format(bmi), body_comments)
    


# In[14]:


# This is my fuction to get Basal Metabolic Rate(BMR)
def bmr_calculator():
    
    bmr_intro = "\n\nNow let's calculate Basal Metabolic Rate(BMR) which is the least amount of energy your body need in a day."
    print(bmr_intro)
    
    global gender
    gender = input('Please enter your gender. Type male of female. ')
    age = float(input('Please enter your age: '))
    
    # Here I am using the Harris-Benedict equcation to calculate BMR 
    global bmr
    if gender == 'male':
        bmr = 66.5 + (13.75 * weight) + (5.003 * 100 * height) - (6.755 * age)
    elif gender == 'female':
        bmr = 655.1 + (9.563 * weight) + (1.850 * 100 * height) - (4.676 * age)
    print('You need to injest ', bmr, ' calories a day to keep your body funtioning.')


# In[15]:


# The following codes are to calculate total daily energy expenditure(TDEE).
def tdee_calculator():
     
    tdee_intro = "\n\nIn order to manage you calorie intake, you also have to know your total daily energy expenditure(TDEE).\n"
    print(tdee_intro)
    
    # This is the activity frequecy chart.
    scale_chart = {
    'Grade' : ['A','B','C','D','E'],
    'Frequency' : ['sedentary','light','moderate','active','very active'],
    'Times of exercise' : ['0-1','1-3','4-5','6-7','more than 7']}
    df_choice1 = pd.DataFrame(scale_chart)
    print(df_choice1)
    
    global tdee
    tdee_coefficient = input("\nPlease enter your activity frequency based on the scale above.\nHint: Enter the letter in correspnding 'Grade' column! ")
    if tdee_coefficient == 'A':
        tdee = bmr * 1.2
    elif tdee_coefficient == 'B':
        tdee = bmr * 1.375
    elif tdee_coefficient == 'C':
        tdee = bmr * 1.55
    elif tdee_coefficient == 'D':
        tdee = bmr * 1.725
    elif tdee_coefficient == 'E':
        tdee = bmr * 1.9
    else:
        print('I need a letter between A-E! ')
    print('Your total daily enery expenditure is about ', tdee, ' calories.\n\n')
    
    


# In[16]:


# This function is going to generate some suggetion to users based on preceding information and user's preference
def calories_suggestion():
     
    intro_calories_suggestion = 'Based on aboving data, do you want to change your body shape?\n'
                             
    body_preference = {'choice':['A','B','C'],
              'preference':['Yes! I would like to reduce bodyfat!',
                            'Yes. I want to gain muscle!',
                            'No. I wanna keep my current weight.']}
    df_choice2 = pd.DataFrame(body_preference)
    print(df_choice2)

    user_preference = input('\nMy choice is: ')

    if user_preference == 'A' and gender == 'female':
        print('You should eat ', tdee - 500, ' to ', tdee - 200, ' calories a day.' )
    if user_preference == 'A' and gender == 'male':
        print('You should eat ', tdee - 1000, ' to ', tdee - 500, ' calories a day.' )
    if user_preference == 'B' and gender == 'female':
        print("You'd better eat ", tdee + 300, ' calories a day.')
    if user_preference == 'B' and gender == 'male':
        print("You'd better eat ", tdee + 500, ' calories a day.')
    if user_preference == 'C':
        print('OK! Remember to intake around ', tdee, ' calories every day.')
        


# In[17]:


# This cell defines a collection of input and output things our chatbot can say and respond to.

GREETINGS_IN = ['hello', 'hi', 'hey', 'hola', 'welcome', 'bonjour', 'greetings']
GREETINGS_OUT = ["Hello, it's nice to talk to you!", 'Nice to meet you!',  "Hey - Let's chat!"]

COMP_IN = ['python', 'code', 'computer', 'algorithm', ]
COMP_OUT = ["Python is what I'm made of.",             "Did you know I'm made of code!?",             "Computers are so magical",             "Do you think I'll pass the Turing test?"]

PEOPLE_IN = ['turing', 'hopper', 'neumann', 'lovelace']
PEOPLE_OUT = ['was awesome!', 'did so many important things!', 'is someone you should look up :).']
PEOPLE_NAMES = {'turing': 'Alan', 'hopper': 'Grace', 'neumann': 'John von', 'lovelace': 'Ada'}

JOKES_IN = ['funny', 'hilarious', 'ha', 'haha', 'hahaha', 'lol']
JOKES_OUT = ['ha', 'haha', 'lol'] 

NONO_IN = ['matlab', 'java', 'C++']
NONO_OUT = ["I'm sorry, I don't want to talk about"]

UNKNOWN = ['Good.', 'Okay', 'Huh?', 'Yeah!', 'Thanks!']

QUESTION = "I'm too shy to answer questions. What do you want to talk about?"

STARTBOT = ['start']


# In[18]:


def have_a_chat():
    """Main function to run our chatbot."""
    
    chat = True
    while chat:

        # Get a message from the user
        msg = input('INPUT: \t')
        out_msg = None

        # Check if the input is a question
        question = is_question(msg)

        # Prepare the input message
        msg = prepare_text(msg)

        # Check for an end msg 
        if end_chat(msg):
            out_msg = 'Bye!'
            chat = False

        # Check for a selection of topics that we have defined to respond to
        #   Here, we will check for a series of topics that we have designed to answer to
        if not out_msg:

            # Initialize to collect a list of possible outputs
            outs = []

            # Check if the input looks like a greeting, add a greeting output if so
            outs.append(selector(msg, GREETINGS_IN, GREETINGS_OUT))

            # Check if the input looks like a computer thing, add a computer output if so
            outs.append(selector(msg, COMP_IN, COMP_OUT))

            # Check if the input mentions a person that is specified, add a person output if so
            if is_in_list(msg, PEOPLE_IN):
                name = find_in_list(msg, PEOPLE_IN)
                outs.append(list_to_string([PEOPLE_NAMES[name], name.capitalize(),
                                            selector(msg, PEOPLE_IN, PEOPLE_OUT)], ' '))

            # Check if the input looks like a joke, add a repeat joke output if so
            outs.append(respond_echo(selector(msg, JOKES_IN, JOKES_OUT), 3, ''))

            # Check if the input has some words we don't want to talk about, say that, if so
            if is_in_list(msg, NONO_IN):
                outs.append(list_to_string([selector(msg, NONO_IN, NONO_OUT), find_in_list(msg, NONO_IN)], ' '))

            # IF YOU WANTED TO ADD MORE TOPICS TO RESPOND TO, YOU COULD ADD THEM IN HERE

            # We could have selected multiple outputs from the topic search above (if multiple return possible outputs)
            #   We also might have appended None in some cases, meaning we don't have a reply
            #   To deal with this, we are going to randomly select an output from the set of outputs that are not None
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)

        # If we don't have an output yet, but the input was a question, return msg related to it being a question
        if not out_msg and question:
            out_msg = QUESTION

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(UNKNOWN)
            
        if(is_in_list(msg, STARTBOT)):
            bmi_calculator()
            bmr_calculator()
            tdee_calculator()
            calories_suggestion()

        print('OUTPUT:', out_msg)


# In[19]:


have_a_chat()

