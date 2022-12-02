use std::fs;

fn get_play(game: String) -> char {
    let result = game.chars().last().unwrap();
    let opponent_played = game.chars().next().unwrap();

    match [result, opponent_played] {
        ['X', 'A'] => 'C',
        ['X', 'B'] => 'A',
        ['X', 'C'] => 'B',
        ['Y', _] => opponent_played,
        ['Z', 'A'] => 'B',
        ['Z', 'B'] => 'C',
        ['Z', 'C'] => 'A',
        _ => 'n'
    }
}

fn main() {
    let file_path = "02-input.txt";
    let raw_input = fs::read_to_string(file_path).expect("Could not read file {file_path}");
    let individual_games: Vec<String> = raw_input.as_str().split("\n").map(|s| s.to_string()).collect();
    // let individual_games: Vec<&str> = ["A Y", "B X", "C Z"].to_vec();
    let mut points: i32 = 0;

    for game in individual_games {
        if game.len() > 0 {
            let game: String = game.to_string();

            // overall result
            match game.chars().last().unwrap() {
                'X' => points += 0,
                'Y' => points += 3,
                'Z' => points += 6,
                _ => ()
            }

            // what was played
            let play = get_play(game);

            match play {
                'A' => points += 1,
                'B' => points += 2,
                'C' => points += 3,
                _ => ()
            }
        }
    }
    println!("{points}");
}
