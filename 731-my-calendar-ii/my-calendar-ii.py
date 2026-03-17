class MyCalendarTwo(object):

    def __init__(self):
        self.bookings = []
        self.overlaps = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        
        # Check triple booking
        for s, e in self.overlaps:
            if start < e and end > s:
                return False
        
        # Add new overlaps
        for s, e in self.bookings:
            if start < e and end > s:
                self.overlaps.append((max(start, s), min(end, e)))
        
        # Add booking
        self.bookings.append((start, end))
        
        return True