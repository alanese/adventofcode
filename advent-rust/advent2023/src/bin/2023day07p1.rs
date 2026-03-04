use std::fs;
use std::collections::HashMap;
use std::cmp::Ordering;

#[derive(PartialEq, Eq, PartialOrd, Ord, Copy, Clone, Hash, Debug)]
enum Card {
    Two,
    Three,
    Four,
    Five,
    Six,
    Seven,
    Eight,
    Nine,
    Ten,
    Jack,
    Queen,
    King,
    Ace
}

impl Card {
    fn from_char(chr: char) -> Card {
        match chr {
            '2' => Card::Two,
            '3' => Card::Three,
            '4' => Card::Four,
            '5' => Card::Five,
            '6' => Card::Six,
            '7' => Card::Seven,
            '8' => Card::Eight,
            '9' => Card::Nine,
            'T' => Card::Ten,
            'J' => Card::Jack,
            'Q' => Card::Queen,
            'K' => Card::King,
            'A' => Card::Ace,
            _ => panic!("Invalid card")
        }
    }
}

#[derive(PartialEq, Eq, PartialOrd, Ord, Debug)]
enum HandType {
    HighCard,
    OnePair,
    TwoPair,
    ThreeOfAKind,
    FullHouse,
    FourOfAKind,
    FiveOfAKind
}

#[derive(PartialEq, Eq, Debug)]
struct Hand {
    cards: [Card; 5]
}

impl Ord for Hand {
    fn cmp(&self, other: &Self) -> Ordering {
        let self_type = self.get_type();
        let other_type = other.get_type();
        if self_type != other_type {
            self_type.cmp(&other_type)
        } else {
            self.cards.cmp(&other.cards)
        }

    }
}

impl PartialOrd for Hand {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        return Some(self.cmp(other));
    }
}

impl Hand {
    fn from_string(hand_str: &str) -> Hand {
        let mut cards = [Card::Two; 5];
        for (i, chr) in hand_str.chars().enumerate() {
            cards[i] = Card::from_char(chr);
        }

        Hand{cards}
    }

    fn get_type(&self) -> HandType {
        //Dummy for now
        
        let counts = self.card_counts();
        if counts.contains_key(&5) {
            return HandType::FiveOfAKind;
        } else if counts.contains_key(&4) {
            return HandType::FourOfAKind;
        } else if counts.contains_key(&3) && counts.contains_key(&2) {
            return HandType::FullHouse;
        } else if counts.contains_key(&3) {
            return HandType::ThreeOfAKind;
        } else if *counts.get(&2).unwrap_or(&0) == 2 {
            return HandType::TwoPair;
        } else if counts.contains_key(&2) {
            return HandType::OnePair;
        }
        
        HandType::HighCard
    }

    fn card_counts(&self) -> HashMap<u32, u32> {
        let mut counts: HashMap<Card, u32> = HashMap::new();
        for card in self.cards {
            let new_count = 1 + counts.get(&card).unwrap_or(&0);
            counts.insert(card, new_count);
        }

        let mut counts_rev: HashMap<u32, u32> = HashMap::new();
        for v in counts.values() {
            let new_count = 1 + counts_rev.get(v).unwrap_or(&0);
            counts_rev.insert(*v, new_count);
        }

        counts_rev
    }
}

fn main() {
    //Read and parse data
    let data = fs::read_to_string("input-07.txt").expect("Unable to read file");
    
    let mut hands: Vec<(Hand, usize)> = Vec::new();
    for line in data.lines() {
        let split: Vec<&str> = line.split_whitespace().collect();
        let new_hand = Hand::from_string(split[0]);
        let value: usize = split[1].parse().unwrap();
        println!("{new_hand:?}");
        println!("{:?}", new_hand.get_type());
        hands.push((new_hand, value));
    }

    hands.sort();

    //Part 1
    let mut total_score: usize = 0;
    for i in 0..hands.len()  {
        total_score += (i+1) * hands[i].1;
    }

    println!("{total_score}");
}