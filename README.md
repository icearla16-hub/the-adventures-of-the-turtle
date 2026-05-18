# The Adventures of the Turtle
___What was that noise?___

_You whip your head around, anxiously scanning the trees for whomever just snapped that twig. You quickly weigh your options: make a run for it, pick a fight, or freeze until the threat reveals itself—_

_—as a bunny. It's casually chewing on a piece of grass, looking so unbothered that you almost feel like it's mocking you. With a sigh of relief, you continue on your way._

You're on the run after stealing the local dictatorship's crown jewels. As the guards close in behind you, there's only one thing standing between you and freedom: the infamous forest surrounding the kingdom. Make it through, and you're home free—the jewels are enough to pay your debts and establish the life of your dreams. Get caught, however, and the rest of your days will become a nightmare. With only your wits to guide you, what will your fate be?


## What is our project about?
Our project is a choose-your-own-adventure personality test. Users face situations within the storyline, and their decisions inform the path they take through the forest, culminating in a unique ending that reveals something about their personality.


## Function Descriptions
Functions cover three major domains: making the Tkinter display, controlling the Turtle within the Tkinter window, and handling files with questions, answer options, and user data.

- `survey.py` - Reading in the file for the questions, asking the questions and offering answer choices, and saving the response from the user
- `questions.txt` - List of questions
- `responses.txt` - Stores list of answers from user
- `answer_options.csv`- List of options for answers (labeled A, B, C)
- `counting.py` - Counts the amount of times that the use r has chosen each choice (A, B, or C), and gives output of which option the user had chosen the most
- `display.py` - The display + turtle class
- `main.py`- Putting it all together (this is what you run to play the game)


## How do you run our project?
Clone the repository with 'git clone https://github.com/icearla16-hub/the-adventures-of-the-turtle.git'. Run the main.py function using 'uv run python main.py'.


## Testing
After executing 'uv run python main.py', users should see:
1. A Tkinter GUI with a Turtle in a forest, questions, and buttons.
2. Questions should prompt the user to make a response with buttons labeled "Option A", "Option B", and "Option C".
3. Upon making a response, the Turtle should move, and the next question is given.
3. The Turtle should stop seven times, asking the user to answer seven questions.
4. At the very end, the user should be shown a conclusion of which personality their choices line up with depending on their choices throughout the game.