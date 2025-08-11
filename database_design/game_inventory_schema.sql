-- Create and select database
DROP DATABASE IF EXISTS game_inventory;
CREATE DATABASE game_inventory;
USE game_inventory;

-- Players table
CREATE TABLE Players (
	player_id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	level INT DEFAULT 1,
	xp INT DEFAULT 0,
	gold INT DEFAULT 0,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

-- Items table
CREATE TABLE Items (
	item_id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	type ENUM('equipment', 'food') NOT NULL,
	effect JSON,
	value INT DEFAULT 0,
	rarity VARCHAR(20)
	PRIMARY KEY (item_id),
	FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE
);

-- Player Inventory
CREATE TABLE PlayerInventory (
	player_id INT,
	item_id INT,
	quantity INT DEFAULT 1,
	PRIMARY KEY (player_id, item_id),
	PRIMARY KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE,
	PRIMARY KEY (item_id) REFERENCES Items(item_id) ON DELETE CASCADE 
);

-- Player Stats
CREATE TABLE PlayerStats (
	player_id INT PRIMARY KEY,
	health INT DEFAULT 100,
	attack INT DEFAULT 10,
	defense INT DEFAULT 5,
	speed INT DEFAULT 5,
	FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE

);

-- Level Requirements
CREATE TABLE LevelRequirements (
	level INT PRIMARY KEY,
	xp_required INT NOT NULL,
	bonus_stats JSON
);
