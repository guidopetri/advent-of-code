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
    let mut sorted_reversed_elf_sum = elf_sums.clone();
    sorted_reversed_elf_sum.sort();
    sorted_reversed_elf_sum.reverse();
    let top_three: Vec<i32> = sorted_reversed_elf_sum[..3].to_vec();
    let top_three_sum: i32 = top_three.iter().sum::<i32>();
    println!("{top_three_sum:?}")
}
