# Sports Stats Tracker
# CS 313E Final Project
# Author: Nancy Kwak
# GitHub: github.com/nancy1404/CS313E_TermProject
# This program reads a baseball dataset (Batting.csv) and
# allows the user to view player statistics. It demonstrates
# object-oriented programming, data structures, and algorithms
# (sorting, searching, heaps) in Python.

import csv  
import heapq

# Player Class
class Player:
    """
    Represents a single baseball player's batting statistics.
    Each Player object stores a few key attributes such as:
    - player ID
    - team ID
    - number of at-bats (AB)
    - number of hits (H)
    - home runs (HR)
    - runs batted in (RBI)
    - walks (BB)
    - strikeouts (SO)
    It also automatically calculates the player's batting average.
    """

    def __init__(self, player_id, team, ab, hits, hr, rbi, bb, so):
        # Basic identifying information
        self.player_id = player_id
        self.team = team

        # Convert string data from the CSV into integers
        self.ab = int(ab)
        self.hits = int(hits)
        self.hr = int(hr)
        self.rbi = int(rbi)
        self.bb = int(bb)
        self.so = int(so)

        # Calculate batting average: hits / at-bats
        # Round to 3 decimal places for readability
        self.avg = round(self.hits / self.ab, 3) if self.ab != 0 else 0.0

    def __str__(self):
        """
        Defines how the object is printed (string representation).
        Example output:
        ohtansh01 (LAA)  AVG: 0.304  HR: 44  RBI: 95
        """
        return f"{self.player_id:12s} ({self.team})  AVG: {self.avg:.3f}  HR: {self.hr:2d}  RBI: {self.rbi:3d}"
    
# StatsManager Class
class StatsManager:
    """
    This class manages a list of Player objects and provides
    functions to load data, display players, sort them, and
    later find top performers or team averages.
    """

    def __init__(self):
        # keep all Player objects inside the list
        self.players = []
    
    # 1. load data
    def load_data(self, filename, limit=20):
        """
        Reads data from the CSV file and creates Player objects.
        Only reads the first 'limit' rows for simplicity.
        """
        with open(filename, newline='') as file:
            reader = csv.DictReader(file) # read rows as dictionaries
            for i, row in enumerate(reader):

                # Stop once read limit number of players
                if i >= limit:
                    break
                # Skip any rows that have missing or empty AB/H values
                if not (row['AB'] and row['H']):
                    continue

                # create new Player object from each CSV row
                player = Player(
                    row['playerID'], row['teamID'],
                    row['AB'], row['H'], row['HR'],
                    row['RBI'], row['BB'], row['SO']
                )

                # Add this Player to the list
                self.players.append(player)
        print(f"Successfully loaded {len(self.players)} players from {filename}")

    # 2. Display All Players
    def display_all(self):
        """
        Prints the list of all players and their key stats.
        """
        if not self.players:
            print("No players loaded yet. Please load data first.")
            return
        
        print("\n--- Player Statistics ---")
        for player in self.players:
            print(player)
        print("--------------------------\n")

    # 3. Sort Players by Stat (Merge Sort)
    def sort_by_avg(self, key="avg", descending=True):
        """
        Sorts the list of Player objects by a chosen stat (default: batting average)
        using the Merge Sort algorithm implemented manually.
        - key: which attribute to sort by (e.g., "avg", "hr", "rbi")
        - descending: True for highest to lowest, False for lowest to highest
        """

        # Helper Function: Merge Two Halves
        def merge(left, right, key, descending):
            merged = []
            i = j = 0
            # Compare elements from both halves until one is exhausted
            while i < len(left) and j < len(right):
                left_val = getattr(left[i], key)
                right_val = getattr(right[j], key)

                # For descending order, pick the larger value first
                if descending:
                    if left_val >= right_val:
                        merged.append(left[i])
                        i += 1
                    else:
                        merged.append(right[j])
                        j += 1
                # For ascending order
                else:
                    if left_val <= right_val:
                        merged.append(left[i])
                        i += 1
                    else:
                        merged.append(right[j])
                        j += 1

            # Add any leftover elements
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged
    
    # Recursive merge_sort function
        def merge_sort(arr, key, descending):
            # Base Case: single element is already sorted
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2

            # Recursively sort both halves
            left_half = merge_sort(arr[:mid], key, descending)
            right_half = merge_sort(arr[mid:], key, descending)

            # Merge the sorted halves
            return merge(left_half, right_half, key, descending)
        
        # Actually perform the merge sort on self.players
        print(f"Sorting players by '{key}' ({'descending' if descending else 'ascending'})...")
        self.players = merge_sort(self.players, key, descending)
        print("Sorting Complete!\n")
              
    # 4. Binary Search for Player
    def search_player(self, target_id):
        """
        Search for a player by their player_id using Binary Search.
        Assumes the players are sorted alphabetically by player_id.
        """

        # sort alphabetically by player_id before seraching
        print("\nSorting players alphabetically for search...")
        self.players = sorted(self.players, key = lambda p: p.player_id)
        print("Players sorted alphabetically.\n")

        # initialize boundaries for binary search
        low = 0
        high = len(self.players) - 1
        steps = 0 # just to show how many comparisons happen

        # Search loop
        while low <= high:
            steps += 1
            mid = (low + high) // 2 # find middle index
            mid_id = self.players[mid].player_id # playerID at mid

            if mid_id == target_id:
                print(f"Player '{target_id}' found in {steps} steps!")
                return self.players[mid] # return the Player object
            elif mid_id < target_id:
                low = mid + 1 # look in right half
            else:
                high = mid - 1 # look in left half
        print(f"Player '{target_id}' not found after {steps} steps.")
        return None # if not found
    
    # 5. Top K Players (using a Heap)
    def top_home_runs(self, k=3, key="hr"):
        """
        Returns and prints the top-k players based on a given stat (default: home runs).
        Uses a heap for efficient top-k retrieval.
        """

        # Check if we have enough players loaded
        if not self.players:
            print("No players available. Please load data first.")
            return
        
        # Use heapq.nlargest to get the top k players by the chosen stat
        top_players = heapq.nlargest(k, self.players, key=lambda p: getattr(p, key))

        print(f"\nTop {k} players by '{key.upper()}:\n")
        for rank, player in enumerate(top_players, start=1):
            print(f"{rank}. {player}")
        print("--------------------------\n")

        # Return list of top players 
        return top_players

    # 6. Team Averages (using Dictionary)
    def team_average(self):
        """
        Calculates and prints the average batting average (AVG)
        for each team using a dictionary of lists.
        """

        if not self.players:
            print("No players loaded. Please load data first.")
            return
        
        # Build dictionary {teamID: [list of AVGs]}
        team_stats = {}
        for p in self.players:
            team_stats.setdefault(p.team, []).append(p.avg)

        # Compute mean batting average per team
        team_avg = {team: round(sum(avgs)/len(avgs), 3)
                    for team, avgs in team_stats.items()}
        
        # Display nicely formatted output
        print("\nTeam Average Batting Averages:\n")
        for team, avg in team_avg.items():
            print(f"{team}: {avg:.3f}")
        print("--------------------------\n")

        return team_avg        


# Main Program
def main():
    """
    The main function is where the program starts running.
    """
    # 1. 
    # Create a StatsManager object to handle everything
    stats = StatsManager()

    # Load player data (reads the first 20 rows from Batting.csv)
    stats.load_data("Batting.csv", limit=20)

    # 2. 
    # Display the loaded players in the console
    stats.display_all()

    # 3.  
    # Sort players by batting average
    stats.sort_by_avg(key="avg", descending = True)
    stats.display_all()

    # Sort players by home runs
    stats.sort_by_avg(key="hr", descending=True)
    stats.display_all()

    # 4. 
    # Binary Search Test
    print("\n--- Binary Search Tests ---")
    result = stats.search_player("barnero01") # existing player
    if result:
        print(result)
    result = stats.search_player("nancyk05") # non-existent
    if result:
        print(result)

    # 5.
    # Top K Players (Heap)
    print("\n--- Top Home Run Hitters ---")
    stats.top_home_runs(k=3, key="hr")

    print("\n--- Top Batting Averages ---")
    stats.top_home_runs(k=3, key="avg")

    # 6.
    # Team Averages
    stats.team_average()


if __name__ == "__main__":
    main()
