use std::{collections::HashMap, vec};
use std::fs::{File, read_to_string};
use fancy_regex::Regex;


fn main() {
    let re = Regex::new(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))").unwrap();
    let mut values: Vec<u16> = vec![];

    let path = String::from("../input.txt");
    let lines = read_lines(&path);
    for (i, line) in lines.iter().enumerate() {
        let mut matches = re.captures_iter(line);
        let first_item = matches.next()
            .expect("failure")
            .expect("failure")
            .get(1)
            .expect("failure")
            .as_str();
        let last_item = matches.last()
            .map_or(
                first_item, |last| last
                .expect("failure")
                .get(1).
                expect("failure")
                .as_str()
            );
        let numstring = format!("{}{}", convert_numbers(first_item), convert_numbers(last_item));
        println!("{}: {} | first: {} - last: {} --> {}", i + 1 ,line, first_item, last_item, numstring);
        values.push(numstring.parse::<u16>().unwrap());
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

fn convert_numbers(number: &str) -> u16 {
    let number_map = HashMap::<&str, u16>::from([
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven", 7),
        ("eight", 8),
        ("nine", 9)   
    ]);

    match number_map.get(number.trim()) {
        Some(map_value) =>  *map_value,
        None => number.parse::<u16>().unwrap()
    }
}