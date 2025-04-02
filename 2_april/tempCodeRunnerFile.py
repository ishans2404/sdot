ef buildTree(lvlOrder):
    if not lvlOrder or lvlOrder[0] == 'N':
        return None
    lvlOrder = lvlOrder.replace("N", " N ").split()
    root = Node(int(lvlOrder[0]))
    queue = deque([root])
    i = 1
    while i < len(lvlOrder):
        node = queue.popleft()
        
        if i < len(lvlOrder) and lvlOrder[i] != 'N':
            node.left = Node(int(lvlOrder[i]))
            queue.append(node.left)
        i += 1
        
        if i < len(lvlOrder) and lvlOrder[i] != 'N':
            node.right = Node(int(lvlOrder[i]))
            queue.append(node.right)
        i += 1
    return root
