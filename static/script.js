function sendToServer() {
    let inputValue = document.getElementById("userInput").value;

    fetch('http://localhost:3000/api/save-input', { // 這裡是後端 API 的 URL！！！
        method: 'POST', // 使用 POST 方法
        headers: {
            'Content-Type': 'application/json' // 告訴伺服器我們發送的是 JSON 格式的資料
        },
        body: JSON.stringify({ input: inputValue }) // 將輸入的內容轉成 JSON 傳送
    })
    .then(response => response.json()) // 解析伺服器回應的 JSON
    .then(data => {
        console.log("伺服器回應：", data);
        document.getElementById("serverResponse").innerText = data.message; // 顯示回應內容
    })
    .catch(error => console.error("錯誤：", error));
}