Practice! Go back to both your deployed PostgreSQL (Titanic data) and MongoDB
(RPG data) instances - use [MongoDB
queries](https://docs.mongodb.com/manual/tutorial/query-documents/) to answer
the same questions as you did from the first module (when the RPG data was in
SQLite):

1. How many total Characters are there?
   - SELECT * FROM charactercreator_character;
-  - 302
-  
2. How many total Items?
   - SELECT COUNT(*) FROM armory_item; 
   - 174
   - 
3. How many of the Items are weapons? How many are not?
   - "SELECT COUNT(*) FROM  armory_item AS ai\
           JOIN armory_weapon AS aw\
           ON ai.item_id = aw.item_ptr_id;"
    - weapons: 37, 
    - 
    - "SELECT COUNT (item_id)\
        FROM armory_item\
        WHERE item_id\
        NOT IN (SELECT item_ptr_id \
        FROM armory_weapon);"
    - non weapons: 137
    - 
4. How many Items does each character have? (Return first 20 rows)
   - "SELECT name , COUNT(item_id) AS count\
    FROM charactercreator_character as ccc\
    JOIN charactercreator_character_inventory as ccci\
    ON ccc.character_id == ccci.character_id\
    GROUP BY ccc.character_id\
    LIMIT 20;"
   -  3,3,2,4,4,1,5,3,4,4,3,3,4,4,4,1,5,5,3,1
   -  
5. How many Weapons does each character have? (Return first 20 rows)
   - "SELECT name, COUNT(*) AS weapons\
    FROM charactercreator_character AS creator\
    JOIN charactercreator_character_inventory AS inventory\
    ON creator.character_id = inventory.character_id\
    JOIN armory_weapon AS aw\
    ON aw.item_ptr_id = inventory.item_id\
    GROUP BY name\
    LIMIT 20;"
  - 2,1,1,1,1,1,1,3,2,1,1,1,2,3,2,2,2,1,1,1
  - 
6. On average, how many Items does each Character have? 
   - SELECT AVG(COUNT)\
    FROM (SELECT COUNT(cci.item_id) AS COUNT\
    FROM charactercreator_character cc,\
        charactercreator_character_inventory cci\
    WHERE cc.character_id = cci.character_id\
    GROUP BY cci.item_id);
- - 5.16
- 
7. On average, how many Weapons does each character have?
   - "SELECT AVG(weapons)\
        FROM (SELECT name, COUNT(*) AS weapons\
        FROM charactercreator_character AS creator\
        JOIN charactercreator_character_inventory AS inventory\
        ON creator.character_id = inventory.character_id\
        JOIN armory_weapon AS aw\
        ON aw.item_ptr_id = inventory.item_id\
        GROUP BY name);"
    - 1.326


With PostgreSQL, answer the following:
1. How many passengers survived, and how many died? 
   1. select count(*) from titanic where survived = 1;
       684
   2. select count(*) from titanic where survived = 0;
       1090
2. How many passengers were in each class?
   1.  select count(*) from titanic where pclass = 1; 
        pclass 1 = 432, 
   2. select count(*) from titanic where pclass = 2;
       pclass 2 = 368, 
   3. select count(*) from titanic where pclass = 3;
       pclass 3 = 974
3. How many passengers survived/died within each class? 
   1. select count(*) from titanic where pclass = 1 and survived = 1
         pclass 1 survived = 272, 
      select count(*) from titanic where pclass = 1 and survived = 0;
         pclass 1 died= 160 
   2.  select count(*) from titanic where pclass = 2 and survived = 1
         pclass 2 survived = 174, 
      select count(*) from titanic where pclass = 2 and survived = 0;
         pclass 2 died= 194 
   3.  select count(*) from titanic where pclass = 3 and survived = 1;
         pclass 3 survived = 238, 
      select count(*) from titanic where pclass = 3 and survived = 0;
        pclass 3 died= 736
4. What was the average age of survivors vs nonsurvivors? 
    select avg(age) from titanic where survived = 1;
        avg age survived = 28.408
    select avg(age) from titanic where survived = 1;
        avg age died = 30.138
5. What was the average age of each passenger class?
     select avg(age) from titanic where pclass = 3;
        pclass 1 = 38.7889
     select avg(age) from titanic where pclass = 3;
        pclass 2 = 29.868
     select avg(age) from titanic where pclass = 3;
        pclass 3 = 25.1887
6.  What was the average fare by passenger class? By survival?
      select avg(fare) from titanic where pclass = 1;
          84.15
      select avg(fare) from titanic where pclass = 2;
          20.66
      select avg(fare) from titanic where pclass = 3;
          13.70
      select avg(fare) from titanic where survived = 1;
          48.39
      select avg(fare) from titanic where survived = 0 ; 
        22.20
12. How many siblings/spouses aboard on average, by passenger class? By survival? 
13. select avg(sibling_spouse_aboard) from titanic where pclass = 1;
         0.4
      select avg(sibling_spouse_aboard) from titanic where pclass = 2;
         0.402
      select avg(sibling_spouse_aboard) from titanic where pclass = 3;
        0.62
      select avg(sibling_spouse_aboard) from titanic where survived = 1;
        0.47
      select avg(sibling_spouse_aboard) from titanic where survived = 0 ; 
        0.557
8. How many parents/children aboard on average, by passenger class? By survival?
9. select avg(parent_child_aboard) from titanic where pclass = 1;
         0.35
      select avg(parent_child_aboard) from titanic where pclass = 2;
         0.38
      select avg(parent_child_aboard) from titanic where pclass = 3;
        0.39
      select avg(parent_child_aboard) from titanic where survived = 1;
        0.46
      select avg(parent_child_aboard) from titanic where survived = 0 ; 
        0.332
9. Do any passengers have the same name?  NOT SURE
    select count(*)from  (SELECT count(name)
                            FROM titanic
                            GROUP BY name
                            HAVING COUNT(*) > 1) titanic ;
    887
11. (Bonus! Hard, may require pulling and processing with Python) How many married
  couples were aboard the Titanic? Assume that two people (one `Mr.` and one
  `Mrs.`) with the same last name and with at least 1 sibling/spouse aboard are
  a married couple. 
  select count(*) from titanic where sibling_spouse_aboard = 1;
  418