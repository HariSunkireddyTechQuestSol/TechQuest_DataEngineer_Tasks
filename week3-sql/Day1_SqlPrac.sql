Use Cricket;
-- Table for storing player information
CREATE TABLE Players (
    player_id INT PRIMARY KEY,
    player_name VARCHAR(100) NOT NULL,
    country VARCHAR(100),
    role VARCHAR(50),  -- e.g., Batsman, Bowler, All-rounder, Wicketkeeper
    age INT,
    batting_style VARCHAR(50),
    bowling_style VARCHAR(50)
);

-- Table for storing match details
CREATE TABLE Matches (
    match_id INT PRIMARY KEY,
    player_id INT,  -- Foreign key that connects to Players table
    opponent_team VARCHAR(100),
    match_date DATE,
    venue VARCHAR(100),
    runs_scored INT,
    wickets_taken INT,
    catches INT,
    FOREIGN KEY (player_id) REFERENCES Players(player_id)
);

-- Insert data into Players table
INSERT INTO Players VALUES
(1, 'Virat Kohli', 'India', 'Batsman', 35, 'Right-hand bat', 'None'),
(2, 'Steve Smith', 'Australia', 'Batsman', 33, 'Right-hand bat', 'None'),
(3, 'Joe Root', 'England', 'Batsman', 32, 'Right-hand bat', 'None'),
(4, 'Kagiso Rabada', 'South Africa', 'Bowler', 27, 'Right-hand bat', 'Right-arm fast'),
(5, 'Trent Boult', 'New Zealand', 'Bowler', 31, 'Left-hand bat', 'Left-arm fast'),
(6, 'Babar Azam', 'Pakistan', 'Batsman', 29, 'Right-hand bat', 'None'),
(7, 'Ravindra Jadeja', 'India', 'All-rounder', 30, 'Left-hand bat', 'Left-arm spin'),
(8, 'Josh Hazlewood', 'Australia', 'Bowler', 31, 'Right-hand bat', 'Right-arm fast'),
(9, 'Ben Stokes', 'England', 'All-rounder', 31, 'Left-hand bat', 'Right-arm fast'),
(10, 'Quinton de Kock', 'South Africa', 'Wicketkeeper', 29, 'Right-hand bat', 'None'),
(11, 'Martin Guptill', 'New Zealand', 'Batsman', 34, 'Right-hand bat', 'None'),
(12, 'Shahid Afridi', 'Pakistan', 'All-rounder', 41, 'Right-hand bat', 'Right-arm spin'),
(13, 'Lasith Malinga', 'Sri Lanka', 'Bowler', 38, 'Right-hand bat', 'Right-arm fast'),
(14, 'Dimuth Karunaratne', 'Sri Lanka', 'Batsman', 34, 'Right-hand bat', 'None'),
(15, 'Jonny Bairstow', 'England', 'Wicketkeeper', 32, 'Right-hand bat', 'None'),
(16, 'Pat Cummins', 'Australia', 'Bowler', 28, 'Right-hand bat', 'Right-arm fast'),
(17, 'Shubman Gill', 'India', 'Batsman', 25, 'Right-hand bat', 'None'),
(18, 'Fakhar Zaman', 'Pakistan', 'Batsman', 29, 'Left-hand bat', 'None'),
(19, 'Kusal Perera', 'Sri Lanka', 'Batsman', 31, 'Right-hand bat', 'None'),
(20, 'Ross Taylor', 'New Zealand', 'Batsman', 36, 'Right-hand bat', 'None');

-- Insert data into Matches table
INSERT INTO Matches VALUES
(1, 1, 'Australia', '2023-05-12', 'Mumbai', 85, 0, 1),
(2, 2, 'India', '2023-04-10', 'Sydney', 92, 0, 0),
(3, 3, 'South Africa', '2023-06-15', 'London', 78, 0, 2),
(4, 4, 'England', '2023-07-20', 'Cape Town', 23, 3, 1),
(5, 5, 'India', '2023-08-02', 'Auckland', 45, 2, 0),
(6, 6, 'Sri Lanka', '2023-03-10', 'Karachi', 101, 0, 1),
(7, 7, 'Pakistan', '2023-09-12', 'Chennai', 47, 1, 3),
(8, 8, 'India', '2023-05-18', 'Melbourne', 34, 4, 0),
(9, 9, 'New Zealand', '2023-09-05', 'London', 56, 2, 1),
(10, 10, 'Australia', '2023-08-25', 'Johannesburg', 38, 0, 2),
(11, 11, 'Pakistan', '2023-07-01', 'Wellington', 61, 0, 1),
(12, 12, 'New Zealand', '2023-06-21', 'Lahore', 36, 1, 0),
(13, 13, 'India', '2023-05-05', 'Colombo', 12, 5, 0),
(14, 14, 'Australia', '2023-07-17', 'Kandy', 74, 0, 1),
(15, 15, 'South Africa', '2023-03-28', 'London', 43, 0, 3),
(16, 16, 'Sri Lanka', '2023-09-13', 'Sydney', 27, 3, 0),
(17, 17, 'England', '2023-05-09', 'Delhi', 99, 0, 2),
(18, 18, 'New Zealand', '2023-04-22', 'Karachi', 51, 0, 1),
(19, 19, 'Australia', '2023-08-16', 'Colombo', 47, 0, 0),
(20, 20, 'India', '2023-09-25', 'Auckland', 58, 0, 1);


Select player_name, country
from Players;

SET SQL_SAFE_UPDATES = 0;

Update players
set bowling_style = "Left-arm medium fast"
where player_name = "Joe Root";

DELETE FROM Matches
WHERE venue = "Lahore";





