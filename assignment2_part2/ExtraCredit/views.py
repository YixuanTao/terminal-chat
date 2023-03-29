import json
import redis
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

redis_host = "redis"
redis_port = 6379
redis_db = 0
redis_password = None

redis_conn = redis.Redis(
    host=redis_host, port=redis_port, db=redis_db, password=redis_password
)

@method_decorator(csrf_exempt, name='dispatch')
class ExecuteCommandView(View):
    def post(self, request):
        # Parse command and message from request body
        data = json.loads(request.body.decode("utf-8"))
        command = data["data"]["command"]
        message = data["data"]["message"]

        # Enqueue email message in Redis queue
        redis_conn.rpush("email_queue", json.dumps(data))

        # Return success response
