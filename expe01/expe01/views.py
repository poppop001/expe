from django.shortcuts import render
from rest_framework.veiws import APIView

class Main(APIView):
    def get(self, request):
        return render(request, 'expe01/main.html')