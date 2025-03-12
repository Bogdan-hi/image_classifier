function uploadFile() {
    let fileInput = document.getElementById("fileInput").files[0];
    let formData = new FormData();
    formData.append("file", fileInput);

    fetch("/upload", { method: "POST", body: formData })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById("result").innerText = "Ошибка: " + data.error;
            } else {
                document.getElementById("result").innerHTML = `<p>Класс: ${data.label} (${(data.confidence * 100).toFixed(2)}%)</p>`;
            }
        });
}
