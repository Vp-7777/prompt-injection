class Grader:

    def __init__(self):
        self.total_steps = 0
        self.correct_steps = 0
        self.false_positives = 0
        self.missed_attacks = 0

    def evaluate_step(self, action, is_attack):
        self.total_steps += 1

        if is_attack:
            if action == "BLOCK":
                self.correct_steps += 1
            else:
                self.missed_attacks += 1

        else:
            if action == "ALLOW":
                self.correct_steps += 1
            elif action == "BLOCK":
                self.false_positives += 1

    def final_score(self):

        if self.total_steps == 0:
            return 0.0

        accuracy = self.correct_steps / self.total_steps

        penalty = (self.false_positives + self.missed_attacks) * 0.1

        score = max(0.0, accuracy - penalty)

        return round(score, 2)