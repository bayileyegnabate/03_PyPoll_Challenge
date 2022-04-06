# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
#file_to_load = os.path.join("..", "Resources", "election_results.csv")
file_to_load = os.path.join("./", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
winning_county = ""
winning_county_count = 0
winning_county_percentage= 0



# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]


        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:
            county_options.append(county_name)


            # 4b: Add the existing county to the list of counties.


            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0


        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1



# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\n\t\t--------------------\n"
        f"\t\t  Election Results\n"
        f"\t\t--------------------\n"
        f"\t\tTotal Votes: {total_votes:,}\n"
        f"\t\t--------------------\n\n"
        f"\t\tCounty Votes:\n"
        f"\t\t-------------\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        county_vote_count = county_votes[county_name]

        # 6c: Calculate the percentage of votes for the county.
        county_vote_percentage = county_vote_count / total_votes * 100
        county_results = (f"\t\t{county_name}: {county_vote_percentage:.1f}% ({county_vote_count:,})")
        county_results_txt = (f"\t\t{county_name}: {county_vote_percentage:.1f}% ({county_vote_count:,})\n")

        # 6d: Print the county results to the terminal.
        print(county_results)

        # 6e: Save the county votes to a text file.
        txt_file.write(county_results_txt)

        # 6f: Write an if statement to determine the winning county and get its vote count.
        if (county_vote_count > winning_county_count) and (county_vote_percentage > winning_county_percentage):
            winning_county_count = county_vote_count
            winning_county_percentage = county_vote_percentage 
            winning_county = county_name

    # 7: Print the county with the largest turnout to the terminal.
    winning_county = (
            f"\n\t\t--------------------------------\n"
            f"\t\t Largest County Turnout: {winning_county.upper()}\n"
            f"\t\t--------------------------------\n")
    print(winning_county)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(f"{winning_county}\n")


    # Save the final candidate vote count to the text file.
    print(f'\t\tCandidate Votes:\n\t\t----------------')
    txt_file.write(f'\t\tCandidate Votes:\n\t\t----------------\n')
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"\t\t{candidate_name}: {vote_percentage:.1f}% ({votes:,})")
        candidate_results_txt = (f"\t\t{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results_txt)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
            f"\n\t\tWinner:\n"
            f"\t\t-------\n"
            f"\t\tWinner: {winning_candidate.upper()}\n"
            f"\t\tWinning Vote Count: {winning_count:,}\n"
            f"\t\tWinning Percentage: {winning_percentage:.1f}%\n"
            f"\t\t-----------------------------\n"
            f"\t\t============ ≈Ω≈ ============\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
