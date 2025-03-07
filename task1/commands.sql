-- 1. Get all tasks of a specific user. Use SELECT to get the tasks of a specific user at his user_id.

SELECT *
FROM tasks
WHERE user_id = 1;

-- 2. Select tasks by specific status. Use a subquery to select tasks with a specific status, such as' new '.

SELECT *
FROM tasks
WHERE status_id IN (SELECT id
    FROM status
    WHERE name = 'new');

-- 3. Update the status of a specific task. Change the status of a specific task to 'in progress' or another status.

UPDATE tasks SET status_id = 2 WHERE id = 6;

-- 4. Get a list of users who do not have any tasks. Use the combination SELECT, WHERE NOT IN, and subquery.

SELECT *
FROM users
WHERE id NOT IN (SELECT user_id
    FROM tasks);

-- 5. Add a new task for a specific user. Use INSERT to add a new task.

INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('TO do', 'breakfast', 1, 7);

-- 6. Get all tasks that are not yet completed. Select a task whose status is not 'completed'.

SELECT *
FROM tasks
WHERE status_id NOT IN (SELECT id
    FROM status
    WHERE name = 'completed');

-- 7. Delete a specific task. Use DELETE to delete a task by its id.

DELETE FROM tasks WHERE id = 5;

-- 8. Find users with a specific email. Use SELECT with the LIKE condition to filter by email.

SELECT *
FROM users
WHERE email LIKE '%.com';

-- 9. Update user name. Use UPDATE to change the user name.

UPDATE users SET fullname = "Elis Kelly" WHERE id = 6;

-- 10. Get the number of jobs for each status. Use SELECT, COUNT, GROUP BY to group tasks by status.

SELECT COUNT(status_id) as total_tasks, status_id
FROM tasks
GROUP BY status_id

-- 11. Get tasks that are assigned to users with a specific email domain part. Use SELECT with the LIKE condition in conjunction with JOIN to select tasks assigned to users whose email contains a specific domain (for example, '% @ example.com').

SELECT u.id AS users_id, u.email, t.title, t.description
FROM users AS u
WHERE email LIKE '%@gmail.com'
INNER JOIN tasks =AS t ON t.user_id = u.id;

-- 12. Get a list of tasks that do not have a description. Select tasks that do not have a description.

SELECT *
FROM tasks
WHERE description NOT LIKE '%'

-- 13. Select users and their tasks that are in progress. Use INNER JOIN to get a list of users and their tasks with a specific status.

SELECT u.id AS users_id, u.email, t.title, t.description
FROM tasks AS t
WHERE status_id = 2
INNER JOIN users AS u ON u.id = t.user_id;

-- 14. Get users and the number of their tasks. Use LEFT JOIN and GROUP BY to select users and count their tasks.

SELECT u.id AS users_id, u.email, COUNT(t.user_id) AS total_tasks
FROM users AS u
LEFT JOIN tasks AS t ON t.user_id = u.id
GROUP BY user_id;

