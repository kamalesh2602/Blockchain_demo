# ✅ Tamper WITHOUT recalculating hash (IMPORTANT FIX)
def tamper_chain(blockchain):
    if len(blockchain.chain) > 1:
        blockchain.chain[1].transactions = ["FAKE LAND TRANSFER"]
        # ❌ DO NOT update hash


# ✅ Validation wrapper
def validate_chain(blockchain):
    return blockchain.is_chain_valid()


# ✅ Simple 51% attack simulation
def simulate_attack(blockchain):
    fake_chain_length = len(blockchain.chain) + 1

    if fake_chain_length > len(blockchain.chain):
        return {
            "attack": "51% attempted",
            "status": "rejected (invalid chain)"
        }