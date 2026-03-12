-- Quizzenberg v2 - Complete Database Setup
-- Run this in MySQL to setup everything!

CREATE DATABASE IF NOT EXISTS india;
USE india;

-- Drop if exists
DROP TABLE IF EXISTS options;
DROP TABLE IF EXISTS questions;

-- Create Tables
CREATE TABLE questions (
    id INT PRIMARY KEY,
    question TEXT NOT NULL
);

CREATE TABLE options (
    id INT PRIMARY KEY,
    opt1 TEXT NOT NULL,
    opt2 TEXT NOT NULL,
    opt3 TEXT NOT NULL,
    opt4 TEXT NOT NULL
);

-- Insert QUESTIONS (from your screenshot)
INSERT INTO questions (id, question) VALUES
(0, "Among the naturally occurring carbohydrates, furanose ring is found in the"),
(1, "'Convulsions' disease is caused by the deficiency of "),
(2, "Denaturation of proteins leads to loss of its biological activity by"),
(3, "Helical structure of protein is stabilised by"),
(4, "Vitamin B6 is known as"),
(5, "Atom of which of the following elements has the greatest ability to attract electrons?"),
(6, "Which element is present in insulin?"),
(7, "Name the heaviest naturally occurring element:"),
(8, "Which element is stored in water?"),
(9, "Alcohol (Ethanol) is denatured with which of the following substances?");

-- Insert OPTIONS (using correct answers from v1)
INSERT INTO options (id, opt1, opt2, opt3, opt4) VALUES
(0, "Glucose Unit of Cane Sugar", "Glucose Unit of Cellulose", "Fructose Unit of Cane Sugar", "Galactose Unit of Lactose"),
(1, "Vitamin K", "Vitamin B6", "Vitamin D", "Vitamin A"),
(2, "Formation of Amino Acids", "Loss of Primary Structure", "Loss of Both Primary and Secondary Structures", "Loss of Both Secondary and Tertiary Structures"),
(3, "Peptide bond", "Hydrogen bond", "Van der Waals force", "Dipole Association"),
(4, "Pyridoxine", "Thiamine", "Tocopherol", "Riboflavin"),
(5, "Silicon", "Sulphur", "Nitrogen", "Chlorine"),
(6, "Iron", "Cobalt", "Zinc", "Magnesium"),
(7, "Plutonium", "Uranium", "Cadmium", "Platinum"),
(8, "White Phosphorus", "Sulphur", "Carbon", "Iodine"),
(9, "Glycerol", "Pyridine & Copper Sulphate", "Aniline", "Ether & Ethanol");

-- Verify data loaded
SELECT COUNT(*) as total_questions FROM questions;
SELECT COUNT(*) as total_options FROM options;
