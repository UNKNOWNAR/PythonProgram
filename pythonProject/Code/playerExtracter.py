import numpy as np
import pandas as pd
class playerExtractor:
    def __init__(self):
        self.players = {}

    def skip_line(self, f, num_lines=1):
        """Skip a specified number of lines in the file."""
        try:
            for _ in range(num_lines):
                next(f)
        except StopIteration:
            pass  # No more lines to skip

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

    def read_file(self, file_path,year):
        with open(file_path, "r") as f:
            player_name = ""
            player_type = self.player_type(f.readline().strip(),f)
            for line in f:
                line = line.strip()
                if line == "Wicketkeeper Batter":
                    self.players[player_name][3] = "Wicketkeeper"
                elif line == "Age:":
                    self.skip_line(f)
                elif line == "Batting:":
                    self.players[player_name][4] = next(f).strip()
                    line = next(f, None)
                    if line and line.strip() =="Bowling:":
                        self.players[player_name][5] = next(f).strip()
                        line = next(f, None)
                        if line:
                            line = line.strip()
                            temp = self.player_type(line,f)
                            if temp:
                                player_type = temp
                elif "†" in line or "â€" in line or "Batter" in line or "Allrounder" in line:
                    continue
                elif line:  # Only add if the line is not empty
                    if line not in self.players:
                        self.players[line] = [player_type,[],None,None,None,None]
                    self.players[line][1].append(year)
                    player_name = line
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
                            self.players[player_name][2]="Captain"
                            line = next(f).strip()
                            if line == "Wicketkeeper Batter":
                                self.players[player_name][3] = "Wicketkeeper"
                        elif line and line.strip() == "Age:":
                            self.skip_line(f)
                    except StopIteration:
                        pass

if __name__ == "__main__":
    file_path = [r"E:\\Cricket TicTacToe Game\\2008\\RCB_2008.txt",
                 r"E:\\Cricket TicTacToe Game\\2009\\RCB_2009.txt",
                 r"E:\\Cricket TicTacToe Game\\2010\\RCB.txt"]
    rcb = playerExtractor()
    for idx,file in enumerate(file_path):
        rcb.read_file(file,2008+idx)
    for player in rcb.players:
        print(player,rcb.players[player])
    print(len(rcb.players))