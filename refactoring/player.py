class Player:
    """A game player with a position, speed, health, and score."""

    def __init__(self, x, y, speed, health, score):
        self.x      = x
        self.y      = y
        self.speed  = speed
        self.health = health
        self.score  = score

    def move(self, dx, dy):
        """Move the player by (dx, dy) scaled by speed."""
        self.x += dx * self.speed
        self.y += dy * self.speed
        return f"Player moved to position ({self.x}, {self.y})."

    def jump(self, velocity):
        """Make the player jump with the given velocity."""
        return f"Player jumps with velocity {velocity}."

    def take_damage(self, amount):
        """Reduce the player's health by amount and report remaining health."""
        self.health -= amount
        return f"Player took {amount} damage. Remaining health: {self.health}."

    def add_score(self, points):
        """Add points to the player's score and report the new total."""
        self.score += points
        return f"Player gained {points} points. Total score: {self.score}."
