"""
statements = {
    'george saint pierre': "I am not impressed by your performance.",
    'conor mcgregor': "I'd like to take this chance to apologize.. To absolutely NOBODY!"
}

def quote(fighter):
    return statements[fighter.lower()]
"""


def quote(fighter):
    return "I am not impressed by your performance." if str.lower(fighter)=='george saint pierre' else "I'd like to take this chance to apologize.. To absolutely NOBODY!"
    
    
"""
def quote(fighter):
    return ["I am not impressed by your performance.",\
    "I'd like to take this chance to apologize.. To absolutely NOBODY!"][fighter.lower() == 'conor mcgregor']
"""
