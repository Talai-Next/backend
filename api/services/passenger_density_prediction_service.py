from datetime import datetime, timedelta
from api.models import Feedback


def passenger_density_prediction(bus_id: int) -> int | float:
    """
    Mock AI: Predict passenger density based on the average of recent feedback (last 30 minutes).
    If no data, assume medium density.
    """
    now = datetime.now()
    recent_feedbacks = Feedback.objects.filter(bus_id=bus_id, timestamp__gte=now - timedelta(minutes=30))

    if not recent_feedbacks.exists():
        return 3  # Default: Medium

    # this should be AI
    return sum(f.passenger_density for f in recent_feedbacks) / recent_feedbacks.count()
