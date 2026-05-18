# Constants
question_file = "questions.txt"
answer_options_file = (
    "answer_options.csv"  # Three answer options are given per question.
)
response_file = "responses.txt"  # A response is the answer option the user chooses.


# opening the question file and creating a list of the questions from questions.txt
def get_question(question_file):
    with open(question_file, "r") as fh:
        question_list = [line.strip() for line in fh]
    return question_list


# opening the .csv file with the answer options, and saving the options
def get_answer_options(answer_options_file):
    with open(answer_options_file, "r") as fh:
        answer_options_list = [line.strip("\n").split(",,") for line in fh]
    return answer_options_list


# saving the answers to responses.txt
def save_answers(response):
    with open(response_file, "a") as file:
        file.write(f"{response}\n")