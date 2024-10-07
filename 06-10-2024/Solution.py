# Medal Assignment Challenge
"""
Given scores of N athletes, find their relative ranks and the people with the top three
highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and
"Bronze Medal".
"""


# Function for medal assignment challenge solution
def assign_medals(scores):
    """
    This function takes a list of athlete scores as input and returns a list where:
    - The athlete with the highest score receives the "Gold Medal"
    - The athlete with the second-highest score receives the "Silver Medal"
    - The athlete with the third-highest score receives the "Bronze Medal"
    - Remaining athletes are assigned their ranks based on their score order.

    :param scores: List[int] - A list of scores for the athletes.
    :return: List[str] - A list with medals for the top 3 and ranks for the rest.
    """

    # Check if the input list is empty
    if not scores:
        return []

    # Finding sorted indices of the scores list in descending order of their scores
    sorted_indexes = sorted(range(len(scores)), key=lambda x: scores[x], reverse=True)

    # Initializing an empty list to store the results
    result = [None] * len(scores)

    # Assigning medals to the top 3 athletes
    for i, idx in enumerate(sorted_indexes):
        if i == 0:
            result[idx] = "Gold Medal"
        elif i == 1:
            result[idx] = "Silver Medal"
        elif i == 2:
            result[idx] = "Bronze Medal"
        else:
            result[idx] = str(i + 1)  # For the rest, assign their ranks as string

    return result


scores = [5, 4, 3, 2, 1]

print(assign_medals(scores))
