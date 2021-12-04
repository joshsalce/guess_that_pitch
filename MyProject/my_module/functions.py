import random
from random import choice

def outs_plus(seq, code, outs):
    """
    Function that edits sequences that are generated with an
    'Outs +' code
    
    If necessary, when the length is not long enough, random values
    between 1 and 5 are added 
    
    Parameters
    ----------
    seq: list
        The sequence that will have random values between 1 and 5 added if necessary
        The length is checked during the function
    code: str
        Input code that is 
        Used for determining if values must be added to the seq input
    outs: int
        The number of outs in the inning
        Added to the value corresponding to the code input,
        it is checked with the length of the seq input
        
    Returns
    -------
    seq: list
        The original seq input with added numbers if necessary
        
    Source for list comprehensions: https://www.w3schools.com/python/python_lists_comprehension.asp
    Note: I am citing list comprehensions here as the first time I use them, but I will use them later in the project.
    Source for random.choice method: https://www.w3schools.com/python/ref_random_choice.asp
    """
    if code == "Outs + 1":
        added_num = 1
    elif code == "Outs + 2":
        added_num = 2
    elif code == "Outs + 3":
        added_num = 3
        
    # Adds values between 1 and 5 if the length of the input seq is less than the outs plus an added number
    while len(seq) < (outs + added_num):
        seq.append(random.choice([x for x in range(1,6)]))
    return seq


def chase_the_func(seq, num):
    """
    Function that manipulates a value to have in the sequence,
    but not at the end of it.
    
    Parameters
    ----------
    seq: list
        Sequence that is manipulated and split in two
    num: int
        Number that cannot be at the end of the sequence
        
    Returns
    -------
    seq_a: list
        Original sequence manipulated from original form
    
    Source for list comprehension but excluding one value:
    https://www.geeksforgeeks.org/python-generate-random-number-except-k-in-list-2/
    """
    # Splits input seq in two to manipulate them separately
    seq_a = seq[:-1]
    seq_b = seq[-1]
    
    if num == seq_b and num in seq_a:
        # Replaces the value with a new one that cannot be the value being replaced
        seq_b = random.choice([x for x in range(1,6) if x != num])
    elif num == seq_b and num not in seq_a:
        seq_b = random.choice([x for x in range(1,6) if x != num])
        seq_a[random.randint(0,len(seq_a) - 1)] = num
    elif num != seq_b and num not in seq_a:
        # Puts the value replaced from seq_b into a random point in seq_a
        seq_a[random.randint(0,len(seq_a) - 1)] = num
    elif num != seq_b and num in seq_a:
        pass
    
    seq_a.append(seq_b)
    
    return(seq_a)


def edit_values(seq, num):
    """
    Function that edits out a specific value from the input list
    
    Parameters
    ----------
    seq: list
        Sequence that will be manipulated with the num input
    num: int
        The value that will be edited out of the input seq
    Returns
    -------
    seq: list
        The original seq input with the num input edited out
    """
    # Edits out the input num from the input seq
    for val in range(0,len(seq)):
        if seq[val] == num:
            seq[val] = random.choice([x for x in range(1,6) if x != num])
            
    return seq


def second_sign(seq, num):
    """
    Function that manipulates a sequence to have a number in the sequence,
    but not within the last two last values
    
    Parameters
    ----------
    seq: list
        Sequence that is manipulated and split in two
    num: int
        Number that cannot be in the last two values of the sequence
    
    Returns
    -------
    seq_c: list
        The original seq input manipulated, put back together
    """
    # Splits the input seq in two to manipulate separately
    seq_a = seq[:-2]
    seq_b = seq[-2:]
    
    if num in seq_a and num not in seq_b:
        pass
    elif num in seq_a and num in seq_b:
        # Edits out values that need to be replaced 
        edit_values(seq_b, num)
    elif num not in seq_a and num in seq_b:
        # Places value that was edited out from seq_b into seq_a
        seq_a[random.randint(0,len(seq_a) - 1)] = num
        edit_values(seq_b, num)
    elif num not in seq_a and num not in seq_b:
        seq_a[random.randint(0,len(seq_a) - 1)] = num
    
    seq_c = seq_a + seq_b
    
    return(seq_c)


def generate_sequence():
    """
    Function that generates a random sequence between three and five values long
    Each value is any value including and in between 1 and 5
    
    Parameters
    ----------
    None
    
    Returns
    -------
    sequence: list
        List three to five values long
        In the list are values from 1-5
    """
    sequence = []
    
    for number in range(0, random.randint(3,5)):
        sequence.append(random.randint(1,5)) 
    
    return sequence


def edit_sequence(seq, code, outs):
    """
    Function that edits a function to suffice its criteria
    
    'Outs +' codes must be long enough to call the appropriate sign
    'Chase the' codes must not have the specific number at the end
    '2nd Sign' codes must not have the specific number in the last two
    
    Parameters
    ----------
    seq: list
        List that will manipualted depending on the code
    code: str
        Specific code that will cause the sequence to be manipulated
    outs: int
        Number of outs in a specific scenario
        Will only be relevant for 'Outs +' codes
    
    Returns
    -------
    sequence: list
        The seq input that is manipulated according to the code used
    sign: int
        The number from the specific index that must be called,
        dependent on what code is used
    """
    if code == "Outs + 1": 
        sequence = outs_plus(seq, code, outs)
        sign = sequence[outs]
    elif code == "Outs + 2":
        sequence = outs_plus(seq, code, outs)
        sign = sequence[(outs + 1)]
    elif code == "Outs + 3":
        sequence = outs_plus(seq, code, outs)
        sign = sequence[(outs + 2)]
    elif code == "Chase the 1":
        sequence = chase_the_func(seq, 1)
        sign = sequence[(sequence.index(1) + 1)]
    elif code == "Chase the 2":
        sequence = chase_the_func(seq, 2)
        sign = sequence[(sequence.index(2) + 1)]    
    elif code == "Chase the 3":
        sequence = chase_the_func(seq, 3)
        sign = sequence[(sequence.index(3) + 1)]
    elif code == "Chase the 4":
        sequence = chase_the_func(seq, 4)
        sign = sequence[(sequence.index(4) + 1)]
    elif code == "Chase the 5":
        sequence = chase_the_func(seq, 5)
        sign = sequence[(sequence.index(5) + 1)]
    elif code == "2nd Sign After 1":
        sequence = second_sign(seq, 1)
        sign = sequence[(sequence.index(1) + 2)]
    elif code == "2nd Sign After 2":
        sequence = second_sign(seq, 2)
        sign = sequence[(sequence.index(2) + 2)]
    elif code == "2nd Sign After 3":
        sequence = second_sign(seq, 3)
        sign = sequence[(sequence.index(3) + 2)]
    elif code == "2nd Sign After 4":
        sequence = second_sign(seq, 4)
        sign = sequence[(sequence.index(4) + 2)]
    elif code == "2nd Sign After 5":
        sequence = second_sign(seq, 5)
        sign = sequence[(sequence.index(5) + 2)]
    
    return(sequence, sign)


def pitch_call(num):
    """
    Function that calls a pitch based on the num input,
    which codes for the pitch that is thrown
    
    The signs are similar to actual baseball signs:
        1 means Fastball
        2 means Cutter
        3 means Curveball
        4 means Slider
        5 means Changeup
    
    Parameters
    ----------
    num: int
        The number called to be thrown
    
    Returns
    -------
    pitch : str
        What pitch the num input corresponds to
    
    """
    if num == 1:
        pitch = "Fastball"
    elif num == 2:
        pitch = "Cutter"
    elif num == 3:
        pitch = "Curveball"
    elif num == 4:
        pitch = "Slider"
    elif num == 5:
        pitch = "Changeup"
    
    return pitch


def game():
    """
    Function that simulates the guessing game of 
    decoding the signs based off the given sequence
    
    Five codes are taken at random, and sequences are built around them
    The number of outs in the inning also change with each scenario
    
    The player's job is to guess in the input what code is used to 
    generate the sequence they are given
    
    The player is given 10 guesses to guess all of the 5 codes used
    
    Parameters
    ----------
    None
    
    Returns
    -------
    Game Interface, player is allowed to guess which code is used
    for each scenario they are given
    
    """
    # Number of guesses the player has
    guesses = 10
    
    # All of the possible codes that sequences can be made from
    sequences = ["Outs + 1", "Outs + 2", "Outs + 3", "Chase the 1", "Chase the 2", "Chase the 3", "Chase the 4", 
    "Chase the 5", "2nd Sign After 1", "2nd Sign After 2", "2nd Sign After 3","2nd Sign After 4","2nd Sign After 5"]

    # 5 random picks from the sequences list
    codes_to_guess = random.sample(sequences, 5)
    
    all_guessed = False
    
    while guesses > 0:
        # Random choice from the 5 randomly picked sequences 
        code = random.choice(codes_to_guess)
        
        # Number of outs that is generated with each situation
        outs = random.randint(0,2)      
        
        # Sequence built around the code picked from codes_to_guess
        sequence = edit_sequence(generate_sequence(), code, outs)
        
        # Game Interface
        print(f"""
        GUESSING GAME: DECIPHER THE OPPOSING PITCHER'S & CATCHER'S CODES

        Your Scenario
        =============
        You are a runner on 2nd base.
        You have {guesses} guesses remaining
        There are {outs} outs.
        Sequence: {sequence[0]}
        Pitch Thrown: {pitch_call(sequence[1])}
        """)
        
        # Where the player guesses what code was used
        input_code = input("What is the sequence that was used to throw this pitch? ")
        
        # If the player guesses correctly, the code is removed and continues on
        # If the player is incorrect, the player loses a guess and the game continues 
        if input_code.lower() == code.lower():
            codes_to_guess.remove(code)
            if len(codes_to_guess) == 0:
                all_guessed = True
                break
            else:
                print("\nCORRECT")
        else:
            print("\nIncorrect.")
            guesses = guesses - 1
    
    # Only true if all the 5 codes are guessed correctly
    if all_guessed:
        print('\033[1m' + 'WINNER') 
        # Source for the bold font: https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python#17303428
    else:
        print("You failed to guess all of the opposing team's codes. You lose.")