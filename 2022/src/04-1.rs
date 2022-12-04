use std::fs;

fn main() {
    let file_path = "04-input.txt";
    let raw_input = fs::read_to_string(file_path).expect("Could not read file {file_path}");
    let lines: Vec<String> = raw_input.as_str().trim().split("\n").map(|s| s.to_string()).collect();

    let mut fully_contained: u32 = 0;

    for line in lines {
        let sections: Vec<String> = line.as_str().split(",").map(|s| s.to_string()).collect();
        let first_section_lims: Vec<u32> = sections[0].as_str().split("-").map(|s| s.parse::<u32>().unwrap()).collect();
        let second_section_lims: Vec<u32> = sections[1].as_str().split("-").map(|s| s.parse::<u32>().unwrap()).collect();

        if ((first_section_lims[0] >= second_section_lims[0]) & (first_section_lims[1] <= second_section_lims[1]))
          | ((first_section_lims[0] <= second_section_lims[0]) & (first_section_lims[1] >= second_section_lims[1])) {
            fully_contained += 1;
          }
    }

    println!("{fully_contained:?}");
}
