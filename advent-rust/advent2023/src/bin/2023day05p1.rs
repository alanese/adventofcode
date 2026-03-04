use std::fs;

#[derive(Debug)]
struct CategoryRange {
    target_start: i64,
    source_start: i64,
    length: i64
}

#[derive(Debug)]
struct CategoryMap {
    maps: Vec<CategoryRange>
}

impl CategoryMap {
    fn translate(&self, num: i64) -> i64{
        for range in &self.maps {
            if range.source_start <= num && num < range.source_start + range.length {
                return num + (range.target_start - range.source_start);
            }
        }

        num
    }
}

fn parse_nums(line: &str) -> Vec<i64> {
    let mut nums: Vec<i64> = Vec::new();
    for num in line.split(" ") {
        nums.push(num.parse().unwrap());
    }

    nums
}

fn parse_map(lines: &Vec<&str>, start_index: usize) -> (CategoryMap, usize) {
    let mut ranges: Vec<CategoryRange> = Vec::new();
    let mut index = start_index;
    while index < lines.len() && lines[index] != "" {
        let nums = parse_nums(lines[index]);
        ranges.push(CategoryRange{
            target_start: nums[0],
            source_start: nums[1],
            length: nums[2]
        });
        index += 1;
    }

    (CategoryMap{maps: ranges}, index)
}

fn main() {
    let data = fs::read_to_string("input-05.txt").expect("Unable to read file");

    let mut lines: Vec<&str> = Vec::new();

    for line in data.lines() {
        lines.push(line);
    }

    let seeds: Vec<i64> = parse_nums(lines[0].split_once(" ").unwrap().1);

    let (seed_to_soil, index) = parse_map(&lines, 3);
    let (soil_to_fertilizer, index) = parse_map(&lines, index+2);
    let (fertilizer_to_water, index) = parse_map(&lines, index+2);
    let (water_to_light, index) = parse_map(&lines, index+2);
    let (light_to_temp, index) = parse_map(&lines, index+2);
    let (temp_to_humid, index) = parse_map(&lines, index+2);
    let (humid_to_loc, _) = parse_map(&lines, index+2);

    let mut min_loc: i64 = std::i64::MAX;

    for seed in seeds {
        let soil = seed_to_soil.translate(seed);
        let fert = soil_to_fertilizer.translate(soil);
        let water = fertilizer_to_water.translate(fert);
        let light = water_to_light.translate(water);
        let temp = light_to_temp.translate(light);
        let humid = temp_to_humid.translate(temp);
        let loc = humid_to_loc.translate(humid);

        if loc < min_loc {
            min_loc = loc;
        }

    }

    println!("{min_loc}");


}