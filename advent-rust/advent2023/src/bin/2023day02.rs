use std::fs;

struct Pull {
    red: u8,
    green: u8,
    blue: u8
}

impl Pull {
    fn compatible(&self, red: u8, green: u8, blue: u8) -> bool {
        return self.red <= red && self.green <= green && self.blue <= blue;
    }
}

fn parse_pull(pull: &str) -> Pull {
    let mut red: u8 = 0;
    let mut green: u8 = 0;
    let mut blue: u8 = 0;

    let colors = pull.split(", ");
    for color in colors {
        let (num, col) = color.split_once(" ").expect("Malformed line");
        let num: u8 = num.parse().expect("Malformed line");
        match col {
            "red" =>   red = num,
            "green" => green = num,
            "blue" => blue = num,
            _ => ()
        }
    }
    return Pull{red: red, green: green, blue: blue};
}

fn parse_game(game: &str) -> (u32, Vec<Pull>) {
    let (game_id_str, pulls) = game.split_once(": ").expect("Malformed line");
    let (_, game_num_str) = game_id_str.split_once(" ").expect("Malformed line");
    let game_id: u32 = game_num_str.parse().expect("Malformed line");

    let mut pull_list: Vec<Pull> = Vec::new();
    let pulls_iter = pulls.split("; ");
    for pull in pulls_iter {
        pull_list.push(parse_pull(pull));
    }

    return (game_id, pull_list);
}

fn game_power(game: &Vec<Pull>) -> u32 {
    let mut red: u8 = 0;
    let mut green: u8= 0;
    let mut blue: u8 = 0;

    for pull in game {
        if pull.red > red {
            red = pull.red;
        }
        if pull.green > green {
            green = pull.green;
        }
        if pull.blue > blue {
            blue = pull.blue;
        }
    }
    return (red as u32) *(blue as u32) *(green as u32);
}

fn main() {
    let input = fs::read_to_string("input-02.txt").expect("Unable to open file");

    let red_cubes: u8 = 12;
    let green_cubes: u8 = 13;
    let blue_cubes: u8 = 14;

    let mut ok_sum: u32 = 0;
    let mut power_sum: u32 = 0;
    for line in input.lines() {
        let (id, pulls)= parse_game(line);
        power_sum += game_power(&pulls);
        let mut ok = true;
        for pull in pulls {
            if !pull.compatible(red_cubes, green_cubes, blue_cubes) {
                ok = false;
                break;
            }
        }
        if ok {
            ok_sum += id;
        }
    }
    println!("{ok_sum}");
    println!("{power_sum}")
    
}