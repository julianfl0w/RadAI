import http from "../http-common";

class UploadFilesService {
  upload(file, notes, onUploadProgress) {
    let formData = new FormData();

    formData.append("file", file);
    //formData.append("notes", notes);

    return http.post("http://127.0.0.1:8082/upload", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
      onUploadProgress,
    });
  }

  getFiles() {
    return http.get("/files");
  }
}

export default new UploadFilesService();
