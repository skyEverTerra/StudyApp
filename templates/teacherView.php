{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lista de Alumnos</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <style>
     body {
            margin: 0;
            padding: 0;
            font-family: 'Comic Sans MS', cursive, sans-serif;
            background-image: url('{% static "img/mondo.jpg" %}');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            overflow-y: auto;
        }

        /* Estilos del encabezado */
        header {
            background-image: url('{% static "img/franja.jpg" %}');
            background-size: cover;
            background-position: center;
            color: white;
            text-align: center;
            padding: 20px;
            position: relative;
        }

        #logo {
            width: 290px;
            height: auto;
            margin: 0 auto;
        }

        /* Estilos del cuerpo principal */
        main {
            padding: 20px;
        }

        /* Estilos del contenedor de juegos */
        #juegos-container {
            background-color: rgba(255, 255, 255, 0.8);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }

        /* Estilos para el botón de login */
        .login-button {
            padding: 10px 20px;
            font-size: 20px;
            background-color: rgb(0, 183, 255); 
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
            margin-top: 20px;
        }

    table {
      border-collapse: collapse;
      width: 100%;
      margin-top: 80px;
      background-color: #727e81; 
    }
    
    th {
      background-color: #6dd8f3; 
      color: #000000; 
    }
    
    td {
      background-color: #b7eff7; 
      color: #000000; 
    }
    
    th, td {
      border: 1px solid #000000; 
      padding: 10px;
      text-align: left;
    }
      
    .container {
      color: #101110; 
    }


        /* Estilo cuando se pasa el cursor sobre el botón */
        .btn-cerrar_sesion:hover {
            background-color: #e02c2c; /* Cambiar color de fondo */
        }

        /* Estilo cuando se presiona el botón */
        .btn-cerrar_sesion:active {
            background-color: #d61010; /* Cambiar color de fondo */
        }
    
  </style>
</head>
<body>
  <header>
    <!-- Logo de la aplicación -->
    <img src="{% static 'img/magia.png' %}" alt="Logo" id="logo">
            <a class="btn-cerrar_sesion" href="{% url 'users:logout' %}">Cerrar Sesion</a>

</header>

      <p>Codigo de maestro: {{ maestro.codigo_maestro }}</p>
  <div class="container">
    <h2 class="text-center">Lista de Alumnos</h2>
    <div class="table-responsive">

      <table id="alumnosTable" class="table table-striped">
  <thead>
    <tr>
      <th>Nombre</th>
      <th>Promedio</th>
      <th>Recomendacion General</th>
    </tr>
  </thead>
  <tbody>
    {% for alumno in alumnos %}
    <tr>
      <td><a href="{% url 'users:graph' %}?a={{ alumno.0.user.username }}">{{ alumno.0.user.username }}</a></td>
      <td>
        <div style="display: flex; align-items: center;">
          <!-- <progress value="{{ alumno.calificacion }}" max="100" style="flex-grow: 1;"></progress> -->
          <span style="margin-left: 5px;">{{ alumno.1 }}</span>
        </div>
      </td>
      <td>
        <span>
          {% if alumno.1 >= 75 %}
            {{ recomendacion.General.0 }}
          {% elif alumno.1 >= 50 %}
            {{ recomendacion.General.1 }}
          {% elif alumno.1 >= 25 %}
            {{ recomendacion.General.2 }}
          {% elif alumno.1 >= 0 %}
            {{ recomendacion.General.3 }}
          {% endif %}
        </span>
      </td>
    </tr>
    {% endfor %}
    {% for alumno in alumnos_ %}
    <tr>
      <td>{{ alumno.user.username }}</td>
      <td>
        <div style="display: flex; align-items: center;">
          <span style="margin-left: 5px;">Sin revisar</span>
        </div>
      </td>
      <td></td>
    </tr>
    {% endfor %}
  </tbody>
</table>

  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>