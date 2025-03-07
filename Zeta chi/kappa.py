# Lisa Rehm, Kappa project

    ## Look for *executive decision* to see things that need to be thought out more

# Welcome to the program...

# Did you want this to be beginner, intermediate, or advanced?
# If user input = beginner call beginner function... etc.

# Do you want to start with grammer, vocabulary...etc?
# If user input = grammer call grammer function...etc

## Grammer function
    # *executive decision* Will I ask the user which piece they want to do first, or give it to them in order? What if they don't want to answer a certain thing yet? How can I give them an updated list of things to choose from that doesn't include things they've already done? Perhaps if input = null then print in user input statement. Perhaps it has to be in a certain order or I can have a recommended order.

    # Sentence structure
        # SVO, SOV, VOS, VSO, etc. provide examples (would you like to see examples for any?) and advice on which is best (would you like advice for which one to choose?). This advice should include reasons for different ones, such as SOV being the most common but others potentialy providing different meanings, etc.
    # Word order



## Vocab function
    # Remind them that spelling and pronounciation do not always go hand in hand. Until later, this program will offer spelling only and they can choose how to pronounce things. Later on there will be options to have pronounciation rules added.
    # Introduce IPA and especially vowels, so the user knows that this 'ai' is one vowel, not two
    # Sonority sequencing principle:
        # Give instructions on how to find numbers, allow all real numbers from 0 to 10

    # ai = input("How frequent do you want 'a' to be?\n") #Make this a function where 'letter' equals variable name?
    # bi = input("How frequent do you want 'b' to be?\n")
    # ci = input("How frequent do you want 'c' to be?\n")
    # di = input("How frequent do you want 'd' to be?\n")
    # a, b, c, d = ai, bi, ci, di

    # Use 'random' function thing to generate random letters from a pool of their inputs, based on the probability that they chose.

    # In order to generate words I would have to teach the program what combinations of letters are probable and which ones are impossible as well as VC rules and probabilties. All of this will be from user inputs.

    # Vowel-consonant interaction:
        # Explanation on what this part does for the language
        # Give examples of what VC looks like in a language (VCV - Anna, CVCC - Rand, etc.)
        # *executive decision* will I have a list of items for them to choose from or will I teach them how to input it and then make it so the computer can learn anything they put in? Stupid proofing says have a list.
        # asnswer = input(Do you want {CV} in your language?)
        # if answer = yes:
            # do a thing
        # else
            # do a different thing
        # The main problem with that is I would end up with a lot of variables and a lot of questions. C, V, CV, VC, CVC, CVV, CCV, CCC, VVV, VVC, VCV, VCC, continued with four and five (maybe more?) (with each one include a warning about it being difficult to pronounce or rare in real languages along with a real life example, e. g. Gaia, Brd, etc.)
        # If I don't have a list, I wonder if there is a way to make them format their list in a way that I can use it automatically as a list in python.
        

    # Consonant cominations:
        # Teach about the importance of each letter group (liquids, fricatives, nasals, etc.), examples, the entire IPA. and what each of these groups does for a word or language (e.x. liquids allow two consonants to be placed next to each other hard, felt, etc.)
        # give examples of consonant combinations: lt, rt, pl, sht, dr, mk, sl, st etc. and if applicable, examples in english (play, chart, silt, art, slit, draw, stop, etc.)
    # Depending on the IPA consonants they allowed, allow them to type a full list of every combination they allow for the beginning, middle, end, or initial. (for sl, beginning = slat, middle = eslen, end = chasl, initial = sl (sl in this case would be its own word)). 





## IPA:
    #*Executive decision* should I make a version of the IPA that is completely translateable to typical keyboard characters? I would also have to include a conversion table and a description of each sound, or advice to look up a real IPA for the sounds.

    # I'd need to implement pronounciation for every letter and teach the computer how to combine them, as well as allow users to implement a different rponounciation that the computer will recognize
