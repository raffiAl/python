import pandas as pd

def updateScores(score):
  underatedScore = []
  minScore = []
  midScore = []

  if (score < 75):
    underatedScore.append(score)

  for scoreTemp in underatedScore:
    minValue = 75 - scoreTemp
    minScore.append(minValue)
  for a, b in zip(underatedScore, minScore):
    midScore.append(a + b)
  
  if (score < 70):
    i = 0
    for index, value in enumerate(midScore):
      i = index
    return midScore[i]
  if (score < 75):
    i = 0
    for index, value in enumerate(midScore):
      i = index
    return midScore[i] + ((minScore[i]/2) + 3) 
  if (score > 75):
    return score + 5
  if (score > 99) :
    return 99



def grade(score):
  return 'A'

scores =  pd.read_excel("filehandling/sample.xlsx")
scores["New Score"] = scores['Score'].apply(updateScores)
scores['Grade'] = scores['New Score'].apply(grade)
scores.to_excel('filehandling/newscore.xlsx', index=False)
