document.getElementById("registroForm").addEventListener("submit", function(event) {
  event.preventDefault(); // Evita envío automático

  let nombre = document.getElementById("nombre").value.trim();
  let email = document.getElementById("email").value.trim();
  let password = document.getElementById("password").value.trim();

  let nombreRegex = /^[a-zA-ZÀ-ÿ\s]{3,20}$/; // Solo letras y espacios, entre 3-20 caracteres
  let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Formato básico de email
  let passwordRegex = /^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,}$/; 
  // Al menos 6 caracteres, una mayúscula y un número

  let valid = true;

  // Validación Nombre
  if (!nombreRegex.test(nombre)) {
    document.getElementById("errorNombre").textContent = "El nombre debe tener entre 3 y 20 letras.";
    valid = false;
  } else {
    document.getElementById("errorNombre").textContent = "";
  }

  // Validación Email
  if (!emailRegex.test(email)) {
    document.getElementById("errorEmail").textContent = "Ingrese un correo válido.";
    valid = false;
  } else {
    document.getElementById("errorEmail").textContent = "";
  }

  // Validación Password
  if (!passwordRegex.test(password)) {
    document.getElementById("errorPassword").textContent = "La contraseña debe tener al menos 6 caracteres, una mayúscula y un número.";
    valid = false;
  } else {
    document.getElementById("errorPassword").textContent = "";
  }

  if (valid) {
    alert("Formulario enviado correctamente ✅");
    // Aquí podrías enviar los datos al servidor con fetch/AJAX
  }
});