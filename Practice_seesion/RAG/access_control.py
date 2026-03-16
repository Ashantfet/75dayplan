RESTRICTED_KEYWORDS = ["salary", "compensation", "bonus", "payroll"]

ROLE_PERMISSIONS = {
    "employee": ["policy", "leave", "holiday", "benefits"],
    "hr": ["policy", "leave", "holiday", "benefits", "salary"]
}

def access_control(query: str, role: str):
    query = query.lower()

    if role not in ROLE_PERMISSIONS:
        return False, "Invalid role"

    # If restricted keyword present and role not HR → block
    for word in RESTRICTED_KEYWORDS:
        if word in query and role != "hr":
            return False, "Access Denied: Restricted Information"

    return True, "Access Granted"
