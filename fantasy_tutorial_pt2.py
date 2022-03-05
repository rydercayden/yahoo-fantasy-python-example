# Please careful when running the Add and Drop functions as this is not reversible
# Please run this code at your own risk
# It is recommended that you try out this code first in a dummy league
# Developer will not be liable for any unitentional updates to your roster

from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa

#connect to yahoo api
sc = OAuth2(None, None, from_file='oauth2.json')

#get game object
gm = yfa.Game(sc, 'nba')

leagues = gm.league_ids()

print(leagues)

#get the league object
#lg = gm.to_league(leauges[0])
lg = gm.to_league('410.l.146626')

#get the team key
teamkey = lg.team_key()

#get the team object
team = lg.to_team(teamkey)

#get team roster
roster = team.roster()

#print(roster)

print("=== MY TEAM ===")

for r in roster:
    print(r)

fa = lg.free_agents("PG")

print("=== FREE AGENTS ===")

for p in fa:
    print(p)

# Drop Lou Williams
team.drop_player(3971)

# Add Seth Curry
team.add_player(5245)

# Add Marcus Smart and drop KCP
team.add_and_drop_players(5317,5159)

newroster = team.roster()

#print(roster)

print("=== MY NEW ROSTER ===")

for r in newroster:
    print(r)