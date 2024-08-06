
import hashlib
class SandDollarBlock:
    '''
        Makiya Laurenza
            SandDollarBlock represents a single block on the blockchain
            
            previous_block_hash (str): The hash of the previous block in the chain.
            transaction_list (list): List of transactions included in this block.
            
            "SD" == SandDollar coin
    '''
    
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "--->".join(transaction_list) + "--->" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

def main():
#   Transactions:
    t1 = "Niesha sends 7 SD to Vyvyan"
    t2 = "Makiya sends 2 SD to Vyvyan"
    t3 = "Makiya sends 5 SD to Fabiola"
    t4 = "Fabiola sends 4.3 SD to Niesha"
    t5 = "George sends 6 SD to Makiya"
    t6 = "Makiya sends 9 SD to Niesha"

    #1 Block:
    initial_block = SandDollarBlock("Initial String", [t1, t2])

    print("Initial Block Data: ",initial_block.block_data, "\n")
    print("Initial Hash: " , initial_block.block_hash, "\n")
    
    #2 Block:
    second_block = SandDollarBlock(initial_block.block_hash, [t3, t4])

    print("Second Block Data: ",second_block.block_data, "\n")
    print("Second Hash: " , second_block.block_hash, "\n")
    
    #3 Block:
    third_block = SandDollarBlock(second_block.block_hash, [t5, t6])

    print("Third Block Data: ", third_block.block_data, "\n")
    print("Third Hash: " , third_block.block_hash, "\n")

#Allow script to be run directly:
if __name__ == "__main__":
     main()
            