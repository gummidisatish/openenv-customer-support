from app.models import Action
from app.graders.grader1 import grade_classification
from app.graders.grader2 import grade_extraction
from app.graders.grader3 import grade_response


class OpenEnv:
    def __init__(self):
        self.current_email = None
        self.score = 0.0
        self.done = False

    # 🔁 RESET ENVIRONMENT
    def reset(self):
        self.done = False
        self.score = 0.0

        self.current_email = {
            "email_id": "E001",
            "sender": "user@example.com",
            "subject": "Refund request",
            "body": "I want a refund for order #1234 placed on 12-03-2024",
            "true_category": "Billing",
            "true_fields": {
                "order_id": "1234",
                "date": "12-03-2024",
                "issue": "refund"
            }
        }

        return {"observation": self.current_email}

    # ⚡ STEP FUNCTION
    def step(self, action_dict):
        action = Action(**action_dict)

        reward = 0.0

        # 🟢 Task 1: Classification
        if action.action_type == "classify":
            reward = grade_classification(
                action.category,
                self.current_email["true_category"]
            )

        # 🟡 Task 2: Extraction
        elif action.action_type == "extract":
            reward = grade_extraction(
                action.extracted_fields,
                self.current_email["true_fields"]
            )

        # 🔴 Task 3: Response
        elif action.action_type == "reply":
            reward = grade_response(action.response)

        # ❌ Invalid action
        else:
            reward = -0.5

        self.score += reward

        return {
            "observation": self.current_email,
            "reward": reward,
            "done": self.done,
            "info": {}
        }

    # 📊 CURRENT STATE
    def state(self):
        return {"observation": self.current_email}

    # 📋 TASK LIST
    def get_tasks(self):
        return [
            {
                "task": "classification",
                "action": {"action_type": "classify", "category": "string"}
            },
            {
                "task": "extraction",
                "action": {"action_type": "extract", "extracted_fields": {}}
            },
            {
                "task": "response",
                "action": {"action_type": "reply", "response": "string"}
            }
        ]

    # 🧮 FINAL SCORE
    def get_score(self):
        return {
            "final_score": round(self.score, 2)
        }