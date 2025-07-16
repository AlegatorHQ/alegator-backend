# Database table for Alegator

IMPORTANT: Users is mostly handled by Supabase Auth. check how to handle it in this

CREATE TABLE tournaments (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    description_tournament TEXT,
    tournament_status TEXT NOT NULL,
    avoid_same_institution BOOLEAN NOT NULL,
    shortname TEXT,
    place TEXT,
    missing_feedbacks BOOLEAN NOT NULL,
    feedback_description TEXT,
    minimum_panel_score INTEGER NOT NULL,
    check_in BOOLEAN NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    creator_id INTEGER NOT NULL REFERENCES users_user(id) ON DELETE PROTECT
);

CREATE TABLE usertournament (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users_user(id) ON DELETE CASCADE,
    tournament_id INTEGER REFERENCES tournaments(id) ON DELETE CASCADE,
    role TEXT NOT NULL
);

CREATE TABLE speakers (
    id SERIAL PRIMARY KEY,
    tournament_id INTEGER NOT NULL REFERENCES tournaments(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    province TEXT NOT NULL,
    delegation TEXT NOT NULL,
    is_novice BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    tournament_id INTEGER NOT NULL REFERENCES tournaments(id) ON DELETE CASCADE,
    name TEXT NOT NULL UNIQUE,
    speaker_1_id INTEGER NOT NULL REFERENCES speakers(id) ON DELETE PROTECT,
    speaker_2_id INTEGER NOT NULL REFERENCES speakers(id) ON DELETE PROTECT
);

CREATE TABLE judges (
    id SERIAL PRIMARY KEY,
    tournament_id INTEGER NOT NULL REFERENCES tournaments(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    province TEXT NOT NULL,
    delegation TEXT NOT NULL,
    team_id INTEGER NOT NULL REFERENCES teams(id) ON DELETE PROTECT,
    basescore DECIMAL(3,2) NOT NULL
);

CREATE TABLE rounds (
    id SERIAL PRIMARY KEY,
    tournament_id INTEGER NOT NULL REFERENCES tournaments(id) ON DELETE CASCADE,
    name TEXT NOT NULL UNIQUE,
    motion TEXT NOT NULL,
    infoslide TEXT NOT NULL,
    round_number INTEGER NOT NULL,
    round_status TEXT NOT NULL,
    round_type BOOLEAN NOT NULL,
    is_silenced BOOLEAN NOT NULL
);

CREATE TABLE draws (
    id SERIAL PRIMARY KEY,
    tournament_id INTEGER NOT NULL REFERENCES tournaments(id) ON DELETE CASCADE,
    round_id INTEGER NOT NULL REFERENCES rounds(id) ON DELETE PROTECT,
    draw_status TEXT NOT NULL,
    ag_id INTEGER REFERENCES speakers(id) ON DELETE CASCADE,
    ao_id INTEGER REFERENCES speakers(id) ON DELETE CASCADE,
    bg_id INTEGER REFERENCES speakers(id) ON DELETE CASCADE,
    bo_id INTEGER REFERENCES speakers(id) ON DELETE CASCADE
);

CREATE TABLE drawsjudges (
    id SERIAL PRIMARY KEY,
    tournament_id INTEGER NOT NULL REFERENCES tournaments(id) ON DELETE CASCADE,
    draw_id INTEGER NOT NULL REFERENCES judges(id) ON DELETE PROTECT,
    judge_id INTEGER NOT NULL REFERENCES judges(id) ON DELETE PROTECT,
    role TEXT NOT NULL,
    is_checked BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE teamresults (
    id SERIAL PRIMARY KEY,
    tournament_id INTEGER NOT NULL REFERENCES tournaments(id) ON DELETE CASCADE,
    draw_id INTEGER REFERENCES draws(id) ON DELETE PROTECT,
    team_id INTEGER REFERENCES teams(id) ON DELETE PROTECT,
    position TEXT NOT NULL,
    points INTEGER NOT NULL
);

CREATE TABLE speakerresults (
    id SERIAL PRIMARY KEY,
    tournament_id INTEGER NOT NULL REFERENCES tournaments(id) ON DELETE CASCADE,
    draw_id INTEGER REFERENCES draws(id) ON DELETE PROTECT,
    speaker_id INTEGER REFERENCES speakers(id) ON DELETE PROTECT,
    speaker_points DECIMAL(3,2) NOT NULL,
    is_iron BOOLEAN NOT NULL DEFAULT FALSE,
    team_result_id INTEGER REFERENCES teamresults(id) ON DELETE PROTECT
);

CREATE TABLE checkins (
    id SERIAL PRIMARY KEY,
    tournament_id INTEGER NOT NULL REFERENCES tournaments(id) ON DELETE CASCADE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    update_at TIMESTAMP NOT NULL,
    round_id INTEGER NOT NULL UNIQUE REFERENCES rounds(id) ON DELETE CASCADE,
    speaker_id INTEGER NOT NULL UNIQUE REFERENCES speakers(id) ON DELETE CASCADE
);

CREATE TABLE feedbacks (
    id SERIAL PRIMARY KEY,
    tournament_id INTEGER NOT NULL REFERENCES tournaments(id) ON DELETE CASCADE,
    draw_id INTEGER NOT NULL REFERENCES draws(id) ON DELETE PROTECT,
    feedback_type VARCHAR(20) NOT NULL CHECK (feedback_type IN ('speaker_to_judge', 'judge_to_speaker')),
    given_by TEXT NOT NULL,
    target TEXT NOT NULL,
    comment TEXT NOT NULL,
    score INTEGER NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending'
);