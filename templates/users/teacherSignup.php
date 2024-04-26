{% load static %}

<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MagicMind Academy</title>
    <style>
        body {
            background-image: url('{% static "img/mario.avif" %}');
            background-size: cover;
            background-position: center bottom;
            background-repeat: no-repeat;
            background-attachment: fixed;
            margin: 0;
        }

        .container {
            text-align: center;
            position: relative;
            margin-top: 370px; /* Ajusta el margen superior según tus necesidades */
        }

        .maestros-img,
        .alumnos-img,
        .imagen-superior {
            position: absolute;
            z-index: 1;
        }

        .maestros-img {
            top: -50px; /* Ajusta la posición vertical de la imagen de maestros */
            left: 25%; /* Ajusta la posición lateral de la imagen de maestros */
            transform: translateX(-50%);
            width: 200px; /* Ajusta el ancho de la imagen de maestros */
        }

        .alumnos-img {
            top: -50px; /* Ajusta la posición vertical de la imagen de alumnos */
            left: 45%; /* Ajusta la posición lateral de la imagen de alumnos para más separación */
            transform: translateX(-50%);
            opacity: 1;
            width: 200px; /* Ajusta el ancho de la imagen de alumnos */
        }

        .imagen-superior {
            top: -150px; /* Ajusta la posición vertical de la imagen superior */
            left: 50%; /* Ajusta la posición lateral de la imagen superior */
            transform: translateX(-50%);
            width: 300px; /* Ajusta el ancho de la imagen superior */
        }

        .boton {
            padding: 20px;
            border: none;
            background: none;
            cursor: pointer;
            margin-top: 20px; /* Ajusta el margen superior de los botones */
            position: relative;
            left: -300px; /* Ajusta el valor de left para mover los botones más hacia la izquierda */
            z-index: 0;
        }

        .boton + .boton {
            margin-left: 200px; /* Ajusta el margen izquierdo entre los botones */
        }

        .boton img {
            position: absolute;
            animation: floatAnimation 3s infinite ease-in-out;
            width: 180px;
        }

        @keyframes floatAnimation {
            0% {
                transform: translateY(0);
            }

            50% {
                transform: translateY(-90px);
            }

            100% {
                transform: translateY(0);
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Imagen de MAESTROS -->
        <img src="{% static 'img/maestros.png' %}" alt="texto" class="maestros-img">
        <!-- Imagen de ALUMNOS -->
        <img src="{% static 'img/ALUMNOS.png' %}" alt="texto" class="alumnos-img">
        <!-- Imagen superior -->
        <img src="{% static 'img/magia.png' %}" alt="Imagen superior" class="imagen-superior">
        <!-- Botón 1 con imagen -->
        <button class="boton">
            <a href="{% url 'users:SignupAsTeacher' %}">
                <img src="{% static 'img/caja.png' %}" alt="Botón 1">
            </a>
        </button>
        <!-- Botón 2 con imagen -->
        <button class="boton">
            <a href="{% url 'users:SignupAsStudent' %}">
                <img src="{% static 'img/caja.png' %}" alt="Botón 2">
            </a>
        </button>
    </div>
    <p class="footer-text">¿Tienes una cuenta? <a href="{% url 'users:login' %}">Entra aquí</a></p>
</body>

</html>