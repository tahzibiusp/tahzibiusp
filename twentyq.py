class Node:
    def __init__(self, left=None, right=None, symbol=None, prob=0):
        self.left = left
        self.right = right
        self.symbol = symbol
        self.prob = prob

def build_huffman_tree(symbols, probabilities):
    total_probability = sum(probabilities)
    
    if total_probability > 1:
        raise ValueError("The sum of probabilities cannot exceed 1.")
    
    nodes = [Node(symbol=s, prob=p) for s, p in zip(symbols, probabilities)]
    
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.prob)
        left = nodes.pop(0)
        right = nodes.pop(0)
        new_node = Node(left=left, right=right, prob=left.prob + right.prob)
        nodes.append(new_node)
    
    return nodes[0]  # Return the root of the Huffman tree

def collect_symbols(node, subtree_numbers):
    if node is None:
        return
    
    if node.symbol is not None:
        subtree_numbers.append(node.symbol)
    else:
        collect_symbols(node.left, subtree_numbers)
        collect_symbols(node.right, subtree_numbers)

def twenty_questions_huffman():
    symbols = [1, 2, 3, 4, 5]
    probabilities = [0.3, 0.2, 0.2, 0.2, 0.2]  # Example probabilities
    
    try:
        huffman_tree = build_huffman_tree(symbols, probabilities)
    except ValueError as e:
        print(f"Error: {e}")
        return
    
    print("Welcome to the Twenty Questions Game!")
    print("Think of a number between 1 and 5, and I'll try to guess it.")
    
    attempts = 0
    current_node = huffman_tree
    subtree_numbers = []
    
    while current_node.symbol is None:
        attempts += 1
        collect_symbols(current_node.left, subtree_numbers)
        question = f"Is your number in this list: {subtree_numbers}? (yes/no): "
        answer = input(question).strip().lower()
        
        if answer == "yes":
            current_node = current_node.left
        elif answer == "no":
            current_node = current_node.right
        else:
            print("Please answer with 'yes' or 'no'.")
            attempts -= 1
            continue
        
        if current_node.symbol is None:
            subtree_numbers = []  # Reset subtree_numbers only if we continue to next iteration

    print(f"Yay! I guessed your number {current_node.symbol} in {attempts} attempts.")

if __name__ == "__main__":
    twenty_questions_huffman()