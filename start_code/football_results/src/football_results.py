def get_result(final_score):
    #return home win if the home score is greater than the away score
    if final_score["home_score"] > final_score["away_score"]:
        return "Home win"

def get_results(final_scores):
    pass
    # (You could try and use a list comprehension for this)