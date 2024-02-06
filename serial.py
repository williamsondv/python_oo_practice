"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=1):
        """creates a new instance of the SerialGenerator class"""
        self.start = start
        self.increment = start
        
    def generate(self):
        """returns next serial value"""
        temp = self.increment
        self.increment += 1
        return temp
    
    
    def reset(self):
        """resets incrementing number to original value"""
        self.increment = self.start 

    def __repr__(self):
        return f'<SerialGenerator start={self.start} next={self.increment}>'

