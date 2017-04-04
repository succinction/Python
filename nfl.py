"""
Prompt the user for either an NFL conference and division or the name of an NFL team.
Based on the response, return either a list of teams in that division or the name of the team's division.
>>> NFL_TEAMS = {'foo':{'bar':['baz']}}
>>> get_teams_by_conference_and_division(NFL_TEAMS, 'foo', 'bar')
['baz']
>>> get_conference_and_division_by_team_name(NFL_TEAMS, 'baz')
('foo', 'bar')
"""

def get_teams_by_conference_and_division(teams, conference, division):
    try:
        div = divis(division)
        for team_index in range(len(teams[conference][div])):
            print(teams[conference][div][team_index])
        print()
    except KeyError:
        print('KeyError. Try again:')
        main(teams)

############################################################################
def divis(x):
    return {
    'n': 'North',
    's': 'South',
    'e': 'East',
    'w': 'West',
    }[x]

def get_conference_and_division_by_team_name(teams, team_name):
    conf = ['AFC', 'NFC']
    divs = ['n', 's', 'e', 'w']
    for co in range(len(conf)):
        for di in range(len(divs)):
            if team_name.title() in teams[conf[co]][divis(divs[di])]:
                print('{} are in the {} conference, {} division.'.format(team_name.title(), conf[co], divis(divs[di])))
                return
    print('no matching team. Try again.')
    main(teams)

############################################################################

def main(teams):
    """Prompt for user input, get a result from the data, print a nicely formatted answer"""
    print()
    user_input = input('Enter the name of either a conference (AFC or NFC) or team: ')
    if user_input.upper() == 'AFC':
        get_teams_by_conference_and_division(NFL_TEAMS, 'AFC', input('Enter Division: n/s/e/w: '))
    elif user_input.upper() == 'NFC':
        get_teams_by_conference_and_division(NFL_TEAMS, 'NFC', input('Enter Division: n/s/e/w: '))
    else:
        get_conference_and_division_by_team_name(NFL_TEAMS, user_input)



if __name__ == '__main__':

    NFL_TEAMS = {
        'AFC': {
            'East': ['Buffalo Bills', 'Miami Dolphins', 'New England Patriots', 'New York Jets'],
            'North': ['Baltimore Ravens', 'Cincinnati Bengals', 'Cleveland Browns', 'Pittsburgh Steelers'],
            'South': ['Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Tennessee Titans'],
            'West': ['Denver Broncos', 'Kansas City Chiefs', 'Oakland Raiders', 'San Diego Chargers']
        },
        'NFC': {
            'East': ['Dallas Cowboys', 'New York Giants', 'Philadelphia Eagles', 'Washington Redskins'],
            'North': ['Chicago Bears', 'Detroit Lions', 'Green Bay Packers', 'Minnesota Vikings'],
            'South': ['Atlanta Falcons', 'Carolina Panthers', 'New Orleans Saints', 'Tampa Bay Buccaneers'],
            'West': ['Arizona Cardinals', 'Los Angeles Rams', 'San Francisco 49ers', 'Seattle Seahawks']
        }
    }

    main(NFL_TEAMS)
