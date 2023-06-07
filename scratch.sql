SELECT
  gr.id AS gamer_id,
  u.first_name || ' ' || u.last_name AS full_name,
  g.id AS game_id,
  g.title,
  g.maker,
  g.number_of_players,
  g.skill_level,
  g.game_type_id
FROM
  levelupapi_game AS g
JOIN levelupapi_gamer AS gr ON g.gamer_id=gr.id
JOIN auth_user AS u ON gr.user_id = u.id;

SELECT
  gr.id AS gamer_id,
  u.first_name || ' ' || u.last_name AS full_name,
  g.id AS game_id,
  g.title AS game_name,
  e.id AS event_id,
  e.time,
  e.date
FROM
  levelupapi_game AS g
JOIN levelupapi_gamer AS gr ON g.gamer_id=gr.id
JOIN auth_user AS u ON gr.user_id = u.id
JOIN levelupapi_event AS e ON gr.id = e.host_id;
