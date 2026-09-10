from client import PoseidonSponge
import json

def handle_request(req):
    pos = PoseidonSponge()
    action = req.get("action")
    if action == "hash":
        left = req.get("left", 0)
        right = req.get("right", 0)
        h = pos.hash_pair(left, right)
        return {"status": "ok", "hash": h}
    return {"status": "error", "message": "Unknown action"}

if __name__ == "__main__":
    print(json.dumps(handle_request({"action": "hash", "left": 10, "right": 20})))
