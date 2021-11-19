import pandas
from matplotlib import pyplot
#from scipy.stats import ttest_ind

# CSV file must contain at least 3 columns:
# * Scores
# * Experience --- e.g., AP, HS, Self, Outreach, None
# * Pronouns --- e.g., he, she, they
data = pandas.read_csv("exam2.csv")
print(data)

data.hist(column='Scores', bins=range(0,51,5))
pyplot.savefig("exam2_distribution.png")

# Compare based on experience
data.boxplot(column='Scores', by='Experience')
pyplot.savefig("exam2_experience.png")

ap_or_hs = data.loc[data['Experience'].isin(['AP', 'HS'])]['Scores']
other = data.loc[data['Experience'].isin(['Self', 'Outreach', 'None'])]['Scores']
#print("Do AP or HS experience impact scores?")
#print(ttest_ind(ap_or_hs, other))

# Compare based on pronouns
data.boxplot(column='Scores', by='Pronouns')
pyplot.savefig("exam2_pronouns.png")

he = data.loc[data['Pronouns'] == 'he']['Scores']
she = data.loc[data['Pronouns'] == 'she']['Scores']
#print("Do pronouns impact scores?")
#print(ttest_ind(he, she))

data.hist(column='Experience', by='Pronouns')
pyplot.savefig("experience_by_pronouns.png")

