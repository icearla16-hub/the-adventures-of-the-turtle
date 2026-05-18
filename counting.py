response_file = "responses.txt"


def count(file_path):
    counts = {"a": 0, "b": 0, "c": 0}

    with open(file_path, "r") as fh:
        for line in fh:
            letter = line.strip().lower()
            if letter in counts:
                counts[letter] += 1
    return counts


# I thought about this function based on the survey.py assignment where we had to
# count our results and focused on adding a score based on the letter and making sure the baseline was at zero to start with


def specific_personality(counts):
    a, b, c = counts["a"], counts["b"], counts["c"]
    if a > b and a > c:
        return "you are the A personality. Despite the possibility of being harmed, you always choose to help."
    elif b > a and b > c:
        return "you are the B personality. You are a practical person who chooses to help when it does not hurt you, but you will not risk yourself unnecessarily."
    else:
        return "you are the C personality. You are a focused person, reliant on only your skills to reach your goals."


# This function was for the specific personalities and making sure based on the score of a's, b's, and c's, only the highest score returns the specific personality distinction based on the counts.


def ties(counts):
    a, b, c = counts["a"], counts["b"], counts["c"]
    max_value = max(a, b, c)
    winners = [letter for letter, count in counts.items() if count == max_value]
    if len(winners) > 1:
        tie = {
            "a": "A personality (despite the possibility of being harmed, you always choose to help)",
            "b": "B personality (you are a practical person who chooses to help when it does not hurt you, but you will not risk yourself unnecessarily)",
            "c": "C personality (you are a focused person, reliant on only your skills to reach your goals)",
        }
        results_for_tie = [tie[i] for i in winners]
        return f"Based on the choices you have made in your path, we believe you are a mix of two personalities. We believe you are both {results_for_tie[0]} and {results_for_tie[1]}! We hope these test results let you understand more about who you are and the decisions you tend to make. Thanks for playing our game!"
    return None


# This function I had to create because in case both letters had the same score. We decided in this special case to have a mix of both personalities rather than just pick one so I created a ties function.
# This ties function used the dictionary of counts with the classifications and returns a mix of personalities if there is a tie of the same highest score.


def results():
    data = count(response_file)
    checking_if_tie = ties(data)
    if checking_if_tie:
        return checking_if_tie
    else:
        personality = specific_personality(data)
        return f"Based on the choices you have made, {personality}\nWe hope these test results let you understand more about who you are and the decisions you tend to make. Thanks for playing our game!"


# This function was just to show results based on the responses from the response file.

if __name__ == "__main__":
    print(results())
