use std::fs;

fn surface((x,y,z): (u32, u32, u32)) -> u32 {
    let area = 2*x*y + 2*x*z + 2*y*z;
    let smallest: u32;
    if x<=z && y<=z {
        smallest = x*y;
    } else if x<=y && z<=y {
        smallest = x*z;
    } else {
        smallest = y*z;
    }
    return area + smallest;
}

fn ribbon((x, y, z): (u32, u32, u32)) -> u32 {
    let volume = x*y*z;
    let perimeter: u32;
    if x<=z && y<=z {
        perimeter = 2*x + 2*y;
    } else if x<=y && z<=y {
        perimeter = 2*x + 2*z;
    } else {
        perimeter = 2*y + 2*z;
    }

    return volume + perimeter;
}

fn parse(line: &str) -> (u32, u32, u32) {
    let v: Vec<&str> = line.split("x").collect();

    let x: u32 = v[0].parse().expect("error - malformed line");
    let y: u32 = v[1].parse().expect("error - malformed line");
    let z: u32 = v[2].parse().expect("error - malformed line");
    
    (x,y,z)
}

fn main() {
    let lines = fs::read_to_string("input-02.txt").expect("Unable to read file");

    let mut total_area: u32 = 0;
    let mut total_ribbon: u32 = 0;

    for line in lines.lines() {
        let dimensions = parse(line);
        total_area += surface(dimensions);
        total_ribbon += ribbon(dimensions);
    }
    println!("{}", total_area);
    println!("{}", total_ribbon);
}