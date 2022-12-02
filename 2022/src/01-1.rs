use std::fs;

fn main() {
    let file_path = "01-input.txt";
    let raw_input = fs::read_to_string(file_path).expect("Could not read file {file_path}");
    let individual_elves: Vec<String> = raw_input.as_str().split("\n\n").map(|s| s.to_string()).collect();

    let mut elf_sums: Vec<i32> = Vec::new();

    for elf in individual_elves {
        let elf: String = elf;
        let calories: Vec<String> = elf.split_whitespace().map(|s| s.to_string()).collect();
        let calories_map = calories.iter().map(|cal| {
            cal.parse::<i32>().unwrap()
        });
        let calories_sum = calories_map.into_iter().sum();

        elf_sums.push(calories_sum);
    }
    let max_elf_sum: &i32 = elf_sums.iter().max().unwrap();
    println!("{max_elf_sum:?}")
}
