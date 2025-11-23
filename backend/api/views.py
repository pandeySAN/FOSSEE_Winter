import pandas as pd
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Dataset
from .serializers import DatasetSerializer
import json

@api_view(['POST'])
def upload_csv(request):
    file = request.FILES['file']
    df = pd.read_csv(file)

    summary = {
        "total_equipment": len(df),
        "average_flowrate": df["Flowrate"].mean(),
        "average_pressure": df["Pressure"].mean(),
        "average_temperature": df["Temperature"].mean(),
        "type_distribution": df["Type"].value_counts().to_dict()
    }

    ds = Dataset.objects.create(
        file_name=file.name,
        summary_json=json.dumps(summary)
    )

    # Keep only last 5
    all_ds = Dataset.objects.all().order_by('-uploaded_at')
    if all_ds.count() > 5:
        for d in all_ds[5:]:
            d.delete()

    return Response(summary)

@api_view(['GET'])
def history(request):
    data = Dataset.objects.all().order_by('-uploaded_at')
    return Response(DatasetSerializer(data, many=True).data)
