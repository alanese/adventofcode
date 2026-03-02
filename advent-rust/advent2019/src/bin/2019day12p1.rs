use std::fs;
use std::cmp::Ordering;
use regex::Regex;

#[derive(Debug, Copy, Clone)]
struct Moon {
    x: i32,
    y: i32,
    z: i32,
    dx: i32,
    dy: i32,
    dz: i32
}

impl Moon {
    fn get_energy(&self) -> i32 {
        (self.x.abs() + self.y.abs() + self.z.abs()) * (self.dx.abs() + self.dy.abs() + self.dz.abs())
    }

    fn accel_towards(&mut self, other: Moon) {
        match self.x.cmp(&other.x) {
            Ordering::Less => self.dx += 1,
            Ordering::Greater => self.dx -= 1,
            Ordering::Equal => ()
        }
        match self.y.cmp(&other.y) {
            Ordering::Less => self.dy += 1,
            Ordering::Greater => self.dy -= 1,
            Ordering::Equal => ()
        }
        match self.z.cmp(&other.z) {
            Ordering::Less => self.dz += 1,
            Ordering::Greater => self.dz -= 1,
            Ordering::Equal => ()
        }
    }

    fn move_step(&mut self) {
        self.x += self.dx;
        self.y += self.dy;
        self.z += self.dz;
    }
}

const MOON_REGEX: &str = r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)>";
fn parse_moon (moon: &str) -> Moon {
    let re = Regex::new(MOON_REGEX).unwrap();

    let captures = re.captures(moon).expect("malformed moon");

    let x: i32 = captures.get(1).unwrap().as_str().parse().unwrap();
    let y: i32 = captures.get(2).unwrap().as_str().parse().unwrap();
    let z: i32 = captures.get(3).unwrap().as_str().parse().unwrap();

    Moon {
        x,
        y,
        z,
        dx: 0,
        dy: 0,
        dz: 0
    }
}

fn main() {
    let data = fs::read_to_string("input-12.txt").expect("Unable to read file");
    
    let mut moons: Vec<Moon> = Vec::new();
    for line in data.lines() {
        moons.push(parse_moon(line));
    }
    
    let mut moons_copy = moons.clone();

    let moon_count = moons_copy.len();
    for step in 0..1000 {
        for i in 0..moon_count {
            let moon_2: Moon = moons_copy.get(i).unwrap().clone();
            for j in 0..moon_count {
                let moon_1: &mut Moon = moons_copy.get_mut(j).unwrap();
                moon_1.accel_towards(moon_2);
            }
        }
        for i in 0..moon_count {
            moons_copy[i].move_step();
        }
        println!("Step {} : {moons_copy:?}", step+1);

    }
    //println!("{moons_copy:?}");
    let mut total = 0;
    for moon in moons_copy {
        total += moon.get_energy();
    }
    println!("{total}");
}