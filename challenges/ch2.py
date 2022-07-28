# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.

# It should look like this:

# Sam Harris => S.H

# patrick Feeney => P.F


def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()

# Testing
print(abbrevName("Kevin portillo"))