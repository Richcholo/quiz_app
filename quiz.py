# TODO: CREATE CLASS 
# TODO: ADD SET OF QUESTIONS AND ANSWERS (USE DICTIONARY) (GROUP IT INTO TOPICS) (USER SELECTS TOPICS)
# TODO: ADD METHOD TO ASK QUESTIONS AND GET USER INPUT
# TODO: ADD METHOD TO CHECK ANSWERS AND CALCULATE SCORE
# TODO: ADD METHOD TO DISPLAY FINAL SCORE
# TODO: ADD METHOD TO RESTART QUIZ
# TODO: ADD METHOD TO EXIT QUIZ

class Quiz:
    def __init__(self):
        self.questions = {
            "Gaming": {
                "What game features the phrase 'Finish Him'": "Mortal Kombat",
                "Which company created Minecraft?": "Mojang",
                "Which game has characters like Garen and Katarina?": "League of Legends",
                "In what game do you battle using creatures called 'Pocket Monsters?": "Pokemon",
                "What horror game series where you have to survive until 6 am?": "Five Nights at Freddy's",
            },


            "Music": {
                "Who is known as the 'King of Pop'?": "Michael Jackson",
                "Who created the album 'BALLADS 1'?": "Joji",
                "What genre of music known for heavy bass and beat drops?": "Dubstep",
                "Which band released the album 'A Rush of Blood to the Head'?": "Coldplay",
                "Who is the lead singer of the band 'Queen'?": "Freddie Mercury",


            },

            "IT Related Questions": {
                "What does 'HTTP' stand for?": "HyperText Transfer Protocol",
                "Who is the creator of java programming language?": "James Gosling",
                "Which programming language is known for its snake logo?": "Python",
                "What does 'GUI' stand for in computing?": "Graphical User Interface",
                "What year was the World Wide Web invented?": "1989",
            }
        }    

         