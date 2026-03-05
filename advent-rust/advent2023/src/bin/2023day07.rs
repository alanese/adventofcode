use std::fs;
use std::collections::HashMap;
use std::cmp::Ordering;

#[derive(PartialEq, Eq, PartialOrd, Ord, Copy, Clone, Hash, Debug)]
enum Card {
    Joker,
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
    fn from_char_p1(chr: char) -> Card {
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

    fn from_char_p2(chr: char) -> Card {
        if chr == 'J' {
            Card::Joker
        } else {
            Card::from_char_p1(chr)
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
            cards[i] = Card::from_char_p1(chr);
        }

        Hand{cards}
    }

    fn from_string_p2(hand_str: &str) -> Hand {
        let mut cards = [Card::Two; 5];
        for (i, chr) in hand_str.chars().enumerate() {
            cards[i] = Card::from_char_p2(chr);
        }

        Hand{cards}
    }

    fn get_type(&self) -> HandType {
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

    fn get_type_p2(&self) -> HandType {
        let (counts, jokers) = self.card_counts_j_sep();

        let max_count = *counts.keys().max().unwrap_or(&0);

        if jokers == 0 {
            return self.get_type();
        }

        if jokers + max_count == 5 {
            return HandType::FiveOfAKind;
        } else if jokers + max_count == 4 {
            return HandType::FourOfAKind;
        } else if (counts.contains_key(&3) && counts.contains_key(&2)) || (*counts.get(&2).unwrap_or(&0) == 2 && jokers == 1) {
            return HandType::FullHouse;
        } else if counts.contains_key(&3) || (counts.contains_key(&2) && jokers == 1) || (counts.contains_key(&1) && jokers == 2) {
            return HandType::ThreeOfAKind;
        } else {
            return HandType::OnePair;
        }
    }

    fn compare_p2(&self, other: &Self) -> Ordering {
        let self_type = self.get_type_p2();
        let other_type = other.get_type_p2();
        if self_type != other_type {
            self_type.cmp(&other_type)
        } else {
            self.cards.cmp(&other.cards)
        }

    }

    fn card_counts(&self) -> HashMap<u32, u32> {
        let (mut counts, j_count) = self.card_counts_j_sep();

        if j_count != 0 {
            let new_count = 1 + counts.get(&j_count).unwrap_or(&0);
            counts.insert(j_count, new_count);
        }

        counts
    }

    fn card_counts_j_sep(&self) -> (HashMap<u32, u32>, u32) {
        let mut counts: HashMap<Card, u32> = HashMap::new();
        for card in self.cards {
            let new_count = 1 + counts.get(&card).unwrap_or(&0);
            counts.insert(card, new_count);
        }

        let mut counts_rev: HashMap<u32, u32> = HashMap::new();
        let mut j_count: u32 = 0;
        for (c, v) in counts {
            if c == Card::Jack || c == Card::Joker {
                j_count = v;
            } else {
                let new_count = 1 + counts_rev.get(&v).unwrap_or(&0);
                counts_rev.insert(v, new_count);
            }
        }

        (counts_rev, j_count)
    }
}

fn main() {
    //Read and parse data
    let data = fs::read_to_string("input-07.txt").expect("Unable to read file");
    
    let mut hands: Vec<(Hand, usize)> = Vec::new();
    let mut p2_hands: Vec<(Hand, usize)> = Vec::new();
    for line in data.lines() {
        let split: Vec<&str> = line.split_whitespace().collect();
        let new_hand = Hand::from_string(split[0]);
        let new_hand_p2 = Hand::from_string_p2(split[0]);
        let value: usize = split[1].parse().unwrap();
        hands.push((new_hand, value));
        p2_hands.push((new_hand_p2, value));
    }

    //Part 1
    hands.sort();

    let mut total_score: usize = 0;
    for i in 0..hands.len()  {
        total_score += (i+1) * hands[i].1;
    }

    println!("{total_score}");

    //Part 2
    p2_hands.sort_by(|a, b| a.0.compare_p2(&b.0));

    total_score = 0;
    for i in 0..hands.len() {
        total_score += (i+1) * p2_hands[i].1;
    }

    println!("{total_score}");
}