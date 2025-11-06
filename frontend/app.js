async function loadFlights() {
  const res = await fetch("http://backend-service:5000/flights");
  const data = await res.json();
  const list = document.getElementById("flight-list");
  list.innerHTML = "";
  data.forEach(f => {
    const li = document.createElement("li");
    li.innerText = `${f.airline} - ₹${f.price}`;
    list.appendChild(li);
  });
}
