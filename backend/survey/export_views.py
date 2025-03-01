import pandas as pd
import pyreadstat
import openpyxl
from django.http import HttpResponse
from .models import Response

def export_spss(request, survey_id):
    responses = Response.objects.filter(survey_id=survey_id)
    data = [[r.question.id, r.question.text, r.answer] for r in responses]
    df = pd.DataFrame(data, columns=["question_id", "question_text", "answer"])
    
    file_path = "/tmp/survey_data.sav"
    pyreadstat.write_sav(df, file_path)
    
    with open(file_path, "rb") as file:
        response = HttpResponse(file.read(), content_type="application/octet-stream")
        response["Content-Disposition"] = "attachment; filename=survey_data.sav"
        return response

def export_excel(request, survey_id):
    responses = Response.objects.filter(survey_id=survey_id)
    data = [[r.question.id, r.question.text, r.answer] for r in responses]
    df = pd.DataFrame(data, columns=["question_id", "question_text", "answer"])
    
    file_path = "/tmp/survey_data.xlsx"
    df.to_excel(file_path, index=False)
    
    with open(file_path, "rb") as file:
        response = HttpResponse(file.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response["Content-Disposition"] = "attachment; filename=survey_data.xlsx"
        return response
