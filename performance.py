import time

def measure_performance(blockchain):
    start = time.time()

    for i in range(3):
        blockchain.mine_block([f"Tx {i}"])

    end = time.time()

    total_time = round(end - start, 4)
    throughput = round(3 / total_time, 4)

    return {
        "blocks_mined": 3,
        "total_time": total_time,
        "throughput": throughput
    }