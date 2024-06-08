const uploadImage = async () => {
  const imageInput = document.getElementById("imageInput");
  const file = imageInput.files[0];
  if (!file) {
    alert("Silakan pilih gambar terlebih dahulu!");
    return;
  }

  const formData = new FormData();
  formData.append("image", file);

  try {
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      body: formData,
    });
    const data = await response.json();
    console.log(data);
    alert("Kelas prediksi: " + data.class);
  } catch (error) {
    console.error("Error:", error);
    alert("Terjadi kesalahan saat mengunggah gambar. Silakan coba lagi.");
  }
};
