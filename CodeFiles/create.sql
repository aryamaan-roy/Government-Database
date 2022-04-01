create table legislative_body_members (
  Member_Name varchar(100) PRIMARY KEY,
  Official_Email varchar(200) UNIQUE,
  Education_Level varchar(100),
  Income_Tax_Returns int,
  Zip_Code INT UNIQUE,
  DOB DATE,
  P_ID varchar(5)
);

CREATE TABLE lbm_phone_numbers (
  Member_name varchar(100),
  Phone_number varchar(13),
  FOREIGN KEY (Member_name) REFERENCES legislative_body_members(Member_Name) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE lbm_address (
  Zipcode int,
  Street varchar(100),
  City varchar(100),
  State_name varchar(100),
  FOREIGN key (Zipcode) REFERENCES legislative_body_members(Zip_Code) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE party (
  Party_ID varchar(5) PRIMARY key,
  Party_Name varchar(50) UNIQUE
);

CREATE TABLE party_details (
  Party_ID varchar(5),
  Symbol varchar(20),
  Num_volunteers int,
  FOREIGN KEY (Party_ID) REFERENCES party(Party_ID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE party_president (
  Party_Name varchar(50),
  Party_President varchar(100),
  FOREIGN KEY (Party_Name) REFERENCES party(Party_Name) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE lok_sabha (
  Member_name varchar(100),
  Constituency_ID varchar(5),
  Start_Year int,
  Finish_Year int,
  Committee_Role varchar(50),
  FOREIGN KEY (Member_name) REFERENCES legislative_body_members(Member_Name) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE rajya_sabha (
  Member_name varchar(100),
  Name_state varchar(20),
  Start_Year int,
  End_Year int,
  FOREIGN KEY (Member_name) REFERENCES legislative_body_members(Member_Name) ON DELETE CASCADE ON UPDATE CASCADE
);

create table department (
  Dept_Name varchar(50) PRIMARY key,
  Minister varchar(100),
  Budget int,
  Number_of_officials int,
  FOREIGN KEY (Minister) REFERENCES lok_sabha(Member_name) ON DELETE CASCADE ON UPDATE CASCADE
);

create table constituency (
  Constituency_ID varchar(5) PRIMARY key,
  Constituency_Name varchar(50) UNIQUE
);

create table constituency_details (
  Constituency_Name varchar(50),
  State_name varchar(50),
  Population_constituency int,
  foreign key (Constituency_Name) REFERENCES constituency(Constituency_Name) ON DELETE CASCADE ON UPDATE CASCADE
);

create table election (
  Constituency_ID varchar(5) UNIQUE,
  Voter_Turnout float,
  Winning_Candidate varchar(100) UNIQUE,
  FOREIGN key (Constituency_ID) REFERENCES constituency(Constituency_ID) ON DELETE CASCADE ON UPDATE CASCADE
);

create table election_candidates (
  Constituency_ID varchar(5),
  Candidates varchar(100)
);

create table elected_party (
  Party_ID varchar(5),
  Winning_Candidate varchar(100),
  foreign key (Winning_Candidate) REFERENCes election(Winning_Candidate) ON DELETE CASCADE ON UPDATE CASCADE
);

create table represent (
  PartyID varchar(5),
  Membername varchar(100),
  ConstituencyID varchar(5),
  FOREIGN KEY (Membername) REFERENCES lok_sabha(Member_name) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (ConstituencyID) REFERENCES constituency(Constituency_ID) ON DELETE CASCADE ON UPDATE CASCADE
);

create table State_name (
  Name_state varchar(50) PRIMARY key,
  Chief_Minister varchar(100),
  Start_Year int,
  finish_Year int
);


