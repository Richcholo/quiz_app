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
                "Which company created Minecraft?": "Mojang",
                "Which game has characters like Garen and Katarina?": "League of Legends",
                "In what game do you battle using creatures called 'Pocket Monsters'?": "Pokemon",
                "What horror game series where you have to survive until 6 am?": "Five Nights at Freddy's",
            },
            "Music": {
                "Who is known as the 'King of Pop'?": "Michael Jackson",
                "Who created the album 'BALLADS 1'?": "Joji",
                "What genre of music known for heavy bass and beat drops?": "Dubstep",
                "Which band released the album 'A Rush of Blood to the Head'?": "Coldplay",
                "Who is the lead singer of the band 'Queen'?": "Freddie Mercury",
            },
            "IT Questions": { 
                "What does 'HTTP' stand for?": "HyperText Transfer Protocol",
                "Who is the creator of java programming language?": "James Gosling",
                "Which programming language is known for its snake logo?": "Python",
                "What does 'GUI' stand for in computing?": "Graphical User Interface",
                "What year was the World Wide Web invented?": "1989",
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