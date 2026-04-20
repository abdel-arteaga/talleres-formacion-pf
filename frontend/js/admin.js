const API_URL = "http://localhost:5000/workshops";
const table = document.getElementById("adminTable");
const form = document.getElementById("workshopForm");

function loadWorkshops() {
  fetch(API_URL)
    .then(res => res.json())
    .then(data => {
      table.innerHTML = "";
      data.forEach(w => {
        table.innerHTML += `
          <tr>
            <td>${w.name}</td>
            <td>${w.date}</td>
            <td>
              <button class="btn btn-danger btn-sm" onclick="deleteWorkshop(${w.id})">Eliminar</button>
            </td>
          </tr>`;
      });
    });
}

form.addEventListener("submit", e => {
  e.preventDefault();
  // Capturamos los valores correctamente
  const workshop = {
    name: document.getElementById("name").value,
    description: document.getElementById("description").value,
    date: document.getElementById("date").value,
    time: document.getElementById("time").value,
    place: document.getElementById("place").value,
    category: document.getElementById("category").value
  };

  fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(workshop)
  })
  .then(() => {
    alert("Taller creado con éxito");
    form.reset();
    loadWorkshops();
  });
});

window.deleteWorkshop = function(id) { // Lo hacemos global para el onclick
  if(confirm("¿Seguro que deseas eliminar este taller?")) {
    fetch(`${API_URL}/${id}`, { method: "DELETE" })
      .then(() => loadWorkshops());
  }
}

loadWorkshops();
