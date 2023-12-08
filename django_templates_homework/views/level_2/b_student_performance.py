"""
Оживите шаблон.

Исходите из предположения, что в курсе не может быть больше 3-х недель.
"""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def students_performance_view(request: HttpRequest) -> HttpResponse:
    performances = [
        {"student_name": "Reed Boles", "week1_completed": 0, "week2_completed": False, "week3_completed": False},
        {"student_name": "David Mitchell", "week1_completed": 1, "week2_completed": True, "week3_completed": True},
        {"student_name": "Teresa Monger", "week1_completed": 0, "week2_completed": False, "week3_completed": True},
        {"student_name": "Doris Dayton", "week1_completed": 1, "week2_completed": False, "week3_completed": False},
    ]
    return render(request, 'level_2/students_performance.html', context={"performances": performances})
