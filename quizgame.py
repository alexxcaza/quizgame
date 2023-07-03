def textclean(message, LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "):
  message = message.upper()
  new = ''
  for char in message:
    if char in LETTERS:
      new += char
  return(new)
correct_score = 0
print('Welcome to the quiz!' )


playing = input('Do you want to play? ')
playing = textclean(playing)

if playing != "YES":
    quit()

print("Ok, let's play")

answer = input("Which quiz would you like to take??   \nA.)DC  \nB.)Marvel   \nC.)Marvel or DC   \nD.)Marvel or DC(hard)   \nAnswer Here: ")
answer = textclean(answer)
if answer == "A":
  answer = input("What is Super Man's real name?   \nA.)Justin Rodgers   \nB.)Bruce Wayne   \nC.)Clark Kent   \nD.)Super Man is his real name   \nAnswer Here: ")
  answer = textclean(answer)
  if answer != "C":
    print('Incorrect!')
  else:
    print('Correct!')
    correct_score += 1

  answer = input("What happened to Batman's parents?   \nA.)They put him up for adoption   \nB.)They were robbed and killed   \nC.)Nothin happened \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "B":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  answer = input("How did Flash get his powers? \nA.)He was born with them   \nB.)He is an alien   \nC.)A science expiriment gone wrong   \nD.)It is technology   \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "C":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  answer = input("What is Super Man's weakness? \nA.)He has none  \nB.)Kryptonite \nC.)Water \nD.)Aluminum  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "B":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  answer = input("Who raised Batman? \nA.)Nobody, he had to raise himself   \nB.)Alfred \nC.)Superman \nD.)His uncle  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "B":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  answer = input("Are there other's with powers like Green Lantern? \nA.)No  \nB.)Yes    \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "B":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  answer = input("Who fights Batman and ends up snapping and breaking his back? \nA.)Bane   \nB.)Joker   \nC.)Brianna Caza   \nD.)Lex Luthor   \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "A":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')
    
  answer = input("Where does Superman work? \nA.)The Daily Bugle   \nB.)New York Times  \nC.)The Daily Bugle   \nD.)LAPD   \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "C":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  answer = input("How far can Darkseid teleport? \nA.)Throughout space and time  \nB.)Between planets \nC.)To other countries \nD.)Across cities  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "A":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  answer = input("Has anyone ever broken a Green Lantern ring? \nA.)No   \nB.)Yes     \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "B":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  answer = input("Why did Penguin become evil? \nA.)He was born into a family of crime   \nB.)He just felt like it  \nC.)He was bullied for being short and having a long nose   \nD.)His friend made him   \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "C":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  answer = input("What is the Riddler's birth name? \nA.)Bruce   \nB.)Liam   \nC.)Edward   \nD.)Brian   \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "C":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  answer = input("Who is Batman's arch-enemy? \nA.)Bane   \nB.)Joker   \nC.)Riddler   \nD.)Penguin  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "B":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  answer = input("Where did Batman train? \nA.)At a karate dojo in Gotham  \nB.)His parents taught him   \nc.)a monestery in the mountains \nD.)He looked up youtube videos \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "C":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  answer = input("Who did Robin become? \nA.)Jason Todd   \nB.)Joker  \nC.)Riddler   \nD.)He took on a regular life  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "A":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  print("You got " + str(correct_score) + " questions correct")
  print("You got " + str(correct_score / 15 *100) + "%")
  if correct_score >= 12:
    print("Amazing job! ")
  if correct_score ==11 :
    print("Good job!")
  if correct_score ==110 :
    print("Good job!")
  if correct_score ==19 :
    print("Good job!")
  if correct_score <= 8:
    print("It's ok, keep trying!")
    




elif answer == "B":
  answer = input("What is spider-man's real name?   \nA.)Peter Porker   \nB.)Peter Parker   \nC.)Tony Stark   \nD.)Steve   \nAnswer Here: ")
  answer = textclean(answer)
  if answer != "B":
    print('Incorrect!')
  else:
    print('Correct!')
    correct_score += 1

  answer = input("Is Iron Man rich or poor?   \nA.)Rich   \nB.)Poor  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "A":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  answer = input("Was Captian America ever an Avenger? \nA.)No   \nB.)Defnitely Not   \nC.)Maybe   \nD.)Yes   \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "D":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  answer = input("Is Thor from Asgard or Earth? \nA.)Asgard  \nB.)Earth  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "A":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  answer = input("Can any other avenger lift Thor's hammer? \nA.)No   \nB.)Yes  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "B":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  answer = input("Who fixed Ultron? \nA.)Spider Man  \nB.)Tony Stark   \nC.)Einstein  \nD.)Brianna Caza   \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "B":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  answer = input("In Spider-Man Homecoming, is Spider Man in High School, College, Middle School, or none? \nA.)High School   \nB.)College   \nC.)None   \nD.)Middle School   \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "A":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')
    
  answer = input("In Civil War, who's team does Spider Man join? \nA.)Aunt May   \nB.)Hulk  \nC.)Iron Man   \nD.)Captain America   \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "C":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  answer = input("Does Hawkeye have children? \nA.)Yes  \nB.)No  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "A":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  answer = input("How long was Captain America frozen for? \nA.)12 years   \nB.)4 years  \nC.)300 years   \nD.)66 years   \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "C":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  answer = input("Who is Thor's brother? \nA.)Captain America   \nB.)Captain Marvel  \nC.)Loki   \nD.)Odin   \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "C":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  answer = input("What is Hulk's real name? \nA.)Bruce Banter   \nB.)Bruce Baner   \nC.)Bruce Banner   \nD.)Bruce Bannner   \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "C":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  answer = input("What color is Hulk's skin? \nA.)Green   \nB.)Purple   \nC.)Blue   \nD.)Rainbow  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "A":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  answer = input("Does Captain America approve of curse words? \nA.)No  \nB.)Yes   \nc.)Sometimes  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "A":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  answer = input("How many Infinity Stones are there? \nA.)4   \nB.)5  \nC.)3   \nD.)6  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "D":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  print("You got " + str(correct_score) + " questions correct")
  print("You got " + str(correct_score / 15 *100) + "%")
  if correct_score >= 12:
    print("Amazing job! ")
  if correct_score ==11 :
    print("Good job!")
  if correct_score ==110 :
    print("Good job!")
  if correct_score ==19 :
    print("Good job!")
  if correct_score <= 8:
    print("It's ok, keep trying!")

  
  










elif answer == "C":
  answer = input("Is Aquaman from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer != "B":
    print('Incorrect!')
  else:
    print('Correct!')
    correct_score += 1

  answer = input("Is Black Panther from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "A":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  answer = input("Is Groot from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "A":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')


  answer = input("Is Blue Beetle from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "B":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')


  answer = input("Is Green Lantern from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "B":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')


  answer = input("Is Star Lord from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "A":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')


  answer = input("Is Thanos from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "A":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')
    

  answer = input("Is Riddler from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "B":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')


  answer = input("Is Superman from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "B":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')


  answer = input("Is Spider Man from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "A":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')


  answer = input("Is Iron Man from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "A":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')


  answer = input("Is Scarlet Witch from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "A":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')


  answer = input("Is Captain America from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "A":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')


  answer = input("Is Joker from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "B":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')


  answer = input("Is Batman from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "B":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  print("You got " + str(correct_score) + " questions correct")
  print("You got " + str(correct_score / 15 *100) + "%")
  if correct_score >= 12:
    print("Amazing job! ")
  if correct_score ==11 :
    print("Good job!")
  if correct_score ==110 :
    print("Good job!")
  if correct_score ==19 :
    print("Good job!")
  if correct_score <= 8:
    print("It's ok, keep trying!")
    



elif answer == "D":
  answer = input("Is Vision from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer != "A":
    print('Incorrect!')
  else:
    print('Correct!')
    correct_score += 1

  answer = input("Is The Atom from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "B":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  answer = input("Is Red Tornado from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "B":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')


  answer = input("Is Urthona from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "A":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')


  answer = input("Is Cypher from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "A":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')


  answer = input("Is The Creeper from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "B":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')


  answer = input("Is Frog Thor from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "A":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')
    

  answer = input("Is Madcap from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "A":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')


  answer = input("Is Moondragon from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "A":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')


  answer = input("Is Plastic Man from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "B":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')


  answer = input("Is Black Canary from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "B":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')


  answer = input("Is Vixen from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "B":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')


  answer = input("Is Ka-Zar from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "B":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')


  answer = input("Is Machine Man from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "A":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')


  answer = input("Is Darkseid from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
  answer = textclean(answer)
  if answer == "B":
    print('Correct!')
    correct_score += 1
  else:
    print('Incorrect!')

  print("You got " + str(correct_score) + " questions correct")
  print("You got " + str(correct_score / 15 *100) + "%")
  if correct_score >= 12:
    print("Amazing job! ")
  if correct_score ==11 :
    print("Good job!")
  if correct_score ==10 :
    print("Good job!")
  if correct_score ==9 :
    print("Good job!")
  if correct_score <= 8:
    print("It's ok, keep trying!")