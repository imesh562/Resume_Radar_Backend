-- Inserting data into quizzes table
INSERT INTO quizzes (title, description, skill, created_at) VALUES
('Python Programming Quiz', 'Test your knowledge of Python programming.', 'Python', NOW()),
('Web Development Quiz', 'Assess your skills in HTML, CSS, and JavaScript.', 'Web Development', NOW()),
('Data Science Quiz', 'Evaluate your understanding of data science concepts.', 'Data Science', NOW()),
('Database Management Quiz', 'Check your knowledge of SQL and databases.', 'Database Management', NOW()),
('Machine Learning Quiz', 'Explore your knowledge in machine learning techniques.', 'Machine Learning', NOW());

-- Inserting data into questions table
INSERT INTO questions (quiz_id, question_text, option_a, option_b, option_c, option_d, correct_answer, created_at) VALUES
-- Questions for Python Programming Quiz (quiz_id = 1)
(1, 'What is the output of print(2 ** 3)?', '8', '6', '4', '2', '8', NOW()),
(1, 'Which keyword is used to define a function in Python?', 'def', 'function', 'define', 'func', 'def', NOW()),
(1, 'What data type is the object below? x = "Hello"', 'String', 'Integer', 'List', 'Boolean', 'String', NOW()),
(1, 'How do you insert COMMENTS in Python code?', '# This is a comment', '// This is a comment', '/* This is a comment */', '<!-- This is a comment -->', '# This is a comment', NOW()),
(1, 'Which method can be used to remove any whitespace from both the beginning and the end of a string?', 'trim()', 'strip()', 'len()', 'ptr()', 'strip()', NOW()),

-- Questions for Web Development Quiz (quiz_id = 2)
(2, 'What does HTML stand for?', 'Hyper Text Markup Language', 'High Text Markup Language', 'Hyperlinks and Text Markup Language', 'Hyper Text Marking Language', 'Hyper Text Markup Language', NOW()),
(2, 'Which tag is used to create a hyperlink in HTML?', '<link>', '<a>', '<href>', '<url>', '<a>', NOW()),
(2, 'Which property is used to change the background color in CSS?', 'bgcolor', 'color', 'background-color', 'background', 'background-color', NOW()),
(2, 'What does CSS stand for?', 'Cascading Style Sheets', 'Colorful Style Sheets', 'Computer Style Sheets', 'Creative Style Sheets', 'Cascading Style Sheets', NOW()),
(2, 'Which HTML element defines the title of a document?', '<title>', '<header>', '<h1>', '<meta>', '<title>', NOW()),

-- Questions for Data Science Quiz (quiz_id = 3)
(3, 'Which library is commonly used for data manipulation in Python?', 'NumPy', 'Pandas', 'Matplotlib', 'Scikit-learn', 'Pandas', NOW()),
(3, 'What is the main purpose of data normalization?', 'Reduce redundancy', 'Enhance visibility', 'Improve accuracy', 'Simplify data', 'Reduce redundancy', NOW()),
(3, 'Which of the following is a supervised learning algorithm?', 'K-Means Clustering', 'Decision Trees', 'Principal Component Analysis', 'None of the above', 'Decision Trees', NOW()),
(3, 'What does "overfitting" mean in machine learning?', 'Model learns the training data too well', 'Model is too simple', 'Model is too complex', 'None of the above', 'Model learns the training data too well', NOW()),
(3, 'Which technique is used for feature selection?', 'PCA', 'LDA', 'RFE', 'All of the above', 'All of the above', NOW()),

-- Questions for Database Management Quiz (quiz_id = 4)
(4, 'Which SQL statement is used to retrieve data from a database?', 'SELECT', 'GET', 'FETCH', 'RETRIEVE', 'SELECT', NOW()),
(4, 'What does SQL stand for?', 'Structured Query Language', 'Standard Query Language', 'Simple Query Language', 'Sequential Query Language', 'Structured Query Language', NOW()),
(4, 'Which command is used to delete a table in SQL?', 'DROP TABLE', 'DELETE TABLE', 'REMOVE TABLE', 'CLEAR TABLE', 'DROP TABLE', NOW()),
(4, 'Which of the following is a valid SQL JOIN?', 'INNER JOIN', 'OUTER JOIN', 'LEFT JOIN', 'All of the above', 'All of the above', NOW()),
(4, 'What is a primary key?', 'A unique identifier for a record', 'A foreign key reference', 'A non-unique field', 'None of the above', 'A unique identifier for a record', NOW()),

-- Questions for Machine Learning Quiz (quiz_id = 5)
(5, 'What is overfitting in machine learning?', 'Model learns noise', 'Model is too simple', 'Model is too complex', 'None of the above', 'Model learns noise', NOW()),
(5, 'Which algorithm is used for classification?', 'Linear Regression', 'K-Means', 'Logistic Regression', 'PCA', 'Logistic Regression', NOW()),
(5, 'What is the purpose of cross-validation?', 'To prevent overfitting', 'To speed up training', 'To increase model complexity', 'None of the above', 'To prevent overfitting', NOW()),
(5, 'Which of the following is a common metric for evaluating classification models?', 'Accuracy', 'Mean Squared Error', 'R-squared', 'All of the above', 'Accuracy', NOW()),
(5, 'What does "feature engineering" involve?', 'Selecting features', 'Creating new features', 'Transforming features', 'All of the above', 'All of the above', NOW());
