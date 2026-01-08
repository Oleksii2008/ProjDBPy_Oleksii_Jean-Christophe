USE projdbpy;

-- ============================
-- TABLE: Dunks
-- ============================
INSERT INTO Dunks (Description) VALUES
('Windmill Reverse', '9.2'),
('Between-the-legs', '9.5'),
('360 Spin', '9.0'),
('One-Hand Power Dunk', '8.8'),
('Free-throw Line Dunk', '9.7'),
('Tomahawk Slam', '8.9'),
('Reverse Alley-Oop', '9.1'),
('Double Clutch Dunk', '8.7'),
('Eurostep Dunk', '9.3'),
('Cradle Dunk', '9.4');

-- ============================
-- TABLE: Players
-- ============================
INSERT INTO Players (Firstname, Lastname, Team, Height, Dunks_id) VALUES
('Zach', 'LaVine', 'Bulls', 1.96, 1),
('Aaron', 'Gordon', 'Magic', 2.03, 2),
('Vince', 'Carter', 'Raptors', 1.98, 3),
('Ja', 'Morant', 'Grizzlies', 1.91, 4),
('Michael', 'Jordan', 'Bulls', 1.98, 5),
('LeBron', 'James', 'Lakers', 2.06, 6),
('Dominique', 'Wilkins', 'Hawks', 1.98, 7),
('Carmelo', 'Anthony', 'Knicks', 2.03, 8),
('Blake', 'Griffin', 'Clippers', 2.06, 9),
('Julius', 'Randle', 'Knicks', 2.03, 10),
('Russell', 'Westbrook', 'Lakers', 1.91, 1),
('Giannis', 'Antetokounmpo', 'Bucks', 2.11, 2),
('Anthony', 'Edwards', 'Timberwolves', 1.98, 3),
('Joel', 'Embiid', '76ers', 2.13, 4),
('Trae', 'Young', 'Hawks', 1.85, 5);

-- ============================
-- TABLE: Judges
-- ============================
INSERT INTO Judges (Firstname, Lastname, Status) VALUES
('Kenny', 'Smith', 'Expert'),
('Shaquille', "O’Neal", 'Legend'),
('Dominique', 'Wilkins', 'Legend'),
('Candace', 'Parker', 'Expert'),
('Dwyane', 'Wade', 'Guest'),
('Chris', 'Webber', 'Expert'),
('Clyde', 'Drexler', 'Legend'),
('Grant', 'Hill', 'Expert'),
('Isiah', 'Thomas', 'Legend'),
('Maya', 'Moore', 'Expert');

-- ============================
-- TABLE: Rounds
-- ============================
INSERT INTO Rounds (Round_number, Dunks_id) VALUES
(1, 1),
(1, 2),
(2, 3),
(2, 4),
(3, 5),
(3, 6),
(4, 7),
(4, 8),
(5, 9),
(5, 10),
(6, 1),
(6, 2),
(7, 3),
(7, 4),
(8, 5);

-- ============================
-- TABLE: Concours
-- ============================
INSERT INTO Concours (Year, Place, Date, Rounds_id) VALUES
(2023, 'Chicago', '2023-02-18', 1),
(2023, 'Chicago', '2023-02-18', 2),
(2023, 'Chicago', '2023-02-18', 3),
(2023, 'Chicago', '2023-02-18', 4),
(2024, 'Los Angeles', '2024-02-17', 5),
(2024, 'Los Angeles', '2024-02-17', 6),
(2024, 'Los Angeles', '2024-02-17', 7),
(2024, 'Los Angeles', '2024-02-17', 8),
(2025, 'New York', '2025-02-15', 9),
(2025, 'New York', '2025-02-15', 10);

-- ============================
-- TABLE: Judges_has_Dunks
-- ============================
INSERT INTO Judges_has_Dunks (Judges_id, Dunks_id, Rating) VALUES
(1, 1, 9),
(2, 1, 10),
(3, 1, 9),
(4, 1, 8),
(5, 1, 9),

(1, 2, 10),
(2, 2, 10),
(3, 2, 9),
(6, 2, 8),
(7, 2, 10),

(3, 3, 9),
(4, 3, 8),
(5, 3, 10),
(6, 3, 9),
(8, 3, 8),

(1, 4, 8),
(2, 4, 9),
(5, 4, 8),
(7, 4, 9),
(9, 4, 10),

(2, 5, 10),
(3, 5, 10),
(5, 5, 9),
(6, 5, 9),
(8, 5, 10),

(1, 6, 9),
(4, 6, 8),
(7, 6, 9),
(9, 6, 10),
(10, 6, 8),

(2, 7, 10),
(3, 7, 9),
(5, 7, 10),
(6, 7, 9),
(8, 7, 9),

(1, 8, 8),
(2, 8, 9),
(4, 8, 8),
(7, 8, 10),
(10, 8, 9),

(3, 9, 9),
(5, 9, 9),
(6, 9, 10),
(8, 9, 9),
(9, 9, 8),

(2, 10, 10),
(4, 10, 9),
(6, 10, 9),
(7, 10, 10),
(10, 10, 9);
