use std::fs;

fn get_result(game: String) -> i32 {
    let first_char = game.chars().next().unwrap();
    let last_char = game.chars().last().unwrap();

    match [first_char, last_char] {
        ['A', 'Y'] => 1,
        ['A', 'X'] => 0,
        ['A', 'Z'] => -1,
        ['B', 'Y'] => 0,
        ['B', 'X'] => -1,
        ['B', 'Z'] => 1,
        ['C', 'Y'] => -1,
        ['C', 'X'] => 1,
        ['C', 'Z'] => 0,
        _ => -2
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
            match game.chars().last().unwrap() {
                'X' => points += 1,
                'Y' => points += 2,
                'Z' => points += 3,
                _ => ()
            }

            let result = get_result(game);

            match result {
                1 => points += 6,
                0 => points += 3,
                -1 => (),
                _ => ()
            }
        }
    }
    println!("{points}");
}
