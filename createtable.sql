CREATE TABLE tasks (
	task_id serial PRIMARY KEY,
	name varchar(50),
	description varchar(255),
	complete bool
)