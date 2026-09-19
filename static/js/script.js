const form = document.querySelector('#weather-form');
const status = document.querySelector('#status');
const card = document.querySelector('#weather-card');

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  const city = form.city.value.trim();
  status.textContent = 'Loading weather…';
  card.hidden = true;
  try {
    const response = await fetch(`/api/weather?city=${encodeURIComponent(city)}`);
    const data = await response.json();
    if (!response.ok) throw new Error(data.error);
    document.querySelector('#location').textContent = `${data.city}, ${data.country}`;
    document.querySelector('#description').textContent = data.description;
    document.querySelector('#temperature').textContent = data.temperature;
    document.querySelector('#feels-like').textContent = data.feels_like;
    document.querySelector('#humidity').textContent = data.humidity;
    document.querySelector('#wind').textContent = data.wind_speed;
    document.querySelector('#advice').textContent = data.advice;
    const icon = document.querySelector('#icon');
    icon.src = `https://openweathermap.org/img/wn/${data.icon}@2x.png`;
    icon.alt = data.description;
    status.textContent = '';
    card.hidden = false;
  } catch (error) { status.textContent = error.message || 'Something went wrong.'; }
});