CATEGORIES = ("Network", "Hardware", "Software", "Other")
URGENCY_LEVELS = ("low", "medium", "high")
STATUSES = ("open", "in_progress", "resolved")
PRIORITIES = ("critical", "high", "medium", "low")  # most urgent first
PRIORITY_RANK = {name: rank for rank, name in enumerate(PRIORITIES)}