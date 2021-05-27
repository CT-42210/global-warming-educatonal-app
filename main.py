import random
import time


question_bank = [
    "increased levels of carbon dioxide", "increased CO2 in the air", "increased air temperature",
    "increased water temperature", "ocean acidification", "coral reef bleaching", "marine life dies",
    "land life dies", "economy suffers", "destruction of property", "less oxygen is produced",
    "complete and total death", "bigger and stronger wild fires", "decreased upwelling", "autotrophs die"
]


def life():
    print("life. \n it is nice. \n in life, we have found many things. one thing is fossil fuels.")
    time.sleep(1)
    fossil_fuels()


def fossil_fuels():
    print("fossil fuels can be used to create a lot of energy. we as a race realised this in the 20'th century. "
          "but since then. we have been rather abusive.")

    question_bank_list1 = list(question_bank)
    question_bank_list2 = list(question_bank)
    random_question1 = random.choice(question_bank_list1)
    random_question2 = random.choice(question_bank_list2)

    def first_handler():
        print("not quite!")
        fossil_fuels()

    def second_handler():
        more_co2_in_air()

    def third_handler():
        print("not quite!")
        fossil_fuels()

    def question():
        print("what does using fossil fuels as energy create?")
        print("1:", random_question1)
        print("2: increased levels of carbon dioxide,")
        print("3:", random_question2)

    question()
    answer = input(" \n type [1], [2] or [3] to answer. \n \n $")

    handlers = {
        '1': first_handler,
        '2': second_handler,
        '3': third_handler
    }

    if answer in handlers:
        time.sleep(1)
        handlers[answer]()
    else:
        print("Unknown choice", answer)
        fossil_fuels()
        time.sleep(3)


def autotrophs_die():
    print("due to decreased upwelling, autotrophs don't have the nutrients to make oxygen. "
          "this causes a domino effect beyond our comprehension. \n ")

    def first_handler():
        marine_life_dies()

    def second_handler():
        less_oxygen_is_produced()

    def third_handler():
        more_co2_in_air()

    def question():
        print("what happens now that the autotrophs?")
        print("1: sea life dies")
        print("2: less oxygen is produced")
        print("3: increased co2 in the air")

    question()
    answer = input(" \n type [1], [2] or [3] to answer. \n \n $")

    handlers = {
        '1': first_handler,
        '2': second_handler,
        '3': third_handler
    }

    if answer in handlers:
        time.sleep(1)
        handlers[answer]()
    else:
        print("Unknown choice", answer)
        autotrophs_die()


def more_co2_in_air():
    print("heavier usage of fossil fuels does create more CO2. increased levels of CO2 have their own problems.")

    def first_handler():
        air_temperature_rises()

    def second_handler():
        ocean_acidification()

    def third_handler():
        water_temperature_rises()

    def question():
        print("what are some possible side affects of increased CO2 levels in the air?")
        print("1: increased air temperatures")
        print("2: ocean acidification")
        print("3: increased water temperatures")

    question()
    answer = input(" \n type [1], [2] or [3] to answer. \n \n $")

    handlers = {
        '1': first_handler,
        '2': second_handler,
        '3': third_handler
    }

    if answer in handlers:
        time.sleep(1)
        handlers[answer]()
    else:
        print("Unknown choice", answer)
        more_co2_in_air()


def ocean_acidification():
    print("ocean acidification is an outcome of increased CO2 levels. "
          "\n diffusion will speed up, and the pH of the ocean will drop."
          "\n but once again, we are not done. ")

    question_bank_list3 = list(question_bank)
    random_question3 = random.choice(question_bank_list3)

    def first_handler():
        coral_reef_bleaching()

    def second_handler():
        print("not quite!")
        ocean_acidification()

    def third_handler():
        marine_life_dies()

    def question():
        print("what are the effects of ocean acidification?")
        print("1: coral reef bleaching")
        print("2:", random_question3)
        print("3: marine life dies")

    question()
    answer = input(" \n type [1], [2] or [3] to answer. \n \n $")

    handlers = {
        '1': first_handler,
        '2': second_handler,
        '3': third_handler
    }

    if answer in handlers:
        time.sleep(1)
        handlers[answer]()
    else:
        print("Unknown choice", answer)
        ocean_acidification()


def marine_life_dies():
    print(" many marine organisms have died. \n ")

    def first_handler():
        economy_suffers()

    def second_handler():
        less_oxygen_is_produced()

    def third_handler():
        land_life_dies()

    def question():
        print("what happens when the majority of marine life dies?")
        print("1: economy suffers")
        print("2: less oxygen is produced")
        print("3: land life dies")

    question()
    answer = input(" \n type [1], [2] or [3] to answer. \n \n $")

    handlers = {
        '1': first_handler,
        '2': second_handler,
        '3': third_handler
    }

    if answer in handlers:
        time.sleep(1)
        handlers[answer]()
    else:
        print("Unknown choice", answer)
        marine_life_dies()


def land_life_dies():
    print("due to the majority of marine life dying, the entire food chain was rattled. "
          "most land life has now died. \n ")

    question_bank_list4 = list(question_bank)
    random_question4 = random.choice(question_bank_list4)

    def first_handler():
        economy_suffers()

    def second_handler():
        print("not quite!")
        land_life_dies()

    def third_handler():
        complete_and_total_death()

    def question():
        print("with both the majority of marine and land life dead, what does this mean for humans?")
        print("1: economy suffers")
        print("2:", random_question4)
        print("3: total and complete death.")

    question()
    answer = input(" \n type [1], [2] or [3] to answer. \n \n $")

    handlers = {
        '1': first_handler,
        '2': second_handler,
        '3': third_handler
    }

    if answer in handlers:
        time.sleep(1)
        handlers[answer]()
    else:
        print("Unknown choice", answer)
        land_life_dies()


def economy_suffers():
    print("due to decreased food, the entire food marked has been shaken. "
          "\n this causes a domino effect leading to most people being unable to pay to feed "
          "themselves, amongst the already dwindling population of food. \n ")

    question_bank_list5 = list(question_bank)
    question_bank_list6 = list(question_bank)
    random_question5 = random.choice(question_bank_list5)
    random_question6 = random.choice(question_bank_list6)

    def first_handler():
        complete_and_total_death()

    def second_handler():
        print("not quite!")
        economy_suffers()

    def third_handler():
        print("not quite!")
        economy_suffers()

    def question():
        print("what happens now?")
        print("1: complete and total death")
        print("2:", random_question5)
        print("3:", random_question6)

    question()
    answer = input(" \n type [1], [2] or [3] to answer. \n \n $")

    handlers = {
        '1': first_handler,
        '2': second_handler,
        '3': third_handler
    }

    if answer in handlers:
        time.sleep(1)
        handlers[answer]()
    else:
        print("Unknown choice", answer)
        economy_suffers()


def less_oxygen_is_produced():
    print("the world is now being faced with an oxygen shortage, "
          "as the the majority of the producers are now dead. \n ")

    def first_handler():
        land_life_dies()

    def second_handler():
        complete_and_total_death()

    def third_handler():
        marine_life_dies()

    def question():
        print("what happens now?")
        print("1: land life dies")
        print("2: complete and total death")
        print("3: marine life dies")

    question()
    answer = input(" \n type [1], [2] or [3] to answer. \n \n $")

    handlers = {
        '1': first_handler,
        '2': second_handler,
        '3': third_handler
    }

    if answer in handlers:
        time.sleep(1)
        handlers[answer]()
    else:
        print("Unknown choice", answer)
        less_oxygen_is_produced()


def air_temperature_rises():
    print("due to increased carbon dioxide levels, the air temperature has risen. \n ")
    question_bank_list7 = list(question_bank)
    random_question7 = random.choice(question_bank_list7)

    def first_handler():
        bigger_wildfires()

    def second_handler():
        water_temperature_rises()

    def third_handler():
        print("not quite!")
        air_temperature_rises()

    def question():
        print("what are side affects of higher air temperatures?")
        print("1: more wild fires")
        print("2: higher water temperatures")
        print("3:", random_question7)

    question()
    answer = input(" \n type [1], [2] or [3] to answer. \n \n $")

    handlers = {
        '1': first_handler,
        '2': second_handler,
        '3': third_handler
    }

    if answer in handlers:
        time.sleep(1)
        handlers[answer]()
    else:
        print("Unknown choice", answer)
        air_temperature_rises()


def water_temperature_rises():
    print("due to increased air temperatures, the water temperatures of the ocean have also risen. \n ")
    question_bank_list8 = list(question_bank)
    random_question8 = random.choice(question_bank_list8)

    def first_handler():
        marine_life_dies()

    def second_handler():
        decreased_upwelling()

    def third_handler():
        print("not quite!")
        water_temperature_rises()

    def question():
        print("what are side affects of higher water temperatures?")
        print("1: sea life dies")
        print("2: decreased upwelling")
        print("3:", random_question8)

    question()
    answer = input(" \n type [1], [2] or [3] to answer. \n \n $")

    handlers = {
        '1': first_handler,
        '2': second_handler,
        '3': third_handler
    }

    if answer in handlers:
        time.sleep(1)
        handlers[answer]()
    else:
        print("Unknown choice", answer)
        water_temperature_rises()


def decreased_upwelling():
    print("due to increased water temperatures, the properties that keep upwelling in motion have stopped. \n ")
    question_bank_list9 = list(question_bank)
    random_question9 = random.choice(question_bank_list9)

    def first_handler():
        marine_life_dies()

    def second_handler():
        print("not quite!")
        decreased_upwelling()

    def third_handler():
        autotrophs_die()

    def question():
        print("what happens now?")
        print("1: sea life dies")
        print("2:", random_question9)
        print("3: autotrophs die")

    question()
    answer = input(" \n type [1], [2] or [3] to answer. \n \n $")

    handlers = {
        '1': first_handler,
        '2': second_handler,
        '3': third_handler
    }

    if answer in handlers:
        time.sleep(1)
        handlers[answer]()
    else:
        print("Unknown choice", answer)
        decreased_upwelling()


def stronger_tropical_storms():
    print("hurricanes, tsunamis, and cyclones are now exponentially stronger. \n ")
    question_bank_list10 = list(question_bank)
    random_question10 = random.choice(question_bank_list10)

    def first_handler():
        print("not quite!")
        stronger_tropical_storms()

    def second_handler():
        pass

    def third_handler():
        land_life_dies()

    def question():
        print("what happens now?")
        print("1:", random_question10)
        print("2: destruction of property")
        print("3: loss of land life")

    question()
    answer = input(" \n type [1], [2] or [3] to answer. \n \n $")

    handlers = {
        '1': first_handler,
        '2': second_handler,
        '3': third_handler
    }

    if answer in handlers:
        time.sleep(1)
        handlers[answer]()
    else:
        print("Unknown choice", answer)
        stronger_tropical_storms()


def property_damage():
    print("hurricanes, tsunamis, wildfires, and cyclones have caused extensive damage to land. \n ")
    question_bank_list11 = list(question_bank)
    random_question11 = random.choice(question_bank_list11)

    def first_handler():
        land_life_dies()

    def second_handler():
        economy_suffers()

    def third_handler():
        print("not quite!")
        property_damage()

    def question():
        print("what are the side effects?")
        print("1: land life dies")
        print("2: economy falls")
        print("3:", random_question11)

    question()
    answer = input(" \n type [1], [2] or [3] to answer. \n \n $")

    handlers = {
        '1': first_handler,
        '2': second_handler,
        '3': third_handler
    }

    if answer in handlers:
        time.sleep(1)
        handlers[answer]()
    else:
        print("Unknown choice", answer)
        property_damage()


def bigger_wildfires():
    print("the hotter air has made it easier for wildfires to spread. \n ")
    question_bank_list12 = list(question_bank)
    question_bank_list13 = list(question_bank)
    random_question12 = random.choice(question_bank_list12)
    random_question13 = random.choice(question_bank_list13)

    def first_handler():
        property_damage()

    def second_handler():
        print("not quite!")
        bigger_wildfires()

    def third_handler():
        print("not quite!")
        bigger_wildfires()

    def question():
        print("what are the side effects of having more wildfires?")
        print("1: property damage")
        print("2:", random_question12)
        print("3:", random_question13)

    question()
    answer = input(" \n type [1], [2] or [3] to answer. \n \n $")

    handlers = {
        '1': first_handler,
        '2': second_handler,
        '3': third_handler
    }

    if answer in handlers:
        time.sleep(1)
        handlers[answer]()
    else:
        print("Unknown choice", answer)
        bigger_wildfires()


def coral_reef_bleaching():
    print("the higher pH of the ocean makes it harder for coral to retain its nutrients. \n ")
    question_bank_list14 = list(question_bank)
    random_question14 = random.choice(question_bank_list14)

    def first_handler():
        print("not quite!")
        coral_reef_bleaching()

    def second_handler():
        marine_life_dies()

    def third_handler():
        autotrophs_die()

    def question():
        print("what happens if there are no surviving coral reefs?")
        print("1:", random_question14)
        print("2: marine life dies")
        print("3: autotrophs die")

    question()
    answer = input(" \n type [1], [2] or [3] to answer. \n \n $")

    handlers = {
        '1': first_handler,
        '2': second_handler,
        '3': third_handler
    }

    if answer in handlers:
        time.sleep(1)
        handlers[answer]()
    else:
        print("Unknown choice", answer)
        coral_reef_bleaching()


def complete_and_total_death():
    print("we have failed as a species. and in our greed, we have killed everything else too. "
          "lets see what you can do to help \n ")
    question = input(" \n type [ok] to proceed. \n \n $")

    if question == "ok":
        solutions()
    elif question == "floppa":
        print("--------------------------------------------------------------")
        print(":i:,:::,,:;,,,,:::i;:;;;;;;;;i;ii;;;;;;;;;iinW+;:;::::::::::::#xi:::::::::::;i:i*+nxnnnzz#*i;:;ii;i;;i*"
              ";;;:::i;:;::::iii;;;;;;*+i;;;i*ii;***iii;;;;;;;\n;i;:::::,:;,,,::;;i:,;;::::i;i;;i;;ii;i;;;;;zW#;::::::"
              "::::::::#xi::::::::::::i;+nWMMMMxn#++*i;iii;i;;;*;;;;:;i;;i;;;iii;::;;;;*+i;:;;i;;:i**;;;:;;;;;i\n:;;;;"
              ":::::i,,,:::i;;,,,,::;*i*iiiii;i;;;;;;;#Wz;::::::::::::::+x*::::::::::::;#MWW@@@@WWMn#*i;iii;i;;i+;:;::"
              ":*;:;::::i*i::;:::*+ii;iii;;:i**;;;:;:;:;;\n:;;;;:::::i,,,:::;;i;iiii;;*iiiiii*+#++*ii;;#Wn;:::::::::::"
              ":::*x*::::::::::::xWWWW@@@@@WWWxn*iiii;i;;;i;;;:::ii;i::;:i*i;;;;;;*+i;;iiiii;***i;;;;:;:;;\n;;;:::::::"
              ";:;iiii;;i;;;;;;;i;*ii+#znMMMMn#+;+Wx;::::::::::::::*x+:::::::::::xWMMMWMz+***+zMxz*i*i;i;ii*;:;:::i;:i"
              ":::;i*i:::;;;*+i;;;;i;;:i+*;;;:;;i;;;\n;ii;;;;;;;;;:::::;;;:;;;;;;i;**+zMMMMWWWMWWx#WM;::::::::::::::in"
              "#::::::::::xWnnxMM*i*iii***#n+**i;i;:;*i;;:::i;:i::::i*i::::::*+ii;iii;;:*+*;;::;:;:;i\n;ii;;;::::;;:::"
              "::;;;:::::::ii*#xxnxMWWWWWMMMWMM;::::::::::::::in#:::::::::xMz#znMM***ii*****+#***;iii;*;:;::;i;:i;;;;i"
              "ii;;;;;;*+i;;;;iii;*+*ii;;;:;:;i\n::;::::::::;:::::::;;:::;;;ii+xMxz###znMMMMxxMW+::::::::::::::;nz::::"
              ":::;MMz###nMMi**ii*******+*i;i::;ii;;:::i;:;::::ii;:::::;*+i;;;;i;;;*+*;;;iiiiiii\n;:;:,::::::i:::::::;"
              ";;iiiiii*nxz*iiiiiiiMMxxnnxWz:::::::::::::;zz:::::::MWn#+#znMMii*************ii;;;ii;;::;i;;i::::iii;;;"
              ";:;*+iiiiii;;;***iiiii;i;;;\n;;;::::::::;:::::::;;;i;;ii*z#*i***ii**ixMxnzz#xWn;:::::::::::;zn;:::::n@x"
              "#++#znxMiiii*****ii****;;::;ii:;:::i;:;:::;ii;::;;;;**;;:;;iiii****i;;;;i;;;\n:::::,:,,::;::::::;;i;;;;"
              ";;**ii****;i**inMxxnz##xWx;:::::::::::#n;::::#@Mz###znnxMiiii*****i*****ii;:;ii;i:;:ii:;::::;i;::::::**"
              "iiiiii;;:***;;;;iiii;;\n::::,,,,,,:;::::::;;i::::;;;iii*i**ii**inMxxnz###MWx:::::::::::#n;:::;WWz###znx"
              "xMx*********i*****ii;:;ii:i:::ii:;::::;i;:;;;;ii*i;;;ii;;:**i;;;;;;i;;;\n;;;:,,,,,,:;;::::::;i;;;;ii;i;"
              "i**iiii***zWxxxn###nMWz::::::::::+ni:::zWx###nnnxxWz**i*************i;;:;i;i;::*i:;:::;iii;;;;;;i*;;::;"
              "i;;i**ii;;;;;i;;;\n:::::,,,,,,:;:::;:;;i;;;;ii;i;i**iiiii**#WMxxnz###nMW*:::::::::*ni::*WMz###zzxxMW+**"
              "i*****+******i;;;;ii:i:;;iiii;i;;iii:::::;**i;:;;;;;:**i;;;;i;i;;:\n:::::::::,::;::;;;;;i;:;;;;;;iiiiii"
              "i*i**+WMMMxn###zxWWi::::::::*ni::+Wxz+##zxxxMxi**i**********i*ii;::;i;i;;;ii;i::;;;i;;i**++##+++*ii;;;*"
              "*i;;;;;;::::\n::::::::::::;:::;;;;;i;;i;;;iiiii*ii*i*i*WMMMxxnzz#nWW#::::::::in*::zMx#++#nxnnM+**iiii**"
              "***++**ii;;;i;i;i;;;i*;;:::;i**++#+##########++++**ii;;;:,,,,\n:::::,::::::;::::;;;ii;iiii*iiiiiiiiiiii"
              "*nWMMMxz+#znWWx;:::;;;;*n+;*nxxz##znnnxM**+***i******+*iiiii;:i*;i:::ii;;;ii*++++++++++++++#######+#+++"
              "**i;:::\n;:::;:::::::;::::;;;iiiiiiii**iiiiiiii***+WMMMxxn#zxWWMz**+##zxzzzznnnxz+*+zxz#n****i*i***ii*+"
              "***i:;;;ii;;;;;***+++++++*+**++++++++++++##########+#*ii\n;;;:;::;::::;::::;;iiiiiiiiii*****iiiii***nWM"
              "Mxnz##nMMMxxnnzznxnzzzznnnz+++zxz#**iiiiiii********ii;;::;i;i*++++++++++*+**********+++++++++++##++++++"
              "+*\n;;;;i::;;::;:::;;;;iiiiiii*ii******i**i***+WMMMn#+#nnxMxxnnz#nMz##zzznnz+++#xnz+;ii***i****ii*+**i;"
              ";;i*+******+++++++**************+****++++++++++#+++\n;;;;;;:;;::;:::;;;iiiiiii*i**********+*****MnMWMzz"
              "zzxMxnnnz#znxn#+#zzzznnz#zzz#+i*****i*i**iii*****+++++*+**+***++++++**++**************++*+++++++##++\ni"
              ";;;;;:;;;:;:;:;;;*i**iii*i**********+*****zMWWMz#zxMMxnnn#+#zxn##*zxnzzznzzzzzz****iiiiiiiiiii++#z#++++"
              "+*****++++++++++*+***********+*******++++++##+\nii;;;;;;;;;;;;;;;;*****iiii**i*******+*****zxMMMxnMMMxn"
              "nxx#*+zxx#+*zMMzzz#znnMM+i*iiiiiiiiiii+#z####++++++++******+++++*+****+******i*******+++++++++#\n;iii**"
              "*ii;;;iiii;i****iiiii**ii******+*****zMMMxxMxxxxxxWM#*#zxx##*+WWnnnz##nMW*i*iiiiiiiii+z#zzz##++#+#++*+*"
              "***++++++++++*+++**************+**++++++#\nii*******iiiiii*i*****iiiii**iii*****+*****+MWMxMxxxxxxxWWz#"
              "znnxz#+*M@nxxnz##xW#i*iiiiiii+zzz#z####++#+++*++*****+*+++++++++++*+****+**********++++++#\n***********"
              "***i****++*******iii******+***iiiz@MWMxxMMxxnWWxznxnxnz#+MWxxnnzz+#x#iiiiii*+#z#####+++#++#++++++******"
              "*+*+++++**************ii******++####\n****+********+*************i*ii***iiiiii*ii*n@WMMxMMnznnW@Mnxxnxn"
              "z#+xMnxnnzz++#zi***++######++++++++++#++++********+++++++***+**********ii******++###z\n**++++*****+****"
              "+***++*+***iiiiiii********i*zWWMMMMnnMxxMMxxxxxxn#*;ix@@WWWxz+++i########+#+++++++*++#++++++******++**+"
              "**+**+*************i*****++##zz\n**++++**+**+++*+++++****ii*******++++*+*****#WMxMMMW@@@@@x#nxxnxn#i,;@"
              "@@WWW++##+;#########+#+++++++####++++*******+**++++**+++***i******iii******++##z\n**++++*+++++++****ii*"
              "****++**+***++*++*i+***#MxMMMW@W@@W@W+zxnnxz+i.+@@@@MMi++##*zzzzzzzzz#z#+*+++####+++++++*i*****+*+****+"
              "+*******+***iiii*ii***+++#\n*+++++*+**iiii**+++++++*+++***+*+++****i***i*xMMMMxWW@@@@@##xnnnn+i.zWM@MM*"
              ";###z+zxnnnnznzzz##++++##zz#++++++*+*+******+**+*+**********iiiiiiii****+++\n************++**+++++++*++"
              "+***+i+******iiiii+xMMMM##WM@@@@z#xnnnz+;,xWnnx+;zz##n+inxxxxnznzzz##+++#zz##+++++**+********+*********"
              "*iii***iii*ii*ii**+++\n***+++*****++++*+++++++i*++*+**i****iiiiiiii#xMMMx#iizW@@@Mznznnz+;:MMM#i*nnz+#n"
              "+;+nxxxxnnzzzzz#+++#z##+++++*****iii*****+********ii****iiiiii*ii**+++\n++++++*****+++**+++++++**+*****"
              "i***iii;;;ii;+xMMMxn#+*+M@@Wznzzzz+iiWWx*#nnzz+zz+;i#MMxxnnzzzzzzz#######++++******ii***++++**+********"
              "*ii;iiiiiii*+++*\n+++++++*++*+++**+++++++********i***i;;;i**+##xMMMMxnz##n@@Wxnzzzz#*#WMz#znznz#z#+ii+z"
              "MMxxnzzzzzzzzzznz####++***+++******+*+*********+***;;iiiiii**+#+*\n*+++*++*+++++++*+++++++iiii;;;iiiii*"
              "+#znnxxx#xxMMMxxz##zW@WMxnzz+*+zMMzzzzzzzz#++i;+#xMMxnnzzzzzzzzznnnz###+#++++++*i*************+++++****"
              "*iiii**+##+\n*++++*+**+++++***+++++iii;;i*++#znnxxxxn#*i;#MxMMWWMxnznWW@Wxn##++#nWMnzzzzzz#*+*ii+#zMMMx"
              "nnzzz#zzzzzznz#######++++*i***************++++****iiii**+##+\n*++*********+#++*++**i*+#znnxxxxxz#*;:,,,"
              ",:;zMxxMWWWMxnxWW@@Mxzzz#zx@xnzznznn#+++*i+##xMMMxnz#####zzzznzz#####+++++*iii*****+****+++++#****iiiii"
              "**+#++\n**+******+******++#znnxxMMxz+i;,.,,,:::::::izxxxMWWWWMMMWW@@WMnzzznWWznznnxx#++++*i+##nxMMMxnzz"
              "zzzzzznzzz#####++++#*i*ii******+++*+*+#+***ii******++++\n********i*+#znxxxxxxnz+i:,.,,::::::::::::::*zx"
              "MxxMWWWWWMMMW@WWMxxxxMx++#znz#+##+**i+#+nxxWMxxnz####zzzzzz#####++++#+***i******+++**+##+**++********+#"
              "#\n;i*++#znnxxxxxn#*;:,.,,::::::::::::::::::::*nMMMxxxMWWWWMxM@@WMxxMxMn**+##**+++++**+++zxxMMxxnz##zz#"
              "zzzz########+#++**************++++**+++*******+###\nzznnxMxxn#*;,.,,:::::::::::::::::::::::::::+zxMMMxx"
              "nxWWWxxx@@@WMMW@M+*+zn*i+***+***+++zxxxMMxnzzzzz##zzz##++####+++++**+********+++****++*********+###\nMM"
              "n#*;,.,,,:::::::::::::;;::::::::::::::::;#zxMMMxxnzxWWMxnx@#@WWWxi;#nxW*i****++i*+#+zxxxMMxnnzz##z#zzz#"
              "#+++####+++++++***+***********+++*ii****++#z#\n,,,,:::::::::::::;;;;;::::::::::::::::::::i#zxMMxxxnzz@@"
              "@MxzzM@@Wx;:;i*#x+++++*+**++++zxxnxxxxznzz###zzz#+++####+*+#+++****++*++++*********ii*****+#z#\n:::::::"
              "::::;;;;;::::::::::::::::::::::::::*zznxxMxxnzzWWMxnz##W@@n;;i#nnWi*ii*+++++####xxnxMxxnnnzzzzzzz###+##"
              "#++++##+***i*********************+**+#z#\n:::::;;;;;;:::::::::::::::::::::::::::::::*znnxxMxxnnzM@WWxnz"
              "z#WW#**i+nxn#+*i*+++++#z#zxxxxxMMnznzzzzzz#######++++++#+++***********************+***#z#\n::::::::::::"
              "::::::::::::::::::::::::::::::*nnxxxxxxnzznW@WMxxMzzMxxznxMMz+****+#+++###nxxxxxxMxnzzzznnzzz####++++++"
              "++++++****+**++*************+***###\n::::::::::::::::::::::::::::::::::::::::::innxxxxxxnnnznW@WWWMxWWx"
              "xxnMWz#+++#z#++++#z#nxxxxxnxMxnnzz#zzzz#####++++++++++**+*****++****i*********+*++##\n:::::::::::::::::"
              ":::::::::::::::::::::::::inxMMxxxxnnnzznWWWMMMMMMMxxMnzz#zznz++++###znxnxxxnxxxnznnz#zz######+++++**+++"
              "*++**++**++*iii***ii****++++#+\n::::::::::::::::::::::::::::::::::::;;;ii**nnxMMxxxxxnnnnnxxxxMxxxxnnzz"
              "zznzz#++++####znnnnMxnnxxnnnnzz##zz##zz##+*+*******+++++++***iii*+*****i*+###z#\n::::::::::::::::::::::"
              "::::::::::;;ii*****iinnxMMMxxxxxnnnznzzznnnzzzznzzzz#+*++++#####nnnnMMxnxMxxxnnnzzz#zzzzz##++*******+#+"
              "++***+**************+zzz+\n::::::::;;;ii***i;::::::::;;ii*****ii;;::,:nxxMMMxxxxxxnnnnnzzzzzzzznnz###++"
              "*++++###zzznnnxxnnnnxxxxnnnnnzzzzzzz#+++*******+++*******++**+***+**+##zz*\n:::iii***+#####+*iii;;;ii**"
              "***i;;:::,,,,,,:nnxMMMMxxxxxnnnnnzzznzzzzznz##++***++#####znnnznxxnnnxMxxxnnnnzzzzznz#+++++++*ii*+*****"
              "+******+++*++++##z#i\nii####++####zznnz##+++***i;;:::,:,::::,,,::nnxMMMMMxxxxnnnnnzzznnz##znz#++***+++#"
              "##zzznzznnxxnzzxMMxxxnnnnnnnnnnz##++#++**i**********ii**++++++#++++*i\nznzz######zznnnnnnzzz####++*ii**"
              "**ii;;;::::nxxxMMMMMMxxxnnnzzzzzzz##zzz#++**++++####zzznzznnxnnznxMWxxxxnnnnnznnnnz###+*iiii*++***++**i"
              "****+++##+++*i;\nxxxxnnzzzzzzzznnnzzzzzzz###nnxxxn#i;::::;;izxxxMMMMMMMxxxnnnzzzzzz######++*+++++#z#z#n"
              "zzzznnnnzzznxWMxxnnnnxxnxxxnnz##+*iiiii*++***********+++++++*i;;\nMMMMMxxnzzznnnnnnnzzzzzznzz#znxxz+i;"
              "*++###nxxxMMMMMMMMMxxnnnzzzzzz#####+*+#+####zz##zzzzznnnnzzzznMWMMxnnxnnnxxxxxnz##+*iii**+**++***++*++*"
              "++++**i;;;\nMMMMxnnzz#zzzzznnnzz####zznnnzznnxnnxnnznnzxxxxMMMMMMMMxxxxnnzz##zz######++++####zz#zzzzzzz"
              "nnnzzzznxMMMMxxnxxxnxxxxxnz##*iiii*+***+++*++++**++++*;::::\nxMMMMMxnz###zzzzzznnnzz###znxxnznnxMMxxxnn"
              "nnxxxMMMMMMMMxxxnnzz###zzzz##++++++#+#zzz#zznnzzznnzzz#zznxMMxxxnnnxxxxMMMxnz#*i;;i*++*****ii**+*+##+*;"
              ":::::\nnxMWMxz####zzzzzz##znnz#######zzznnnxMMxxxxxxxxxMMMMMMMxxnnzz#zzzzzzz##++++++###zz##znnnzzznnnzz"
              "#zznxxMMMMxnnxxnxxMMxnn#+*i;ii*******i*i**++++*i:::,,,\nznxMMMn##z#zzznnznzzz+++++#+++####znxMMMMnnMxxx"
              "MMMMMxMxxxn#####znzzzzz#++++#+##zz#zzznnnnnzznnnzzzznnxMMxxxxxxxxxxxMxxnz#+i;;;i******+*+***+*i;::::,,,"
              "\nnnxMMxnnnznnnxxxxMxnz+++#######zzzzxxxxxzzxMxxMMMMMMMMxxn##+++##zznzzz#+++####znz##zznnnnnnnznnnz#zzz"
              "xxxxxxxxxxxxxxxxxnzz#*i;iii***++++++++*i;::;;;:::\nzznxxxxxnzznxxxMMMMxz#+##znnnnnnxxxxxxxnnzMMMxMMMMMM"
              "MMMxnz#***++#znnzzz#+*+###zzzz#zznnznnnnnnnnzzznznxxxxxxxxxxxxxxxnznnz+*i;ii***++**+++**i;;;;;;;::\n#zn"
              "nxMxxzznxxxMWWWMMxnzzzzznnnnxMWWxxMxnnnMWMMMMMMMMMMxxn#+*iii*+#zz###+##+###z###z#znnnnnnnnnnnzzzzzznxxx"
              "xxxxxxxxxxxnnzxn+i;;;i********+***i;;;ii;::,\n##zxMMMnnnnxMWWWWWWMnzzzznnxxxxMWWWMMMMMxxMWWMMMMMMMMxnz#"
              "++*ii;;i*++##+#+#+#####+###zznnnnnznnnnnnnzzzznxxxxxxnxxxxxnnnzzn#;::;;ii**ii**+*iii;;i*i:,,.\nnzzxMMxx"
              "xxxxMWWWWWWMxnnnnnxxMMMMWWWMMWWMxMMWWWMMMMMMxnz#+**iiiii;i**+++#+++#########zznnnnnnnzznnnnzzzznnxxnxxx"
              "xxxxxxnnzzz+;::;i***i;ii**ii;i;i*;:,...\nnnnxMMnnzznnxMWWWWMMxnnxxxxxMMMWW@@WWWWMMMMWWWMMMMMxxzz#**iiii"
              "iiii**++++##+###++##+##zznnnnnzzznnxxnzzzznxxxxxnxnnnxxnnzz#+i::;iii*i;;i*i;::,,,,......\nxxnnMMMxxnnxM"
              "MWWWWWMxxnnxxxxMWWWWW@@W@@WMWWW@@WMMMMxxn#+****i**ii***+##+######+++#+##zznnnnnnzzznxnnnzzzznnxxxxnnnxn"
              "nnnzz##*;;;iiiiii**i;:,...........\nxxxxMWWWMMxxMWWMMWWMxxxxxxMxMWWWW@@@@@@@MWWW@@WWMMMxnz#+*+*********"
              "++++##+++++++++++#zzzznnnzzznnxnnnzzzzznnxnnnxxxnnxnnnz##+*i;;;i;;::,,.............\nnxxxMWWWMMMMWWWMMM"
              "MMxxxxMxMMMWWWWW@@@@@@WMMWW@@WMMMxz###+*******+++++##++++++++#++++#zzzznnnnznnznnxnzzzznnnnnnnnnnnnnxnz"
              "zz##+*i;:,...................\nxMMMMWWWWMxxWWWMMMMxxxxMMMMMMWWWWWW@@@@@WMMMW@@@WMMMxnz#++*+*++++##+++++"
              "+***++++++++++zzznnnnzznznnnnnzznnnnzzznnnnnnnnnnnzz#+++*;,...................\nxxxMWWWWWWMMMWWWMMMxxxM"
              "MMMMMMWWWWW@@@@@@WMMxMW@@WMMxxxzzz#++++++#+++++##+**++******++##zznnnnnnnnnnnnznzznnnnnnzznnnnnnznnnnz#"
              "##+*i:,.................\nxxMMWWWWWWWWWWWWMMMxxxxxMMMMxMWWWWW@@@W@WxxnxMM@@WMxxxnzz##++##+++++##+++*+++"
              "+*****+++###znnnnnnnnnnnnzzznnzzzznnzzzzzzzzzznnz#+#+ii,.................\nMMMMMW@@WWWWWWWMMMxxxxxxxMMM"
              "xMWWWWW@W@@@WnnnnxMWW@WMMxxnzz#+++++#++++#+++*********+++##z#znnnnnnnnnzzzzzznnzzzznznnnnnnnzzzzzz###+*"
              "i;.................\nxMMMWW@@WWMMWWWMxxxxxxxxxxMMMMMMMWWWWWW@xnnxxMMWWW@WMMxxnz#++++#++++###++*****+***"
              "*++#####znnnnnnnnnzzzzzzzznnnnzzzznnnnzz########+*i,................\nxxMWWWWWWMMMMWWMMxxxxxxxxxxMWMMxn"
              "xMWWW@xnxnnxxMMMMMMxMMxxxnzz#+#+*++++++****+*++++++####zzznnnznnnxnnnnzzzzzzzzzzzznnnnnnzz######++**,.."
              "..............\nnxxMMMMWMMMMMWWWMMMxxxxxxxxxMMMxxnxMW@WnxnnnnxMxMxxz#znnxxxxxn##+###**+*++****++++++#zz"
              "z##znnnzznnxxxxnzzzzzzzznzzznnnnnnnz######+++i...............``\nxxxxxxxxMxxxxMWWWMMMxxxxMMxxxMxxxxMMMW"
              "MnzznnnxxxMn##++#zznnnnzzzzzz#++++*#*****+#######zz#znznnnznxxxxxnnzzzzznznnzznnnnzz#########+,........"
              ".......``\nxMMWMMxxxxxnnnxMWWMMxxMMxMMMxxnnxMMMWWMnznnnxxxxxxn#+##zzzznnnnnnnzz#++#+##+***++zzz###zzzzz"
              "nxnnnznxxxMxxnnzz##zzzzzznnnzzz###+###+*............``.```\nWMMMMMWWMxnzzzzxMWWMMxMMxxMMMxxznxMWWWxnznx"
              "xxxxnnnxzzznxxxnxxxxxxnnznnzz###++++++##++##z###zzxxnxnnxxMMxxxnn#+++#z###zznzzzz#######+,...........``"
              ".```\nWWMMWWMMxxxxnzznnMMMMxxxxxxMMMxnznMW@WMnnxxxxxnzznnxxnxxxxxxxxxxxnnnnxnnn#z+++++++++##z##z#+zxxxx"
              "nnxMMMMMxxz#++#######znzzzzzz#####+i...........`.`..,\nxMWMMMMMxxxxxxnnnMMMMxxxxxxxxxxxxnMW@WWxnxxxnz##"
              "znnxxxxxxxxnzzzznxxnnMxxMMMnzz#z#+i++#zz##++zznxnnxxMMMMMxxn######z###zzzzzzzz###+#++,.......`..,,:;ii\n"
              "nMxxMMMMMMMxxxxnzzxMMMxxxnnnnxxnnxMxW@WWxxxxnz#+zznnnxxxMMxnnz###znnnnxxxxxnz#n#zz*i+*####"
              "+#zznxnznxMxMMW"
              "WWMxnzzzzz###zzznnzzz#z#####+:.....,,:;iiiiii\nWMMMMWWMMMMxxxnnnnxxxxxnzzzznnnznMMW@@Mxxxnz##zzzznnxxxx"
              "xnzznnnzzznnnnxnxxz#+#++*****+#+++##znxnnMxxxxMMWWWMxnnnzzzzzzzzzzzzzzz#####+;.,::;iiiiiiiiiii")
        print("--------------------------------------------------------------")
        complete_and_total_death()
    elif question == "troll" or "trolled":
        print("--------------------------------------------------------------")
        print("░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░\n░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░\n░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░\n░░░█░"
              "░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░\n░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░\n█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█\n█░▒█░█▀▄▄"
              "░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█\n░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░\n░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░\n░░░█░░░░██░░▀"
              "█▄▄▄█▄▄█▄████░█░░░\n░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░\n░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░\n░░░░░░░▀▄▄░▒▒▒▒░░"
              "░░░░░░░░▒░░░█░\n░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░\n░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░")
        print("--------------------------------------------------------------")
        complete_and_total_death()
    else:
        print("try again.")


def run():
    print("welcome to Nick and Nathans climate change story thing. "
          "\n the educational part, or the first part, was built by Nick. "
          "\n the choose your own adventure part, or the second part, was done by nathan."
          "\n if you get 2 of the same question, "
          "just guess which one it might be. if you guess the incorrect one, you can try again.")
    question = input(" \n type [ok] to proceed. \n \n $")

    if question == "ok":
        print("loading assets")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print("loaded!")
        print("--------------------------------------------------------------")
        print("             _____             \n          .-'.  ':'-.          \n"
              "        .''::: .:    '.        \n       /   :::::'      \       \n "
              "     ;.    ':' `       ;      \n      |       '..       |      \n    "
              "  ; '      ::::.    ;      \n       \       '::::   /       \n       "
              " '.      :::  .'        \n          '-.___'_.-'           ")
        print("--------------------------------------------------------------")
        time.sleep(1)
        life()
    elif question == "floppa":
        print("--------------------------------------------------------------")
        print(":i:,:::,,:;,,,,:::i;:;;;;;;;;i;ii;;;;;;;;;iinW+;:;::::::::::::#xi:::::::::::;i:i*+nxnnnzz#*i;:;ii;i;;i*"
              ";;;:::i;:;::::iii;;;;;;*+i;;;i*ii;***iii;;;;;;;\n;i;:::::,:;,,,::;;i:,;;::::i;i;;i;;ii;i;;;;;zW#;::::::"
              "::::::::#xi::::::::::::i;+nWMMMMxn#++*i;iii;i;;;*;;;;:;i;;i;;;iii;::;;;;*+i;:;;i;;:i**;;;:;;;;;i\n:;;;;"
              ":::::i,,,:::i;;,,,,::;*i*iiiii;i;;;;;;;#Wz;::::::::::::::+x*::::::::::::;#MWW@@@@WWMn#*i;iii;i;;i+;:;::"
              ":*;:;::::i*i::;:::*+ii;iii;;:i**;;;:;:;:;;\n:;;;;:::::i,,,:::;;i;iiii;;*iiiiii*+#++*ii;;#Wn;:::::::::::"
              ":::*x*::::::::::::xWWWW@@@@@WWWxn*iiii;i;;;i;;;:::ii;i::;:i*i;;;;;;*+i;;iiiii;***i;;;;:;:;;\n;;;:::::::"
              ";:;iiii;;i;;;;;;;i;*ii+#znMMMMn#+;+Wx;::::::::::::::*x+:::::::::::xWMMMWMz+***+zMxz*i*i;i;ii*;:;:::i;:i"
              ":::;i*i:::;;;*+i;;;;i;;:i+*;;;:;;i;;;\n;ii;;;;;;;;;:::::;;;:;;;;;;i;**+zMMMMWWWMWWx#WM;::::::::::::::in"
              "#::::::::::xWnnxMM*i*iii***#n+**i;i;:;*i;;:::i;:i::::i*i::::::*+ii;iii;;:*+*;;::;:;:;i\n;ii;;;::::;;:::"
              "::;;;:::::::ii*#xxnxMWWWWWMMMWMM;::::::::::::::in#:::::::::xMz#znMM***ii*****+#***;iii;*;:;::;i;:i;;;;i"
              "ii;;;;;;*+i;;;;iii;*+*ii;;;:;:;i\n::;::::::::;:::::::;;:::;;;ii+xMxz###znMMMMxxMW+::::::::::::::;nz::::"
              ":::;MMz###nMMi**ii*******+*i;i::;ii;;:::i;:;::::ii;:::::;*+i;;;;i;;;*+*;;;iiiiiii\n;:;:,::::::i:::::::;"
              ";;iiiiii*nxz*iiiiiiiMMxxnnxWz:::::::::::::;zz:::::::MWn#+#znMMii*************ii;;;ii;;::;i;;i::::iii;;;"
              ";:;*+iiiiii;;;***iiiii;i;;;\n;;;::::::::;:::::::;;;i;;ii*z#*i***ii**ixMxnzz#xWn;:::::::::::;zn;:::::n@x"
              "#++#znxMiiii*****ii****;;::;ii:;:::i;:;:::;ii;::;;;;**;;:;;iiii****i;;;;i;;;\n:::::,:,,::;::::::;;i;;;;"
              ";;**ii****;i**inMxxnz##xWx;:::::::::::#n;::::#@Mz###znnxMiiii*****i*****ii;:;ii;i:;:ii:;::::;i;::::::**"
              "iiiiii;;:***;;;;iiii;;\n::::,,,,,,:;::::::;;i::::;;;iii*i**ii**inMxxnz###MWx:::::::::::#n;:::;WWz###znx"
              "xMx*********i*****ii;:;ii:i:::ii:;::::;i;:;;;;ii*i;;;ii;;:**i;;;;;;i;;;\n;;;:,,,,,,:;;::::::;i;;;;ii;i;"
              "i**iiii***zWxxxn###nMWz::::::::::+ni:::zWx###nnnxxWz**i*************i;;:;i;i;::*i:;:::;iii;;;;;;i*;;::;"
              "i;;i**ii;;;;;i;;;\n:::::,,,,,,:;:::;:;;i;;;;ii;i;i**iiiii**#WMxxnz###nMW*:::::::::*ni::*WMz###zzxxMW+**"
              "i*****+******i;;;;ii:i:;;iiii;i;;iii:::::;**i;:;;;;;:**i;;;;i;i;;:\n:::::::::,::;::;;;;;i;:;;;;;;iiiiii"
              "i*i**+WMMMxn###zxWWi::::::::*ni::+Wxz+##zxxxMxi**i**********i*ii;::;i;i;;;ii;i::;;;i;;i**++##+++*ii;;;*"
              "*i;;;;;;::::\n::::::::::::;:::;;;;;i;;i;;;iiiii*ii*i*i*WMMMxxnzz#nWW#::::::::in*::zMx#++#nxnnM+**iiii**"
              "***++**ii;;;i;i;i;;;i*;;:::;i**++#+##########++++**ii;;;:,,,,\n:::::,::::::;::::;;;ii;iiii*iiiiiiiiiiii"
              "*nWMMMxz+#znWWx;:::;;;;*n+;*nxxz##znnnxM**+***i******+*iiiii;:i*;i:::ii;;;ii*++++++++++++++#######+#+++"
              "**i;:::\n;:::;:::::::;::::;;;iiiiiiii**iiiiiiii***+WMMMxxn#zxWWMz**+##zxzzzznnnxz+*+zxz#n****i*i***ii*+"
              "***i:;;;ii;;;;;***+++++++*+**++++++++++++##########+#*ii\n;;;:;::;::::;::::;;iiiiiiiiii*****iiiii***nWM"
              "Mxnz##nMMMxxnnzznxnzzzznnnz+++zxz#**iiiiiii********ii;;::;i;i*++++++++++*+**********+++++++++++##++++++"
              "+*\n;;;;i::;;::;:::;;;;iiiiiii*ii******i**i***+WMMMn#+#nnxMxxnnz#nMz##zzznnz+++#xnz+;ii***i****ii*+**i;"
              ";;i*+******+++++++**************+****++++++++++#+++\n;;;;;;:;;::;:::;;;iiiiiii*i**********+*****MnMWMzz"
              "zzxMxnnnz#znxn#+#zzzznnz#zzz#+i*****i*i**iii*****+++++*+**+***++++++**++**************++*+++++++##++\ni"
              ";;;;;:;;;:;:;:;;;*i**iii*i**********+*****zMWWMz#zxMMxnnn#+#zxn##*zxnzzznzzzzzz****iiiiiiiiiii++#z#++++"
              "+*****++++++++++*+***********+*******++++++##+\nii;;;;;;;;;;;;;;;;*****iiii**i*******+*****zxMMMxnMMMxn"
              "nxx#*+zxx#+*zMMzzz#znnMM+i*iiiiiiiiiii+#z####++++++++******+++++*+****+******i*******+++++++++#\n;iii**"
              "*ii;;;iiii;i****iiiii**ii******+*****zMMMxxMxxxxxxWM#*#zxx##*+WWnnnz##nMW*i*iiiiiiiii+z#zzz##++#+#++*+*"
              "***++++++++++*+++**************+**++++++#\nii*******iiiiii*i*****iiiii**iii*****+*****+MWMxMxxxxxxxWWz#"
              "znnxz#+*M@nxxnz##xW#i*iiiiiii+zzz#z####++#+++*++*****+*+++++++++++*+****+**********++++++#\n***********"
              "***i****++*******iii******+***iiiz@MWMxxMMxxnWWxznxnxnz#+MWxxnnzz+#x#iiiiii*+#z#####+++#++#++++++******"
              "*+*+++++**************ii******++####\n****+********+*************i*ii***iiiiii*ii*n@WMMxMMnznnW@Mnxxnxn"
              "z#+xMnxnnzz++#zi***++######++++++++++#++++********+++++++***+**********ii******++###z\n**++++*****+****"
              "+***++*+***iiiiiii********i*zWWMMMMnnMxxMMxxxxxxn#*;ix@@WWWxz+++i########+#+++++++*++#++++++******++**+"
              "**+**+*************i*****++##zz\n**++++**+**+++*+++++****ii*******++++*+*****#WMxMMMW@@@@@x#nxxnxn#i,;@"
              "@@WWW++##+;#########+#+++++++####++++*******+**++++**+++***i******iii******++##z\n**++++*+++++++****ii*"
              "****++**+***++*++*i+***#MxMMMW@W@@W@W+zxnnxz+i.+@@@@MMi++##*zzzzzzzzz#z#+*+++####+++++++*i*****+*+****+"
              "+*******+***iiii*ii***+++#\n*+++++*+**iiii**+++++++*+++***+*+++****i***i*xMMMMxWW@@@@@##xnnnn+i.zWM@MM*"
              ";###z+zxnnnnznzzz##++++##zz#++++++*+*+******+**+*+**********iiiiiiii****+++\n************++**+++++++*++"
              "+***+i+******iiiii+xMMMM##WM@@@@z#xnnnz+;,xWnnx+;zz##n+inxxxxnznzzz##+++#zz##+++++**+********+*********"
              "*iii***iii*ii*ii**+++\n***+++*****++++*+++++++i*++*+**i****iiiiiiii#xMMMx#iizW@@@Mznznnz+;:MMM#i*nnz+#n"
              "+;+nxxxxnnzzzzz#+++#z##+++++*****iii*****+********ii****iiiiii*ii**+++\n++++++*****+++**+++++++**+*****"
              "i***iii;;;ii;+xMMMxn#+*+M@@Wznzzzz+iiWWx*#nnzz+zz+;i#MMxxnnzzzzzzz#######++++******ii***++++**+********"
              "*ii;iiiiiii*+++*\n+++++++*++*+++**+++++++********i***i;;;i**+##xMMMMxnz##n@@Wxnzzzz#*#WMz#znznz#z#+ii+z"
              "MMxxnzzzzzzzzzznz####++***+++******+*+*********+***;;iiiiii**+#+*\n*+++*++*+++++++*+++++++iiii;;;iiiii*"
              "+#znnxxx#xxMMMxxz##zW@WMxnzz+*+zMMzzzzzzzz#++i;+#xMMxnnzzzzzzzzznnnz###+#++++++*i*************+++++****"
              "*iiii**+##+\n*++++*+**+++++***+++++iii;;i*++#znnxxxxn#*i;#MxMMWWMxnznWW@Wxn##++#nWMnzzzzzz#*+*ii+#zMMMx"
              "nnzzz#zzzzzznz#######++++*i***************++++****iiii**+##+\n*++*********+#++*++**i*+#znnxxxxxz#*;:,,,"
              ",:;zMxxMWWWMxnxWW@@Mxzzz#zx@xnzznznn#+++*i+##xMMMxnz#####zzzznzz#####+++++*iii*****+****+++++#****iiiii"
              "**+#++\n**+******+******++#znnxxMMxz+i;,.,,,:::::::izxxxMWWWWMMMWW@@WMnzzznWWznznnxx#++++*i+##nxMMMxnzz"
              "zzzzzznzzz#####++++#*i*ii******+++*+*+#+***ii******++++\n********i*+#znxxxxxxnz+i:,.,,::::::::::::::*zx"
              "MxxMWWWWWMMMW@WWMxxxxMx++#znz#+##+**i+#+nxxWMxxnz####zzzzzz#####++++#+***i******+++**+##+**++********+#"
              "#\n;i*++#znnxxxxxn#*;:,.,,::::::::::::::::::::*nMMMxxxMWWWWMxM@@WMxxMxMn**+##**+++++**+++zxxMMxxnz##zz#"
              "zzzz########+#++**************++++**+++*******+###\nzznnxMxxn#*;,.,,:::::::::::::::::::::::::::+zxMMMxx"
              "nxWWWxxx@@@WMMW@M+*+zn*i+***+***+++zxxxMMxnzzzzz##zzz##++####+++++**+********+++****++*********+###\nMM"
              "n#*;,.,,,:::::::::::::;;::::::::::::::::;#zxMMMxxnzxWWMxnx@#@WWWxi;#nxW*i****++i*+#+zxxxMMxnnzz##z#zzz#"
              "#+++####+++++++***+***********+++*ii****++#z#\n,,,,:::::::::::::;;;;;::::::::::::::::::::i#zxMMxxxnzz@@"
              "@MxzzM@@Wx;:;i*#x+++++*+**++++zxxnxxxxznzz###zzz#+++####+*+#+++****++*++++*********ii*****+#z#\n:::::::"
              "::::;;;;;::::::::::::::::::::::::::*zznxxMxxnzzWWMxnz##W@@n;;i#nnWi*ii*+++++####xxnxMxxnnnzzzzzzz###+##"
              "#++++##+***i*********************+**+#z#\n:::::;;;;;;:::::::::::::::::::::::::::::::*znnxxMxxnnzM@WWxnz"
              "z#WW#**i+nxn#+*i*+++++#z#zxxxxxMMnznzzzzzz#######++++++#+++***********************+***#z#\n::::::::::::"
              "::::::::::::::::::::::::::::::*nnxxxxxxnzznW@WMxxMzzMxxznxMMz+****+#+++###nxxxxxxMxnzzzznnzzz####++++++"
              "++++++****+**++*************+***###\n::::::::::::::::::::::::::::::::::::::::::innxxxxxxnnnznW@WWWMxWWx"
              "xxnMWz#+++#z#++++#z#nxxxxxnxMxnnzz#zzzz#####++++++++++**+*****++****i*********+*++##\n:::::::::::::::::"
              ":::::::::::::::::::::::::inxMMxxxxnnnzznWWWMMMMMMMxxMnzz#zznz++++###znxnxxxnxxxnznnz#zz######+++++**+++"
              "*++**++**++*iii***ii****++++#+\n::::::::::::::::::::::::::::::::::::;;;ii**nnxMMxxxxxnnnnnxxxxMxxxxnnzz"
              "zznzz#++++####znnnnMxnnxxnnnnzz##zz##zz##+*+*******+++++++***iii*+*****i*+###z#\n::::::::::::::::::::::"
              "::::::::::;;ii*****iinnxMMMxxxxxnnnznzzznnnzzzznzzzz#+*++++#####nnnnMMxnxMxxxnnnzzz#zzzzz##++*******+#+"
              "++***+**************+zzz+\n::::::::;;;ii***i;::::::::;;ii*****ii;;::,:nxxMMMxxxxxxnnnnnzzzzzzzznnz###++"
              "*++++###zzznnnxxnnnnxxxxnnnnnzzzzzzz#+++*******+++*******++**+***+**+##zz*\n:::iii***+#####+*iii;;;ii**"
              "***i;;:::,,,,,,:nnxMMMMxxxxxnnnnnzzznzzzzznz##++***++#####znnnznxxnnnxMxxxnnnnzzzzznz#+++++++*ii*+*****"
              "+******+++*++++##z#i\nii####++####zznnz##+++***i;;:::,:,::::,,,::nnxMMMMMxxxxnnnnnzzznnz##znz#++***+++#"
              "##zzznzznnxxnzzxMMxxxnnnnnnnnnnz##++#++**i**********ii**++++++#++++*i\nznzz######zznnnnnnzzz####++*ii**"
              "**ii;;;::::nxxxMMMMMMxxxnnnzzzzzzz##zzz#++**++++####zzznzznnxnnznxMWxxxxnnnnnznnnnz###+*iiii*++***++**i"
              "****+++##+++*i;\nxxxxnnzzzzzzzznnnzzzzzzz###nnxxxn#i;::::;;izxxxMMMMMMMxxxnnnzzzzzz######++*+++++#z#z#n"
              "zzzznnnnzzznxWMxxnnnnxxnxxxnnz##+*iiiii*++***********+++++++*i;;\nMMMMMxxnzzznnnnnnnzzzzzznzz#znxxz+i;"
              "*++###nxxxMMMMMMMMMxxnnnzzzzzz#####+*+#+####zz##zzzzznnnnzzzznMWMMxnnxnnnxxxxxnz##+*iii**+**++***++*++*"
              "++++**i;;;\nMMMMxnnzz#zzzzznnnzz####zznnnzznnxnnxnnznnzxxxxMMMMMMMMxxxxnnzz##zz######++++####zz#zzzzzzz"
              "nnnzzzznxMMMMxxnxxxnxxxxxnz##*iiii*+***+++*++++**++++*;::::\nxMMMMMxnz###zzzzzznnnzz###znxxnznnxMMxxxnn"
              "nnxxxMMMMMMMMxxxnnzz###zzzz##++++++#+#zzz#zznnzzznnzzz#zznxMMxxxnnnxxxxMMMxnz#*i;;i*++*****ii**+*+##+*;"
              ":::::\nnxMWMxz####zzzzzz##znnz#######zzznnnxMMxxxxxxxxxMMMMMMMxxnnzz#zzzzzzz##++++++###zz##znnnzzznnnzz"
              "#zznxxMMMMxnnxxnxxMMxnn#+*i;ii*******i*i**++++*i:::,,,\nznxMMMn##z#zzznnznzzz+++++#+++####znxMMMMnnMxxx"
              "MMMMMxMxxxn#####znzzzzz#++++#+##zz#zzznnnnnzznnnzzzznnxMMxxxxxxxxxxxMxxnz#+i;;;i******+*+***+*i;::::,,,"
              "\nnnxMMxnnnznnnxxxxMxnz+++#######zzzzxxxxxzzxMxxMMMMMMMMxxn##+++##zznzzz#+++####znz##zznnnnnnnznnnz#zzz"
              "xxxxxxxxxxxxxxxxxnzz#*i;iii***++++++++*i;::;;;:::\nzznxxxxxnzznxxxMMMMxz#+##znnnnnnxxxxxxxnnzMMMxMMMMMM"
              "MMMxnz#***++#znnzzz#+*+###zzzz#zznnznnnnnnnnzzznznxxxxxxxxxxxxxxxnznnz+*i;ii***++**+++**i;;;;;;;::\n#zn"
              "nxMxxzznxxxMWWWMMxnzzzzznnnnxMWWxxMxnnnMWMMMMMMMMMMxxn#+*iii*+#zz###+##+###z###z#znnnnnnnnnnnzzzzzznxxx"
              "xxxxxxxxxxxnnzxn+i;;;i********+***i;;;ii;::,\n##zxMMMnnnnxMWWWWWWMnzzzznnxxxxMWWWMMMMMxxMWWMMMMMMMMxnz#"
              "++*ii;;i*++##+#+#+#####+###zznnnnnznnnnnnnzzzznxxxxxxnxxxxxnnnzzn#;::;;ii**ii**+*iii;;i*i:,,.\nnzzxMMxx"
              "xxxxMWWWWWWMxnnnnnxxMMMMWWWMMWWMxMMWWWMMMMMMxnz#+**iiiii;i**+++#+++#########zznnnnnnnzznnnnzzzznnxxnxxx"
              "xxxxxxnnzzz+;::;i***i;ii**ii;i;i*;:,...\nnnnxMMnnzznnxMWWWWMMxnnxxxxxMMMWW@@WWWWMMMMWWWMMMMMxxzz#**iiii"
              "iiii**++++##+###++##+##zznnnnnzzznnxxnzzzznxxxxxnxnnnxxnnzz#+i::;iii*i;;i*i;::,,,,......\nxxnnMMMxxnnxM"
              "MWWWWWMxxnnxxxxMWWWWW@@W@@WMWWW@@WMMMMxxn#+****i**ii***+##+######+++#+##zznnnnnnzzznxnnnzzzznnxxxxnnnxn"
              "nnnzz##*;;;iiiiii**i;:,...........\nxxxxMWWWMMxxMWWMMWWMxxxxxxMxMWWWW@@@@@@@MWWW@@WWMMMxnz#+*+*********"
              "++++##+++++++++++#zzzznnnzzznnxnnnzzzzznnxnnnxxxnnxnnnz##+*i;;;i;;::,,.............\nnxxxMWWWMMMMWWWMMM"
              "MMxxxxMxMMMWWWWW@@@@@@WMMWW@@WMMMxz###+*******+++++##++++++++#++++#zzzznnnnznnznnxnzzzznnnnnnnnnnnnnxnz"
              "zz##+*i;:,...................\nxMMMMWWWWMxxWWWMMMMxxxxMMMMMMWWWWWW@@@@@WMMMW@@@WMMMxnz#++*+*++++##+++++"
              "+***++++++++++zzznnnnzznznnnnnzznnnnzzznnnnnnnnnnnzz#+++*;,...................\nxxxMWWWWWWMMMWWWMMMxxxM"
              "MMMMMMWWWWW@@@@@@WMMxMW@@WMMxxxzzz#++++++#+++++##+**++******++##zznnnnnnnnnnnnznzznnnnnnzznnnnnnznnnnz#"
              "##+*i:,.................\nxxMMWWWWWWWWWWWWMMMxxxxxMMMMxMWWWWW@@@W@WxxnxMM@@WMxxxnzz##++##+++++##+++*+++"
              "+*****+++###znnnnnnnnnnnnzzznnzzzznnzzzzzzzzzznnz#+#+ii,.................\nMMMMMW@@WWWWWWWMMMxxxxxxxMMM"
              "xMWWWWW@W@@@WnnnnxMWW@WMMxxnzz#+++++#++++#+++*********+++##z#znnnnnnnnnzzzzzznnzzzznznnnnnnnzzzzzz###+*"
              "i;.................\nxMMMWW@@WWMMWWWMxxxxxxxxxxMMMMMMMWWWWWW@xnnxxMMWWW@WMMxxnz#++++#++++###++*****+***"
              "*++#####znnnnnnnnnzzzzzzzznnnnzzzznnnnzz########+*i,................\nxxMWWWWWWMMMMWWMMxxxxxxxxxxMWMMxn"
              "xMWWW@xnxnnxxMMMMMMxMMxxxnzz#+#+*++++++****+*++++++####zzznnnznnnxnnnnzzzzzzzzzzzznnnnnnzz######++**,.."
              "..............\nnxxMMMMWMMMMMWWWMMMxxxxxxxxxMMMxxnxMW@WnxnnnnxMxMxxz#znnxxxxxn##+###**+*++****++++++#zz"
              "z##znnnzznnxxxxnzzzzzzzznzzznnnnnnnz######+++i...............``\nxxxxxxxxMxxxxMWWWMMMxxxxMMxxxMxxxxMMMW"
              "MnzznnnxxxMn##++#zznnnnzzzzzz#++++*#*****+#######zz#znznnnznxxxxxnnzzzzznznnzznnnnzz#########+,........"
              ".......``\nxMMWMMxxxxxnnnxMWWMMxxMMxMMMxxnnxMMMWWMnznnnxxxxxxn#+##zzzznnnnnnnzz#++#+##+***++zzz###zzzzz"
              "nxnnnznxxxMxxnnzz##zzzzzznnnzzz###+###+*............``.```\nWMMMMMWWMxnzzzzxMWWMMxMMxxMMMxxznxMWWWxnznx"
              "xxxxnnnxzzznxxxnxxxxxxnnznnzz###++++++##++##z###zzxxnxnnxxMMxxxnn#+++#z###zznzzzz#######+,...........``"
              ".```\nWWMMWWMMxxxxnzznnMMMMxxxxxxMMMxnznMW@WMnnxxxxxnzznnxxnxxxxxxxxxxxnnnnxnnn#z+++++++++##z##z#+zxxxx"
              "nnxMMMMMxxz#++#######znzzzzzz#####+i...........`.`..,\nxMWMMMMMxxxxxxnnnMMMMxxxxxxxxxxxxnMW@WWxnxxxnz##"
              "znnxxxxxxxxnzzzznxxnnMxxMMMnzz#z#+i++#zz##++zznxnnxxMMMMMxxn######z###zzzzzzzz###+#++,.......`..,,:;ii\n"
              "nMxxMMMMMMMxxxxnzzxMMMxxxnnnnxxnnxMxW@WWxxxxnz#+zznnnxxxMMx"
              "nnz###znnnnxxxxxnz#n#zz*i+*####+#zznxnznxMxMMW"
              "WWMxnzzzzz###zzznnzzz#z#####+:.....,,:;iiiiii\nWMMMMWWMMMMxxxnnnnxxxxxnzzzznnnznMMW@@Mxxxnz##zzzznnxxxx"
              "xnzznnnzzznnnnxnxxz#+#++*****+#+++##znxnnMxxxxMMWWWMxnnnzzzzzzzzzzzzzzz#####+;.,::;iiiiiiiiiii")
        print("--------------------------------------------------------------")
        run()
    elif question == "troll" or "trolled":
        print("--------------------------------------------------------------")
        print("░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░\n░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░\n░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░\n░░░█░"
              "░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░\n░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░\n█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█\n█░▒█░█▀▄▄"
              "░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█\n░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░\n░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░\n░░░█░░░░██░░▀"
              "█▄▄▄█▄▄█▄████░█░░░\n░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░\n░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░\n░░░░░░░▀▄▄░▒▒▒▒░░"
              "░░░░░░░░▒░░░█░\n░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░\n░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░")
        print("--------------------------------------------------------------")
        run()
    else:
        print("try again.")
    time.sleep(0.5)


# nathans code below this


def solutions():
    print("--------------------------------------------------------------")
    print("Now you know the dangers of increased levels of fossil fuels in the atmosphere. "
          "Let's see if you can fix it.")
    time.sleep(3)
    fix_it()


def fix_it():
    print("We will give you a few options as solutions. "
          "You can go through the program multiple times to see what needs to be done.")
    time.sleep(3)

    def first_handler():
        print("have you learned nothing? \n try again.")
        time.sleep(5)
        life()

    def second_handler():
        print("If we stopped greenhouse gas emissions today, global warming could be stopped by 2033. "
              "However, this is extremely impractical, as it would cause many people to lose their jobs, "
              "and the world wouldn't really function. "
              "\n We need to transition to renewal energy resources over a slightly longer period of time.")
        solutions()

    def third_handler():
        print("This is the best option. However, once we reach 2030, we will need to make another decision.")
        q2()

    def question():
        print("How do you want to fix climate change?")
        print("1: do nothing")
        print("2: completely stop greenhouse gas emissions today")
        print("3: follow the plan President Biden recently outlined: "
              "Reduce emissions by 50% from 2000-2005 levels by 2030")
        print("------------------")
    question()
    answer = input(" Type in one answer:\n type [1], \n type [2], \n type [3] \n \n $")
    handlers = {
        '1': first_handler,
        '2': second_handler,
        '3': third_handler
    }
    if answer in handlers:
        handlers[answer]()
    else:
        print("Unknown choice", answer)
        fix_it()


def q2():
    print("once we've reached 2030, we have to decide what to do in the future. There are 2 basic options.")

    def first_handler1():
        print("This is the wrong choice. The process outlined in the beginning will happen, albeit at a slower rate.")

    def second_handler1():
        print("This is the only way to stave off the problems outlined in the first part of the program\n")
        answer_1 = input("press [1] to understand the dangers of sea levels rising\n \n $")

        if answer_1 == "1":
            q3()
        else:
            print("unknown choice")
            second_handler1()

    def question1():
        print("1: stop our efforts here, and live life as it currently is.")
        print("2: continue phasing out fossil fuels, and eventually use all renewable resources.")

    question1()
    answer = input("Type in your answer now \n type [1], \n type [2]\n \n $")
    handlers = {
        '1': first_handler1,
        '2': second_handler1
    }
    if answer in handlers:
        handlers[answer]()
    else:
        print("Unknown choice", answer)
        q2()


def q3():
    print("let's see some consequences of global warming:\n\n --------")
    time.sleep(2)

    def first_handler2():
        print("If this were to happen, sea levels would rise by as much as 230 feet. "
              "One study showed that if sea levels rose 250 feet, "
              "the city of Montreal would be completely flooded, save for Mont Royal, "
              "with just a little bit of it peeking up above the water. (source: weather.com)")
        time.sleep(3)
        other1 = input("press [1] to view what happens if the ocean temperature rises by 2 degrees C. "
                       "Press [2] to end\n\n$")
        if other1 == "1":
            second_handler2()
        else:
            pass

    def second_handler2():
        print("Although this situation is far less drastic then the other, it is far more likely. "
              "If ocean temperatures rose by 2 degrees C, sea levels would rise by as much as 0.66 feet, "
              "flooding most coastal cities. This would also make storm surges far more dangerous. (source:nasa)")
        time.sleep(3)
        other = input("press [1] to view what happens if all of the polar ice caps melt\n\n Press [2] to end \n \n$")
        if other == "1":
            first_handler2()
        else:
            pass

    def question2():
        print("1: see what happens if all of the polar ice caps melt")
        print("2: see what happens if the ocean temperature rises by 2 degrees C")
        time.sleep(1)
    question2()
    answer = input("Type in your answer now \n type [1], \n type [2]\n \n $")
    handlers = {
        '1': first_handler2,
        '2': second_handler2,
    }
    if answer in handlers:
        handlers[answer]()
    else:
        print("Unknown choice", answer)
        q3()


run()
