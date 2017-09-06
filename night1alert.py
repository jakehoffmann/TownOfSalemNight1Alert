"""This simulates a night 1 alert by the veteran in Town of Salem ranked practice mode.
The idea is to test the viability of the strategy. Of course, killing a town early on and having a confirmed veteran is perhaps not as bad simply losing a town. The upside of killing a bad guy is very high too. The data alone is not enough but it's still fun to look at.

This simulates a night 1 alert by the veteran in Town of Salem, ranked practice mode.

Assumptions (most of the big ones):
 1) Escort doesn't act night 1. This seems like a bad play anyways and it will simplify things.
 2) Consort DOES act night 1. Consort knows who the mafia are so it's in their best interest to roleblock somebody night 1.
 3) BG and Doctor act night 1.
 4) Janitor, Forger always act on the same target as GF/Mafioso.
 5) Transporter visits but his action is "ignored" since it's irrelevant from a probability point of view.
 6) Witch visits but her action is also "ignored".
TODO: 7) Should the disguiser/forger act night 1? For now, they do.
"""

import random
from itertools import chain
import logging

LOGFILE = 'results.log'
logging.basicConfig(filename=LOGFILE, level=logging.ERROR, format='%(message)s', filemode='w')

# Escort removed from visitors, as we assume she doesn't act on Night 1
visitors = ['Jailor', 'Investigator', 'Lookout', 'Sheriff', 'Transporter', 'Bodyguard', 'Doctor', 'Godfather', 'Mafioso', 'Blackmailer', 'Consigliere', 'Consort', 'Disguiser', 'Forger', 'Framer', 'Janitor', 'Arsonist', 'Serial Killer', 'Witch']

def simulate_night_one():

    # Step 1: assign roles

    V = 'Veteran'
    J = 'Jailor'
    TI = ['Investigator', 'Lookout', 'Sheriff', 'Spy']
    TS = ['Escort', 'Mayor', 'Medium', 'Retributionist', 'Transporter']
    TP = ['Bodyguard', 'Doctor']
    TK = ['Vigilante'] # no Veteran here since there is always a Veteran in this simulation and Veteran is unique!

    GF = 'Godfather'
    M = 'Mafioso'
    RM = ['Blackmailer', 'Consigliere', 'Consort', 'Disguiser', 'Forger', 'Framer', 'Janitor']

    NK = ['Arsonist', 'Serial Killer', 'Werewolf']
    NE = ['Executioner', 'Jester', 'Witch']

    good_guys = [J] + TI + TS + TP + TK
    bad_guys = [GF, M] + RM + NK + NE

    veteran_kills = []

    # Unique roles: jailor, mayor, retri, veteran. If they get chosen, remove them from the pool of possible
    #  roles to be selected for Random Town (RT).
    randomTI = random.choice(TI)

    randomTS = random.choice(TS)
    if randomTS == 'Mayor' or randomTS == 'Retributionist':
        TS.remove(randomTS)

    randomTP = random.choice(TP)

    RT = TI + TS + TP + TK

    randomRT1 = random.choice(RT)
    if randomRT1 in ['Mayor', 'Retributionist']:
        RT.remove(randomRT1)

    randomRT2 = random.choice(RT)
    if randomRT2 in ['Mayor', 'Retributionist']:
        RT.remove(randomRT2)

    randomRT3 = random.choice(RT)
    if randomRT3 in ['Mayor', 'Retributionist']:
        RT.remove(randomRT3)

    randomRT4 = random.choice(RT)
    if randomRT4 in ['Mayor', 'Retributionist']:
        RT.remove(randomRT4)

    randomRM1 = random.choice(RM)
    randomRM2 = random.choice(RM)

    randomNK = random.choice(NK)
    randomNE = random.choice(NE)

    players = [{'role': V},         # 0
               {'role': J},         # 1
               {'role': randomTI},  # 2
               {'role': randomTS},  # 3
               {'role': randomTP},  # 4
               {'role': randomRT1}, # 5 
               {'role': randomRT2}, # 6
               {'role': randomRT3}, # 7
               {'role': randomRT4}, # 8 
               {'role': GF},        # 9
               {'role': M},         # 10 
               {'role': randomRM1}, # 11 
               {'role': randomRM2}, # 12 
               {'role': randomNK},  # 13
               {'role': randomNE}]  # 14


    # Step 2,  Night 1 occurs:
    #  1) Town and neutral players with a visiting role will visit one player other than themselves.
    #  2) Mafia players with a visiting role will visit one non-mafia player other than themselves.
    #  3) If the veteran is jailed, no killings happen for this simulation.
    #  4) Roleblocks are important as they stop other possible visits to the veteran from happening.
    #  5) Doctor healing a veteran's visitor will save the visitor.

    # Generate random visits according to above rules
    #  Start with the townies...
    for player_num in range(0, 9):
        if players[player_num]['role'] in visitors:
            players[player_num]['visits'] = random.choice([x for x in range(15) if x != player_num])

    #  Now the mafia...
    visited_by_random_maf = False
    visited_by_solo_mafia = -1     # This denotes one of the random mafia who "goes solo", ie. wont visit the Godfather's target and won't visit the same person as another "solo", ie. Consort, Consig, Disguiser, Framer
    for player_num in range(9, 13):
        # Make sure Mafioso, Janitor, Forger would visit the Godfather's target (but two non-killing mafia won't visit the Godfather's target)
        if players[player_num]['role'] in ['Janitor', 'Forger'] and not visited_by_random_maf:
            players[player_num]['visits'] = players[9]['visits']
            visited_by_random_maf = True
        elif players[player_num]['role'] == 'Mafioso':
            players[player_num]['visits'] = players[9]['visits']
        elif players[player_num]['role'] == 'Godfather':
            players[player_num]['visits'] = random.choice([x for x in chain(range(0, 9), range(13, 15)) if x != player_num])
        # the other random mafia would not visit the Godfather's target, they would also not visit same target
        elif players[player_num]['role'] in visitors:
            players[player_num]['visits'] = random.choice([x for x in chain(range(0, 9), range(13, 15)) if x != player_num and x != players[9]['visits'] and x != visited_by_solo_mafia])
            visited_by_solo_mafia = players[player_num]['visits']

            
### I believe the following line is taken care of by the above for loop
#   players[10]['visits'] = players[9]['visits']
            
    #  Finally, the neutrals...
    for player_num in range(13, 15):
        if players[player_num]['role'] in visitors:
            players[player_num]['visits'] = random.choice([x for x in range(15) if x != player_num])

    # Now carry out the actions of the players
    #  First the Jailor...
    jailed = players[1]['visits']
    if jailed == 0:
        logging.debug('Jailor jails the Veteran. No veteran kills night 1.\n\n')
        return [[], 0, 0]
    players[jailed]['jailed'] = True

    #  Now the Consorts (if any)...
    roleblock_immune = ['Escort', 'Consort', 'Transporter', 'Veteran']
    for maybe_consort in [11, 12]: # 11, 12 are random mafia (possible consorts)
        if players[maybe_consort]['role'] == 'Consort' and not players[maybe_consort].get('jailed', False):
            consort_visits = players[maybe_consort]['visits']
            if players[consort_visits] not in roleblock_immune:
                players[consort_visits]['roleblocked'] = True

    #  Now the Doctors (if any)...
    for maybe_doctor in [4, 5, 6, 7, 8]: # 4-8 are town protective and random town
        if players[maybe_doctor]['role'] == 'Doctor' and not players[maybe_doctor].get('jailed', False) and not players[maybe_doctor].get('roleblocked', False):
            doctor_visits = players[maybe_doctor]['visits']
            players[doctor_visits]['healed'] = True

    # Now assess the damage...
    good_result = 0
    bad_result = 0
    #  Check the Godfather and Mafioso first as at most one of them will visit somebody...
    if players[10]['visits'] == 0 and not players[10].get('jailed', False) and not players[10].get('roleblocked', False) and not players[10].get('healed', False):
        veteran_kills.append('Mafioso')
        good_result = bad_result + 1
    elif players[9]['visits'] == 0 and not players[9].get('jailed', False) and not players[9].get('roleblocked', False) and not players[9].get('healed', False):
        veteran_kills.append('Godfather')
        good_result = bad_result + 1 
    #  now check the rest of the players...
    for player_num in chain(range(1, 9), range(11, 15)): # see who visited the Veteran
        if players[player_num].get('visits', -1) == 0 and not players[player_num].get('jailed', False) and not players[player_num].get('roleblocked', False) and not players[player_num].get('healed', False):
            veteran_kills.append(players[player_num]['role'])
            if players[player_num]['role'] in good_guys:
                bad_result = bad_result + 1
            else:
                good_result = good_result + 1

    for player in players:
        blocked = []
        if player.get('jailed', False):
            blocked.append('Jailed')
        if player.get('roleblocked', False):
            blocked.append('Roleblocked')
        role_visited = ''
        if player.get('visits', False):
            role_visited = '({})'.format(players[player['visits']]['role'])
        logging.debug('{blocked}{role} {visits} {player_visited} {role_visited}'.format(
            role=player['role'],
            visits='visits' if player['role'] in visitors else '',
            player_visited=player.get('visits', ''),
            role_visited=role_visited,
            blocked='(' + ', '.join(blocked) + ') ' if blocked != [] else ''
        ))

    logging.debug('---\nThe veteran kills: {}'.format('nobody!' if veteran_kills == [] else ', '.join(veteran_kills)))
    logging.debug('\n')

    return [veteran_kills, good_result, bad_result]
    

# Now we run the simulation a lot of times and track the results.

num_of_simulations = 1000000

total_good_results = 0
total_bad_results = 0
total_veteran_kills = 0
max_good_result = 0
max_bad_result = 0
max_kills = 0
best_difference = 0
worst_difference = 0
kills_per_night_dist = [0] * 12  # maximum of 11 kills with current assumptions
good_kill_dist = [0] * 5         # maximum of 4 good kills with current assumptions
bad_kill_dist = [0] * 8          # maximum of 7 bad kills with current assumptions
role_kill_dist = {role: 0 for role in visitors}

for x in range(num_of_simulations):

    results = simulate_night_one()

    kills = results[0]
    good_result = results[1]
    bad_result = results[2]

    num_kills = good_result + bad_result
    kills_per_night_dist[num_kills] += 1
    good_kill_dist[good_result] += 1
    bad_kill_dist[bad_result] += 1
    total_good_results += good_result
    total_bad_results += bad_result
    total_veteran_kills += good_result + bad_result
    max_good_result = max(max_good_result, good_result)
    max_bad_result = max(max_bad_result, bad_result)
    for killed in kills:
        role_kill_dist[killed] += 1
    
    if max_kills < num_kills:
        max_kills = num_kills
        bloodthirsty_kills = kills
    
    if best_difference < good_result - bad_result:
        best_difference = good_result - bad_result
        best_night_kills = kills
    if worst_difference < bad_result - good_result:
        worst_difference = bad_result - good_result
        worst_night_kills = kills
        

print('Simulation ran {} times'.format(num_of_simulations))
print('Most bloodthirsty veteran: {} kills ({})'.format(max_kills, ', '.join(bloodthirsty_kills)))
print('Total good results: {}'.format(total_good_results))
print('Total bad results: {}'.format(total_bad_results))
print('Total veteran kills: {}'.format(total_veteran_kills))
print('Good results per night: {}'.format(total_good_results / num_of_simulations))
print('Bad results per night: {}'.format(total_bad_results / num_of_simulations))
print('Veteran kills per night: {}'.format(total_veteran_kills / num_of_simulations))
print('On his best night, the veteran killed: {} (+{})'.format(', '.join(best_night_kills), best_difference))
print('On his worst night, the veteran killed: {} (-{})'.format(', '.join(worst_night_kills), worst_difference))
print('Kill distribution:\n{}'.format(kills_per_night_dist))
print('Good kill distribution:\n{}'.format(good_kill_dist))
print('Bad kill distribution:\n{}'.format(bad_kill_dist))
print('Veteran kill distribution:')
sorted_role_kill_dist = sorted(role_kill_dist.items(), key=lambda x:x[1])
for role, times_killed in sorted_role_kill_dist:
    print('{} {}'.format(role.ljust(13), times_killed))
