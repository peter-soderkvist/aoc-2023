use std::{collections::HashMap, vec};
use std::fs::{File, read_to_string};


fn main() {
    let mut values: Vec<u32> = vec![];
    
    let path = String::from("../../../input.txt");
    let lines = read_lines(&path);
    for line in lines.iter() {
        let min_cubes: HashMap::<&str, u32> = get_min_cubes(line);
        values.push(
            (min_cubes.get("red").unwrap()) *
            (min_cubes.get("green").unwrap()) *
            (min_cubes.get("blue").unwrap())
        );
    }

    let sum: u32 = values.iter().sum();
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

fn get_min_cubes(game: &str) -> HashMap::<&str, u32> {
    let mut colors = HashMap::<&str, u32>::from([
        ("red", 1),
        ("green", 1),
        ("blue", 1)
    ]);

    let mut game_split: Vec<String> = split_to_vec(game.to_string(), ':');
    game_split.remove(0);

    let outcome_split: Vec<String> = split_to_vec(game_split.get(0).unwrap().to_string(), ';');
    for outcome in outcome_split {
        let color_split: Vec<String> = split_to_vec(outcome, ',');
        for color in color_split {
            let cube_split: Vec<String> = split_to_vec(color.trim().to_string(), ' ');
            let cubes: u32 = cube_split.get(0)
                .cloned()
                .unwrap()
                .parse::<u32>()
                .unwrap();
            let color: String = cube_split.get(1)
                .cloned()
                .unwrap();
            
            if cubes > *colors.get(color.as_str()).unwrap() {
                *colors.get_mut(color.as_str()).unwrap() = cubes;
            }
        }
    }

    colors
}

fn split_to_vec(string_to_split: String, delim: char) -> Vec<String> {
    return string_to_split.split(delim).map(str::to_string).collect();
}
