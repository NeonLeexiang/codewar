def warn_the_sheep(queue):
    return 'Oi! Sheep number ' + str(len(queue) - queue.index('wolf') - 1) + '! You are about to be eaten by a wolf!' if (len(queue) - queue.index('wolf') - 1) != 0 else 'Pls go away and stop eating my sheep' 
    
    
    """
    def warn_the_sheep(queue):
        n = len(queue) - queue.index('wolf') - 1
        return f'Oi! Sheep number {n}! You are about to be eaten by a wolf!' if n else 'Pls go away and stop eating my sheep'
    """
