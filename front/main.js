// frontend/scripts/main.js

document.addEventListener("DOMContentLoaded", () => {
    const registerForm = document.getElementById("registerForm");
    const folderForm = document.getElementById("folderForm");
    const accountForm = document.getElementById("accountForm");

    // Registro de Usuario
    registerForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const nombre_usuario = document.getElementById("registerUsername").value;
        const contraseña_maestra = document.getElementById("registerPassword").value;

        const response = await fetch("http://localhost:5000/register", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ nombre_usuario, contraseña_maestra })
        });
        const data = await response.json();
        document.getElementById("registerMessage").innerText = data.message || data.error;
    });

    // Crear Carpeta
    folderForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const nombre_usuario = document.getElementById("folderUsername").value;
        const nombre = document.getElementById("folderName").value;
        const tipo = document.getElementById("folderType").value;

        const response = await fetch(`http://localhost:5000/${nombre_usuario}/carpeta`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ nombre, tipo })
        });
        const data = await response.json();
        document.getElementById("folderMessage").innerText = data.message || data.error;
    });

    // Agregar Cuenta
    accountForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const nombre_usuario = document.getElementById("accountUsername").value;
        const nombre_carpeta = document.getElementById("accountFolder").value;
        const nombre_usuario_cuenta = document.getElementById("accountName").value;
        const correo_electronico = document.getElementById("accountEmail").value;
        const contraseña = document.getElementById("accountPassword").value;

        const response = await fetch(`http://localhost:5000/${nombre_usuario}/carpeta/${nombre_carpeta}/cuenta`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                nombre_usuario: nombre_usuario_cuenta,
                correo_electronico,
                contraseña
            })
        });
        const data = await response.json();
        document.getElementById("accountMessage").innerText = data.message || data.error;
    });
});
