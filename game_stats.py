class GameStats:
    '''Track statistics for Sideways Shooter '''

    def __init__(self, sws_settings):
        ''' Initialize statistics '''
        self.sws_settings = sws_settings
        self.reset_stats()

        # Start Sideways Shooter in an active state
        self.game_active = False

        # High score which is not reseted
        self.high_score = 0

    def reset_stats(self):
        ''' Initialize statistics that can change during the game '''
        self.ships_left = self.sws_settings.ship_limit
        self.score = 0
        self.level = 1
