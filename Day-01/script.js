const yesButton = document.getElementById('yesButton');
const noButton = document.getElementById('noButton');
const anotherButton = document.getElementById('anotherButton');
const backButton = document.getElementById('backButton');
const introView = document.getElementById('introView');
const jokeView = document.getElementById('jokeView');
const byeView = document.getElementById('byeView');
const jokeCard = document.getElementById('jokeCard');
const frontText = document.getElementById('frontText');
const backText = document.getElementById('backText');

function showView(viewName) {
  introView.classList.toggle('hidden', viewName !== 'intro');
  jokeView.classList.toggle('hidden', viewName !== 'joke');
  byeView.classList.toggle('hidden', viewName !== 'bye');
}

function setCardContent(question, answer) {
  frontText.textContent = question;
  backText.textContent = answer;
  jokeCard.classList.remove('is-flipped');
  jokeCard.setAttribute('aria-label', 'Flip the joke card');
}

async function fetchJoke() {
  try {
    const response = await fetch('https://v2.jokeapi.dev/joke/Any?type=twopart');

    if (!response.ok) {
      throw new Error('Unable to load joke right now.');
    }

    const data = await response.json();

    if (data.type === 'twopart') {
      setCardContent(data.setup, data.delivery);
    } else {
      setCardContent(data.joke, 'That was the punchline.');
    }
  } catch (error) {
    frontText.textContent = 'The joke machine is taking a quick break.';
    backText.textContent = error.message;
  }
}

yesButton.addEventListener('click', async () => {
  showView('joke');
  await fetchJoke();
});

noButton.addEventListener('click', () => {
  showView('bye');
});

anotherButton.addEventListener('click', async () => {
  await fetchJoke();
});

backButton.addEventListener('click', () => {
  showView('bye');
});

jokeCard.addEventListener('click', () => {
  jokeCard.classList.toggle('is-flipped');
});

jokeCard.addEventListener('keydown', (event) => {
  if (event.key === 'Enter' || event.key === ' ') {
    event.preventDefault();
    jokeCard.classList.toggle('is-flipped');
  }
});
