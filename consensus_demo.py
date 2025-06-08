# Consensus Mechanism Simulation (PoW, PoS, DPoS)
import random

# PoW: Power-Based Selection 
miners = [
    {'name': 'MinerA', 'power': random.randint(1, 100)},
    {'name': 'MinerB', 'power': random.randint(1, 100)},
    {'name': 'MinerC', 'power': random.randint(1, 100)}
]

selected_pow = max(miners, key=lambda x: x['power'])
print("  Proof of Work (PoW):")
print("  Miners and power:", miners)
print(f" Selected Miner: {selected_pow['name']} (Power: {selected_pow['power']})")
print("  Logic: Highest power gets to validate the block.\n")

# PoS: Stake-Based Selection 
stakers = [
    {'name': 'StakerX', 'stake': random.randint(100, 1000)},
    {'name': 'StakerY', 'stake': random.randint(100, 1000)},
    {'name': 'StakerZ', 'stake': random.randint(100, 1000)}
]

selected_pos = max(stakers, key=lambda x: x['stake'])
print(" Proof of Stake (PoS):")
print(" Stakers and stake:", stakers)
print(f" Selected Staker: {selected_pos['name']} (Stake: {selected_pos['stake']})")
print(" Logic: More stake = more trust = more likely to be selected.\n")

# DPoS: Voter-Based Delegate Selection
delegates = ['Delegate1', 'Delegate2', 'Delegate3']
voters = [
    {'voter': 'Alice', 'vote': random.choice(delegates)},
    {'voter': 'Bob', 'vote': random.choice(delegates)},
    {'voter': 'Charlie', 'vote': random.choice(delegates)}
]

vote_count = {}
for v in voters:
    vote = v['vote']
    vote_count[vote] = vote_count.get(vote, 0) + 1

selected_dpos = max(vote_count, key=vote_count.get)

print(" Delegated Proof of Stake (DPoS):")
print(" Voters:", voters)
print(" Vote Counts:", vote_count)
print(f" Selected Delegate: {selected_dpos}")
print(" Logic: Delegate with most votes gets to validate.\n")
