class Counter:
    """Attempt to model a simple tally counter."""

    def __init__(self, tally=None):
        """Set the counter to zero."""
        if tally:
            #set the counter to an initial value.
            self.tally = tally
        else:
            #start the counter from zero.
            self.tally = 0

    def increment(self):
        """Increment the counter by 1."""
        self.tally+= 1

    def decrement(self):
        """Decrement the counter by 1."""
        if self.tally <= 0:
            self.reset()
        else:
            self.tally-= 1

    def reset(self):
        """Reset the counter to 0."""
        self.tally = 0

#testing the implementation of the class and its methods.
restaurant_counter = Counter()
concert_counter = Counter(100)

#getters
print(f"{restaurant_counter.tally}")
print(f"{concert_counter.tally}\n")

#testing the increment() method.
for i in range(5):
    restaurant_counter.increment()
    concert_counter.increment()
print(f"{restaurant_counter.tally}")
print(f"{concert_counter.tally}\n")

#testing the decrement() method.
for i in range(10):
    restaurant_counter.decrement()
    concert_counter.decrement()
print(f"{restaurant_counter.tally}")
print(f"{concert_counter.tally}\n")

#testing the reset() method.
restaurant_counter.reset()
concert_counter.reset()
print(f"{restaurant_counter.tally}")
print(f"{concert_counter.tally}\n")

#testing ideas
restaurant_counter.tally = 124
print(restaurant_counter.tally)
print(restaurant_counter)