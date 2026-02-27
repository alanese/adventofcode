use std::fs;
use std::collections::HashSet;

fn match_count(card: &str) -> u32 {
    let (_, card) = card.split_once(": ").expect("Malformed line");
    let (winners, numbers) = card.split_once(" | ").expect("Malformed line");
    let mut win_set: HashSet<u32> = HashSet::new();
    for winner in winners.split_whitespace(){
        win_set.insert(winner.parse().expect("Malformed line"));
    }

    let mut match_count = 0;
    for num in numbers.split_whitespace(){
        if win_set.contains(&num.parse().expect("Malformed line")) {
            match_count += 1;
        }
    }

    return match_count;
}

fn main() {
    let data = fs::read_to_string("input-03.txt").expect("Unable to open file");

    let mut total_score: u32 = 0;
    let mut card_counts: Vec<u128> = Vec::new();
    card_counts.push(1);
    let mut total_cards: u128 = 0;
    for (i, line) in data.lines().enumerate() {
        if i >= card_counts.len() {
            card_counts.push(1);
        }
        let count: u128 = card_counts[i];
        total_cards = total_cards + count;

        let matches = match_count(line);
        for j in i+1..=i+(matches as usize) {
            if card_counts.len() <= j {
                card_counts.push(count+1);
            } else {
                card_counts[j] += count;
            }
        }
        if matches > 0 {
            total_score += 2u32.pow(matches-1);
        }
    }
    println!("{total_score}");
    println!("{total_cards}");


}