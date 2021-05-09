# imports.
import sqlite3

# queries.
# 1.how many total characters are there? #302
q1 = 'SELECT COUNT (character_id) \
FROM charactercreator_character'
# 2.how many of each specific subclass?
# cleric. #75
q2a = 'SELECT COUNT (character_ptr_id) \
FROM charactercreator_cleric'
# fighter. #68
q2b = 'SELECT COUNT (character_ptr_id) \
FROM charactercreator_fighter'
# mage. #108
q2c = 'SELECT COUNT (character_ptr_id) \
FROM charactercreator_mage'
# necromancer. #11
q2d = 'SELECT COUNT (mage_ptr_id) \
FROM charactercreator_necromancer'
# thief. #51
q2e = 'SELECT COUNT (character_ptr_id) \
FROM charactercreator_thief'
# 3.how many total items? #174
q3 = 'SELECT COUNT (item_id) \
FROM armory_item'
# 4a.how many of the items are weapons? #37
q4a = 'SELECT COUNT (item_ptr_id) \
FROM armory_weapon'
# 4b.how many are not? #137
q4b = 'SELECT COUNT (item_id) \
FROM armory_item \
WHERE item_id \
NOT IN \
(SELECT item_ptr_id \
 FROM armory_weapon)'
# 5.how many items does each character have? (return first 20 rows)
q5 = 'SELECT cc.name, COUNT(ai.name) \
FROM charactercreator_character cc, \
	 armory_item ai, \
	 charactercreator_character_inventory cci \
WHERE cc.character_id = cci.character_id \
AND ai.item_id = cci.item_id \
GROUP BY ai.item_id \
ORDER BY COUNT(ai.name) DESC \
LIMIT 20'
# 6.how many weapons does each character have? (return first 20 rows)
q6 = 'SELECT cc.name, COUNT(ai.name) \
FROM charactercreator_character cc, \
     armory_item ai, \
     charactercreator_character_inventory cci, \
     armory_weapon aw \
WHERE cc.character_id = cci.character_id \
AND ai.item_id = cci.item_id \
AND ai.item_id = aw.item_ptr_id \
GROUP BY ai.item_id \
ORDER BY COUNT(ai.name) DESC \
LIMIT 20'
# 7.on average, how many items does each character have? #5.160919540229885
q7 = 'SELECT AVG(COUNT) \
FROM \
(SELECT COUNT(ai.item_id) AS COUNT \
 FROM charactercreator_character cc, \
      armory_item ai, \
      charactercreator_character_inventory cci \
WHERE cc.character_id = cci.character_id \
AND ai.item_id = cci.item_id \
GROUP BY ai.item_id) '
# 8.on average, how many weapons does each character have? #5.486486486486487
q8 = 'SELECT AVG(COUNT) \
FROM \
(SELECT COUNT(ai.item_id) AS COUNT \
 FROM charactercreator_character cc, \
	 armory_item ai, \
	 charactercreator_character_inventory cci, \
	 armory_weapon aw \
 WHERE cc.character_id = cci.character_id \
 AND ai.item_id = cci.item_id \
 AND ai.item_id = aw.item_ptr_id \
 GROUP BY ai.name)'

# connection.
conn = sqlite3.connect('rpg_db.sqlite3')

# executes.
# 1.how many total characters are there? #302
curs1 = conn.cursor()
print('Total characters =', curs1.execute(q1).fetchall())
# 2.how many of each specific subclass?
# 2a.cleric. #75
curs2a = conn.cursor()
print('Total clerics =', curs2a.execute(q2a).fetchall())
#2b.fighter. #68
curs2b = conn.cursor()
print('Total fighters =', curs2b.execute(q2b).fetchall())
# 2c.mage. #108
curs2c = conn.cursor()
print('Total mages =', curs2c.execute(q2c).fetchall())
# 2d.necromancer. #11
curs2d = conn.cursor()
print('Total necromancers =', curs2d.execute(q2d).fetchall())
# 2e.thief. #51
curs2e = conn.cursor()
print('Total thiefs =', curs2e.execute(q2e).fetchall())
# 3.how many total items? #174
curs3 = conn.cursor()
print('Total items =', curs3.execute(q3).fetchall())
# 4a.how many of the items are weapons? #37
curs4a = conn.cursor()
print('Total items = weapons =', curs4a.execute(q4a).fetchall())
# 4b.#37 how many are not? #137
curs4b = conn.cursor()
print('Total items = non weapons =', curs3.execute(q4b).fetchall())
# 5.how many items does each character have? (return first 20 rows)
curs5 = conn.cursor()
print('Total items each character has, top 20 =', curs5.execute(q5).fetchall())
# 6.how many weapons does each character have? (return first 20 rows)
curs6 = conn.cursor()
print('Total items = weapons each character has, top 20 =',
      curs6.execute(q6).fetchall())
# 7.on average, how many items does each character have? #5.160919540229885
curs7 = conn.cursor()
print('AVG items each character has =', curs7.execute(q7).fetchall())
# 8.on average, how many weapons does each character have? #5.486486486486487
curs8 = conn.cursor()
print('AVG items = weapons each character has =', curs8.execute(q8).fetchall())

# close cursors.
curs1.close()
curs2a.close()
curs2b.close()
curs2c.close()
curs2d.close()
curs2e.close()
curs3.close()
curs4a.close()
curs4b.close()
curs5.close()
curs6.close()
curs7.close()
curs8.close()

# commit.
conn.commit()
