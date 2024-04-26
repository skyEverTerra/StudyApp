<?php
// Verificar si se han enviado datos del formulario
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Obtener el nombre de usuario y la contraseña del formulario
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Aquí puedes realizar la autenticación, por ejemplo, verificar en una base de datos
    // Por simplicidad, supongamos un usuario y contraseña fijos
    $valid_username = "usuario";
    $valid_password = "contraseña";

    // Verificar las credenciales
    if ($username === $valid_username && $password === $valid_password) {
        // Inicio de sesión exitoso
        echo "¡Inicio de sesión exitoso!";
        // Puedes redirigir a otra página después del inicio de sesión si lo deseas
    } else {
        // Credenciales incorrectas
        echo "Usuario o contraseña incorrectos.";
    }
}
?>