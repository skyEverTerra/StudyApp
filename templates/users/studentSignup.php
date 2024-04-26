{% extends "users/base.html" %}
{% load static %}
{% block head_content %}
    <link rel="stylesheet" href="{% static 'css/mystyle.css' %}">
    <title>Maestro login</title>
{% endblock %}
{% block container %}
    {% if form.errors %}
    <p class="alert alert-danger"> Error las contraseñas no coinciden o ingreso un codigo de maestro no valido</p>
    {% endif %}
    <div class="login-container">
        <h2><i class="fas fa-user-lock"></i> Bienvenido Alumno!</h2>
        <form method="POST" action="{% url 'users:SignupAsStudent' %}">
            {% csrf_token %}

            <div class="mb-3">
                <label for="nombre" class="form-label"><i class="fas fa-user"></i> Nombre</label>
                <input type="text" class="form-control" id="nombre" name="username" minlength="6" required>
            </div>
            <div class="mb-3">
                <label for="correo" class="form-label"><i class="fas fa-user"></i> Correo</label>
                <input type="email" class="form-control" id="nombre" name="email" required>
            </div>
            <div class="mb-3">
                <label for="contraseña" class="form-label"><i class="fas fa-lock"></i> Contraseña</label>
                <input type="password" class="form-control" id="contrasena" name="password" required>
            </div>
            <div class="mb-3">
                <label for="contrasena" class="form-label"><i class="fas fa-lock"></i> Repetir contraseña</label>
                <input type="password" class="form-control" id="contrasena" name="password_confirmation" required>
            </div>
            <div class="mb-3">
                <label for="contrasena" class="form-label"><i class="fas fa-lock"></i> Codigo de maestro</label>
                <input type="text" class="form-control" id="codigo_maestro" name="teacher_code" required>
            </div>
            <button type="submit" class="btn btn-primary"><i class="fas fa-sign-in-alt"></i> Ingresar</button>
        </form>
        <a class="btn-salir" href="{% url 'users:redirect' %}">Salir</a>
    </div>
{% endblock %}