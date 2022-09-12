## This code will capture the date from an input variable, and return that once it has read the date
import re
date = str("the date is February 18, 2018")
MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"

match = re.search(r'(' + MONTHS + ')\s+\d{1,2},\s+\d{4}', date).group()
print(match)