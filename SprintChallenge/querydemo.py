CREATE_TABLE = '''
CREATE TABLE IF NOT EXISTS demo(
                                s VARCHAR(6),
                                x INT,
                                y INT
                                )
                                '''
# Inserting data into demo table
INSERT_INTO = '''
INSERT INTO demo (s, x, y) VALUES('g', 3, 9),
                                 ('v', 5, 7),
                                 ('f', 8, 7); '''
