import pandas as pd
import sqlite3
class playerExtractor:
    def __init__(self):
        self.players = {}# playerType,YearsPlayed,Captain,WicketKeeper,Batting Style,Bowling Style
        idx = 0

    def skip_line(self, f, num_lines=1):
        """Skip a specified number of lines in the file."""
        try:
            for _ in range(num_lines):
                next(f)
        except StopIteration:
            pass  # No more lines to skip

    def extract_team(self,file_path):
        # Start from the end, skipping the file extension
        idx = len(file_path) - 5
        team = ""
        while  file_path[idx] != "\\":
            team = file_path[idx] + team
            idx -= 1
        self.idx = idx
        return team

    def extract_year(self,file_path):
        idx = self.idx-2
        year = ""
        #print(file_path[idx])
        while file_path[idx] != "\\":
            year = file_path[idx] + year
            idx -= 1
        return year

    def player_type(self,line,f):
        if line and line == "ALLROUNDERS":
            self.skip_line(f)  # Skip the next line after identifying the type
            return "ALLROUNDERS"
        elif line and line == "BATTERS":
            self.skip_line(f)  # Skip the next line after identifying the type
            return "BATTERS"
        elif line and line == "BOWLERS":
            self.skip_line(f)  # Skip the next line after identifying the type
            return "BOWLERS"

    def read_file(self, file_path,player_team,year):
        with open(file_path, "r") as f:
            player_name = ""
            player_type = self.player_type(f.readline().strip(),f)
            for line in f:
                line = line.strip()
                if line == "Wicketkeeper Batter":
                    self.players[player_name][2] = True
                elif line == "Age:":
                    self.skip_line(f)
                elif line == "Batting:":
                    self.players[player_name][3] = next(f).strip()
                    line = next(f, None)
                    if line and line.strip() =="Bowling:":
                        self.players[player_name][4] = next(f).strip()
                        line = next(f, None)
                        if line:
                            line = line.strip()
                            temp = self.player_type(line,f)
                            if temp:
                                player_type = temp
                elif "†" in line or "â€" in line or "Batter" in line or "Allrounder" in line:
                    continue
                elif line:  # Only add if the line is not empty
                    player_name = line
                    if player_name not in self.players:
                        self.players[player_name] = [player_type,None,False,None,None,player_team]
                    if self.players[player_name][1] is None:
                        self.players[player_name][1] = str(year)
                    else:
                        self.players[player_name][1] += ","+str(year)
                    try:
                        line = next(f, None)
                        if line and line.strip() == "Withdrawn":
                            del self.players[player_name]
                            while True:
                                line = next(f)
                                if line.strip() == "Batting:":
                                    break
                            next(f)
                            line = next(f)
                            if line.strip()=="Bowling:":
                                self.skip_line(f)
                                self.skip_line(f)
                        elif line and line.startswith("("):
                            line = next(f).strip()
                            if line == "Wicketkeeper Batter":
                                self.players[player_name][2] = True
                        elif line and line.strip() == "Age:":
                            self.skip_line(f)
                    except StopIteration:
                        pass

    def  create_database(self,team,db_path="E:\\Cricket TicTacToe Game\\IPL_player_database.db"):
        """Create an SQLite database and insert player data."""
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {team} (
                PlayerName TEXT PRIMARY KEY,
                PlayerType TEXT,
                YearsPlayed TEXT,
                WicketKeeper INTEGER,
                BattingStyle TEXT,
                BowlingStyle TEXT,
                Team TEXT
            )
        """)
        # Insert data
        for player_name, details in self.players.items():
            cursor.execute(f"""
                    INSERT OR REPLACE INTO {team} (PlayerName, PlayerType, YearsPlayed, WicketKeeper, BattingStyle, BowlingStyle, Team)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """, (player_name, details[0], details[1], int(details[2]), details[3], details[4], details[5]))
        conn.commit()
        conn.close()

    def create_file(self):  # creating a csv file
        # playerType, YearsPlayed, WicketKeeper, Batting Style, Bowling Style, Team
        player_df = pd.DataFrame.from_dict(
            self.players,
            orient='index',
            columns=['PlayerType', 'YearsPlayed', 'WicketKeeper', 'BattingStyle', 'BowlingStyle','Team']
        )
        player_df.to_csv("E:\\Cricket TicTacToe Game\\RCB_Players.csv",)
        print(player_df)

if __name__ == "__main__":
    team_and_year = {
                    2008 : ["CSK","DC","DCG","KKR","MI","PBKS","RCB","RR"],
                    2009 : ["CSK","DC","DCG","KKR","MI","PBKS","RCB","RR"],
                    2010 : ["CSK","DC","DCG","KKR","MI","PBKS","RCB","RR"],
    }
    file_path = [r"E:\\Cricket TicTacToe Game\\2008\\RCB.txt",
                 r"E:\\Cricket TicTacToe Game\\2009\\RCB.txt",
                 r"E:\\Cricket TicTacToe Game\\2010\\RCB.txt"]
    team = playerExtractor()
    team_name = team.extract_team(file_path[0])
    for idx,file in enumerate(file_path):
        year = team.extract_year(file)
        team.read_file(file,team_name,year)
    team.create_database(team_name)
    team.create_file()
    print(len(team.players))