import requests

BASE_URL = "http://127.0.0.1:8000"


def run_baseline():
    try:
        # Reset
        requests.get(f"{BASE_URL}/reset")

        # Task 1
        res1 = requests.post(f"{BASE_URL}/step", json={
            "action_type": "classify",
            "category": "Billing"
        }).json()

        # Task 2
        res2 = requests.post(f"{BASE_URL}/step", json={
            "action_type": "extract",
            "extracted_fields": {
                "order_id": "1234",
                "date": "12-03-2024",
                "issue": "refund"
            }
        }).json()

        # Task 3
        res3 = requests.post(f"{BASE_URL}/step", json={
            "action_type": "reply",
            "response": "Sorry, your refund for order 1234 will be processed"
        }).json()

        return {
            "task1": res1.get("reward", 0),
            "task2": res2.get("reward", 0),
            "task3": res3.get("reward", 0),
            "total": res1.get("reward", 0) + res2.get("reward", 0) + res3.get("reward", 0)
        }

    except Exception as e:
        return {"error": str(e)}