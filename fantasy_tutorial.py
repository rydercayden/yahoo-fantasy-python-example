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

print(roster)