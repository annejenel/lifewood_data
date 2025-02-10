from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Application, ContactMessage
from .serializers import ApplicationSerializer, ContactMessageSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class ApplicationCreateView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        print("\n===== DEBUGGING REQUEST DATA =====")
        print("Received Data:", request.data)
        print("Received Files:", request.FILES)

        full_name = request.data.get("fullName")
        age = request.data.get("age")
        degree = request.data.get("degree")
        job_experience = request.data.get("jobExperience")
        contact_time = request.data.get("contactTime")
        resume = request.FILES.get("resume")

        if not all([full_name, age, degree, job_experience, contact_time, resume]):
            return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            application = Application.objects.create(
                full_name=full_name,
                age=age,
                degree=degree,
                job_experience=job_experience,
                contact_time=contact_time,
                resume=resume
            )
            return Response({"message": "Application submitted successfully!"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": "Internal server error", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ContactMessageCreateView(APIView):
    def post(self, request):
        print("\n===== DEBUGGING CONTACT US REQUEST DATA =====")
        print("Received Data:", request.data)

        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Your message has been sent successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
