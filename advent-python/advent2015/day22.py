from enum import Enum
from typing import Dict, List, NamedTuple, Optional, Tuple

class State(Enum):
    ACTIVE = 1
    PLAYER_WIN = 2
    BOSS_WIN = 3
    ERROR = 4

class Spell(Enum):
    MAGIC_MISSILE = 1
    DRAIN = 2
    SHIELD = 3
    POISON = 4
    RECHARGE = 5

class GameStatus(NamedTuple):
    player_hp: int
    player_mp: int
    shield_duration: int
    poison_duration: int
    recharge_duration: int
    boss_hp: int
    boss_dmg: int
    state: State

SPELL_COSTS: Dict[Spell, int] = {Spell.MAGIC_MISSILE: 53,
                                 Spell.DRAIN: 73,
                                 Spell.SHIELD: 113,
                                 Spell.POISON: 173,
                                 Spell.RECHARGE: 229}
POISON_DMG = 3
RECHARGE_MP = 101

def boss_turn(state: GameStatus) -> GameStatus:
    player_hp, player_mp, shield_duration, poison_duration, recharge_duration, boss_hp, boss_dmg, _ = state
    if shield_duration > 0:
        shield_duration -= 1
    if poison_duration > 0:
        poison_duration -= 1
        boss_hp -= POISON_DMG
    if recharge_duration > 0:
        recharge_duration -= 1
        player_mp += RECHARGE_MP

    if boss_hp <= 0:
        return GameStatus(player_hp, player_mp, shield_duration, poison_duration, recharge_duration, boss_hp, boss_dmg, State.PLAYER_WIN)

    player_armor = 7 if shield_duration > 0 else 0
    player_hp -= max(boss_dmg - player_armor, 1)
    if player_hp <= 0:
        return GameStatus(player_hp, player_mp, shield_duration, poison_duration, recharge_duration, boss_hp, boss_dmg, State.BOSS_WIN)
    else:
        return GameStatus(player_hp, player_mp, shield_duration, poison_duration, recharge_duration, boss_hp, boss_dmg, State.ACTIVE)
        
def player_turn(state: GameStatus, hard_mode: bool, spell: Spell) -> GameStatus:
    player_hp, player_mp, shield_duration, poison_duration, recharge_duration, boss_hp, boss_dmg, _ = state
    if hard_mode:
        player_hp -= 1
        if player_hp <= 0:
            return GameStatus(0, 0, 0, 0, 0, 0, 0, State.BOSS_WIN)
    if shield_duration > 0:
        shield_duration -= 1
    if poison_duration > 0:
        poison_duration -= 1
        boss_hp -= POISON_DMG
    if recharge_duration > 0:
        recharge_duration -= 1
        player_mp += RECHARGE_MP

    if boss_hp <= 0:
        return GameStatus(player_hp, player_mp, shield_duration, poison_duration, recharge_duration, boss_hp, boss_dmg, State.PLAYER_WIN)
    if SPELL_COSTS[spell] > player_mp:
        return GameStatus(0, 0, 0, 0, 0, 0, 0, State.ERROR)
    player_mp -= SPELL_COSTS[spell]
    match spell:
        case Spell.MAGIC_MISSILE:
            boss_hp -= 4
        case Spell.DRAIN:
            boss_hp -= 2
            player_hp += 2
        case Spell.SHIELD:
            if shield_duration != 0:
                return GameStatus(0, 0, 0, 0, 0, 0, 0, State.ERROR)
            shield_duration = 6
        case Spell.POISON:
            if poison_duration != 0:
                return GameStatus(0, 0, 0, 0, 0, 0, 0, State.ERROR)
            poison_duration = 6
        case Spell.RECHARGE:
            if recharge_duration != 0:
                return GameStatus(0, 0, 0, 0, 0, 0, 0, State.ERROR)
            recharge_duration = 5

    if boss_hp <= 0:
        return GameStatus(player_hp, player_mp, shield_duration, poison_duration, recharge_duration, boss_hp, boss_dmg, State.PLAYER_WIN)
    else:
        return GameStatus(player_hp, player_mp, shield_duration, poison_duration, recharge_duration, boss_hp, boss_dmg, State.ACTIVE)
    
def min_win_from(start: GameStatus, hard_mode: bool, seen:Dict[GameStatus, Tuple[List[Spell], Optional[int]]] = {}, max_rest: Optional[int] = None) -> Tuple[List[Spell], Optional[int]]:
    if start in seen:
        return seen[start]
    #Possible player turns
    followup_turns: List[Tuple[Spell, GameStatus]] = []
    min_seen = None
    min_sequence = []

    #Check if any spells win this turn
    for spell in Spell:
        if max_rest is not None and SPELL_COSTS[spell] > max_rest:
            continue
        spell_turn = player_turn(start, hard_mode, spell)
        if spell_turn.state == State.PLAYER_WIN:
            if min_seen is None or SPELL_COSTS[spell] < min_seen:
                min_seen = SPELL_COSTS[spell]
                min_sequence = [spell]
        if spell_turn.state == State.ACTIVE:
            followup_turns.append((spell, spell_turn))

    after_boss_turns = []
    for spell, turn in followup_turns:
        after_boss_turn = boss_turn(turn)
        if after_boss_turn.state == State.PLAYER_WIN:
            if min_seen is None or SPELL_COSTS[spell] < min_seen:
                min_seen = SPELL_COSTS[spell]
                min_sequence = [spell]
        elif after_boss_turn.state == State.ACTIVE:
            after_boss_turns.append((spell, after_boss_turn))
    
    for spell, turn in after_boss_turns:
        new_max_rest = None if max_rest is None else max_rest - SPELL_COSTS[spell]
        min_from_turn_seq, min_from_turn = min_win_from(turn, hard_mode, seen, new_max_rest)
        if min_seen is None and min_from_turn is not None:
            min_seen = SPELL_COSTS[spell] + min_from_turn
            min_sequence = min_from_turn_seq + [spell]
        elif min_seen is not None and min_from_turn is not None and SPELL_COSTS[spell] + min_from_turn < min_seen:
            min_seen = SPELL_COSTS[spell] + min_from_turn
            min_sequence = min_from_turn_seq + [spell]
    
    seen[start] = min_sequence, min_seen
    #print(f"Min from {start}: {min_sequence}, {min_seen}")
    return min_sequence, min_seen    


with open("input-22.txt") as f:
    boss_hp = int(f.readline().strip().split()[-1])
    boss_dmg = int(f.readline().strip().split()[-1])


initial_status = GameStatus(50, 500, 0, 0, 0, boss_hp, boss_dmg, State.ACTIVE)
print(f"Part 1: {min_win_from(initial_status, False)}")
print(f"Part 2 (Hard Mode): {min_win_from(initial_status, True, {})}")
