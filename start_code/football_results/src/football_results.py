def get_result(final_score):
    #return home win if the home score is greater than the away score
    if final_score["home_score"] > final_score["away_score"]:
        return "Home win"
    #return away win if the away score is greater than the home score
    elif final_score["away_score"] > final_score["home_score"]:
        return "Away win"
    #return draw if both the home and away scores are the same
    else:
        return "Draw"

def get_results(final_scores):
    pass
    # (You could try and use a list comprehension for this)
    #For each score in the final scores list, we want to run the get result function, then add the result to a new list
    results = [get_result(score) for score in final_scores]
    return results