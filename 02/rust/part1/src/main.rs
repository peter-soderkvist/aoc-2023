use std::{collections::HashMap, vec};
use std::fs::{File, read_to_string};


fn main() {
    let mut values: Vec<u16> = vec![];

    let path = String::from("../../../input.txt");
    let lines = read_lines(&path);
    for line in lines.iter() {
        values.push(is_game_possible(line));
    }

    let sum: u16 = values.iter().sum();
    println!("Sum: {}", sum);
}

fn read_lines(filename: &String) -> Vec<String> {
    match File::open(filename) {
        Err(why) => panic!("Could not open {}", why),
        Ok(_) => read_to_string(filename)
            .unwrap()
            .lines()
            .map(String::from)
            .collect(),
    }
}

fn is_game_possible(game: &str) -> u16 {
    let colors = HashMap::<&str, u16>::from([
        ("red", 12),
        ("green", 13),
        ("blue", 14)
    ]);
    
    let mut game_split: Vec<String> = split_to_vec(game.to_string(), ':');
    let game_name_slice = game_split.get(0)
        .cloned()
        .unwrap()
        .trim()
        .split(' ')
        .map(str::to_string)
        .collect::<Vec<String>>();
    game_split.remove(0);
    let game_num: &String = game_name_slice.get(1).unwrap();

    let outcome_split: Vec<String> = split_to_vec(game_split.get(0).unwrap().to_string(), ';');
    for outcome in outcome_split {
        let color_split: Vec<String> = split_to_vec(outcome, ',');
        for color in color_split {
            let cube_split: Vec<String> = split_to_vec(color.trim().to_string(), ' ');
            let cubes: u16 = cube_split.get(0).cloned().unwrap().parse::<u16>().unwrap();
            let color: String = cube_split.get(1).cloned().unwrap();
            
            if cubes > *colors.get(color.as_str()).unwrap() {
                return 0;
            }
        }
    }

    game_num.parse::<u16>().unwrap()
}

fn split_to_vec(string_to_split: String, delim: char) -> Vec<String> {
    return string_to_split.split(delim).map(str::to_string).collect();
}
