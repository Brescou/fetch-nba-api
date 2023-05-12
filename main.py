import requests
import json
import pandas as pd
import time

start_season = 2000
end_season = 2022
seasons = [
    f"{season}-{str(season + 1)[-2:]}" for season in range(start_season, end_season + 1)]

# Player Index
# base_url = "https://stats.nba.com/stats/playerindex?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season={season}&SeasonSegment=&SeasonType=Regular%20Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight="

# Player Stats
# base_url = "https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season={season}&SeasonSegment=&SeasonType=Regular%20Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight="

# Team Stats
base_url = "https://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2022-23&SeasonSegment=&SeasonType=Regular Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision="

request_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://www.nba.com/",
    "Connection": "keep-alive",
}

all_seasons_data = pd.DataFrame()

for season in seasons:
    print(f"Getting data for season {season}")
    url = base_url.format(season=season)
    response = requests.get(url, headers=request_headers)
    data = json.loads(response.text)
    headers = data["resultSets"][0]["headers"]
    rows = data["resultSets"][0]["rowSet"]
    df = pd.DataFrame(rows, columns=headers)
    df["SEASON"] = season
    all_seasons_data = pd.concat([all_seasons_data, df], ignore_index=True)
    time.sleep(5)

print(all_seasons_data.head())
all_seasons_data.to_csv("src/data/nba_team_stats_2000-2023.csv", index=False)
