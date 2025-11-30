# NOTE: tapos na main logic, meron nang scoring system
# TODO: Expand yung quiz para TEN QUESTION EACH and add kayo 2 new topics
# TODO: Add a save_highscore() function to write the best score to a .txt file,

import random

class Quiz:
    def __init__(self):
        self.score = 0
        self.current_topic = None
        self.q_index = 0 
        
        # Note: Keys here must match the text in index.py buttons exactly
        self.questions = {
            "Gaming": {
                "What game features the phrase 'Finish Him'?": "Mortal Kombat",
                "What famous game did 'Mojang' create?": "Minecraft",
                "Which game has characters like Garen and Katarina?": "League of Legends",
                "In what game do you battle using creatures called 'Pocket Monsters'?": "Pokemon",
                "What horror game series where you have to survive until 6 am?": "Five Nights at Freddy's",
                "What game is 'Gamefreak' known for?":"Pokemon",
                "What game is the currency 'V-bucks' from?":"Fortnite",
                "What game won the 'Game of the Year' at The Game Awards 2022":"Elden Ring",
                "What game did the genre 'souls-like' came from?":"Demon's Souls",
                "What game is Artorias from?":"Dark Souls",
            },
            "Music": {
                "Who is known as the 'King of Pop'?": "Michael Jackson",
                "Who created the album 'BALLADS 1'?": "Joji",
                "What is the artist name of Chris Comstock?": "Marshmello",
                "Who was suspected to kill a 15year old girl?": "d4vd",
                "Who is the lead singer of the band 'Queen'?": "Freddie Mercury",
                "Which famous singer star in Stranger Things?":"Djo",
                "Whose music was commonly used in gaming channels' intro?":"Alan Walker",
                "Who is the lead singer of the band 'Panic!At the Disco'":"Bredon Urie",
                "What was Freddie Mercury's real name?":"Farrokh Bulsara",
                "Which singer died from taking a shit?":"Elvis Presly",
            },
            "Who's that Champion?": { 
                "Which champion has to meet someone and deliver them their weapon?": "Poppy",
                "Cassiopeia has a biological sibling. Who is it?": "Katarina",
                "Who chases Jhin?": "Shen",
                "Who was responsible for building the Howling Abyss?": "Ornn",
                "Which champion is originally called Ignacarious Gigantareno Rex Le Spes Offerentis?": "Smolder",
                "Which champion has Sarah as their birth name?":"Miss Fortune",
                "Who created Blitzcrank?":"Viktor",
                "Who was Yasuo's apprentice?":"Taliyah",
                "Who is connected to the primordial demon of Joy":"Nilah",
                "Who made a contract with the Watchers?":"Lissandra",
            },
            "Movies": {
                "A story about a boat and a necklace":"Titanic",
                "My dog died, me go kill people":"John Wick",
                "Millionaire guy fighting a guy who just laughs":"The Dark Knight",
                "I ate apple, I go sleep":"Snow White",
                "A group of people takes a really looong walk to destroy a piece of jewelry":"Lord of the Rings",
                "An old man kidnaps a smol boi using balloons":"Up",
                "My eyes turned blue, me go become Emperor":"Dune",
                "A chicken was taken on a boat trip":"Moana",
                "Bro takes steroids, and now fights Nazis":"Captain America",
                "Murders 4 children while his slaves clean up the mess":"Willy Wonka",
            },
            "Math": {
                "52 Divided By 4 Equals?":"13",
                "What is the least common multiple of 6, 8, and 12?":"24",
                "An improper fraction must always be bigger than what number?":"1",
                "What is the next number in the Fibonacci Sequences 0,1,1,2,3,5,8,13,21,34?":"55",
                "What is the only number that is written in alphabetical order?":"40",
                "What is the sum of the other four faces on a dice if you throw a six?":"14",
                "Which number is the only one whose meaning can be written in the same number of letters?":"4",
                "Which of the first ten numbers is the most prime?":"7",
                "What is the sum of a triangle's interior angles?":"180",
                "Which prime number is the only even one?":"2",
            }
        }

    def start_topic(self, topic):
        self.current_topic = topic
        self.q_index = 0
        self.score = 0

    def get_question_data(self):
        topic_data = self.questions[self.current_topic]
        questions_list = list(topic_data.keys())

        # Check if we ran out of questions
        if self.q_index >= len(questions_list):
            return "Quiz Finished", []

        current_q_text = questions_list[self.q_index]
        correct_answer = topic_data[current_q_text]

        # Generate Options Logic
        
        # 1. Get all possible answers in this topic
        all_answers = list(topic_data.values())
        
        # 2. Filter out the correct answer so we only have wrong ones
        wrong_answers = [ans for ans in all_answers if ans != correct_answer]
        
        # 3. Pick 3 random wrong answers
        # (Note: This requires at least 4 total questions in the topic dictionary to work)
        options = random.sample(wrong_answers, 3) 
        
        # 4. Add the correct answer and shuffle
        options.append(correct_answer)
        random.shuffle(options)

        return current_q_text, options

    # Checks the user's answer, updates score, and moves index
    def check_answer(self, user_choice):
        topic_data = self.questions[self.current_topic]
        questions_list = list(topic_data.keys())
        
        # Get correct answer for current question
        current_q_text = questions_list[self.q_index]
        correct_answer = topic_data[current_q_text]

        if user_choice == correct_answer:
            self.score += 1
        
        # Move to next question automatically
        self.q_index += 1

    def save_highscore(self):
        # Save highscore per topic with a simple key-value format
        highscores = {}
        try:
            with open("highscore.txt", "r") as file:
                for line in file:
                    if ':' in line:
                        topic, score = line.strip().split(':', 1)
                        highscores[topic] = int(score)
        except (FileNotFoundError, ValueError):
            pass

        topic = self.current_topic
        prev_high = highscores.get(topic, 0)

        #Compare and save if current score is higher
        if self.score > prev_high:
            highscores[topic] = self.score
            with open("highscore.txt", "w") as file:
                for topic, score in highscores.items():
                    file.write(f"{topic}:{score}\n")
            return True
        return False

    def get_highscore(self, topic):
        # Load highscore for a specific topic
        try:
            with open("highscore.txt", "r") as file:
                for line in file:
                    if ':' in line:
                        t, score = line.strip().split(':', 1)
                        if t == topic:
                            return int(score)
        except (FileNotFoundError, ValueError):
            pass
        return 0