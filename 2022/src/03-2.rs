use std::fs;
use std::collections::HashSet;
use std::iter::FromIterator;

fn main() {
    let file_path = "03-input.txt";
    let raw_input = fs::read_to_string(file_path).expect("Could not read file {file_path}");
    let backpacks: Vec<String> = raw_input.as_str().trim().split("\n").map(|s| s.to_string()).collect();

    // let backpacks: Vec<String> = "vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw".split_whitespace().map(|s| s.to_string()).collect();

    let mut total_points: u64 = 0;

    for backpack in backpacks.chunks(3) {
        // println!("{:?}", backpack);
        let first_set: HashSet<char> = HashSet::from_iter(backpack[0].chars());
        let second_set: HashSet<char> = HashSet::from_iter(backpack[1].chars());
        let third_set: HashSet<char> = HashSet::from_iter(backpack[2].chars());

        let intersection: HashSet<char> = &(&first_set & &second_set) & &third_set;

        let common_item = intersection.iter().next().unwrap();
        let ascii_char = *common_item as u64;
        //println!("{:?}, {:?}", common_item, ascii_char);
        let points = match ascii_char {
            ascii_char if ascii_char < 91 => ascii_char - 38,
            _ => ascii_char - 96,
        };
        total_points = total_points + points;
        // println!("{:?}, {:?}, {:?}", common_item, ascii_char, total_points);
    }

    println!("{:?}", total_points);
}
