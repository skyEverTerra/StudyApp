{% load static %}

<img src="data:image/png;base64,{{ graph }}" alt="Gráfico de Calificaciones">
        <a class="btn-salir" href="{% url 'users:redirect' %}">Salir</a>