USE dunk_contest;

INSERT INTO Dunks (id, Name, Created_at) VALUES
(1, 'Windmill', '2024-01-01 10:00:00'),
(2, '360°', '2024-01-01 10:00:00'),
(3, 'Tomahawk', '2024-01-01 10:00:00'),
(4, 'Between the legs', '2024-01-01 10:00:00'),
(5, 'Reverse', '2024-01-01 10:00:00'),
(6, 'Alley-oop', '2024-01-01 10:00:00'),
(7, 'Free throw line', '2024-01-01 10:00:00'),
(8, 'Eastbay', '2024-01-01 10:00:00');

INSERT INTO Players (id, Firstname, Lastname, Team, Height, id_dunk, date_added) VALUES
(1, 'Michael', 'Jordan', 'Chicago Bulls', '1.98', 1, '2024-01-15 09:00:00'),
(2, 'LeBron', 'James', 'Los Angeles Lakers', '2.06', 3, '2024-01-15 09:15:00'),
(3, 'Kobe', 'Bryant', 'Los Angeles Lakers', '1.98', 2, '2024-01-15 09:30:00'),
(4, 'Vince', 'Carter', 'Toronto Raptors', '1.98', 7, '2024-01-15 09:45:00'),
(5, 'Zach', 'LaVine', 'Chicago Bulls', '1.96', 4, '2024-01-15 10:00:00'),
(6, 'Aaron', 'Gordon', 'Denver Nuggets', '2.06', 8, '2024-01-15 10:15:00'),
(7, 'Dominique', 'Wilkins', 'Atlanta Hawks', '2.03', 1, '2024-01-15 10:30:00'),
(8, 'Julius', 'Erving', 'Philadelphia 76ers', '2.01', 7, '2024-01-15 10:45:00');

INSERT INTO Judges (Firstname, Lastname, Email, STATUS, Created_at) VALUES
('Kenny', 'Smith', 'kenny@nba.com', 'Expert', '2024-01-10 08:00:00'),
('Shaquille', "O’Neal", 'shaq@nba.com', 'Legend', '2024-01-10 08:15:00'),
('Dominique', 'Wilkins', 'dom@nba.com', 'Legend', '2024-01-10 08:30:00'),
('Candace', 'Parker', 'candace@nba.com', 'Expert', '2024-01-10 08:45:00'),
('Dwyane', 'Wade', 'dwayne@nba.com', 'Guest', '2024-01-10 08:45:00'),
('Chris', 'Webber', 'chris@nba.com', 'Expert', '2024-01-10 08:45:00'),
('Clyde', 'Drexler', 'clyde@nba.com', 'Legend', '2024-01-10 08:45:00'),
('Grant', 'Hill', 'grant@nba.com', 'Expert', '2024-01-10 08:45:00'),
('Isiah', 'Thomas', 'isiah@nba.com', 'Legend', '2024-01-10 08:45:00'),
('Maya', 'Moore', 'maya@nba.com', 'Expert', '2024-01-10 08:45:00');

INSERT INTO Contests (id, Year, Location, Contest_date, Created_at) VALUES
(1, 2024, 'Indianapolis', '2024-02-17', '2024-01-20 10:00:00'),
(2, 2024, 'Los Angeles', '2024-07-15', '2024-01-20 10:30:00'),
(3, 2025, 'New York', '2025-02-16', '2024-12-01 11:00:00');
