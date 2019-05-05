from enum import Enum


class CacheType(Enum):
    search_clans = 'cache_search_clans'
    war_clans = 'cache_war_clans'

    search_players = 'cache_search_players'
    war_players = 'cache_war_players'

    current_wars = 'cache_current_wars'
    war_logs = 'cache_war_logs'

    league_groups = 'cache_league_groups'
    league_wars = 'cache_league_wars'

    locations = 'cache_locations'
    leagues = 'cache_leagues'
    seasons = 'cache_seasons'

    def __str__(self):
        return self.value


HOME_TROOP_ORDER = [
    'Barbarian',
    'Archer',
    'Giant',
    'Goblin',
    'Wall Breaker',
    'Balloon',
    'Wizard',
    'Healer',
    'Dragon',
    'P.E.K.K.A',
    'Baby Dragon',
    'Miner',
    'Electro Dragon',
    'Minion',
    'Hog Rider',
    'Valkyrie',
    'Golem',
    'Witch',
    'Lava Hound',
    'Bowler',
    'Ice Golem',
]

BUILDER_TROOPS_ORDER = [
    'Raged Barbarian',
    'Sneaky Archer',
    'Boxer Giant',
    'Beta Minion',
    'Bomber',
    'Baby Dragon',
    'Cannon Cart',
    'Night Witch',
    'Drop Ship',
    'Super P.E.K.K.A'
]

SPELL_ORDER = [
    'Lightning Spell',
    'Healing Spell',
    'Rage Spell',
    'Jump Spell',
    'Freeze Spell',
    'Clone Spell',
    'Poison Spell',
    'Earthquake Spell',
    'Haste Spell',
    'Skeleton Spell',
    'Bat Spell'
]

HERO_ORDER = [
    'Barbarian King',
    'Archer Queen',
    'Grand Warden',
    'Battle Machine'
]

SIEGE_MACHINE_ORDER = [
    'Wall Wrecker',
    'Battle Blimp',
    'Stone Slammer'
]
