
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="styles.css">
    <!-- Importación de fuente desde Google Fonts -->
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Comic+Sans+MS&display=swap');
    </style>
    <title>Interfaz de Juegos</title>
    <!-- Estilos CSS internos -->
    <style>
        /* Estilos generales */
        body {
            margin: 0;
            padding: 0;
            font-family: 'Comic Sans MS', cursive, sans-serif;
            background-image: url('mondo.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            overflow-y: auto;
        }

        /* Estilos del encabezado */
        header {
            background-image: url('franja.jpg');
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

        .eslogan {
            margin-top: 90px;
            font-size: 18px;
            color: #333;
        }

        /* Estilos para el contenedor de imágenes */
        .image-container {
            text-align: center;
            margin-top: 20px;
        }

        /* Estilos para las imágenes dentro del contenedor */
        .medium-image {
            display: block;
            max-width: 100%;
            height: auto;
            margin: 0 auto 10px;
        }

        /* Estilos para el carrusel */
        .carousel {
            max-width: 600px; /* Tamaño mediano */
            margin: 0 auto;
        }

        /* Estilo para las imágenes del carrusel */
        .carousel-inner img {
            max-height: 300px; /* Altura mediana */
        }

        /* Estilos para el menú */
        .navbar-nav {
            margin: 0 auto; /* Centra los elementos del menú */
            margin-top: 25px; /* Ajusta la posición vertical */
        }

        .navbar-nav .nav-item {
            margin-right: 10px; /* Espacio entre elementos del menú */
        }

        .navbar-brand {
            margin-right: 20px; /* Espacio a la derecha del texto "Menú" */
        }

        /* Estilo para el texto del menú */
        .navbar-nav .nav-link {
            font-size: 17px; /* Tamaño de fuente para el texto del menú */
            color: white !important; /* Color del texto del menú */
        }

        /* Estilo para el fondo del menú */
        .navbar-dark .navbar-nav .nav-link {
            background-color: #28B463 !important; /* Fondo del menú */
        }

        /* Estilos para el botón */
        .btn-cerrar_sesion {
            background-color: #18c95c; /* Color de fondo */
            border: 1px solid gainsboro; /* Borde sólido con color gainsboro */
            color: white; /* Color del texto */
            padding: 10px 20px; /* Espaciado interno */
            text-align: center; /* Alineación del texto */
            text-decoration: none; /* Sin decoración de texto */
            display: inline-block; /* Mostrar como bloque en línea */
            font-size: 16px; /* Tamaño del texto */
            margin: 4px 2px; /* Margen exterior */
            cursor: zoom-out; /* Cursor tipo puntero */
            border-radius: 4px; /* Bordes redondeados */
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
<body class="scrollable-body">
    <!-- Encabezado -->
    <header>
        <!-- Logo de la aplicación -->
        <img src="magia.png" alt="Logo" id="logo">

        <button type="button" class="btn-cerrar_sesion" onclick="window.location.href='login.html'">Cerrar Sesion</button>
      
       
    </header>

    <!-- Navbar de Bootstrap -->
    <nav class="navbar navbar-expand-lg navbar-dark" style="background-color: #28B463 ; ">
        <div class="container">
          
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <!-- Elementos del menú -->
                   
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            Lenguaje
                        </a>
                        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <a class="dropdown-item" href="ABC.html">Abecedario</a>
                        </div>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            Pensamiento Lógico <br> Matemático
                        </a>
                        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <a class="dropdown-item" href="Numeros.html">Números</a>
                            <a class="dropdown-item" href="Sumas.html">Sumas</a>
                        </div>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                          Creatividad 
                        </a>
                        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <a class="dropdown-item" href="artes.html">Artes visuales</a>
                            <a class="dropdown-item" href="#"></a>

                        </div>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                          Socioemocional
                        </a>
                        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <a class="dropdown-item" href="Socioemocional.html">Emociones

</a>
                          

                        </div>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Conocimiento <br> Del Entorno
                        </a>
                        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <a class="dropdown-item" href="Conocimiento_entorno.html">Cuidar el ambiente</a>
                            <a class="dropdown-item" href="Videos.html">Animales</a>

                        </div>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                          Autonomia Personal
                        </a>
                        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <a class="dropdown-item" href="Autonomia.html">valores</a>
                            <a class="dropdown-item" href="#"></a>

                        </div>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                          Ingles
                        </a>
                        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <a class="dropdown-item" href="numrs.HTML">Numeros</a>
                            <a class="dropdown-item" href="Colors.html">Colores</a>

                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Cuerpo principal -->
    <main>
        <!-- Contenedor de juegos -->
        <div id="juegos-container">
            <!-- Eslogan de la aplicación -->
            <p class="eslogan">
                ¡Descubre el hechizo de aprender con MagicMin Academy!
                Donde cada juego es una llave mágica para desbloquear las competencias de lectura y escritura en los más pequeños.
                Nuestros juegos didácticos convierten cada desafío en una oportunidad para crecer. ¡Magia, diversión y aprendizaje en un solo lugar!
            </p>
            
                <!-- Imagen GIF -->
                <img src="https://i.gifer.com/origin/95/9592fe08911171b05f3c6aac39d0df83_w200.gif" alt="GIF Bangida" style="max-width: 100%;">
    

            <!-- Carrusel -->
            <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
                <ol class="carousel-indicators">
                    <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                    <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                </ol>
                <div class="carousel-inner">
                    <div class="carousel-item active">
                        <img src="imagen1.png" class="d-block w-100" alt="Imagen 1">
                    </div>
                    <div class="carousel-item">
                        <img src="imagen2.png" class="d-block w-100" alt="Imagen 2">
                    </div>
                    <div class="carousel-item">
                        <img src="imagen3.png" class="d-block w-100" alt="Imagen 2">
                    </div>
                    <div class="carousel-item">
                        <img src="imagen4.png" class="d-block w-100" alt="Imagen 2">
                    </div>
                    <div class="carousel-item">
                        <img src="imagen5.png" class="d-block w-100" alt="Imagen 2">
                    </div>
                    <div class="carousel-item">
                        <img src="imagen6.png" class="d-block w-100" alt="Imagen 2">
                    </div>
                </div>
                <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="sr-only">Previous</span>
                </a>
                <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="sr-only">Next</span>
                </a>
            </div>
        </div>
    </main>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
