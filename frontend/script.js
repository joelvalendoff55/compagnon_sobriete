const form = document.getElementById('chat-form');
const chatBox = document.getElementById('chat-box');
const input = document.getElementById('user-message');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  
  const userMessage = input.value.trim();
  if (!userMessage) return;

  appendMessage('user', userMessage);
  input.value = '';

  // Ajouter message "en train d’écrire..."
  const typingDiv = document.createElement('div');
  typingDiv.classList.add('message', 'assistant');
  typingDiv.textContent = 'Le Compagnon Sobriété écrit';
  chatBox.appendChild(typingDiv);
  chatBox.scrollTop = chatBox.scrollHeight;

  let typingInterval = startTypingAnimation(typingDiv);

  try {
    const response = await fetch('https://compagnon-sobriete.onrender.com/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ user_message: userMessage })
    });

    const data = await response.json();

    stopTypingAnimation(typingInterval);
    typingDiv.textContent = ''; // Effacer "en train d’écrire..."
    typeWriter(typingDiv, data.response);

  } catch (error) {
    stopTypingAnimation(typingInterval);
    typingDiv.textContent = "Erreur de communication avec l'assistant.";
  }
});

// Fonction appendMessage inchangée
function appendMessage(sender, text) {
  const messageDiv = document.createElement('div');
  messageDiv.classList.add('message', sender);
  messageDiv.textContent = text;
  chatBox.appendChild(messageDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
  return messageDiv;
}

// Animation points typing
function startTypingAnimation(element) {
  let dotCount = 0;
  return setInterval(() => {
    dotCount = (dotCount + 1) % 4;
    element.textContent = "Le Compagnon Sobriété écrit" + ".".repeat(dotCount);
  }, 500);
}

function stopTypingAnimation(interval) {
  clearInterval(interval);
}

// Animation écriture réponse
function typeWriter(element, text, i = 0) {
  if (i < text.length) {
    element.textContent += text.charAt(i);
    setTimeout(() => typeWriter(element, text, i + 1), 30);
  }
}

