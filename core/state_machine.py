class StateMachine:
    def __init__(self, strategy, timer):
        self.strategy = strategy
        self.timer = timer

    def run(self):
        # Check session
        if self.timer.is_session_over():
            print("🔄 Session ended, reset")
            self.timer.reset()
            self.strategy.has_traded = False
