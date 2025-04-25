// SVG animation
const frames = document.querySelectorAll(".ai-frame");
let current = 0;

animation = setInterval(() => {
  frames[current].style.display = "none";
  current = (current + 1) % frames.length;
  frames[current].style.display = "block";
}, 400);


// chatbox switch on/off
function toggleChat() {
    const chatbox = document.getElementById('chatbox');
    const frames = document.querySelectorAll('.ai-frame');
    const isChatBoxHidden = window.getComputedStyle(chatbox).display === 'none';
    
    if (isChatBoxHidden) {
      chatbox.style.display = 'flex';
      clearInterval(animation);
      frames.forEach(frame => frame.style.display = 'none');
      frames[0].src = '/static/AI_assistant_chating.svg';
      frames[0].style.display = 'block';
      animation = null;
    } else {
      chatbox.style.display = 'none';
      clearInterval(animation);
      frames[0].src = '/static/AI_1.svg'; 
      let current = 0;
      frames.forEach((frame, index) => frame.style.display = index === 0 ? 'block' : 'none');
      animation = setInterval(() => {
        frames[current].style.display = "none";
        current = (current + 1) % frames.length;
        frames[current].style.display = "block";
      }, 400);
    }
  }  


// create user id
function getOrCreateUserId() {
  let userId = localStorage.getItem('anon_user_id');
  if (!userId) {
    userId = crypto.randomUUID();
    localStorage.setItem('anon_user_id', userId);
  }
  return userId;
}


// turn **Words** into bold
function formatBold(text) {
  return text
  .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
  .replace(/\n/g, '<br>');

}

// send message to flask
async function sendMessage() {
    const input = document.getElementById('user-input');
    const message = input.value.trim();
    if (message === '') return;
    const userId = getOrCreateUserId();
  
    const chatBody = document.getElementById('chat-body');
  
    const userMsg = document.createElement('div');
    userMsg.className = 'message user';
    userMsg.textContent = message;
    chatBody.appendChild(userMsg);
    input.value = '';
    chatBody.scrollTop = chatBody.scrollHeight;

    if (message.includes('請幫我匯出宣葇的履歷')) {
      addExportButton();
      return
    }

    if (message.includes('想填寫使用者回饋表單')) {
      addFeedbackButton();
      return
    }

    const botMsg = document.createElement('div');
    botMsg.className = 'message bot';
    botMsg.textContent = '思考中...';
    chatBody.appendChild(botMsg);
    chatBody.scrollTop = chatBody.scrollHeight;
  

    const res = await fetch('http://127.0.0.1:5000/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ user_id: userId, message: message })
    });

    const data = await res.json();
    if (data.spell_response) {
      botMsg.textContent = data.spell_response;
      const resMsg = document.createElement('div');
      resMsg.className = 'message bot';
      resMsg.innerHTML = formatBold(data.ques_response);
      chatBody.appendChild(resMsg);
    } else {
      botMsg.innerHTML = formatBold(data.ques_response);
    }
    chatBody.scrollTop = chatBody.scrollHeight;
    
  }

  /* catch (err) {
      botMsg.textContent = '小助理目前不想上班，請稍後再試';
    }*/


// preset botton
function fillInput(text) {
    const input = document.getElementById('user-input');
    input.value = text;
    input.focus();
  }


// add export button
function addExportButton() {
  const chatBody = document.getElementById('chat-body');
  const botMsg = document.createElement('div');
  botMsg.className = 'message bot';
  botMsg.innerHTML = '<p>您可以點擊下方按鈕匯出履歷PDF</p><button class="export-btn" onclick="exportPDF()">匯出履歷PDF</button>';
  chatBody.appendChild(botMsg);
  chatBody.scrollTop = chatBody.scrollHeight;
}


// export PDF
function exportPDF() {
  const link = document.createElement("a");
  link.href = "/static/Michelle_Resume.pdf";  
  link.download = "Michelle_Resume.pdf"; 
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}


// add feedback button
function addFeedbackButton() {
  const chatBody = document.getElementById('chat-body');
  const botMsg = document.createElement('div');
  botMsg.className = 'message bot';
  botMsg.innerHTML = '<p>您可以點擊下方按鈕填寫使用回饋表單</p><button class="feedback-btn" onclick="jumpToFeedback()">填寫回饋表單</button>';
  chatBody.appendChild(botMsg);
  chatBody.scrollTop = chatBody.scrollHeight;
}


// jump to feedback page
function jumpToFeedback() {
  window.location.href = '/feedback';
}


// send feedback
function sendFeedback(event) {
  event.preventDefault();

  const userId = getOrCreateUserId();
  const form = document.getElementById("fb-form");
  const formData = new FormData(form);

  const data = {
    user_id: userId,
    rating: formData.get("rating") || null,  
    attract: formData.get("attract-input") || null,
    suggestion: formData.get("suggest-input") || null,
    company: formData.get("company-name") || null,
    identity: formData.get("identity") || null,
    email: formData.get("email") || null
  };
  
  fetch("http://127.0.0.1:5000/feedback", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(data)
  }).then(response => {
    if (response.ok) {
      document.getElementById("popup-overlay").style.display = "flex";
      form.reset();
    } else {
      alert("送出失敗，請稍後再試！");
    }
  })
  .catch(error => {
    console.error("錯誤發生：", error);
    alert("系統發生錯誤，請稍後再試！");
  });

}


// close popup
function closePopup() {
  document.getElementById("popup-overlay").style.display = "none";
}



