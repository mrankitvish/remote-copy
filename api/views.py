from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import uuid
from django.shortcuts import get_object_or_404
from .models import Notes

class HomeView(APIView):
    # GET method for HomeView
    def get(self, request):
        # Generate a unique token using uuid
        token = uuid.uuid4()
        # Create a new Note instance with the generated token
        note = Notes.objects.create(token=token)
        # Return the generated token in the response
        return Response({"token": token}, status=status.HTTP_200_OK)

class TextView(APIView):
    # GET method for TextView
    def get(self, request, token):
        # Get the Note object with the provided token
        note = get_object_or_404(Notes, token=token)
        # Return the text of the Note object in the response
        return Response({"text": note.text}, status=status.HTTP_200_OK)

    # POST method for TextView
    def post(self, request, token):
        # Get the Note object with the provided token
        note = get_object_or_404(Notes, token=token)
        # Get the text from the request data
        text = request.data.get("text")

        # If text is provided
        if text is not None:
            # Update the Note object's text with the provided text
            note.text = text
            # Save the Note object
            note.save()
            # Return a success message in the response
            return Response({"message": "Text saved successfully"}, status=status.HTTP_201_CREATED)
        else:
            # If no text is provided, return an error message in the response
            return Response({"error": "No text provided"}, status=status.HTTP_400_BAD_REQUEST)

    # DELETE method for TextView
    def delete(self, request, token):
        # Get the Note object with the provided token
        note = get_object_or_404(Notes, token=token)
        # Delete the Note object
        note.delete()
        # Return a success message in the response
        return Response({"message": "Note deleted successfully"}, status=status.HTTP_200_OK)