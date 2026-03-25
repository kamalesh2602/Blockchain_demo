from fastapi import FastAPI
from blockchain import Blockchain
from wallet import Wallet
from attack import tamper_chain, validate_chain, simulate_attack
from performance import measure_performance

app = FastAPI()

blockchain = Blockchain()
users = {}

# ---------------------------
# 1. Create User
# ---------------------------
@app.post("/create-user")
def create_user(name: str):
    users[name] = Wallet()
    return {"message": f"{name} created"}


# ---------------------------
# 2. Create Transaction
# ---------------------------
@app.post("/create-transaction")
def create_transaction(sender: str, receiver: str, property_id: str):
    tx = {
        "sender": sender,
        "receiver": receiver,
        "property": property_id
    }

    signature = users[sender].sign(str(tx))
    tx["signature"] = signature.hex()

    return tx


# ---------------------------
# 3. Mine Block
# ---------------------------
@app.post("/mine")
def mine(tx: dict):
    time_taken = blockchain.mine_block([tx])
    return {"message": "Block mined", "time_taken": time_taken}


# ---------------------------
# 4. View Chain
# ---------------------------
@app.get("/chain")
def get_chain():
    return [vars(b) for b in blockchain.chain]


# ---------------------------
# 5. Tamper
# ---------------------------
@app.get("/tamper")
def tamper():
    tamper_chain(blockchain)
    return {"message": "Block tampered"}


# ---------------------------
# 6. Validate
# ---------------------------
@app.get("/validate")
def validate():
    return {"valid": validate_chain(blockchain)}


# ---------------------------
# 7. Attack
# ---------------------------
@app.get("/attack")
def attack():
    return simulate_attack(blockchain)


# ---------------------------
# 8. Performance
# ---------------------------
@app.get("/performance")
def performance():
    return measure_performance(blockchain)